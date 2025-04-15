from widgets.dps.enums import *
from widgets.dps.effect import *
from widgets.dps.hero import Hero

import numpy as np
from functools import partial
from typing import List


class Status:
    def __init__(self,
                 status_id: str,
                 caster: Hero,
                 target: List[int],
                 start_time: float,
                 end_time: float,
                 max_stack: int,
                 refresh_interval: float = 0):
        self.status_id = status_id
        self.caster = caster
        self.target = target

        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.next_update = self.start_time
        self.next_step = "apply"

        self.refresh_interval = int(refresh_interval)
        self.max_stack = max_stack

    def __lt__(self, other):
        return self.next_update < other.next_update
    
    def update_next_step(self, current_t):
        if current_t < self.start_time:
            self.next_update = self.start_time
            return
        elif self.refresh_interval > 0:
            next_refresh = np.ceil(current_t - self.start_time) + self.start_time + SEC_TO_MS
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
    
    def get_target_with_id(self, target_id):
        party = self.caster.party
        target = party.character_list[target_id]
        return target


# Apply damage
def DebuffDamageRefresh(status, current_time, damage):
    hero = status.caster
    apply_instant_effect(hero = hero,
                         damage_type = DamageType.Debuff,
                         time = current_time,
                         damage_coeff = damage)


class DebuffSting(Status):
    def __init__(self, status_id, caster, start_time, duration):
        target = [-1]
        start_time, end_time = start_time, start_time + duration * SEC_TO_MS
        max_stack = 0
        refresh_interval = SEC_TO_MS

        super().__init__(status_id, caster, target, start_time, end_time, max_stack, refresh_interval)
    
    def apply_fn(self, target_id, current_time):
        pass

    def refresh_fn(self, target_id, current_time):
        DebuffDamageRefresh(self, current_time, 10)

    def delete_fn(self, target_id, current_time):
        pass


class BuffAttackSpeed(Status):
    def __init__(self, status_id, caster, target, start_time, duration, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target=target,
                         start_time=start_time,
                         end_time=start_time + SEC_TO_MS * duration,
                         max_stack=0,
                         refresh_interval=0)
        self.value = value/100
    
    def apply_fn(self, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.attack_speed_coeff += self.value
    
    def delete_fn(self, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.attack_speed_coeff -= self.value


class BuffDamageAmplify(Status):
    def __init__(self, status_id, caster, target, start_time, duration, applying_dmg_type, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target=target,
                         start_time=start_time,
                         end_time=start_time + SEC_TO_MS * duration,
                         max_stack=0,
                         refresh_interval=0)
        self.applying_dmg_type = applying_dmg_type
        self.value = value/100
    
    def apply_fn(self, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, self.value)
    
    def delete_fn(self, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, -self.value)