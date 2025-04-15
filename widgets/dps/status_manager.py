from widgets.dps.enums import *

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
        self.effect_queue = []
        self.active_status = [AutoDeletingDefaultDict() for _ in range(10)]    # Index -1 implies debuff

    def update_next_update(self, time):
        self.party.next_update[10] = time

    def add_status_reserv(self, status):
        """
        Add a reservation for activating and deactivating buffs/debuffs to status_heap.
        
        """
        if len(status.target) > 0:
            insort(self.effect_queue, status)
            self.update_next_update(self.effect_queue[0].next_update)

    
    def resolve_status_reserv(self, current_time):
        """
        Do the reserved statuses applying/removing based on the current time.
        """

        while self.effect_queue and self.effect_queue[0].next_update <= current_time:
            status = self.effect_queue.pop(0)
            
            match status.next_step:
                case "apply":
                    if status.max_stack == 0:           # extend
                        # case: need to extend existing status' duration
                        if self.get_applying_status_stack(status) > 0:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            existing_status.end_time += status.end_time
                            existing_status.update_next_step(current_time)

                            # reorder to fit extended duration
                            self.effect_queue.pop(status_idx)
                            self.add_status_reserv(existing_status)
                        else:                           # no existing same buff/debuff; Add new one
                            self._add_status(status, current_time)
                    
                    elif status.max_stack == np.inf:    # individual
                        self._add_status(status, current_time)
                    
                    else:                               # overlap
                        # case: need to delete oldest status
                        if self.get_applying_status_stack(status) >= status.max_stack:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            self.effect_queue.pop(status_idx)
                        self._add_status(status, current_time)
                    
                case "refresh":
                    self._refresh_status(status, current_time)
                case "delete":
                    self._delete_status(status, current_time)
                case _:
                    raise
        self.update_next_update(self.effect_queue[0].next_update
                                    if len(self.effect_queue) > 0 else np.inf)


    def _add_status(self, status, current_time):
        for target_id in status.target:
            status.apply_fn(target_id, current_time)
            self.active_status[target_id][status.status_id] += 1
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _refresh_status(self, status, current_time):
        for target_id in status.target:
            status.refresh_fn(target_id, current_time)
        status.next_update = status.end_time
        status.update_next_step(current_time)
        self.add_status_reserv(status)

    def _delete_status(self, status, current_time):
        for target_id in status.target:
            status.delete_fn(target_id, current_time)
            self.active_status[target_id][status.status_id] -= 1
    
    def has_buff(self, hero_id, buff_id):
        return buff_id in self.active_status[hero_id]

    def has_debuff(self, debuff_id):
        return debuff_id in self.active_status[0]
    
    def get_applying_status_stack(self, status):
        any_target_id = status.target[0]
        return self.active_status[any_target_id].get(status.status_id, 0)

    def get_applying_status_from_reservations(self, status):
        valid_statuses = [
            (s_idx, s) for s_idx, s in enumerate(self.effect_queue)
            if s.status_id == status.status_id and s.next_step != "apply"
        ]
        if not valid_statuses:
            return -1, None

        return min(valid_statuses, key=lambda x: x[1].start_time)