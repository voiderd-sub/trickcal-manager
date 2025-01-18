from widgets.dps.enums import *
from widgets.dps.effect import *
from widgets.dps.status_manager import Status

import numpy as np
from functools import partial


# Apply damage
def DebuffDamageRefresh(status, current_time, damage):
    hero = status.caster
    instant_effect(hero, "Debuff", current_time, damage)


class DebuffSting(Status):
    def __init__(self, status_id, caster, start_time, duration):
        target = [0]
        start_time, end_time = int(start_time), int(start_time + duration * MS_IN_SEC)
        max_stack = 0
        refresh_interval = MS_IN_SEC

        super().__init__(status_id, caster, target, start_time, end_time, max_stack, refresh_interval)
    
    def apply_fn(self, target_id, current_time):
        pass

    def refresh_fn(self, target_id, current_time):
        DebuffDamageRefresh(self, current_time, 10)

    def delete_fn(self, target_id, current_time):
        pass