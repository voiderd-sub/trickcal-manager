from widgets.dps.enums import *

import numpy as np
from collections import defaultdict


def find_valid_skill_level(L, i):
    for j in range(i-1, -1, -1):
        if L[j] is not None:
            return j+1
    return 0


class Hero:
    def __init__(self, user_provided_info):
        for key, value in user_provided_info.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return self.name if hasattr(self, "name") else "HeroNameDefault"

    def init_simulation(self):
        # Check skill level data is exists.
        # If not, use the value of the level that has data but is lower than the user's skill level.
        for skill_type in ["lowerskill", "upperskill"]:
            skill_values = getattr(self, skill_type+"_value", None)
            if not skill_values:
                user_level = getattr(self, skill_type+"_level")
                valid_level = find_valid_skill_level(skill_values, user_level)
                if user_level != valid_level:
                    setattr(self, skill_type+"_level", valid_level)
                    print(f"Data for {skill_type} level {user_level} is not exists.")
                    print(f"Use data of level {valid_level} instead.")

        self.aa_cd = int(300 * MS_IN_SEC / self.attack_speed)
        self.sp = self.init_sp
        self.sp_timer = 0
        self.upper_skill_timer = int(self.upper_skill_cd * MS_IN_SEC * 0.5)
        self.aa_timer = 0
        self.last_updated = 0
        self.last_action = ActionType.Wait
        self.last_action_time = 0
        if not hasattr(self, "atk"):
            self.atk = 100
        self.amplify = 0.
        self.atk_coeff = 1.
        self.attack_speed_coeff = 1.
        self.acceleration = 1.

        self.action_log = []
        self.action_timestamps = {action: [] for action in ActionType if action != ActionType.Wait}
        self.damage_records = defaultdict(list)

    def choose_action(self):
        if self.sp == self.max_sp:
            return ActionType.LowerSkill
        elif self.upper_skill_timer == 0:
            return ActionType.UpperSkill
        elif self.aa_timer == 0:
            if self.is_enhanced(): return ActionType.AutoAttackEnhanced
            else:                  return ActionType.AutoAttackBasic
        return ActionType.Wait

    def update(self, t):
        # update sp
        dt = t - self.last_updated
        if self.last_action not in (ActionType.LowerSkill, ActionType.UpperSkill):
            self.sp_timer += dt
            if self.sp_timer >= SP_INTERVAL:
                num_sp_recover, self.sp_timer = divmod(self.sp_timer, SP_INTERVAL)
                self.sp = min(self.max_sp, self.sp + self.sp_recovery_rate * num_sp_recover)

        # update cd
        self.aa_timer = max(0, self.aa_timer - dt)
        self.upper_skill_timer = max(0, self.upper_skill_timer - dt)
        self.aa_cd = int(300 * MS_IN_SEC / (self.acceleration**2 * self.attack_speed_coeff * self.attack_speed))

        self.last_updated = t

    def step(self, t):
        self.update(t)
        action = self.choose_action()

        match action:
            case ActionType.AutoAttackBasic | ActionType.AutoAttackEnhanced:
                self.aa_timer = self.aa_cd
                if action == ActionType.AutoAttackBasic:
                    dt = self.BasicAttack(t)
                else:
                    dt = self.EnhancedAttack(t)
            case ActionType.LowerSkill:
                self.sp = 0
                dt = self.LowerSkill(t)
            case ActionType.UpperSkill:
                self.upper_skill_timer = int(self.upper_skill_cd * MS_IN_SEC)
                dt = self.UpperSkill(t)
            case ActionType.Wait:
                dt = min(SP_INTERVAL - self.sp_timer, self.aa_timer, self.upper_skill_timer)
        
        self.last_action = action
        self.action_log.append((t / MS_IN_SEC, action))
        if action != ActionType.Wait:
            self.action_timestamps[action].append(t / MS_IN_SEC)

        return t + dt
    
    def calculate_cumulative_damage(self, max_T):
        for key, record in self.damage_records.items():
            for i in range(len(record) - 1, -1, -1):
                if record[i][0] < max_T:
                    self.damage_records[key] = record[i][1]
                    break
        
    def BasicAttack(self, t):
        pass

    def EnhancedAttack(self, t):
        pass

    def LowerSkill(self, t):
        pass

    def UpperSkill(self, t):
        pass

    def is_enhanced(self):
        return False

    def trigger_enhanced(self):
        pass
    
    def add_buff(self, buff):
        self.party.buff_manager.add_buff(buff)
    
    def get_damage(self, damage):
        enemy_amplify = self.party.get_amplify(self)
        additional_coeff = self.party.get_additional_coeff(self)
        amplify = max(0.25, 1 + self.amplify + enemy_amplify)
        return 0.8 * (self.atk * self.atk_coeff) * amplify * (damage/100) * additional_coeff


class EnhancedAttackChecker:
    def __init__(self, hero):
        self.hero = hero
    
    def is_enhanced(self):
        raise NotImplementedError


class ProbabilisticEAC(EnhancedAttackChecker):
    def __init__(self, hero, p):
        super().__init__(hero)
        self.p = p

    def is_enhanced(self):
        return np.random.rand() < self.p

class PeriodicEAC(EnhancedAttackChecker):
    def __init__(self, hero, cycle):
        super().__init__(hero)
        self.cycle = cycle

    def is_enhanced(self):
        timestamp = self.hero.action_timestamps
        num_attack = len(timestamp[ActionType.AutoAttackBasic]) + len(timestamp[ActionType.AutoAttackEnhanced])
        return (num_attack+1) % self.cycle == 0

class BuffedEAC(EnhancedAttackChecker):
    def __init__(self, hero, buff_id):
        super().__init__(hero)
        self.buff_id = buff_id

    def is_enhanced(self):
        party = self.hero.party
        return self.hero.has_buff(self.buff_id)