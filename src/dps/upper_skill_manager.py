from dps.enums import *

from bisect import insort
import numpy as np


class UpperSkillManager:
    def __init__(self, party):
        self.party = party

    def init_simulation(self):
        # (priority, hero_id)
        self.request_queue = []
    
    def update_next_update(self):
        next_time = self.party.current_time if self.request_queue else np.inf
        self.party.next_update[11] = next_time

    def add_request(self, hero_id):
        # Check for duplicates
        if any(req[1] == hero_id for req in self.request_queue):
            return

        priority = self.party.upper_skill_priorities[hero_id]
        request_tuple = (priority, hero_id)
        insort(self.request_queue, request_tuple)

        # wake up manager
        if self.party.next_update[11] == np.inf:
            self.party.next_update[11] = self.party.current_time
    
    def resolve_request(self, current_time):
        if not self.request_queue:
            self.party.next_update[11] = np.inf
            return
        
        # Pop the highest priority hero
        _, hero_id = self.request_queue.pop(0)
        hero = self.party.character_list[hero_id]
        rule = hero.upper_skill_rule

        # Cancel current action if the rule says so
        if rule.cancel_current_movement:
            self.party.action_manager.cancel_actions_by_hero(hero_id)

        # Activate hero's upper skill flag
        hero.upper_skill_flag = True
        
        # Decide when the hero should act next
        is_busy = hero.last_movement != MovementType.Wait
        
        if not is_busy or rule.cancel_current_movement:
            # Wake up hero to cast skill immediately if they are not busy,
            # or if their action was just cancelled.
            self.party.next_update[hero_id] = current_time
        # Otherwise, if the hero is busy and the rule is to wait,
        # do nothing and let the hero finish their current action.

        # Set global lock for the next request
        if self.request_queue:
            self.party.next_update[11] = current_time + GLOBAL_UPPER_SKILL_LOCK_MS
        else:
            self.party.next_update[11] = np.inf 