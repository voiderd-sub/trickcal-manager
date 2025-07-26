from dps.action import *
from dps.hero import Hero


class Daya(Hero):
    lowerskill_value = [236, None, None, None, None, None, None, None, None, 454, 488, 522, 556]
    upperskill_value = [322, None, None, None, None, None, None, None, 572, 619, 666, 713, 760]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)

        self.hero_id = 14
        self.name = "Daya"
        self.name_kr = "다야"

        self.attack_type = AttackType.Magic
        self.personality = Personality.Naive
        self.attack_speed = 118
        self.init_sp = 0
        self.max_sp = 370
        self.sp_recovery_rate = 24
        self.sp_per_aa = 1
        self.upper_skill_cd = 40

        self.motion_time = {
            "Basic" : 1.836 * SEC_TO_MS,
            "Enhanced" : VERY_BIG_NUMBER,
            "LowerSkill" : 2.166 * SEC_TO_MS,
            "UpperSkill" : 3.866 * SEC_TO_MS,
        }
        self.eac = ProbabilisticEAC(self, 0.4)
    
    def is_enhanced(self):
        return self.eac.is_enhanced()
    
    def BasicAttack(self, t):
        motion_time = min(int(self.motion_time["Basic"]), self.aa_cd)
        action_list = [(0.5000, 13.5), (0.5625, 18), (0.6250, 13.5)]
        delay = 0.3 * SEC_TO_MS
        for t_ratio, damage in action_list:
            action = ProjectileAction(time = t + motion_time * t_ratio,
                                   hero = self,
                                   damage_coeff = damage,
                                   base_delay = delay,
                                   source_movement = MovementType.AutoAttackBasic,
                                   damage_type = DamageType.AutoAttackBasic)
            self.reserv_action(action)
        return motion_time
    
    def EnhancedAttack(self, t):
        motion_time = min(self.motion_time["Enhanced"], self.aa_cd)
        shoot_time = t + motion_time * 0.5800
        delay = 0.3 * SEC_TO_MS
        debuff_sting_enhanced_attack = DebuffSting(f"다야_{self.party_idx}_강평", self, 4)
        self.reserv_status(debuff_sting_enhanced_attack)
        action = ProjectileAction(time = shoot_time,
                                hero = self,
                                damage_coeff = 100.,
                                base_delay = delay,
                                source_movement = MovementType.AutoAttackEnhanced,
                                damage_type = DamageType.AutoAttackEnhanced)
        self.reserv_action(action)
        return motion_time

    def LowerSkill(self, t):
        motion_time = self.motion_time["LowerSkill"] / self.acceleration
        hit_time = t + motion_time * 0.5800
        damage = self.lowerskill_value[self.lowerskill_level-1]
        debuff_sting_lowerskill = DebuffSting(f"다야_{self.party_idx}_저학년", self, 8)
        self.reserv_status(debuff_sting_lowerskill)
        action = InstantAction(time = hit_time,
                                hero = self,
                                damage_coeff = damage,
                                source_movement = MovementType.LowerSkill,
                                damage_type = DamageType.LowerSkill)       
        self.reserv_action(action)
        return motion_time

    def UpperSkill(self, t):
        motion_time = self.motion_time["UpperSkill"] / self.acceleration
        hit_time = t + motion_time * 0.4450
        damage = self.upperskill_value[self.upperskill_level-1]
        action = InstantAction(time = hit_time,
                                hero = self,
                                damage_coeff = damage,
                                source_movement = MovementType.UpperSkill,
                                damage_type = DamageType.UpperSkill)
        self.reserv_action(action)
        return motion_time
