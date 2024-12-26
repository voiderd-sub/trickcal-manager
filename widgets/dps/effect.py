

def instant_effect(hero, action_type, time, damage):
    damage_records = hero.damage_records[action_type]
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append(time, last_cumulative_damage + damage)

def projectile_effect(hero, action_type, time, damage, hit_delay):
    damage_records = hero.damage_records[action_type]
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append(time + hit_delay, last_cumulative_damage + damage)

def buff_effect(hero, action_type, time, a):
    pass

def debuff_effect(hero, time, debuff_name):
    hero.party.apply_debuff(time, debuff_name)