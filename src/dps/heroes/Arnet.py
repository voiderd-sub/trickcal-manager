from dps.action import ProjectileAction, InstantAction, StatusAction, Action
from dps.hero import Hero, CooldownCondition
from dps.enums import *
from dps.status import StatusTemplate, BuffDeception, StatusReservation, BuffStatCoeff, BuffAmplify, target_self, target_predefined, target_all
from dps.stat_utils import apply_stat_bonuses

def calculate_cumulative_damage(hero):
    """Calculate current cumulative damage for a hero (at the current time)"""
    total_damage = 0
    for damage_list in hero.damage_records.values():
        if damage_list:
            total_damage += damage_list[-1][1]  # Last cumulative damage of that damage type
    return total_damage


class StartMVPTrackingAction(Action):
    """Start MVP damage tracking for all heroes"""
    def __init__(self, hero, source_movement, damage_type):
        super().__init__(hero, ActionType.Status, source_movement, damage_type)
    
    def action_fn(self, current_time):
        # Calculate initial cumulative damage for all heroes
        initial_damages = self._calculate_initial_damages()
        
        # Mark that MVP tracking has started
        self.hero.mvp_tracking_started = True
        
        # Schedule end tracking action in pending effect queue (5 seconds later)
        end_action = EndMVPTrackingAction(self.hero, self.source_movement, self.damage_type, initial_damages)
        self.hero.party.action_manager.add_pending_effect(current_time, end_action, 5.0)
    
    def _calculate_initial_damages(self):
        """Calculate initial cumulative damage for all heroes"""
        initial_damages = {}
        party = self.hero.party
        for hero_idx in party.active_indices:
            hero = party.character_list[hero_idx]
            initial_damages[hero_idx] = calculate_cumulative_damage(hero)
        return initial_damages


class StartMVPTrackingActionA2(StartMVPTrackingAction):
    """Start MVP tracking with fireworks effect for aside level 2+"""
    def action_fn(self, current_time):
        # Calculate initial cumulative damage for all heroes
        initial_damages = self._calculate_initial_damages()
        
        # Mark that MVP tracking has started
        self.hero.mvp_tracking_started = True
        
        # Schedule end tracking action in pending effect queue (5 seconds later)
        end_action = EndMVPTrackingActionA2(self.hero, self.source_movement, self.damage_type, initial_damages)
        self.hero.party.action_manager.add_pending_effect(current_time, end_action, 5.0)


class EndMVPTrackingAction(Action):
    """End MVP damage tracking and select MVP"""
    def __init__(self, hero, source_movement, damage_type, initial_damages):
        super().__init__(hero, ActionType.Status, source_movement, damage_type)
        self.initial_damages = initial_damages
    
    def action_fn(self, current_time):
        # Calculate final cumulative damage for all heroes
        hero_damages = {}
        party = self.hero.party
        for hero_idx in party.active_indices:
            hero = party.character_list[hero_idx]
            final_damage = calculate_cumulative_damage(hero)
            initial_damage = self.initial_damages[hero_idx]
            hero_damages[hero_idx] = final_damage - initial_damage
        
        # Select MVP and apply buff
        if hero_damages:
            mvp_hero_idx = max(hero_damages.items(), key=lambda x: x[1])[0]
        else:
            mvp_hero_idx = min(party.active_indices)
        # Apply MVP buff to mvp_hero
        self.hero.apply_mvp_buff(mvp_hero_idx, current_time)
        
        # Resume SP recovery for caster(= self.hero)
        self.hero.resume_sp_recovery()
        
        # Reset MVP tracking flag
        self.hero.mvp_tracking_started = False


class EndMVPTrackingActionA2(EndMVPTrackingAction):
    """End MVP tracking with fireworks effect for aside level 2+"""
    def action_fn(self, current_time):
        # Call parent method for basic MVP tracking
        super().action_fn(current_time)
        
        # Apply fireworks effect
        # Get the MVP hero index from the parent method's result
        party = self.hero.party
        hero_damages = {}
        for hero_idx in party.active_indices:
            hero = party.character_list[hero_idx]
            final_damage = calculate_cumulative_damage(hero)
            initial_damage = self.initial_damages[hero_idx]
            hero_damages[hero_idx] = final_damage - initial_damage
        
        if hero_damages:
            mvp_hero_idx = max(hero_damages.items(), key=lambda x: x[1])[0]
        else:
            mvp_hero_idx = min(party.active_indices)
        is_consecutive = (mvp_hero_idx == self.hero.last_mvp_hero_idx)
        self.hero.last_mvp_hero_idx = mvp_hero_idx
        self.hero.apply_fireworks_effect(current_time, is_consecutive)


class MVPStatus(StatusTemplate):
    """MVP buff that increases attack speed and damage"""
    def __init__(self, status_id, caster, duration, attack_speed_bonus, amplify_bonus):
        super().__init__(status_id=status_id,
                         caster=caster,
                         target_resolver_fn=None,
                         max_stack=1,
                         refresh_interval=0,
                         status_type="buff")
        self.duration = duration
        self.attack_speed_bonus = attack_speed_bonus
        self.amplify_bonus = amplify_bonus
    
    def set_target_indices(self, target_indices):
        self.target_resolver_fn = target_predefined(target_indices)
    
    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {StatType.AttackSpeed: self.attack_speed_bonus})
        target.add_amplify(DamageType.ALL, self.amplify_bonus)
    
    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {StatType.AttackSpeed: -self.attack_speed_bonus})
        target.add_amplify(DamageType.ALL, -self.amplify_bonus)


class Arnet(Hero):
    lowerskill_value = [(80 + 5 * level, 84 + 8 * level) for level in range(13)]
    upperskill_value = [1980 + 180 * level for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)
        self.motion_time = {
            MovementType.AutoAttackBasic: MAX_MOTION_TIME,
            MovementType.AutoAttackEnhanced: MAX_MOTION_TIME,
            MovementType.LowerSkill: 2.5,
            MovementType.UpperSkill: 3.6,
        }
        
        # Counter for distinguishing odd/even basic attacks
        self.basic_attack_counter = 0
        
        # Flag to track if MVP tracking has started
        self.mvp_tracking_started = False
        
        # Track last MVP for consecutive check
        self.last_mvp_hero_idx = None
    
    def init_simulation(self):
        super().init_simulation()
        self.basic_attack_counter = 0
        self.mvp_tracking_started = False
        self.last_mvp_hero_idx = None

    def _setup_status_templates(self):
        name = self.get_unique_name()
        
        # Deception buff (dummy buff)
        self.status_templates[f"{name}_강평_눈속임"] = BuffDeception(
            status_id=f"{name}_강평_눈속임",
            caster=self,
            duration=6.0,
            target_resolver_fn=target_self
        )
        
        # MVP buff (will be created dynamically with target)
        attack_speed_bonus, amplify_bonus = self.lowerskill_value[self.lowerskill_level - 1]
        self.status_templates[f"{name}_MVP"] = MVPStatus(
            status_id=f"{name}_MVP",
            caster=self,
            duration=12.0,
            attack_speed_bonus=attack_speed_bonus,
            amplify_bonus=amplify_bonus,
        )

    def apply_mvp_buff(self, mvp_hero_idx, current_time):
        """Apply MVP buff to the selected hero"""
        name = self.get_unique_name()
        mvp_template = self.status_templates[f"{name}_MVP"]
        mvp_template.set_target_indices([mvp_hero_idx])
        
        # Create and apply status reservation
        reservation = StatusReservation(template=mvp_template, start_time=current_time)
        self.party.status_manager.add_status_reserv(reservation)

    def apply_fireworks_effect(self, current_time, is_consecutive):
        """Apply fireworks effect: damage to enemies and buff to allies"""
        # Instant damage action (900% magic damage to enemies)
        damage_action = InstantAction(
            hero=self,
            damage_coeff=900,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.LowerSkill
        )
        
        # Schedule damage action 0.2 seconds later
        self.party.action_manager.add_pending_effect(current_time, damage_action, 0.2)
        
        # Status action for buff (damage increase or attack speed increase)
        name = self.get_unique_name()
        if is_consecutive:
            # Attack speed increase for consecutive MVP
            buff_template = BuffStatCoeff(
                status_id=f"{name}_MVP_A2_공속",
                caster=self,
                duration=12.0,
                stat_bonuses={StatType.AttackSpeed: 150},
                target_resolver_fn=target_all
            )
        else:
            # Damage increase for non-consecutive MVP
            buff_template = BuffAmplify(
                status_id=f"{name}_MVP_A2_일반공격피증",
                caster=self,
                duration=12.0,
                value=150,
                applying_dmg_type=DamageType.AutoAttackBasic,
                target_resolver_fn=target_all
            )
        
        # Schedule buff action 0.2 seconds later
        buff_action = StatusAction(
            hero=self,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE,
            status_template=buff_template
        )
        self.party.action_manager.add_pending_effect(current_time, buff_action, 0.2)

    def _setup_basic_attack_actions(self):
        # Odd-numbered attack: projectile action at 45% timing, 0.45s hit delay
        odd_action = ProjectileAction(
            hero=self,
            damage_coeff=100,
            hit_delay=0.45,
            source_movement=MovementType.AutoAttackBasic,
            damage_type=DamageType.AutoAttackBasic,
        )
        
        # Even-numbered attack: heal at 53% timing (not implemented, empty action)
        # HP heal: 5% of max HP
        # even_action = InstantAction(
        #     hero=self,
        #     damage_coeff=0,  # Healing is not implemented with damage_coeff
        #     source_movement=MovementType.AutoAttackBasic,
        #     damage_type=DamageType.AutoAttackBasic,
        # )
        
        return [[(odd_action, 0.45)], []]

    def _setup_enhanced_attack_actions(self):
        # Apply deception buff at 55% timing
        name = self.get_unique_name()
        deception_buff = StatusAction(
            hero=self,
            status_template=self.status_templates[f"{name}_강평_눈속임"],
            source_movement=MovementType.AutoAttackEnhanced,
            damage_type=DamageType.NONE,
        )
        return [[(deception_buff, 0.55)]]

    def _setup_lower_skill_actions(self):
        # Start MVP tracking at 47% timing
        start_action = StartMVPTrackingAction(
            hero=self,
            source_movement=MovementType.LowerSkill,
            damage_type=DamageType.NONE,
        )
        
        return [[(start_action, 0.47)]]

    def _setup_upper_skill_actions(self):
        damage_per_projectile = self.upperskill_value[self.upperskill_level - 1] / 12
        timings = [0.22, 0.38, 0.48, 0.57, 0.76, 0.82, 0.84, 0.86, 0.92, 0.94, 0.96, 0.98]
        
        actions = []
        for timing in timings:
            projectile_action = ProjectileAction(
                hero=self,
                damage_coeff=damage_per_projectile,
                hit_delay=0.6,
                source_movement=MovementType.UpperSkill,
                damage_type=DamageType.UpperSkill,
            )
            actions.append((projectile_action, timing))
        
        # TODO: 출전 금지 (50% 시점)
        
        return [actions]

    def setup_eac(self):
        # 3s cooldown at simulation start
        # After that, cooldown starts when enhanced attack is triggered. Cooldown is 10s.
        return CooldownCondition(self, 10.0, 3.0)

    def _choose_basic_attack_template(self):
        # Select different template for odd/even basic attacks
        self.basic_attack_counter += 1
        return (self.basic_attack_counter - 1) % 2  # 0: odd, 1: even

    def LowerSkill(self, template_index, t):
        # Pause SP recovery immediately when lower skill starts (only for self)
        # Will be manually resumed by EndMVPTrackingAction or upper skill cancellation
        self.pause_sp_recovery(float('inf'))
        
        # Call parent method to execute normal lower skill actions
        super().LowerSkill(template_index, t)

    def UpperSkill(self, template_index, t):
        # Resume SP recovery only if MVP tracking hasn't started yet
        if not self.mvp_tracking_started:
            self.resume_sp_recovery()
        
        # Call parent method to execute normal upper skill actions
        super().UpperSkill(template_index, t)

    def _setup_aside_skill_l2(self):
        """Enable fireworks effect for aside level 2+"""
        # Override _setup_lower_skill_actions to use fireworks version
        def _setup_lower_skill_actions_with_fireworks(self):
            # Start MVP tracking at 47% timing with fireworks
            start_action = StartMVPTrackingActionA2(
                hero=self,
                source_movement=MovementType.LowerSkill,
                damage_type=DamageType.NONE,
            )
            
            return [[(start_action, 0.47)]]
        
        # Replace the method
        self._setup_lower_skill_actions = _setup_lower_skill_actions_with_fireworks.__get__(self, Arnet)

    def _initialize_aside_skill_l3(self):
        # Increase middle row damage dealt by 26%
        for ally_idx in self.party.active_indices:
            ally = self.party.character_list[ally_idx]
            if ally.party_idx // 3 == 1:    # middle row
                ally.add_amplify(DamageType.ALL, 26.0) 