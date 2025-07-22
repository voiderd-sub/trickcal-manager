from dps.enums import *

from collections import defaultdict
from bisect import bisect_left, insort
import numpy as np


# Helper; defaultdict w/ deleting key when val = 0
class AutoDeletingDefaultDict(defaultdict):
    def __init__(self):
        super().__init__(int)

    def __setitem__(self, key, value):
        if value == 0:
            self.pop(key, None)
        else:
            super().__setitem__(key, value)


class StatusManager:
    def __init__(self, party):
        self.party = party

    def init_simulation(self):
        # Priority queue for status reservations (sorted by time)
        self.status_queue = []
        
        # Active statuses for each character (including enemy at index 9)
        # Each character has separate buff and debuff dictionaries
        self.active_buffs = [AutoDeletingDefaultDict() for _ in range(10)]    # 0-8: heroes, 9: enemy
        self.active_debuffs = [AutoDeletingDefaultDict() for _ in range(10)]  # 0-8: heroes, 9: enemy
        
        # Index for fast lookup of statuses by ID
        self.status_by_id = defaultdict(list)  # status_id -> list of Status objects

    def update_next_update(self, time):
        self.party.next_update[10] = time

    def add_status_reserv(self, status):
        """
        Add a reservation for activating and deactivating buffs/debuffs to status_heap.
        Also index the status for fast lookup.
        """
        if len(status.template.target) > 0:
            insort(self.status_queue, status)
            self.update_next_update(self.status_queue[0].next_update)
            
            # Index status for fast lookup
            self.status_by_id[status.template.status_id].append(status)

    
    def resolve_status_reserv(self, current_time):
        """
        Do the reserved statuses applying/removing based on the current time.
        """

        while self.status_queue and self.status_queue[0].next_update <= current_time:
            status = self.status_queue.pop(0)
            
            # Remove from index
            self.status_by_id[status.template.status_id].remove(status)
            
            match status.next_step:
                case "apply":
                    if status.template.max_stack == 0:           # extend
                        # case: need to extend existing status' duration
                        if self.get_applying_status_stack(status) > 0:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            if existing_status is not None:
                                existing_status.end_time += status.end_time
                                existing_status.update_next_step(current_time)

                                # reorder to fit extended duration
                                self.status_queue.pop(status_idx)
                                self.add_status_reserv(existing_status)
                        else:                           # no existing same buff/debuff; Add new one
                            self._add_status(status, current_time)
                    
                    elif status.template.max_stack == np.inf:    # individual
                        self._add_status(status, current_time)
                    
                    else:                               # overlap
                        # case: need to delete oldest status
                        if self.get_applying_status_stack(status) >= status.template.max_stack:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            if existing_status is not None:
                                self.status_queue.pop(status_idx)
                        self._add_status(status, current_time)
                    
                case "refresh":
                    self._refresh_status(status, current_time)
                case "delete":
                    self._delete_status(status, current_time)
                case _:
                    raise
        self.update_next_update(self.status_queue[0].next_update
                                    if len(self.status_queue) > 0 else np.inf)


    def _add_status(self, status, current_time):
        for target_id in status.template.target:
            status.apply_fn(target_id, current_time)
            
            # Determine if it's a buff or debuff and add to appropriate dictionary
            if status.is_buff():
                self.active_buffs[target_id][status.template.status_id] += 1
            else:
                self.active_debuffs[target_id][status.template.status_id] += 1
                
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _refresh_status(self, status, current_time):
        for target_id in status.template.target:
            status.refresh_fn(target_id, current_time)
        status.next_update = status.end_time
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _delete_status(self, status, current_time):
        for target_id in status.template.target:
            status.delete_fn(target_id, current_time)
            
            # Remove from appropriate dictionary
            if status.is_buff():
                self.active_buffs[target_id][status.template.status_id] -= 1
            else:
                self.active_debuffs[target_id][status.template.status_id] -= 1
    
    def has_buff(self, hero_id, buff_id):
        """Check if hero has a specific buff"""
        return buff_id in self.active_buffs[hero_id]

    def has_debuff(self, hero_id, debuff_id):
        """Check if hero has a specific debuff"""
        return debuff_id in self.active_debuffs[hero_id]
    
    def get_buff_count(self, hero_id, buff_id):
        """Get the number of stacks of a specific buff"""
        return self.active_buffs[hero_id].get(buff_id, 0)
    
    def get_debuff_count(self, hero_id, debuff_id):
        """Get the number of stacks of a specific debuff"""
        return self.active_debuffs[hero_id].get(debuff_id, 0)
    
    def get_applying_status_stack(self, status):
        """Get current stack count of a status type"""
        any_target_id = status.template.target[0]
        if status.is_buff():
            return self.active_buffs[any_target_id].get(status.template.status_id, 0)
        else:
            return self.active_debuffs[any_target_id].get(status.template.status_id, 0)

    def get_applying_status_from_reservations(self, status):
        """Get existing status from reservations (optimized with indexing)"""
        valid_statuses = [
            (s_idx, s) for s_idx, s in enumerate(self.status_queue)
            if s.template.status_id == status.template.status_id and s.next_step != "apply"
        ]
        if valid_statuses:
            return min(valid_statuses, key=lambda x: x[1].start_time)
        return -1, None
    
    def get_statuses_by_id(self, status_id):
        """Fast lookup of all statuses with given ID"""
        return self.status_by_id[status_id]
    
    def get_all_active_statuses(self, hero_id):
        """Get all active buffs and debuffs for a hero"""
        return {
            'buffs': dict(self.active_buffs[hero_id]),
            'debuffs': dict(self.active_debuffs[hero_id])
        }