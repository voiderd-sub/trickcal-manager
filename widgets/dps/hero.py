from .enums import *
from .step_function import StepFunction

import numpy as np
from collections import defaultdict


class Hero:
    def __init__(self, user_provided_info):
        for key, value in user_provided_info.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return self.name if hasattr(self, "name") else "HeroNameDefault"

    def init_simulation(self):
        self.aa_cd = int(300 * MS_IN_SEC / self.attack_speed)
        self.sp = self.init_sp
        self.sp_timer = 0
        self.upper_skill_timer = int(self.upper_skill_cd * MS_IN_SEC * 0.5)
        self.aa_timer = 0
        self.last_updated = 0
        self.last_action = ActionType.Wait
        self.last_action_time = 0
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
        """
        action_log를 기반으로 누적 대미지를 계산합니다.
        대미지는 일반공격, 강화공격, Lower Skill, Upper Skill로 나눠 계산됩니다.
        """
        # 공격 유형별로 대미지를 저장할 딕셔너리
        cumulative_damage_data = {
            ActionType.AutoAttackBasic: [],
            ActionType.AutoAttackEnhanced: [],
            ActionType.LowerSkill: [],
            ActionType.UpperSkill: [],
        }

        # 각 공격 유형에 대한 기본 데이터
        damage_data = {
            ActionType.AutoAttackBasic: {
                "motion_time": self.aa_motion_time[ActionType.AutoAttackBasic],
                "coefficients": [0.5, 0.5],  # 예: 두 번의 타격, 각각 50% 대미지
                "delay_factors": [0.5, 1.0],  # 예: 첫 번째 타격 50%, 두 번째 타격 100% 지연
            },
            ActionType.AutoAttackEnhanced: {
                "motion_time": self.aa_motion_time[ActionType.AutoAttackEnhanced],
                "coefficients": [1.0],  # 강화공격 한 번의 타격
                "delay_factors": [0.7],  # 타격이 70% 모션 시간 후 발생
            },
            ActionType.LowerSkill: {
                "motion_time": self.lower_skill_motion_time,
                "coefficients": [1.5],  # 스킬의 총 대미지 계수
                "delay_factors": [0.5],  # 50% 모션 시간 후 발생
            },
            ActionType.UpperSkill: {
                "motion_time": self.upper_skill_motion_time,
                "coefficients": [3.0, 1.0],  # 스킬의 여러 타격 계수
                "delay_factors": [0.3, 0.9],  # 첫 타격 30%, 두 번째 타격 90% 후 발생
            },
        }

        for timestamp, action in self.action_log:
            if action not in damage_data:
                continue

            damage_info = damage_data[action]
            motion_time = damage_info["motion_time"]
            coefficients = damage_info["coefficients"]
            delay_factors = damage_info["delay_factors"]

            for coeff, delay_factor in zip(coefficients, delay_factors):
                damage_time = timestamp + motion_time * delay_factor
                damage = coeff * getattr(self, "attack_power", 1)  # 기본 공격력 1

                # 타임스탬프와 대미지를 누적
                cumulative_damage_data[action].append((damage_time, damage))

        # 누적 대미지 리스트를 StepFunction으로 변환
        cumulative_damage = {}
        for action, data in cumulative_damage_data.items():
            if data:
                breakpoints = [0] + [t for t, _ in data] + [max_T]
                values = [0] + np.cumsum([d for _, d in data]).tolist()
                cumulative_damage[action] = StepFunction(
                    np.array(breakpoints, dtype=float),
                    np.array(values, dtype=float)
                )
                print(action)
                print(cumulative_damage[action].breakpoints)
                print(cumulative_damage[action].values)
            else:
                cumulative_damage[action] = StepFunction.from_constant(0, 0, 0)

        return cumulative_damage
    
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