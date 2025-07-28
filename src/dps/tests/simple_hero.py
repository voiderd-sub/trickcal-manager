from dps.hero import Hero
from dps.enums import *
from dps.action import InstantAction, ProjectileAction

class SimpleHero(Hero):
    BASIC_DMG = 100
    lowerskill_value = [1000] * 13
    upperskill_value = [1000000] * 13

    def __init__(self, name="SimpleHero"):
        info = {
            "name": name,
            "name_kr": name,
            "attack": 100,
            "init_sp": 0,
            "max_sp": 100,
            "sp_per_aa": 0,
            "sp_recovery_rate": 10,
            "attack_speed": 300,
            "lowerskill_level": 1,
            "upperskill_level": 1,
            "aside_level": 0,
            "upper_skill_cd": 30,
            "attack_type": AttackType.Physic,
        }
        super().__init__(info)
        self.motion_time = {
            MovementType.AutoAttackBasic: 1,
            MovementType.AutoAttackEnhanced: 1,
            MovementType.LowerSkill: 2,
            MovementType.UpperSkill: 3,
        }

    def BasicAttack(self, t):
        action = InstantAction(
            self, 
            SimpleHero.BASIC_DMG, 
            MovementType.AutoAttackBasic, 
            DamageType.AutoAttackBasic,
            post_fn=lambda action: self.aa_post_fn()
        )
        motion_time = self.get_motion_time(MovementType.AutoAttackBasic)
        self.reserv_action(action, t + 0.5 * motion_time)
        return motion_time

    def LowerSkill(self, t):
        action = ProjectileAction(self, SimpleHero.lowerskill_value[self.lowerskill_level], 1.5, MovementType.LowerSkill, DamageType.LowerSkill)
        motion_time = self.get_motion_time(MovementType.LowerSkill)
        self.reserv_action(action, t + 0.5 * motion_time)
        return motion_time

    def UpperSkill(self, t):
        action = InstantAction(self, SimpleHero.upperskill_value[self.upperskill_level], MovementType.UpperSkill, DamageType.UpperSkill)
        motion_time = self.get_motion_time(MovementType.UpperSkill)
        self.reserv_action(action, t + 0.5 * motion_time)
        return motion_time