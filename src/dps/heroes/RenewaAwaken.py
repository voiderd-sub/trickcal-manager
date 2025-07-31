from dps.action import ProjectileAction, StatusAction, InstantAction
from dps.hero import Hero, PeriodicCondition
from dps.status import BuffStatCoeff, target_self, BuffReduceDamageTakenAndAccelerate
from dps.enums import *
from functools import partial


class RenewaAwaken(Hero):
    lowerskill_value = [400 + 50 * i for i in range(13)]
    upperskill_value = [(600, 32), (720, 36), (840, 40), (960, 45), (1080, 49), (1200, 53), (1320, 57), (1440, 62), (1560, 66), (1680, 70), (1800, 74), (1920, 79), (2040, 83)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)

        self.motion_time = {
            MovementType.AutoAttackBasic: MAX_MOTION_TIME,
            MovementType.AutoAttackEnhanced: MAX_MOTION_TIME,
            MovementType.LowerSkill: 4.985,
            MovementType.UpperSkill: 16.03,
        }

    def _setup_status_templates(self):
        name = self.get_unique_name()
        self.status_templates[f"{name}_강평_공증"] = BuffStatCoeff(
            status_id=f"{name}_강평_공증",
            caster=self,
            duration=8.0,
            value=15,
            target_resolver_fn=target_self,
            stat_type=StatType.AttackPhysic,
        )

        self.status_templates[f"{name}_저학_공속증"] = BuffStatCoeff(
            status_id=f"{name}_저학_공속증",
            caster=self,
            duration=10.0,
            value=80,
            target_resolver_fn=target_self,
            stat_type=StatType.AttackSpeed,
        )

        _, accel_factor = self.upperskill_value[self.upperskill_level-1]
        self.status_templates[f"{name}_고학_피감_가속"] = BuffReduceDamageTakenAndAccelerate(
            status_id=f"{name}_고학_피감_가속",
            caster=self,
            duration=10.0,
            value=30,
            ramp_up_duration=7.0,
            hold_duration=3.0,
            max_factor=accel_factor
        )


    def _setup_basic_attack_actions(self):
        action = ProjectileAction(
            hero=self,
            damage_coeff=90,
            hit_delay=0.3,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        return [(action, 0.48)]

    def _setup_enhanced_attack_actions(self):
        name = self.get_unique_name()
        damage_action = InstantAction(
            hero=self,
            damage_coeff=360,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.NONE,
            status_template=self.status_templates[f"{name}_강평_공증"],
        )
        return [(damage_action, 0.48), (buff_action, 0.48)]

    def _setup_lower_skill_actions(self):
        actions = []
        total_damage = self.lowerskill_value[self.lowerskill_level - 1]
        damage_per_hit = total_damage / 5
        name = self.get_unique_name()

        def remove_buff():
            # A function that removes a buff and, if successful,
            # applies an attack speed buff. Currently unimplemented.
            pass
        
        def remove_shield():
            # A function that removes a shield and, if successful,
            # applies a heal. Currently unimplemented.
            pass
        
        t_ratios = [0.379, 0.426, 0.465, 0.531, 0.788]
        for i in range(5):
            if i == 0 or i == 2:
                damage_action = InstantAction(
                    hero=self,
                    damage_coeff=damage_per_hit,
                    source_movement=MovementType.LowerSkill,
                    damage_type=DamageType.LowerSkill,
                    post_fn=remove_buff,
                )
            elif i == 1 or i == 3:
                damage_action = InstantAction(
                    hero=self,
                    damage_coeff=damage_per_hit,
                    source_movement=MovementType.LowerSkill,
                    damage_type=DamageType.LowerSkill,
                    post_fn=remove_shield,
                )
            else:
                damage_action = InstantAction(
                    hero=self,
                    damage_coeff=damage_per_hit,
                    source_movement=MovementType.LowerSkill,
                    damage_type=DamageType.LowerSkill,
                    post_fn=lambda action: remove_buff() or remove_shield()
                )
            actions.append((damage_action, t_ratios[i]))

        return actions

    def _setup_upper_skill_actions(self):
        actions = []
        name = self.get_unique_name()
        total_damage, _ = self.upperskill_value[self.upperskill_level - 1]
        damage_per_hit = total_damage / 6

        # Schedule buff and acceleration
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.NONE,
            status_template=self.status_templates[f"{name}_고학_피감_가속"],
        )
        actions.append((buff_action, 4.23 / self.motion_time[MovementType.UpperSkill]))

        # Schedule damage hits
        hit_times = [11.67, 12.0, 12.5, 13.0, 13.5, 14.0]
        for hit_time in hit_times:
            damage_action = InstantAction(
                hero=self,
                damage_coeff=damage_per_hit,
                source_movement=MovementType.UpperSkill,
                damage_type=DamageType.UpperSkill,
            )
            actions.append((damage_action, hit_time / self.motion_time[MovementType.UpperSkill]))

        return actions

    def setup_eac(self):
        return PeriodicCondition(self, 4)

    def _activate_aside_skill_l2_special(self):
        """Activates the missile launch cycle for the Level 2 aside skill.
        The first missile is launched at 7.06 seconds.
        """
        self._schedule_next_aside_missile(0)

    def _schedule_next_aside_missile(self, current_time_ms):
        """Schedules the next missile launch, factoring in current acceleration."""
        acceleration = self.party.get_current_acceleration_factor(current_time_ms)
        cooldown_sec = 6 / acceleration
        next_fire_time = current_time_ms + cooldown_sec * SEC_TO_MS

        # Create a dummy action that triggers the actual effect
        trigger_action = InstantAction(
            hero=self,
            damage_coeff=0,
            source_movement=MovementType.AsideSkill,
            damage_type=DamageType.NONE,
            post_fn=partial(self._aside_skill_effect, next_fire_time)
        )
        # Use add_pending_effect to make it uncancelable by other hero actions
        self.add_non_cancelable_action(trigger_action, current_time_ms, delay=cooldown_sec)

    def _aside_skill_effect(self, fire_time_ms, _=None):
        """Handles the missile's effects: damage, CDR, and scheduling the next cycle."""
        # 1. Schedule the damage and CDR effect after a short delay
        acceleration = self.party.get_current_acceleration_factor(fire_time_ms)
        hit_delay_sec = 0.55
        hit_time = fire_time_ms + (hit_delay_sec * SEC_TO_MS / acceleration)

        # Damage action
        damage_action = InstantAction(
            hero=self,
            damage_coeff=400,
            source_movement=MovementType.AsideSkill,
            damage_type=DamageType.AsideSkill,
            post_fn=lambda action: self.update_timers_and_request_skill(
                self.party.current_time,
                additonal_upper_skill_cd_reduce=2 * SEC_TO_MS
            )
        )
        self.add_non_cancelable_action(damage_action, hit_time, delay=0)

        # 2. Schedule the next missile launch based on the current fire time
        self._schedule_next_aside_missile(fire_time_ms)
