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
            "hero_class": Class.Dealer,  # 역할군 추가
            "grade": 1,  # 학년 추가
            "base_stat": {
                StatType.Hp: 100,
                StatType.AttackPhysic: 100,
                StatType.AttackMagic: 100,
                StatType.DefensePhysic: 100,
                StatType.DefenseMagic: 100,
                StatType.CriticalRate: 100,
                StatType.CriticalMult: 100,
                StatType.CriticalResist: 100,
                StatType.CriticalMultResist: 100,
            },  # 기본스탯 설정
            "personal_stat": {},  # 개인스탯 (빈 딕셔너리)
            "global_stat": {},  # 전체스탯 (빈 딕셔너리)
        }
        super().__init__(info)
        self.motion_time = {
            MovementType.AutoAttackBasic: 1,
            MovementType.AutoAttackEnhanced: 1,
            MovementType.LowerSkill: 2,
            MovementType.UpperSkill: 3,
        }

    def _setup_basic_attack_actions(self):
        action = InstantAction(
            hero=self, 
            damage_coeff=SimpleHero.BASIC_DMG, 
            source_movement=MovementType.AutoAttackBasic, 
            damage_type=DamageType.AutoAttackBasic
        )
        return [[(action, 0.5)]]

    def _setup_lower_skill_actions(self):
        action = ProjectileAction(
            hero=self, 
            damage_coeff=SimpleHero.lowerskill_value[self.lowerskill_level-1], 
            hit_delay=1.5, 
            source_movement=MovementType.LowerSkill, 
            damage_type=DamageType.LowerSkill
        )
        return [[(action, 0.5)]]

    def _setup_upper_skill_actions(self):
        action = InstantAction(
            hero=self,
            damage_coeff=SimpleHero.upperskill_value[self.upperskill_level-1], 
            source_movement=MovementType.UpperSkill, 
            damage_type=DamageType.UpperSkill
        )
        return [[(action, 0.5)]]