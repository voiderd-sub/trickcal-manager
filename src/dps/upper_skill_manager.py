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

        priority = hero_id
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

        # Activate hero's upper skill
        hero = self.party.character_list[hero_id]
        hero.upper_skill_flag = True
        self.party.next_update[hero_id] = current_time # Wake up hero to cast skill immediately

        # Set global lock
        self.party.next_update[11] = current_time + GLOBAL_UPPER_SKILL_LOCK_MS

        # If queue is empty, sleep until new request
        if not self.request_queue:
            self.party.next_update[11] = np.inf 