from widgets.dps.enums import *
from widgets.dps.action import *

import numpy as np
from functools import partial
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from widgets.dps.hero import Hero


class StatusTemplate:
    def __init__(self,
                 status_id: str,
                 caster: 'Hero',
                 target: List[int],
                 max_stack: int,
                 refresh_interval: float = 0,
                 status_type: str = "buff"):
        self.status_id = status_id
        self.caster = caster
        self.target = target
        self.status_type = status_type
        self.max_stack = max_stack
        self.refresh_interval = int(refresh_interval)

    def is_buff(self):
        return self.status_type == "buff"

    def apply_fn(self, reservation, target_id, current_time):
        raise NotImplementedError
    def refresh_fn(self, reservation, target_id, current_time):
        raise NotImplementedError
    def delete_fn(self, reservation, target_id, current_time):
        raise NotImplementedError
    def get_target_with_id(self, target_id):
        party = self.caster.party
        target = party.character_list[target_id]
        return target

class StatusReservation:
    def __init__(self, template: StatusTemplate, start_time, end_time):
        self.template = template
        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.next_update = self.start_time
        self.next_step = "apply"

    def __lt__(self, other):
        return self.next_update < other.next_update

    def update_next_step(self, current_t):
        if current_t < self.start_time:
            self.next_update = self.start_time
            return
        elif self.template.refresh_interval > 0:
            next_refresh = int(np.ceil(current_t - self.start_time) + self.start_time + SEC_TO_MS)
            if next_refresh <= self.end_time:
                self.next_update = int(next_refresh)
                self.next_step = "refresh"
                return
        self.next_update = self.end_time
        self.next_step = "delete"

    def is_buff(self):
        return self.template.is_buff()

    def apply_fn(self, target_id, current_time):
        self.template.apply_fn(self, target_id, current_time)
    def refresh_fn(self, target_id, current_time):
        self.template.refresh_fn(self, target_id, current_time)
    def delete_fn(self, target_id, current_time):
        self.template.delete_fn(self, target_id, current_time)


# Apply damage
def DebuffDamageRefresh(status, current_time, damage):
    hero = status.caster
    apply_instant_damage(hero = hero,
                         damage_type = DamageType.Debuff,
                         time = current_time,
                         damage_coeff = damage)


class DebuffSting(StatusTemplate):
    def __init__(self, status_id, caster, duration):
        target = [9]  # Enemy at index 9
        max_stack = 0
        refresh_interval = SEC_TO_MS
        super().__init__(status_id, caster, target, max_stack, refresh_interval, "debuff")
        self.duration = duration  # duration은 고정값이므로 남김
    
    def apply_fn(self, reservation, target_id, current_time):
        pass

    def refresh_fn(self, reservation, target_id, current_time):
        DebuffDamageRefresh(reservation, current_time, 10)

    def delete_fn(self, reservation, target_id, current_time):
        pass


class BuffAttackSpeed(StatusTemplate):
    def __init__(self, status_id, caster, target, duration, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target=target,
                         max_stack=0,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = duration
        self.value = value/100
    
    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.attack_speed_coeff += self.value
    
    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.attack_speed_coeff -= self.value


class BuffDamageAmplify(StatusTemplate):
    def __init__(self, status_id, caster, target, duration, applying_dmg_type, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target=target,
                         max_stack=0,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = duration
        self.applying_dmg_type = applying_dmg_type
        self.value = value/100
    
    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, self.value)
    
    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, -self.value)