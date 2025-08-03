from dps.action import ProjectileAction, InstantAction
from dps.hero import Hero
from dps.enums import *
from dps.stat_utils import apply_stat_bonuses
import numpy as np



class Sylla(Hero):
    lowerskill_value = [390, 410, 440, 470, 500,
                        540, 590, 630, 690, 740,
                        790, 840, 890]
    upperskill_value = [1019, 1071, 1145, 1229, 1313,
                        1418, 1533, 1659, 1806, 1953,
                        2100, 2247, 2394]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.exclusive_weapon_name = "실라의 바람살"

        self.motion_time = {
            MovementType.AutoAttackBasic: 1.0,
            MovementType.LowerSkill: 2.5,
            MovementType.UpperSkill: 3.6,
        }

    def _setup_basic_attack_actions(self):
        action = ProjectileAction(
            hero=self,
            damage_coeff=70,
            hit_delay=0.63,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        return [(action, 0.45)]

    def _setup_enhanced_attack_actions(self):
        return []

    def _setup_lower_skill_actions(self):
        actions = []
        total_damage = self.lowerskill_value[self.lowerskill_level - 1]
        damage_per_hit = total_damage / 5
        
        t_ratios = [0.18, 0.30, 0.67, 0.70, 0.73]
        for t_ratio in t_ratios:
            damage_action = InstantAction(
                hero=self,
                damage_coeff=damage_per_hit,
                source_movement=MovementType.LowerSkill,
                damage_type=DamageType.LowerSkill,
            )
            actions.append((damage_action, t_ratio))

        return actions

    def _setup_upper_skill_actions(self):
        damage = self.upperskill_value[self.upperskill_level - 1]
        action = ProjectileAction(
            hero=self,
            damage_coeff=damage,
            hit_delay=0.3,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.UpperSkill,
        )
        return [(action, 0.59)]

    def _setup_aside_skill_l2(self):
        def whirlwind_on_hit():
            if self.party.rng.random() < 0.75:
                whirlwind_action = InstantAction(
                    hero=self,
                    damage_coeff=120,
                    source_movement=MovementType.AsideSkill,
                    damage_type=DamageType.AsideSkill
                )
                self.reserv_action(whirlwind_action, self.party.current_time)
        self.aa_post_fns.append(whirlwind_on_hit)

    def _initialize_aside_skill_l2(self):
        apply_stat_bonuses(self, {StatType.AttackSpeed: 40})

    def _setup_ew_l1(self):
        self.motion_time[MovementType.AutoAttackBasic] = MAX_MOTION_TIME
        
        action1 = ProjectileAction(
            hero=self,
            damage_coeff=80,
            hit_delay=0.5,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        action2 = ProjectileAction(
            hero=self,
            damage_coeff=80,
            hit_delay=0.6,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        # This will be sorted in `_setup_all_movement_actions`
        self._action_templates[MovementType.AutoAttackBasic] = [(action1, 0.45), (action2, 0.80)]
    
    def _initialize_ew_l3(self):
        # additional attackspeed 12.5%
        apply_stat_bonuses(self, {StatType.AttackSpeed: 12.5})