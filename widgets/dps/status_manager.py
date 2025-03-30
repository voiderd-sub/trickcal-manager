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
        self.status_reservations = []
        self.active_status = [AutoDeletingDefaultDict() for _ in range(10)]    # Index 0 implies debuff

    def add_status_reserv(self, status):
        """
        Add a reservation for activating and deactivating buffs/debuffs to status_heap.
        
        """

        insort(self.status_reservations, status)
        self.party.next_update[0] = self.status_reservations[0].next_update

    
    def resolve_status_reserv(self, current_time):
        """
        Do the reserved statuses applying/removing based on the current time.
        """

        while self.status_reservations and self.status_reservations[0].next_update <= current_time:
            status = self.status_reservations.pop(0)
            
            match status.next_step:
                case "apply":
                    if status.max_stack == 0:           # extend
                        # case: need to extend existing status' duration
                        if self.get_applying_status_stack(status) > 0:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            existing_status.end_time += status.end_time
                            existing_status.update_next_step(current_time)

                            # reorder to fit extended duration
                            self.status_reservations.pop(status_idx)
                            self.add_status_reserv(existing_status)
                        else:                           # no existing same buff/debuff; Add new one
                            self._add_status(status, current_time)
                    
                    elif status.max_stack == np.inf:    # individual
                        self._add_status(status, current_time)
                    
                    else:                               # overlap
                        # case: need to delete oldest status
                        if self.get_applying_status_stack(status) >= status.max_stack:
                            status_idx, existing_status = self.get_applying_status_from_reservations(status)
                            self.status_reservations.pop(status_idx)
                        self._add_status(status, current_time)
                    
                case "refresh":
                    self._refresh_status(status, current_time)
                case "delete":
                    self._delete_status(status, current_time)
                case _:
                    raise
        self.party.next_update[0] = (self.status_reservations[0].next_update
                                     if len(self.status_reservations) > 0 else np.inf)


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
            (s_idx, s) for s_idx, s in enumerate(self.status_reservations)
            if s.status_id == status.status_id and s.next_step != "apply"
        ]
        if not valid_statuses:
            return -1, None

        return min(valid_statuses, key=lambda x: x[1].start_time)


class Status:
    def __init__(self, status_id, caster, target, start_time, end_time, max_stack, refresh_interval = 0):
        self.status_id = status_id
        self.caster = caster
        self.target = target

        self.start_time = start_time
        self.end_time = end_time
        self.next_update = start_time
        self.next_step = "apply"

        self.refresh_interval = refresh_interval
        self.max_stack = max_stack

    def __lt__(self, other):
        return self.next_update < other.next_update
    
    def update_next_step(self, current_t):
        if current_t < self.start_time:
            self.next_update = self.start_time
            return
        elif self.refresh_interval > 0:
            next_refresh = np.ceil(current_t - self.start_time) + self.start_time + MS_IN_SEC
            if next_refresh <= self.end_time:
                self.next_update = next_refresh
                self.next_step = "refresh"
                return
        self.next_update = self.end_time
        self.next_step = "delete"
    
    def apply_fn(self, target_id, current_time):
        raise NotImplementedError
    
    def refresh_fn(self, target_id, current_time):
        raise NotImplementedError
    
    def delete_fn(self, target_id, current_time):
        raise NotImplementedError