from dps.action import *
from dps.hero import Hero, ProbabilisticCondition, BuffCondition, OrCondition
from dps.status import (BuffStatCoeff, BuffAmplify, 
                        target_self, target_all, target_all_wo_self)
from dps.enums import *
from dps.data.hero_data import HERO_DATA


class Epica(Hero):
    lowerskill_value = [(60 + 3 * level, 8 + 0.5 * level) for level in range(13)]
    upperskill_value = [72 + 6 * level for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
  
        self.motion_time = {
            MovementType.AutoAttackBasic: [1.690, 1.690],
            MovementType.AutoAttackEnhanced: [1.667, 1.667],
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
            stat_bonuses={StatType.AttackSpeed: self_as_buff_val},
            target_resolver_fn=target_self
        )
        self.status_templates[f"{name}_저학년_전체"] = BuffStatCoeff(
            status_id=f"{name}_저학년_전체",
            caster=self, 
            duration=10.0, 
            stat_bonuses={StatType.AttackSpeed: other_as_buff_val},
            target_resolver_fn=target_all_wo_self
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
        basic_template = []
        action = ProjectileAction(
            hero=self,
            damage_coeff=100,
            hit_delay=0.5,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        basic_template.append((action, 0.65))
        
        a2_template = []
        action1 = ProjectileAction(
            hero=self,
            damage_coeff=100,
            hit_delay=0.5,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        action2 = ProjectileAction(
            hero=self,
            damage_coeff=100,
            hit_delay=0.5,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        a2_template.append((action1, 0.65))
        a2_template.append((action2, 0.71))
        
        return [basic_template, a2_template]

    def _setup_enhanced_attack_actions(self):
        basic_template = []
        action = ProjectileAction(
            hero=self,
            damage_coeff=200,
            hit_delay=1.05,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        basic_template.append((action, 0.71))
        
        a2_template = []
        action1 = ProjectileAction(
            hero=self,
            damage_coeff=200,
            hit_delay=1.05,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        action2 = ProjectileAction(
            hero=self,
            damage_coeff=200,
            hit_delay=1.05,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        a2_template.append((action1, 0.71))
        a2_template.append((action2, 0.95))
        
        return [basic_template, a2_template]
    
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
        
        return [[(self_buff_action, 0.55), (other_buff_action, 0.55)]]

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
        
        return [[(buff_action, 0.09)] + damage_actions]

    def _setup_aside_skill_l2(self):
        # Override action template selection if aside level is 2 or higher
        # The increased enhanced attack probability is handled in setup_eac.
        self._choose_basic_attack_template = lambda: 1
        self._choose_enhanced_attack_template = lambda: 1
    
    def _initialize_aside_skill_l3(self):
        # Increase middle row damage dealt by 19.5%, reduce damage taken by 9.75%
        for ally_idx in self.party.active_indices:
            ally = self.party.character_list[ally_idx]
            if ally.party_idx // 3 == 1:    # middle row
                ally.reduce_damage_taken(DamageType.ALL, 9.75) 
                ally.add_amplify(DamageType.ALL, 19.5)

    def setup_eac(self):
        prob = 0.25 + (0.15 if self.aside_level >= 2 else 0)
        buff_cond = BuffCondition(self, f"{self.get_unique_name()}_저학년")
        prob_cond = ProbabilisticCondition(self, prob)
        return OrCondition(self, buff_cond, prob_cond)
