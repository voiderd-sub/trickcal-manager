from dps.action import InstantAction, StatusAction
from dps.hero import Hero, PeriodicCondition
from dps.enums import *
from dps.status import StatusTemplate, target_self, BuffStatCoeff, StatusReservation
from dps.stat_utils import apply_stat_bonuses


class DarkBulletBuff(StatusTemplate):
    def __init__(self, caster: 'Hero'):
        super().__init__(
            status_id=caster.get_unique_name() + "_마탄",
            caster=caster,
            target_resolver_fn=target_self,
            max_stack=6,
            refresh_interval=0,
            status_type="buff"
        )
        self.duration = float('inf')

    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        if target:
            apply_stat_bonuses(target, {StatType.AttackPhysic: 5})

    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        if target:
            apply_stat_bonuses(target, {StatType.AttackPhysic: -5})

    def refresh_fn(self, reservation, target_id, current_time):
        pass


class xXionx(Hero):
    lowerskill_value = [(160 + 20 * level) for level in range(13)]
    upperskill_value = [(360 + 25 * level) for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.motion_time = {
            MovementType.AutoAttackBasic: 2.25,
            MovementType.AutoAttackEnhanced: 2.667,
            MovementType.UpperSkill: 5.5,
        }

    def init_run(self):
        super().init_run()
        if self.aside_level >= 2:
            self.update_timers_and_request_skill = self.update_timers_and_request_skill_aside_2
            self.choose_and_execute_movement = self.choose_and_execute_movement_aside_2

    def init_simulation(self):
        super().init_simulation()
        self._next_aside_l2_buff_time = None

    def _setup_status_templates(self):
        # darkbullet buff
        name = self.get_unique_name()
        self.status_templates[name + "_마탄"] = DarkBulletBuff(caster=self)
        self.status_templates[name + "_A2_공속"] = BuffStatCoeff(
            status_id=name + "_A2_공속",
            caster=self,
            target_resolver_fn=target_self,
            duration=6,
            stat_type=StatType.AttackSpeed,
            value=100, # 100% increase
            max_stack=1 # Refresh duration on re-application
        )

    def _schedule_aside_l2_buff(self, time):
        # Only schedule if this time is earlier than current scheduled time
        if self._next_aside_l2_buff_time is None or time < self._next_aside_l2_buff_time:
            self._next_aside_l2_buff_time = time
            if time < self.party.next_update[self.party_idx]:
                self.party.next_update[self.party_idx] = time

    def _apply_aside_l2_buff(self):
        name = self.get_unique_name()
        buff_template = self.status_templates[name + "_A2_공속"]
        self.apply_status_immediately(buff_template)

    def update_timers_and_request_skill_aside_2(self, t,
                                        additional_sp=0,
                                        additonal_upper_skill_cd_reduce=0):
        
        if self._next_aside_l2_buff_time is not None and t >= self._next_aside_l2_buff_time:
            self._apply_aside_l2_buff()
            self._next_aside_l2_buff_time = None
            
        super().update_timers_and_request_skill(t, additional_sp, additonal_upper_skill_cd_reduce)

    def choose_and_execute_movement_aside_2(self, t):
        is_last_movement_skill = self.last_movement in (MovementType.LowerSkill, MovementType.UpperSkill)
        if self.upper_skill_flag and is_last_movement_skill:
             # A skill is being cancelled by an upper skill.
             original_end_time = self.party.next_update[self.party_idx]
             
             # Check if we need to cancel the scheduled buff
             if (self._next_aside_l2_buff_time is not None and 
                 abs(self._next_aside_l2_buff_time - original_end_time) < 0.1):  # 0.1ms tolerance
                 self._next_aside_l2_buff_time = None
             
             # Apply buff immediately at cancellation time
             self._apply_aside_l2_buff()

        movement_before_super = self.choose_movement()
        
        if movement_before_super in (MovementType.LowerSkill, MovementType.UpperSkill):
            motion_time = self.get_motion_time(movement_before_super)
            skill_end_time = t + motion_time
            self._schedule_aside_l2_buff(skill_end_time)

        return super().choose_and_execute_movement(t)

    def setup_eac(self):
        return PeriodicCondition(self, cycle=4)

    def _setup_basic_attack_actions(self):
        action = InstantAction(
            hero=self,
            damage_coeff=175,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        return [(action, 0.45)]

    def _setup_enhanced_attack_actions(self):
        name = self.get_unique_name()
        damage_action = InstantAction(
            hero=self,
            damage_coeff=200,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
        )
        
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.AutoAttackEnhanced,
            status_template=self.status_templates[name + "_마탄"]
        )
        
        return [(damage_action, 0.31), (buff_action, 0.74)]

    def get_motion_time(self, movement_type: MovementType):        
        if movement_type == MovementType.LowerSkill:
            name = self.get_unique_name() + "_마탄"
            current_stacks = self.party.status_manager.get_buff_count(self.party_idx, name)
            num_attacks = min(current_stacks + 2, 6)

            time_to_buff = 0.983
            time_to_first_hit_from_buff = 1.2
            time_between_hits = 61 / 60
            time_after_last_hit = 2.333
            
            total_duration_sec = (time_to_buff + 
                                  time_to_first_hit_from_buff + 
                                  max(0, num_attacks - 1) * time_between_hits + 
                                  time_after_last_hit)
            acceleration = self.party.get_current_acceleration_factor(self.party.current_time)
            
            return total_duration_sec * SEC_TO_MS / acceleration
        
        return super().get_motion_time(movement_type)

    def LowerSkill(self, t):
        action_tuples = []
        
        name = f"{self.get_unique_name()}_마탄"
        current_stacks = self.party.status_manager.get_buff_count(self.party_idx, name)
        num_attacks = min(current_stacks + 2, 6)

        # 1. Reserve buff actions
        time_to_buff_ms = t + 0.983 * SEC_TO_MS
        buff_action = StatusAction(
            hero=self, 
            source_movement=MovementType.LowerSkill, 
            damage_type=DamageType.LowerSkill, 
            status_template=self.status_templates[name]
        )
        
        action_tuples.append((buff_action, time_to_buff_ms))
        action_tuples.append((buff_action, time_to_buff_ms))

        # 2. Reserve damage actions
        if num_attacks > 0:
            first_hit_time_ms = t + (0.983 + 1.2) * SEC_TO_MS
            time_between_hits_ms = (61 / 60) * SEC_TO_MS

            for i in range(num_attacks):
                damage_action = InstantAction(
                    hero=self,
                    damage_coeff=420,
                    source_movement=MovementType.LowerSkill,
                    damage_type=DamageType.LowerSkill,
                    post_fns_on_launch=[self._consume_darkbullet]
                )
                hit_time = first_hit_time_ms + i * time_between_hits_ms
                action_tuples.append((damage_action, hit_time))
        
        self.reserv_action_chain(action_tuples)

    def _consume_darkbullet(self, action):
        name = f"{self.get_unique_name()}_마탄"
        self.party.status_manager.consume_oldest_stack(name)

    def _setup_upper_skill_actions(self):
        name = self.get_unique_name()
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.UpperSkill,
            status_template=self.status_templates[name + "_마탄"]
        )
        
        damage_action = InstantAction(
            hero=self,
            damage_coeff=685,
            source_movement=MovementType.UpperSkill,
            damage_type=DamageType.UpperSkill
        )

        return [(buff_action, 0.68), (damage_action, 0.69)]
