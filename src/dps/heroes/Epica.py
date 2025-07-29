from dps.action import *
from dps.hero import Hero, ProbabilisticCondition, BuffCondition, OrCondition
from dps.status import (BuffStatCoeff, BuffAmplify, 
                        target_self, target_all, target_all_wo_self)
from dps.enums import *


class Epica(Hero):
    lowerskill_value = [(60 + 3 * level, 8 + 0.5 * level) for level in range(13)]
    upperskill_value = [72 + 6 * level for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.hero_id = 17
        self.name = "Epica"
        self.name_kr = "에피카"
        self.is_eldain = True
        
        self.attack_type = AttackType.Physic
        self.personality = Personality.Jolly
        self.attack_speed = 102
        self.init_sp = 100
        self.max_sp = 450
        self.sp_recovery_rate = 20
        self.sp_per_aa = 0
        self.upper_skill_cd = 54

        self.motion_time = {
            MovementType.AutoAttackBasic: 1.690,
            MovementType.AutoAttackEnhanced: 1.667,
            MovementType.LowerSkill: 2.900,
            MovementType.UpperSkill: 10.00,
        }

    def _setup_status_templates(self):
        self_as_buff_val, other_as_buff_val = self.lowerskill_value[self.lowerskill_level - 1]
        name = self.get_unique_name()
        
        # Lower skill templates
        self.status_templates[f"{name}_저학년"] = BuffStatCoeff(
            status_id=f"{name}_저학년",
            caster=self, 
            duration=10.0, 
            value=self_as_buff_val,
            target_resolver_fn=target_self,
            stat_type=StatType.AttackSpeed
        )
        self.status_templates[f"{name}_저학년_전체"] = BuffStatCoeff(
            status_id=f"{name}_저학년_전체",
            caster=self, 
            duration=10.0, 
            value=other_as_buff_val,
            target_resolver_fn=target_all_wo_self,
            stat_type=StatType.AttackSpeed
        )
        
        # Upper skill template
        self.status_templates[f"{name}_고학년"] = BuffAmplify(
            status_id=f"{name}_고학년",
            caster=self, 
            duration=8.0, 
            value=27,
            applying_dmg_type=DamageType.ALL,
            target_resolver_fn=target_all
        )

    def _setup_basic_attack_actions(self):
        actions_info = [(0.65, 100)]
        if self.aside_level >= 2:
            actions_info.append((0.71, 100))

        action_template = []
        for t_ratio, damage_coeff in actions_info:
            action = ProjectileAction(
                hero=self,
                damage_coeff=damage_coeff,
                hit_delay=0.5,
                source_movement=MovementType.AutoAttackBasic,
                damage_type=DamageType.AutoAttackBasic,
            )
            action_template.append((action, t_ratio))
        return action_template

    def _setup_enhanced_attack_actions(self):
        actions_info = [(0.95, 200)]
        if self.aside_level >= 2:
            actions_info.append((0.71, 200))
        
        action_template = []
        for t_ratio, damage_coeff in actions_info:
            action = ProjectileAction(
                hero=self,
                damage_coeff=damage_coeff,
                hit_delay=1.05,
                source_movement=MovementType.AutoAttackEnhanced,
                damage_type=DamageType.AutoAttackEnhanced,
            )
            action_template.append((action, t_ratio))
        return action_template
    
    def _setup_lower_skill_actions(self):
        # Self buff action
        self_buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE,
            status_template=self.status_templates[f"{self.get_unique_name()}_저학년"]
        )
        
        # Other party members buff action
        other_buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE,
            status_template=self.status_templates[f"{self.get_unique_name()}_저학년_전체"]
        )
        
        return [(self_buff_action, 0.55), (other_buff_action, 0.55)]

    def _setup_upper_skill_actions(self):
        # Damage actions
        damage_actions = []
        damage = self.upperskill_value[self.upperskill_level - 1]
        hit_delay = 0.35
        for j in range(3):
            for i in range(8):
                t_ratio = 0.28 + 0.013 * i + 0.12 * j
                action = ProjectileAction(
                    hero=self,
                    damage_coeff=damage,
                    hit_delay=hit_delay,
                    source_movement=MovementType.UpperSkill,
                    damage_type=DamageType.AutoAttackBasic,
                )
                damage_actions.append((action, t_ratio))
        
        # Buff action
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.NONE,
            status_template=self.status_templates[f"{self.get_unique_name()}_고학년"]
        )
        
        return damage_actions + [(buff_action, 0.09)]

    def setup_eac(self):
        prob = 0.25 + (0.15 if self.aside_level >= 2 else 0)
        buff_cond = BuffCondition(self, f"{self.get_unique_name()}_저학년")
        prob_cond = ProbabilisticCondition(self, prob)
        return OrCondition(self, buff_cond, prob_cond)
