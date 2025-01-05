
from widgets.dps.enums import *
from widgets.dps.step_function import StepFunction

def instant_effect(hero, action_type, time, damage):
    time = int(time)
    damage_records = hero.damage_records[action_type]
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((time / MS_IN_SEC, last_cumulative_damage + damage))

def projectile_effect(hero, action_type, time, damage, hit_delay):
    time = int(time)
    damage_records = hero.damage_records[action_type]
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((int(time + hit_delay) / MS_IN_SEC, last_cumulative_damage + damage))

def buff_effect(hero, action_type, time, a):
    pass

def debuff_effect(hero, time, duration, debuff_name):
    time = int(time)
    hero.party.buff_manager.add_debuff(time, duration, debuff_name)
    num_ticks = int(duration)   # truncate decimal point; (since duration >= 0)

    match debuff_name:
        case DebuffType.Poisoning:                     # 중독 : 틱당 7.5%
            dmg_per_tick = 7.5
        case DebuffType.Sting | DebuffType.Frostbite:  # 쓰라림 및 동상 : 틱당 10%
            dmg_per_tick = 10
        case DebuffType.Burn:                          # 화상 : 틱당 30%
            dmg_per_tick = 30

    damage_records = StepFunction([(0, 0)]+[(time/MS_IN_SEC + i, dmg_per_tick * i) for i in range(1, num_ticks + 1)])
    hero.debuff_damage_records += damage_records
