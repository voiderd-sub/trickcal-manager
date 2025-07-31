from dps.enums import *

from bisect import insort
import numpy as np
from functools import total_ordering


@total_ordering
class SkillRequest:
    def __init__(self, hero_id: int, priority: int, latest_activation_time: float = float('inf')):
        self.hero_id = hero_id
        self.priority = priority
        self.latest_activation_time = latest_activation_time

    def __lt__(self, other):
        if not isinstance(other, SkillRequest):
            return NotImplemented
        return self.priority < other.priority

    def __eq__(self, other):
        if not isinstance(other, SkillRequest):
            return NotImplemented
        return self.priority == other.priority


class UpperSkillManager:
    def __init__(self, party):
        self.party = party

    def init_simulation(self):
        self.request_queue = []  # Stores SkillRequest objects
        # Stores (earliest_time, latest_time, hero_id, priority) tuples
        self.delayed_requests = []
        self.locked_until = 0
    
    def add_request(self, hero_id):
        if any(req.hero_id == hero_id for req in self.request_queue):
            return
        if any(req[2] == hero_id for req in self.delayed_requests):
            return

        # For direct requests (CooldownReadyCondition)
        priority = self.party.upper_skill_priorities[hero_id]
        request = SkillRequest(hero_id, priority)
        insort(self.request_queue, request)
        # A new request might be immediately processable. Wake up now.
        self.party.next_update[11] = self.party.current_time

    def add_delayed_request(self, hero_id, delay_min_sec, delay_max_sec):
        current_time = self.party.current_time
        earliest_time = round(current_time + delay_min_sec * SEC_TO_MS)
        latest_time = round(current_time + delay_max_sec * SEC_TO_MS)
        priority = self.party.upper_skill_priorities[hero_id]
        
        request_tuple = (earliest_time, latest_time, hero_id, priority)
        insort(self.delayed_requests, request_tuple)
        # Schedule to wake up at the new event time if it's earlier than the current plan.
        self.party.next_update[11] = min(self.party.next_update[11], earliest_time)

    def check_and_update_requests(self):
        """Called by external events like cooldown reduction."""
        self.resolve_delayed_requests(self.party.current_time)

    def resolve_delayed_requests(self, current_time):
        still_delayed = []
        processed_count = 0
        request_moved = False

        # self.delayed_requests is sorted by earliest_time.
        # So, we only need to check requests that can be processed at the current time.
        for earliest, latest, hero_id, priority in self.delayed_requests:
            if earliest > current_time:
                break  # No more requests to process at the current time.
            
            processed_count += 1

            if current_time > latest:
                continue # The request has expired.

            hero = self.party.character_list[hero_id]
            if hero.upper_skill_timer == 0:
                # The hero's skill is ready, so add it to the main request queue.
                request = SkillRequest(hero_id, priority, latest)
                insort(self.request_queue, request)
                request_moved = True
            else:
                # The hero is not ready yet, but the request is still valid.
                # Keep it in the list to check again later.
                still_delayed.append((earliest, latest, hero_id, priority))

        # Reconstruct the list, excluding the processed requests.
        # [Requests that are still valid but the hero isn't ready] + [Requests whose time has not yet come]
        self.delayed_requests = still_delayed + self.delayed_requests[processed_count:]
        
        if request_moved:
            # A delayed request became a current request. Wake up now to process it.
            self.party.next_update[11] = current_time

    def resolve_request(self, current_time):
        # First, process any delayed requests that might be ready
        self.resolve_delayed_requests(current_time)

        # Abort if globally locked or no requests are pending.
        if not self.party.is_global_upper_skill_ready(current_time):
            self.party.next_update[11] = self.locked_until
            return
        if not self.request_queue:
            # If no requests, find next delayed request time. If none, sleep infinitely.
            next_delayed_time = float('inf')
            if self.delayed_requests:
                for earliest, _, _, _ in self.delayed_requests:
                    if earliest > current_time:
                        next_delayed_time = earliest
                        break
            self.party.next_update[11] = next_delayed_time
            return

        # Find all heroes who can cast *now* (are idle or can cancel)
        for i, request in enumerate(self.request_queue):
            hero = self.party.character_list[request.hero_id]
            rule = hero.upper_skill_rule

            if current_time > request.latest_activation_time:
                continue

            # A hero is considered busy if their current action is not yet finished.
            # This can happen in 3 scenarios:
            # 1. The hero's last movement is not wait.
            is_last_movement_not_wait = hero.last_movement != MovementType.Wait
            # 2. The action's scheduled end time (`next_update`) is in the future.
            # is_mid_action = self.party.next_update[hero.party_idx] > current_time
            is_mid_action = (self.party.next_update[hero.party_idx] > current_time) or hero.woke_up_early
            
            is_busy = is_last_movement_not_wait and is_mid_action
            can_cancel = is_busy and rule.cancelable_movements and hero.last_movement in rule.cancelable_movements

            if not is_busy or can_cancel:
                hero.upper_skill_flag = True
                if can_cancel:
                    self.party.action_manager.cancel_actions_by_hero(hero.party_idx)
                self.party.next_update[hero.party_idx] = current_time
                self.request_queue.pop(i)
                return

            # The hero will set the global lock upon skill execution, which schedules the next update.
            # So, we don't need to do anything else here.
            
        # No immediate candidates, but queue is not empty. All are busy.
        # Schedule wakeup for when the first hero becomes free or a delayed request fires.
        next_event_time = float('inf')
        
        # Find when the first waiting hero will be free.
        for request in self.request_queue:
            next_event_time = min(next_event_time, self.party.next_update[request.hero_id])

        # Also consider the next delayed request.
        if self.delayed_requests:
            for earliest, _, _, _ in self.delayed_requests:
                if earliest > current_time:
                    next_event_time = min(next_event_time, earliest)
                    break
        
        self.party.next_update[11] = next_event_time 