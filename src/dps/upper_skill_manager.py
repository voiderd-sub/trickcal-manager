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
    
    def update_next_update(self):
        current_time = self.party.current_time
        if current_time < self.locked_until:
            self.party.next_update[11] = self.locked_until
            return
        
        if self.locked_until > 0 and current_time >= self.locked_until:
            self.locked_until = 0

        if self.request_queue:
            self.party.next_update[11] = current_time
            return

        next_delayed_time = float('inf')
        for earliest, _, _, _ in self.delayed_requests:
            if current_time < earliest:
                next_delayed_time = min(next_delayed_time, earliest)
            else:
                next_delayed_time = min(next_delayed_time, current_time)
                break
        
        self.party.next_update[11] = next_delayed_time
        

    def add_request(self, hero_id):
        if any(req.hero_id == hero_id for req in self.request_queue):
            return
        if any(req[2] == hero_id for req in self.delayed_requests):
            return

        # For direct requests (CooldownReadyCondition)
        priority = self.party.upper_skill_priorities[hero_id]
        request = SkillRequest(hero_id, priority)
        insort(self.request_queue, request)
        self.update_next_update()

    def add_delayed_request(self, hero_id, delay_min_sec, delay_max_sec):
        current_time = self.party.current_time
        earliest_time = round(current_time + delay_min_sec * SEC_TO_MS)
        latest_time = round(current_time + delay_max_sec * SEC_TO_MS)
        priority = self.party.upper_skill_priorities[hero_id]
        
        request_tuple = (earliest_time, latest_time, hero_id, priority)
        insort(self.delayed_requests, request_tuple)
        self.update_next_update()

    def check_and_update_requests(self):
        """Called by external events like cooldown reduction."""
        self.resolve_delayed_requests(self.party.current_time)

    def resolve_delayed_requests(self, current_time):
        still_delayed = []
        processed_count = 0

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
            else:
                # The hero is not ready yet, but the request is still valid.
                # Keep it in the list to check again later.
                still_delayed.append((earliest, latest, hero_id, priority))

        # Reconstruct the list, excluding the processed requests.
        # [Requests that are still valid but the hero isn't ready] + [Requests whose time has not yet come]
        self.delayed_requests = still_delayed + self.delayed_requests[processed_count:]
        self.update_next_update()

    def resolve_request(self, current_time):
        # First, process any delayed requests that might be ready
        self.resolve_delayed_requests(current_time)
        
        if not self.request_queue:
            self.update_next_update() # Recalculate next update time
            return

        # Process one request per call to respect global lock
        request = self.request_queue[0]

        # Final check for validity
        if current_time > request.latest_activation_time:
            self.request_queue.pop(0) # Discard expired request
            self.update_next_update() # Check next in queue
            return

        # If we are here, the request is valid and will be executed
        self.request_queue.pop(0)
        hero = self.party.character_list[request.hero_id]
        rule = hero.upper_skill_rule

        if rule.cancel_current_movement:
            self.party.action_manager.cancel_actions_by_hero(request.hero_id)

        hero.upper_skill_flag = True
        
        is_busy = hero.last_movement != MovementType.Wait
        if not is_busy or rule.cancel_current_movement:
            self.party.next_update[request.hero_id] = current_time
            
        # Set global lock and sleep. The return is crucial to prevent
        # update_next_update from overwriting the lock.
        self.locked_until = current_time + GLOBAL_UPPER_SKILL_LOCK_MS
        self.party.next_update[11] = self.locked_until
        return 