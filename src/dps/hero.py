from dps.enums import *
from dps.action import InstantAction

import numpy as np
from collections import defaultdict
import random


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

        self.aa_cd = int(300 * SEC_TO_MS / self.attack_speed)
        self.sp = self.init_sp
        self.sp_timer = 0
        self.upper_skill_timer = int(self.upper_skill_cd * SEC_TO_MS * 0.5)
        self.aa_timer = 0
        self.last_updated = 0
        self.last_movement = MovementType.Wait
        self.last_movement_time = 0
        if not hasattr(self, "atk"):
            self.atk = 100
        self.amplify_dict = {dt: 0.0 for dt in DamageType.leaf_types()}
        self.atk_coeff = 1.
        self.attack_speed_coeff = 1.
        self.acceleration = 1.

        self.movement_log = []
        self.movement_timestamps = {MovementType.AutoAttackBasic: [],
                                  MovementType.AutoAttackEnhanced: [],
                                  MovementType.LowerSkill: [],
                                  MovementType.UpperSkill: [],
                                  }
        self.damage_records = defaultdict(list)
        
        # 제거: action_templates, current_movement_actions, current_action_index 관련 코드
        # self.action_templates = {i: [] for i in MovementType}
        # self.current_movement_actions = []
        # self.current_action_index = 0
        
        # 제거: self.init_movements() 호출

        self.last_motion_time = 0  # 단일 값으로 변경

    # 제거: init_movements() 메서드

    def schedule_action_template(self, action, time, delay=0):
        """Schedule an action with the given time and delay"""
        self.reserv_action((time, delay, action))

    def choose_movement(self):
        if self.sp == self.max_sp:
            return MovementType.LowerSkill
        elif self.upper_skill_timer == 0:
            return MovementType.UpperSkill
        elif self.aa_timer == 0:
            if self.is_enhanced(): return MovementType.AutoAttackEnhanced
            else:                  return MovementType.AutoAttackBasic
        return MovementType.Wait

    def update(self, t):
        # update sp
        dt = t - self.last_updated
        if self.last_movement not in (MovementType.LowerSkill, MovementType.UpperSkill):
            self.sp_timer += dt
            if self.sp_timer >= SP_INTERVAL:
                num_sp_recover, self.sp_timer = divmod(self.sp_timer, SP_INTERVAL)
                self.sp = min(self.max_sp, self.sp + self.sp_recovery_rate * num_sp_recover)

        # update cd
        self.aa_timer = max(0, self.aa_timer - dt)
        self.upper_skill_timer = max(0, self.upper_skill_timer - dt)
        self.aa_cd = self.get_aa_cd()

        self.last_updated = t

    def step(self, t):
        self.update(t)
        movement = self.choose_movement()
        match movement:
            case MovementType.AutoAttackBasic | MovementType.AutoAttackEnhanced:
                self.aa_timer = self.aa_cd
            case MovementType.LowerSkill:
                self.sp = 0
            case MovementType.UpperSkill:
                self.upper_skill_timer = int(self.upper_skill_cd * SEC_TO_MS)
            case MovementType.Wait:
                dt = min(SP_INTERVAL - self.sp_timer, self.aa_timer, self.upper_skill_timer)
        if movement != MovementType.Wait:
            dt = self.do_movement(movement, t)
            self.movement_timestamps[movement].append(int(t // SEC_TO_MS))
        self.last_movement = movement
        self.movement_log.append((int(t // SEC_TO_MS), movement))
        return t + dt
    
    def calculate_cumulative_damage(self, max_T):
        for key, record in self.damage_records.items():
            for i in range(len(record) - 1, -1, -1):
                if record[i][0] < max_T:
                    self.damage_records[key] = record[i][1]
                    break
        
    def do_movement(self, movement_type, t):
        motion_time = self.get_motion_time(movement_type)
        self.last_motion_time = motion_time
        self.last_updated = t
        
        # movement별 첫 번째 액션 예약
        if movement_type == MovementType.AutoAttackBasic:
            self.BasicAttack(t)
        elif movement_type == MovementType.AutoAttackEnhanced:
            self.EnhancedAttack(t)
        elif movement_type == MovementType.LowerSkill:
            self.LowerSkill(t)
        elif movement_type == MovementType.UpperSkill:
            self.UpperSkill(t)
        
        return motion_time

    # 제거: schedule_next_action() 메서드

    # Placeholder 메서드들 (하위 클래스에서 구현)
    def BasicAttack(self, t):
        """기본 공격 - 하위 클래스에서 구현"""
        raise NotImplementedError

    def EnhancedAttack(self, t):
        """강화 공격 - 하위 클래스에서 구현"""
        raise NotImplementedError

    def LowerSkill(self, t):
        """저학년 스킬 - 하위 클래스에서 구현"""
        raise NotImplementedError

    def UpperSkill(self, t):
        """고학년 스킬 - 하위 클래스에서 구현"""
        raise NotImplementedError

    def is_enhanced(self):
        return False

    def trigger_enhanced(self):
        pass
    
    def reserv_action(self, action_tuple):
        self.party.action_manager.add_action_reserv(action_tuple)

    def aa_post_fn(self):
        self.sp = min(self.max_sp, self.sp + self.sp * self.sp_per_aa)

    def get_aa_cd(self):
        return int(300 * SEC_TO_MS / (self.acceleration**2 * min(10., self.attack_speed_coeff) * self.attack_speed))
    
    def get_motion_time(self, movement_type: MovementType):
        match movement_type:
            case MovementType.AutoAttackBasic:
                return min(self.motion_time["Basic"], self.get_aa_cd())
            case MovementType.AutoAttackEnhanced:
                return min(self.motion_time["Basic"], self.get_aa_cd())
            case MovementType.LowerSkill:
                return self.motion_time["LowerSkill"] / self.acceleration
            case MovementType.UpperSkill:
                return self.motion_time["UpperSkill"] / self.acceleration

        return
    

    def get_amplify(self, damage_type):
        return self.amplify_dict[damage_type]

    def add_amplify(self, damage_type: DamageType, value: float):
        for dt in DamageType.get_leaf_members(damage_type):
            self.amplify_dict[dt] += value
    
    def get_damage(self, damage, movement_type):
        enemy_amplify = self.party.get_amplify(self)
        additional_coeff = self.party.get_additional_coeff(self)        # 성격시너지 등
        amplify = max(0.25, 1 + self.get_amplify(movement_type) + enemy_amplify)
        return 0.8 * (self.atk * self.atk_coeff) * amplify * (damage/100) * additional_coeff

    def get_name(self):
        return self.name_kr

    def has_buff(self, buff_id):
        return self.party.status_manager.has_buff(self.party_idx, buff_id)

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
        timestamps = self.hero.movement_timestamps
        num_attack = len(timestamps[MovementType.AutoAttackBasic]) + len(timestamps[MovementType.AutoAttackEnhanced])
        return (num_attack+1) % self.cycle == 0