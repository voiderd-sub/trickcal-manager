
from widgets.dps.enums import *
from widgets.dps.step_function import StepFunction

def instant_effect(hero, action_type, time, damage_coeff):
    time = int(time)
    damage_records = hero.damage_records[action_type]
    damage = hero.get_damage(damage_coeff)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((time / MS_IN_SEC, last_cumulative_damage + damage))

def projectile_effect(hero, action_type, time, damage_coeff, hit_delay):
    time = int(time)
    damage_records = hero.damage_records[action_type]
    damage = hero.get_damage(damage_coeff)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((int(time + hit_delay) / MS_IN_SEC, last_cumulative_damage + damage))

def buff_effect(hero, action_type, time, a):
    pass

def debuff_effect(hero, status):
    hero.party.buff_manager.add_status_reserv(status)
