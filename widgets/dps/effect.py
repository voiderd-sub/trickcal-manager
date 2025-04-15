
from widgets.dps.enums import *


# Class for applying effects
class Effect:
    def __init__(self,
                 time: float,
                 hero,   # Hero
                 effect_type: EffectType,
                 source_action: ActionType = None,
                 damage_type: DamageType = None,
                 post_fn = None):
        self.time = int(time)
        self.hero = hero
        self.source_action = source_action
        self.damage_type = damage_type if damage_type else ActionType.act_type_to_dmg_type(source_action)
        self.effect_type = effect_type  # Instant, Buff, Debuff, Projectile
        self.post_fn = post_fn

    def __lt__(self, other):
        return self.time < other.time

    def get_starting_time(self):
        return self.time


def apply_instant_effect(hero, damage_type, time, damage_coeff, action_type=None):
    time = int(time)
    action_type = action_type if action_type else damage_type.name
    damage_records = hero.damage_records[action_type]
    damage = hero.get_damage(damage_coeff, damage_type)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((time / SEC_TO_MS, last_cumulative_damage + damage))

def apply_delayed_effect(hero, damage_type, time, damage_coeff, hit_delay, action_type=None):
    action_type = action_type if action_type else damage_type.name
    damage_records = hero.damage_records[action_type]
    damage = hero.get_damage(damage_coeff, damage_type)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((int(time + hit_delay) / SEC_TO_MS, last_cumulative_damage + damage))


class InstantEffect(Effect):
    def __init__(self, time, hero, damage_coeff, source_action=None, damage_type=None, post_fn=None):
        super().__init__(time, hero, EffectType.Instant, source_action, damage_type, post_fn)
        self.damage_coeff = damage_coeff

    def effect_fn(self):
        apply_instant_effect(hero = self.hero,
                             damage_type = self.damage_type,
                             time = self.time,
                             damage_coeff = self.damage_coeff,
                             action_type = self.source_action)
        if self.post_fn:
            self.post_fn()


class DelayedEffect(Effect):
    def __init__(self, time, hero, damage_coeff, delay=0, source_action=None, damage_type=None, post_fn=None):
        super().__init__(int(time + delay), hero, EffectType.Delayed, source_action, damage_type, post_fn)
        self.damage_coeff = damage_coeff
        self.delay = delay

    def effect_fn(self):
        apply_delayed_effect(hero = self.hero,
                             damage_type = self.damage_type,
                             time = self.time,
                             damage_coeff = self.damage_coeff,
                             hit_delay = self.delay,
                             action_type = self.source_action)
        if self.post_fn:
            self.post_fn()
    
    def get_starting_time(self):
        return int(self.time - self.delay)


# 이거 2개 구현할 필요 없지 않음?
class BuffEffect(Effect):
    pass

class DebuffEffect(Effect):
    pass
