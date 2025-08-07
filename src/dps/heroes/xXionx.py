from dps.action import InstantAction, StatusAction
from dps.hero import Hero, PeriodicCondition
from dps.enums import *
from dps.status import StatusTemplate, target_self, BuffStatCoeff
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
    lowerskill_value = [(180 + 20 * level) for level in range(13)]
    upperskill_value = [(385 + 25 * level) for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.motion_time = {
            MovementType.AutoAttackBasic: 2.25,
            MovementType.AutoAttackEnhanced: 2.667,
            MovementType.LowerSkill: [6.550, 7.567, 8.584, 9.601, 10.618],  # motion time for 2~6 dark bullets
            MovementType.UpperSkill: 5.5,
        }

    def _setup_aside_skill_l2(self):
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
            stat_bonuses={StatType.AttackSpeed: 100}, # 100% increase
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
            template_index = self._choose_movement_template(movement_before_super)
            motion_time = self.get_motion_time(movement_before_super, template_index)
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
        return [[(action, 0.45)]]

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
        
        return [[(damage_action, 0.31), (buff_action, 0.74)]]

    def _setup_lower_skill_actions(self):
        name = self.get_unique_name()
        templates = []
        
        # Generate templates for 2~6 dark bullets (since 2 dark bullets are charged)
        motion_times = [6.550, 7.567, 8.584, 9.601, 10.618]  # motion time for 2~6 dark bullets
        
        for darkbullet_count in range(5):  # 0~4 (corresponds to 2~6 dark bullets)
            template = []
            actual_darkbullet_count = darkbullet_count + 2  # actual number of dark bullets
            num_attacks = min(actual_darkbullet_count + 2, 6)
            motion_time = motion_times[darkbullet_count]
            
            # Buff actions (add 2 dark bullets)
            buff_action = StatusAction(
                hero=self, 
                source_movement=MovementType.LowerSkill, 
                damage_type=DamageType.LowerSkill, 
                status_template=self.status_templates[name + "_마탄"]
            )
            buff_t_ratio = 0.983 / motion_time
            template.append((buff_action, buff_t_ratio))
            template.append((buff_action, buff_t_ratio))
            
            # Damage actions
            first_hit_t_ratio = (0.983 + 1.2) / motion_time  # first attack timing
            time_between_hits_ratio = (61 / 60) / motion_time  # interval between attacks
            
            for i in range(num_attacks):
                damage_action = InstantAction(
                    hero=self,
                    damage_coeff=420,
                    source_movement=MovementType.LowerSkill,
                    damage_type=DamageType.LowerSkill,
                    post_fns_on_launch=[self._consume_darkbullet]
                )
                hit_t_ratio = first_hit_t_ratio + i * time_between_hits_ratio
                template.append((damage_action, hit_t_ratio))
            
            templates.append(template)
        
        return templates

    def _choose_movement_template(self, movement_type):
        if movement_type == MovementType.LowerSkill:
            name = self.get_unique_name() + "_마탄"
            current_stacks = self.party.status_manager.get_buff_count(self.party_idx, name)
            # Map to range 0~4 for 2~6 dark bullets
            template_index = max(0, min(current_stacks - 2, 4))  # map 2~6 to 0~4
            return template_index
        return 0

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

        return [[(buff_action, 0.68), (damage_action, 0.69)]]

    def _initialize_aside_skill_l3(self):
        # Increase back row damage dealt by 19.5%, reduce damage taken by 9.75%
        for ally_idx in self.party.active_indices:
            ally = self.party.character_list[ally_idx]
            if ally.party_idx // 3 == 2:    # back row
                ally.add_amplify(DamageType.ALL, 19.5)
                ally.reduce_damage_taken(DamageType.ALL, 9.75)