from dps.action import InstantAction, StatusAction
from dps.hero import Hero
from dps.enums import *
from dps.status import BuffStatCoeff, BuffDamageReduction, target_self, target_all, StatusTemplate
from dps.stat_utils import apply_stat_bonuses


class BuffPersistenceGlobal(StatusTemplate):
    """
    A buff that applies to the caster but affects all allies.
    The buff is only visible on the caster, but the stat bonuses apply to all allies.
    """
    def __init__(self, status_id, caster):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target_resolver_fn=target_self,
                         max_stack=0,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = float('inf')
    
    def apply_fn(self, reservation, target_id, current_time):
        # Apply stat bonuses to all allies (including self)
        party = self.caster.party
        for i in party.active_indices:
            target = party.character_list[i]
            apply_stat_bonuses(target, {StatType.AttackSpeed: 33})
            target.add_amplify(DamageType.Skill, 50)

        
    def delete_fn(self, reservation, target_id, current_time):
        # It should never be deleted
        raise ValueError("BuffPersistenceGlobal should never be deleted")


class Vela(Hero):
    lowerskill_value = [(450 + 25 * level, 20 + level) for level in range(13)]
    upperskill_value = [(600 + 20 * level, 180 + 20 * level, 40 + 2 * level) for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.motion_time = {
            MovementType.AutoAttackBasic: MAX_MOTION_TIME,
            MovementType.AutoAttackEnhanced: MAX_MOTION_TIME,
            MovementType.LowerSkill: 3.35,
            MovementType.UpperSkill: 4.97,
        }


    def _setup_status_templates(self):
        name = self.get_unique_name()
        _, atk_buff_value = self.lowerskill_value[self.lowerskill_level - 1]
        
        self.status_templates[f"{name}_존속"] = BuffStatCoeff(
            status_id=f"{name}_존속",
            caster=self,
            duration=7.0,
            stat_bonuses={
                StatType.AttackPhysic: atk_buff_value,
                StatType.AttackMagic: atk_buff_value,
                StatType.Hp: 30
            },
            target_resolver_fn=target_all
        )
        
        # If not A2, it is a dummy buff
        self.status_templates[f"{name}_영속"] = BuffStatCoeff(
            status_id=f"{name}_영속",
            caster=self,
            duration=float('inf'),
            stat_bonuses={},
            target_resolver_fn=target_self
        )
        
        # Apply damage reduction when 'Endurance' is triggered (A2)
        self.status_templates[f"{name}_A2_존속_피해감소"] = BuffDamageReduction(
            status_id=f"{name}_A2_존속_피해감소",
            caster=self,
            duration=7.0,
            applying_dmg_type=DamageType.ALL,
            value=25,
            target_resolver_fn=target_all
        )

    def _setup_basic_attack_actions(self):
        action1 = InstantAction(
            hero=self,
            damage_coeff=60,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        
        action2 = InstantAction(
            hero=self,
            damage_coeff=60,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        
        return [[(action1, 0.15), (action2, 0.47)]]

    def _setup_enhanced_attack_actions(self):
        action = InstantAction(
            hero=self,
            damage_coeff=200,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        
        return [[(action, 0.58)]]

    def _setup_lower_skill_actions(self):
        damage, _ = self.lowerskill_value[self.lowerskill_level - 1]
        damage_action = InstantAction(
            hero=self,
            damage_coeff=damage,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.LowerSkill,
        )
        
        endurance_buff = StatusAction(
            hero=self,
            status_template=self.status_templates[f"{self.get_unique_name()}_존속"],
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE
        )
        
        persistence_buff = StatusAction(
            hero=self,
            status_template=self.status_templates[f"{self.get_unique_name()}_영속"],
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE
        )
        
        return [[(damage_action, 0.58), (endurance_buff, 0.58), (persistence_buff, 0.58)]]

    def _setup_upper_skill_actions(self):
        damage, hp_restore_all, hp_restore_self = self.upperskill_value[self.upperskill_level - 1]
        
        damage_action = InstantAction(
            hero=self,
            damage_coeff=damage,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.UpperSkill,
        )
        
        # self heal at 71% (not implemented)
        return [[(damage_action, 0.09)]]

    def _setup_aside_skill_l2(self):
        # Apply damage reduction buff when 'Endurance' is triggered
        # Get the original lower skill actions and add a new action       
        damage_reduction_buff = StatusAction(
            hero=self,
            status_template=self.status_templates[f"{self.get_unique_name()}_A2_존속_피해감소"],
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE
        )
        
        self._action_templates[MovementType.LowerSkill][0].append((damage_reduction_buff, 0.61))
        
        # Override the 'Persistence' template to 'BuffPersistenceGlobal'
        name = self.get_unique_name()
        self.status_templates[f"{name}_영속"] = BuffPersistenceGlobal(
            status_id=f"{name}_영속",
            caster=self,
        )
    
    def _initialize_aside_skill_l3(self):
        # Increase damage dealt by all allies by 22.5%
        for ally_idx in self.party.active_indices:
            ally = self.party.character_list[ally_idx]
            ally.add_amplify(DamageType.ALL, 22.5)