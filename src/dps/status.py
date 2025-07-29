from dps.enums import *
from dps.action import *
from dps.stat_utils import apply_stat_bonuses

import numpy as np
from functools import partial
from typing import List, TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from dps.hero import Hero

def target_self(hero: 'Hero') -> List[int]:
    return [hero.party_idx]

def target_all(hero: 'Hero') -> List[int]:
    # Returns all hero indices (0-8), excluding the enemy (9).
    return [i for i, char in enumerate(hero.party.character_list) if char is not None and i < 9]

def target_all_wo_self(hero: 'Hero') -> List[int]:
    # Returns all hero indices (0-8) except self, excluding the enemy (9).
    return [i for i, char in enumerate(hero.party.character_list) if char is not None and i < 9 and i != hero.party_idx]

class StatusTemplate:
    def __init__(self,
                 status_id: str,
                 caster: 'Hero',
                 target_resolver_fn: Callable[['Hero'], List[int]],
                 max_stack: int,
                 refresh_interval: float = 0,
                 status_type: str = "buff"):
        self.status_id = status_id
        self.caster = caster
        self.target_resolver_fn = target_resolver_fn
        self.status_type = status_type
        self.max_stack = max_stack
        self.refresh_interval = refresh_interval

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
    def __init__(self, template: StatusTemplate, start_time):
        self.template = template
        self.start_time = start_time
        self.duration = getattr(self.template, 'duration', 0)
        self.end_time = round(start_time + self.duration * SEC_TO_MS)
        self.next_update = self.start_time
        self.next_step = "apply"
        self.resolved_targets = self.template.target_resolver_fn(self.template.caster)

    def __lt__(self, other):
        return self.next_update < other.next_update

    def update_next_step(self, current_t):
        if current_t < self.start_time:
            self.next_update = self.start_time
            return
        elif self.template.refresh_interval > 0:
            next_refresh = round(current_t + SEC_TO_MS)
            if next_refresh <= self.end_time:
                self.next_update = next_refresh
                self.next_step = "refresh"
                return
        self.next_update = self.end_time
        self.next_step = "delete"

    def get_targets(self):
        return self.resolved_targets
    
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
        target_resolver_fn = lambda _: [9]  # Enemy at index 9
        max_stack = 0
        refresh_interval = SEC_TO_MS
        super().__init__(status_id, caster, target_resolver_fn, max_stack, refresh_interval, "debuff")
        self.duration = duration
    
    def apply_fn(self, reservation, target_id, current_time):
        pass

    def refresh_fn(self, reservation, target_id, current_time):
        DebuffDamageRefresh(reservation, current_time, 10)

    def delete_fn(self, reservation, target_id, current_time):
        pass


class BuffStatCoeff(StatusTemplate):
    def __init__(self, status_id, caster, target_resolver_fn, duration, stat_type: StatType, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target_resolver_fn=target_resolver_fn,
                         max_stack=0,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = duration
        self.stat_type = stat_type
        self.value = value
    
    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {self.stat_type: self.value})
        
    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {self.stat_type: -self.value})


class BuffAmplify(StatusTemplate):
    def __init__(self, status_id, caster, target_resolver_fn, duration, applying_dmg_type, value):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target_resolver_fn=target_resolver_fn,
                         max_stack=0,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = duration
        self.applying_dmg_type = applying_dmg_type
        self.value = value
    
    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, self.value)
    
    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        target.add_amplify(self.applying_dmg_type, -self.value)