from dps.enums import *

from collections import defaultdict
from bisect import insort
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

    def update_next_update(self):
        next_time = self.status_queue[0].next_update if self.status_queue else float('inf')
        self.party.next_update[10] = next_time if next_time == float('inf') else round(next_time)

    def add_status_reserv(self, status):
        """
        Add a reservation for activating and deactivating buffs/debuffs to status_heap.
        Also index the status for fast lookup.
        """
        if status.get_targets():
            insort(self.status_queue, status)
            self.update_next_update()
            
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
                    if status.template.max_stack == 0:  # extend
                        # Find an already active status to extend
                        status_idx, existing_status = self.get_applying_status_from_reservations(status, active_only=True)
                        
                        if existing_status:
                            # An active status exists, so we extend it.
                            new_duration = status.end_time - status.start_time
                            existing_status.end_time += new_duration
                            existing_status.update_next_step(current_time)
                            
                            # Reorder the queue since end_time has changed
                            self.status_queue.pop(status_idx)
                            insort(self.status_queue, existing_status)

                            # The new status that triggered the extension is now consumed.
                            # It was already removed from the queue at the start of the loop,
                            # so we just need to ensure it's removed from the index.
                            if status in self.status_by_id[status.template.status_id]:
                                self.status_by_id[status.template.status_id].remove(status)
                        else:
                            # No active status, so just add the new one.
                            self._add_status(status, current_time)

                    elif status.template.max_stack == np.inf:  # individual
                        self._add_status(status, current_time)

                    else:  # overlap
                        # Remove oldest statuses until we are under the max_stack limit.
                        while self.get_applying_status_stack(status) >= status.template.max_stack:
                            oldest_idx, oldest_status = self.get_applying_status_from_reservations(status, active_only=True)
                            if oldest_status is not None:
                                # Pop from queue and manually remove from index
                                self.status_queue.pop(oldest_idx)
                                if oldest_status in self.status_by_id[oldest_status.template.status_id]:
                                    self.status_by_id[oldest_status.template.status_id].remove(oldest_status)
                                
                                # Call delete_fn and decrement stack count
                                self._delete_status(oldest_status, current_time)
                            else:
                                # Should not be reachable if get_applying_status_stack is correct
                                break 
                        self._add_status(status, current_time)
                    
                case "refresh":
                    self._refresh_status(status, current_time)
                case "delete":
                    self._delete_status(status, current_time)
                case _:
                    raise
        self.update_next_update()


    def _add_status(self, status, current_time):
        for target_id in status.get_targets():
            status.apply_fn(target_id, current_time)
            
            # Determine if it's a buff or debuff and add to appropriate dictionary
            if status.is_buff():
                self.active_buffs[target_id][status.template.status_id] += 1
            else:
                self.active_debuffs[target_id][status.template.status_id] += 1
                
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _refresh_status(self, status, current_time):
        for target_id in status.get_targets():
            status.refresh_fn(target_id, current_time)
        status.next_update = status.end_time
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _delete_status(self, status, current_time):
        print(f"  └── DELETING status: {status.template.status_id} at {current_time}ms")
        for target_id in status.get_targets():
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
        any_target_id = status.get_targets()[0]
        if status.is_buff():
            return self.active_buffs[any_target_id].get(status.template.status_id, 0)
        else:
            return self.active_debuffs[any_target_id].get(status.template.status_id, 0)

    def get_applying_status_from_reservations(self, status, active_only=False):
        """Get existing status from reservations."""
        valid_statuses = []
        for i, s in enumerate(self.status_queue):
            if s.template.status_id == status.template.status_id and s.caster_id == status.caster_id:
                if active_only and s.next_step == "apply":
                    continue
                valid_statuses.append((i, s))

        if valid_statuses:
            return min(valid_statuses, key=lambda x: x[1].start_time)
        return -1, None
    
    def get_statuses_by_id(self, status_id):
        """Fast lookup of all statuses with given ID"""
        return self.status_by_id[status_id]
    
    def consume_oldest_stack(self, status_id):
        """
        Finds the oldest active status reservation for a given status_id,
        and sets its end time to the current time, effectively consuming it.
        """
        all_reservations = self.get_statuses_by_id(status_id)
        
        active_reservations = [
            r for r in all_reservations
            if r.start_time <= self.party.current_time and r.next_step not in ('apply', 'delete')
        ]

        if not active_reservations:
            return

        to_remove = min(active_reservations, key=lambda r: r.start_time)

        # To remove the status, we manipulate its end_time and let resolve_status_reserv handle it.
        try:
            # Remove from queue to re-insert with updated time.
            self.status_queue.remove(to_remove)
        except ValueError:
            # It might have been already processed in the same tick. Safe to ignore.
            pass
        
        to_remove.end_time = self.party.current_time
        to_remove.update_next_step(self.party.current_time)
        self.add_status_reserv(to_remove)

    def get_all_active_statuses(self, hero_id):
        """Get all active buffs and debuffs for a hero"""
        return {
            'buffs': dict(self.active_buffs[hero_id]),
            'debuffs': dict(self.active_debuffs[hero_id])
        }