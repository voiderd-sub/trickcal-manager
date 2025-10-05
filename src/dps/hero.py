from dps.data.hero_data import HERO_DATA
from dps.enums import *
from dps.skill_conditions import *
from dps.artifact import Artifact
from dps.action import ProjectileAction, InstantAction
from dps.status import StatusReservation

import numpy as np
from collections import defaultdict
from functools import partial


def find_valid_skill_level(L, i):
    for j in range(i-1, -1, -1):
        if L[j] is not None:
            return j+1
    return 0


class Hero:
    grade_bonuses = {1: 0, 2: 6, 3: 17, 4: 31, 5: 47, 6: 65}

    def __init__(self, user_provided_info):
        self.name = self.__class__.__name__
        if self.name in HERO_DATA:
            for key, value in HERO_DATA[self.name].items():
                # 'class' is a reserved keyword in Python, so we use 'hero_class' instead
                if key == "class":
                    setattr(self, "hero_class", value)
                else:
                    setattr(self, key, value)

        for key, value in user_provided_info.items():
            setattr(self, key, value)
        
        self.grade = getattr(self, 'grade', 1)

        self._base_stats = getattr(self, 'base_stat', {})
        self._personal_stats = getattr(self, 'personal_stat', {})
        self._global_stats = getattr(self, 'global_stat', {})
        
        self.artifacts = []
        # Action templates for each movement type
        self._action_templates = {}
        self.status_templates = {}
        self.applied_effects = set()
        self.artifact_counters = dict()   # Counters for artifact effects
        self.exclusive_weapon_name = None
        self.equipped_exclusive_weapon_level = 0
        self.aa_post_fns = []
        if not hasattr(self, "is_eldain"):       # Whether the hero is Eldain; default is False
            self.is_eldain = False

    
    def __repr__(self):
        return self.name if hasattr(self, "name") else "HeroNameDefault"

    def add_artifact(self, artifact: Artifact):
        self.artifacts.append(artifact)

    def init_run(self):
        """
        Initializes settings that are constant across multiple simulations in a single run.
        This includes one-time setup effects from artifacts.
        """
        self.applied_effects = set()
        self.aa_post_fns = [self._aa_sp_recovery]
        
        # Apply one-time setup effects from artifacts, checking for stackability.
        for artifact in self.artifacts:
            effect_key = artifact.effect_id
            if not artifact.stackable:
                if effect_key in self.applied_effects:
                    continue  # Skip already-applied non-stackable setup effect
                self.applied_effects.add(effect_key)
            artifact.apply_setup_effect(self)

        # Check skill level data is exists.
        # If not, use the value of the level that has data but is lower than the user's skill level.
        for skill_type in ["lowerskill", "upperskill"]:
            skill_values = getattr(self, skill_type+"_value", None)
            if not skill_values:
                user_level = getattr(self, skill_type+"_level")
                valid_level = find_valid_skill_level(skill_values, user_level)
                if user_level != valid_level:
                    setattr(self, skill_type+"_level", valid_level)

        # Initialize movement triggers and upper skill rule
        self.upper_skill_rule = None
        self.movement_triggers = defaultdict(list)

        # Check for exclusive weapon
        if self.exclusive_weapon_name:
            for artifact in self.artifacts:
                if artifact.name == self.exclusive_weapon_name:
                    self.equipped_exclusive_weapon_level = artifact.level
                    break

    def init_simulation(self):
        """
        Initializes/resets the hero's state for a single simulation run.
        This includes timers, counters, and logs.
        """
        self._initialize_eac()

        self.amplify_modifiers = {}
        self.sp = self.init_sp
        self.sp_timer = 0
        self.sp_recovery_fixed_bonus = 0
        self.sp_recovery_percent_bonus = 0
        self.upper_skill_timer = round(self.upper_skill_cd * SEC_TO_MS * 0.5)
        self.aa_timer = 0
        self.last_updated = 0
        self.last_movement = MovementType.Wait
        self.last_movement_time = 0
        self.upper_skill_flag = False
        self.next_t_without_interrupt = -1
        self.woke_up_early = False

        # Initialize base stats and coefficients
        if not hasattr(self, "attack"):
            self.attack = 100
        if not hasattr(self, "defense"):
            self.defense = 500
        if not hasattr(self, "hp"):
            self.hp = 10000
        if not hasattr(self, "attack_speed"):
            self.attack_speed = 100
        if not hasattr(self, "crit_rate"):
            self.crit_rate = 5
        if not hasattr(self, "crit_damage"):
            self.crit_damage = 150
            
        self.amplify_dict = {dt: 1.0 for dt in DamageType.leaf_types()}
        self.taken_amplify_dict = {dt: 1.0 for dt in DamageType.leaf_types()}
        for stat_type in StatType:
            setattr(self, stat_type.value+"_coeff", 1.0)

        # Apply stat bonuses from artifacts
        for artifact in self.artifacts:
            artifact.apply_stats(self)

        self.movement_log = []
        self.movement_timestamps = {MovementType.AutoAttackBasic: [],
                                  MovementType.AutoAttackEnhanced: [],
                                  MovementType.LowerSkill: [],
                                  MovementType.UpperSkill: [],
                                  }
        self.damage_records = defaultdict(list)
        self.last_motion_time = 0
        
        # SP recovery pause system
        self.sp_recovery_pause_end_time = 0


    def _calculate_final_stats(self):
        """Calculate final stats (base + personal + global + grade bonus)"""
        
        for stat_type in StatType:
            if stat_type == StatType.AttackSpeed:
                continue

            base_value = self._base_stats.get(stat_type, 0)
            personal_value = self._personal_stats.get(stat_type, 0)
            global_value = self._global_stats.get(stat_type, 0)
            
            # Apply personal/global bonus to base stat
            total_value = base_value + personal_value + global_value
            
            # Apply grade bonus (only for HP, Attack, Defense)
            if stat_type in [StatType.Hp, StatType.AttackPhysic, StatType.AttackMagic, 
                           StatType.DefensePhysic, StatType.DefenseMagic]:
                bonus_percent = self._get_grade_bonus_percent()
                if bonus_percent > 0:
                    total_value *= (1 + bonus_percent / 100)
            
            # Set final stat
            setattr(self, stat_type.value, total_value)
        
        # Apply special effect for grade 6
        if self.grade == 6:
            self._apply_role_special_effect()

    def add_sp_recovery_fixed_bonus(self, value):
        self.sp_recovery_fixed_bonus += value

    def add_sp_recovery_percent_bonus(self, value):
        self.sp_recovery_percent_bonus += value

    def _get_grade_bonus_percent(self):
        """Return stat bonus percent by grade"""
        return self.grade_bonuses.get(self.grade, 0)

    def _apply_role_special_effect(self):
        """Apply special effect for grade 6 by role"""
        if self.hero_class == Class.Dealer:
            # 100% attack increase (instead of 65%)
            if hasattr(self, 'attack_physic'):
                self.attack_physic = self._base_stats[StatType.AttackPhysic] * 2.0
            if hasattr(self, 'attack_magic'):
                self.attack_magic = self._base_stats[StatType.AttackMagic] * 2.0
        elif self.hero_class == Class.Tanker:
            # 100% HP increase (instead of 65%)
            if hasattr(self, 'max_hp'):
                self.max_hp = self._base_stats[StatType.Hp] * 2.0
        elif self.hero_class == Class.Supporter:
            # 30% increase to base SP recovery rate (고정 수치로 변환)
            # 기본 SP 회복량의 30%에 해당하는 고정 수치 증가
            fixed_bonus = self.sp_recovery_rate * 0.3
            self.add_sp_recovery_fixed_bonus(fixed_bonus)

    def increase_grade(self, amount=1):
        """Increase grade (for spell effects)"""
        self.grade = min(6, self.grade + amount)  # Max grade is 6

    def _setup_all_movement_actions(self):
        """Pre-generates and sorts action templates for all movement types."""
        auto_attack_basic_templates = self._setup_basic_attack_actions()
        for template in auto_attack_basic_templates:
            for (action, t_ratio) in template:
                if isinstance(action, ProjectileAction):
                    action.instant_action.post_fns_on_launch.append(lambda _: self.aa_post_fn())
                elif isinstance(action, InstantAction):
                    action.post_fns_on_launch.append(lambda _: self.aa_post_fn())
        self._action_templates[MovementType.AutoAttackBasic] = auto_attack_basic_templates

        auto_attack_enhanced_templates = self._setup_enhanced_attack_actions()
        for template in auto_attack_enhanced_templates:
            for (action, t_ratio) in template:
                if isinstance(action, ProjectileAction):
                    action.instant_action.post_fns_on_launch.append(lambda _: self.aa_post_fn())
                elif isinstance(action, InstantAction):
                    action.post_fns_on_launch.append(lambda _: self.aa_post_fn())
        self._action_templates[MovementType.AutoAttackEnhanced] = auto_attack_enhanced_templates

        self._action_templates[MovementType.LowerSkill] = self._setup_lower_skill_actions()
        self._action_templates[MovementType.UpperSkill] = self._setup_upper_skill_actions()

        # Check that all templates are sorted by t_ratio (the second element in the tuple)
        for templates in self._action_templates.values():
            for template in templates:
                if template:
                    t_ratios = [x[1] for x in template]
                    assert all(t_ratios[i] <= t_ratios[i+1] for i in range(len(t_ratios)-1)), \
                        f"Action template t_ratios are not monotonically increasing: {t_ratios}"

    def _setup_basic_attack_actions(self):
        """Returns a list of templates, where each template is a list of (action, t_ratio)."""
        return [[]]

    def _setup_enhanced_attack_actions(self):
        """Returns a list of templates, where each template is a list of (action, t_ratio)."""
        return [[]]

    def _setup_lower_skill_actions(self):
        """Returns a list of templates, where each template is a list of (action, t_ratio)."""
        return [[]]

    def _setup_upper_skill_actions(self):
        """Returns a list of templates, where each template is a list of (action, t_ratio)."""
        return [[]]

    def _setup_status_templates(self):
        """Initializes status templates for the hero. Should be overridden by subclasses."""
        pass

    def choose_movement(self):
        if self.upper_skill_flag:
            return MovementType.UpperSkill
        
        if self.sp == self.max_sp:
            return MovementType.LowerSkill
        elif self.aa_timer == 0:
            if self.is_enhanced(): return MovementType.AutoAttackEnhanced
            else:                  return MovementType.AutoAttackBasic
        return MovementType.Wait

    def update_timers_and_request_skill(self, t,
                                        additional_sp=0,
                                        additonal_upper_skill_cd_reduce=0):
        dt = t - self.last_updated
        
        # Check if SP recovery is paused
        sp_recovery_paused = t < self.sp_recovery_pause_end_time
        
        # Update SP - block all SP recovery if paused
        if not sp_recovery_paused:
            self.sp = min(self.max_sp, self.sp + additional_sp)
            if self.last_movement not in (MovementType.LowerSkill, MovementType.UpperSkill):
                self.sp_timer += dt            
                if self.sp_timer >= SP_INTERVAL:
                    num_sp_recover, self.sp_timer = divmod(self.sp_timer, SP_INTERVAL)
                    self.sp = min(self.max_sp, self.sp + self.get_sp_recovery_rate() * num_sp_recover)

        # update aa cd
        self.aa_timer = max(0, self.aa_timer - dt)
        
        # update upper skill cd
        prev_upper_skill_timer = self.upper_skill_timer
        self.upper_skill_timer = max(0, self.upper_skill_timer - dt 
                                        - additonal_upper_skill_cd_reduce)
        if prev_upper_skill_timer > 0 and self.upper_skill_timer == 0:
            if self.upper_skill_rule and self.upper_skill_rule.should_request(self):
                self.party.upper_skill_manager.add_request(self.party_idx)

        self.last_updated = t

        if (not sp_recovery_paused and additional_sp > 0) or additonal_upper_skill_cd_reduce > 0:
            # Wake up hero early if SP or cooldown is applied
            self.original_next_t = self.party.next_update[self.party_idx]
            self.party.next_update[self.party_idx] = t
            self.woke_up_early = True


    def choose_and_execute_movement(self, t):
        # If the hero woke up early, it means the hero is in the middle of a movement.
        # There are two cases: (1) using upper skill during movement, (2) not using upper skill.
        # In case (1), execute the movement if woke_up_early and upper_skill_flag == True.
        # In case (2), do not perform a new movement, only update the next update time.
        if self.woke_up_early:
            self.woke_up_early = False
            if not self.upper_skill_flag and self.last_movement != MovementType.Wait:
                # Only set the next update time without performing a movement.
                dt = self.original_next_t - t
                dt = self.reserve_wakeup_during_motion(t, dt)
                return t + dt
        
        movement = self.choose_movement()
        
        if movement == MovementType.Wait:
            # Check if SP recovery is paused
            sp_recovery_paused = t < self.sp_recovery_pause_end_time
            
            # Calculate wait time - include SP recovery pause end time if paused
            if sp_recovery_paused:
                wait_time = min(self.sp_recovery_pause_end_time - t, self.aa_timer, self.upper_skill_timer)
            else:
                wait_time = min(SP_INTERVAL - self.sp_timer, self.aa_timer, self.upper_skill_timer)
            dt = max(1, round(wait_time))
        else:
            # Start the movement and get its full duration
            match movement:
                case MovementType.AutoAttackBasic | MovementType.AutoAttackEnhanced:
                    self.aa_timer = self.get_aa_cd()
                case MovementType.LowerSkill:
                    self.sp = 0
                case MovementType.UpperSkill:
                    self.party.set_global_upper_skill_lock(t)
                    self.upper_skill_timer = round(self.upper_skill_cd * SEC_TO_MS)
                    self.upper_skill_flag = False
            
            # Trigger other heroes' skills if this movement is a trigger
            if movement in self.movement_triggers:
                for target_hero_id, delay_min, delay_max in self.movement_triggers[movement]:
                    self.party.upper_skill_manager.add_delayed_request(target_hero_id, delay_min, delay_max)

            dt = round(self.do_movement(movement, t))
            self.movement_timestamps[movement].append(round(t) / SEC_TO_MS)
            dt = self.reserve_wakeup_during_motion(t, dt)

        self.last_movement = movement
        self.movement_log.append((t, movement))
        return t + dt

    def reserve_wakeup_during_motion(self, t, dt):
        # Consider the case where the upper skill cooldown is 0 during the movement.
        if self.upper_skill_timer > 0 and self.upper_skill_timer < dt:
            self.original_next_t = t + dt
            dt = self.upper_skill_timer
            self.woke_up_early = True
        return dt
    
    def calculate_cumulative_damage(self, max_T):
        for key, record in self.damage_records.items():
            for i in range(len(record) - 1, -1, -1):
                if record[i][0] < max_T:
                    self.damage_records[key] = record[i][1]
                    break
        
    def do_movement(self, movement_type, t):
        # Get template index for the movement type
        template_index = self._choose_movement_template(movement_type)
        motion_time = self.get_motion_time(movement_type, template_index)
        self.last_motion_time = motion_time
        self.last_updated = t
        
        # Dispatch to specific movement methods
        if movement_type == MovementType.AutoAttackBasic:
            self.BasicAttack(template_index, t)
        elif movement_type == MovementType.AutoAttackEnhanced:
            self.EnhancedAttack(template_index, t)
            self.eac.on_enhanced_attack(t)      # self.eac is not None here.
        elif movement_type == MovementType.LowerSkill:
            self.LowerSkill(template_index, t)
        elif movement_type == MovementType.UpperSkill:
            self.UpperSkill(template_index, t)
        
        return motion_time

    def _reserv_actions_from_template(self, movement_type, template_index, t):
        """Helper to create and reserve actions from a template."""
        motion_time = self.get_motion_time(movement_type, template_index)
        action_tuples = []
        templates = self._action_templates.get(movement_type, [[]])
        template = templates[template_index]
        
        for action, t_ratio in template:
            action_tuples.append((action, t + motion_time * t_ratio))
        
        if not action_tuples:
            return
        
        self.reserv_action_chain(action_tuples)

    def BasicAttack(self, template_index, t):
        self._reserv_actions_from_template(MovementType.AutoAttackBasic, template_index, t)

    def EnhancedAttack(self, template_index, t):
        self._reserv_actions_from_template(MovementType.AutoAttackEnhanced, template_index, t)

    def LowerSkill(self, template_index, t):
        self._reserv_actions_from_template(MovementType.LowerSkill, template_index, t)

    def UpperSkill(self, template_index, t):
        self._reserv_actions_from_template(MovementType.UpperSkill, template_index, t)

    def _choose_movement_template(self, movement_type):
        """Override this to choose which template to use for each movement type."""
        return 0

    def is_enhanced(self):
        return self.eac and self.eac.is_met()

    def reserv_action(self, action, t, on_complete_callback=None):
        self.party.action_manager.add_action_reserv(t, action, on_complete_callback)

    def reserv_action_chain(self, action_tuples):
        """
        Reserves a chain of actions using callbacks, without modifying the action templates.
        :param action_tuples: A list of (action, execution_time) tuples.
        """
        if not action_tuples:
            return

        def create_reservation_callback(index):
            if index >= len(action_tuples):
                return None
            
            action, time = action_tuples[index]
            
            # Create a callback that will reserve the NEXT action in the chain.
            next_callback = create_reservation_callback(index + 1)
            
            # Return a function that, when called, reserves the CURRENT action with the next_callback.
            return partial(self.reserv_action, action, time, next_callback)

        # Start the chain by calling the first reservation function.
        first_reservation_fn = create_reservation_callback(0)
        if first_reservation_fn:
            first_reservation_fn()
    
    def add_non_cancelable_action(self, action, t, delay):
        self.party.action_manager.add_pending_effect(t, action, delay)

    def aa_post_fn(self):
        for aa_post_fn_component in self.aa_post_fns:
            aa_post_fn_component()

    def _aa_sp_recovery(self):
        self.sp = min(self.max_sp, self.sp + self.sp_per_aa)

    def get_sp_recovery_rate(self):
        return (self.sp_recovery_rate + self.sp_recovery_fixed_bonus) * (1 + self.sp_recovery_percent_bonus / 100)

    def get_aa_cd(self):
        attack_speed_coeff = self.get_coeff(StatType.AttackSpeed)
        acceleration = self.party.get_current_acceleration_factor(self.party.current_time)
        return round(300 * SEC_TO_MS / (acceleration**2 * min(10., attack_speed_coeff) * self.attack_speed), 0)
    
    def get_motion_time(self, movement_type: MovementType, template_index: int = 0):
        motion_times = self.motion_time.get(movement_type)
        if motion_times is None:
            raise ValueError(f"Motion time for {movement_type} is not defined.")
        
        # If motion_times is a list, get the specific template's motion time
        if isinstance(motion_times, list):
            if template_index >= len(motion_times):
                raise ValueError(f"Template index {template_index} out of range for {movement_type}")
            base_motion_time_sec = motion_times[template_index]
        else:
            # Backward compatibility: if motion_times is a single value
            base_motion_time_sec = motion_times
        
        motion_time_ms = base_motion_time_sec * SEC_TO_MS
        acceleration = self.party.get_current_acceleration_factor(self.party.current_time)

        match movement_type:
            case MovementType.AutoAttackBasic | MovementType.AutoAttackEnhanced:
                return min(motion_time_ms, self.get_aa_cd())
            case MovementType.LowerSkill | MovementType.UpperSkill:
                return motion_time_ms / acceleration
        
        raise ValueError(f"Invalid movement type: {movement_type}")
    

    def get_amplify(self, damage_type):
        return self.amplify_dict[damage_type]

    def add_amplify(self, damage_type: DamageType, value: float):
        for dt in DamageType.get_leaf_members(damage_type):
            self.amplify_dict[dt] += value / 100
    
    def reduce_damage_taken(self, damage_type: DamageType, value: float):
        """Reduces the damage taken by the hero by a certain percentage."""
        for dt in DamageType.get_leaf_members(damage_type):
            self.taken_amplify_dict[dt] -= value / 100
    
    def get_coeff(self, stat_type: StatType):
        """
        Gets the final calculated coefficient for a given stat.
        This can be monkey-patched by artifacts/statuses to apply dynamic bonuses.
        """
        attr_name = stat_type.to_hero_attr(is_coeff=True)
        return getattr(self, attr_name)
    
    def get_damage(self, damage, damage_type):
        enemy_amplify = self.party.get_amplify(self)
        additional_coeff = self.party.get_additional_coeff(self)  # include type_effectiveness, hidden damage decrease, etc.

        conditional_amplify = 0
        for modifier_fn in self.amplify_modifiers.values():
            conditional_amplify += modifier_fn(damage_type) / 100

        applying_amplify = max(0.25, self.get_amplify(damage_type) + enemy_amplify + conditional_amplify)

        attack_stat_type = StatType.AttackPhysic if self.attack_type == AttackType.Physic else StatType.AttackMagic
        applying_attack_coeff = max(0.2, self.get_coeff(attack_stat_type))
        
        damage = 0.8 * (self.attack * applying_attack_coeff) * applying_amplify * (damage/100) * additional_coeff

        return damage

    def get_name(self):
        return self.name_kr

    def get_unique_name(self):
        return f"{self.name}_{self.party_idx}"

    def add_movement_trigger(self, movement_type, target_hero_id, delay_min_sec, delay_max_sec):
        self.movement_triggers[movement_type].append((target_hero_id, delay_min_sec, delay_max_sec))

    def set_upper_skill_rule(self, rule):
        self.upper_skill_rule = rule

    def has_buff(self, buff_id):
        return self.party.status_manager.has_buff(self.party_idx, buff_id)

    def setup_eac(self):
        """Sets up the Enhanced Attack Condition for the hero. Should be overridden by subclasses."""
        return None

    def _initialize_eac(self):
        """Initializes/resets the EAC for a new simulation run."""
        self.eac = self.setup_eac()
        if self.eac:
            self.eac.init_simulation()

    def setup_aside_skills(self):
        """
        Sets up aside skill effects that are constant for the entire run.
        This is called once from party.init_run().
        """
        if not hasattr(self, "aside_level") or self.aside_level == 0:
            return
        # Only L2 has run-setup effect.
        if self.aside_level >= 2:
            self._setup_aside_skill_l2()

    def setup_exclusive_weapon_effects(self):
        """Sets up exclusive weapon effects that are constant for the entire run."""
        if self.equipped_exclusive_weapon_level >= 1:
            self._setup_ew_l1()
        if self.equipped_exclusive_weapon_level >= 3:
            self._setup_ew_l3()

    def initialize_aside_skills(self):
        """
        Initializes/resets aside skill effects for each simulation.
        This is called from party.init_simulation().
        """
        if not hasattr(self, "aside_level") or self.aside_level == 0:
            return

        if self.aside_level >= 1:
            self._initialize_aside_skill_l1()
        if self.aside_level >= 2:
            self._initialize_aside_skill_l2()
        if self.aside_level >= 3:
            self._initialize_aside_skill_l3()

    def initialize_exclusive_weapon_effects(self):
        """Initializes/resets exclusive weapon effects for each simulation."""
        if self.equipped_exclusive_weapon_level >= 1:
            self._initialize_ew_l1()
        if self.equipped_exclusive_weapon_level >= 3:
            self._initialize_ew_l3()

    # --- Stubs for subclasses to override ---

    def _setup_aside_skill_l2(self):
        pass

    def _setup_ew_l1(self):
        pass

    def _setup_ew_l3(self):
        pass

    def _initialize_aside_skill_l1(self):
        """Applies a fixed 6% stat bonus for Level 1 aside skill."""
        bonus_stats = getattr(self, "aside_stats_l1", [])
        for stat_type in bonus_stats:
            attr_name = stat_type.to_hero_attr(is_coeff=True)
            current_coeff = getattr(self, attr_name, 1.0)
            setattr(self, attr_name, current_coeff + 0.06)

    def _initialize_aside_skill_l2(self):
        pass

    def _initialize_aside_skill_l3(self):
        pass
    
    def _initialize_ew_l1(self):
        pass

    def _initialize_ew_l3(self):
        pass
    
    def apply_status_immediately(self, status_template):
        """
        Create a status reservation and apply it immediately.
        
        Args:
            status_template: The status template to apply
        """
        reservation = StatusReservation(template=status_template, start_time=self.party.current_time)
        self.party.status_manager.add_status_reserv(reservation)
        self.party.status_manager.resolve_status_reserv(self.party.current_time)

    def pause_sp_recovery(self, end_time):
        """
        Pause SP recovery until the specified end time.
        
        Args:
            end_time: Time when SP recovery should resume (in milliseconds)
        """
        self.sp_recovery_pause_end_time = end_time

    def resume_sp_recovery(self):
        """
        Resume SP recovery immediately.
        Called when skill is cancelled or when pause period ends.
        """
        self.sp_recovery_pause_end_time = 0


class EnhancedAttackCondition:
    """Base class for enhanced attack conditions."""
    def __init__(self, hero):
        self.hero = hero

    def is_met(self):
        raise NotImplementedError
    
    def on_enhanced_attack(self, t):
        """A hook to update state after an enhanced attack. t is current time."""
        pass

    def init_simulation(self):
        """Reset state for a new simulation."""
        pass

class ProbabilisticCondition(EnhancedAttackCondition):
    """Triggers based on probability."""
    def __init__(self, hero, probability):
        super().__init__(hero)
        self.probability = probability

    def is_met(self):
        return self.hero.party.rng.random() < self.probability

class PeriodicCondition(EnhancedAttackCondition):
    """Triggers every N attacks."""
    def __init__(self, hero, cycle):
        super().__init__(hero)
        assert cycle > 0, "Cycle must be positive."
        assert isinstance(cycle, int), "Cycle must be an integer."
        self.cycle = cycle

    def init_simulation(self):
        self.counter = 0

    def is_met(self):
        self.counter += 1
        self.counter %= self.cycle
        return self.counter == 0

class BuffCondition(EnhancedAttackCondition):
    """Triggers if the hero has a specific buff."""
    def __init__(self, hero, buff_id):
        super().__init__(hero)
        self.buff_id = buff_id

    def is_met(self):
        return self.hero.has_buff(self.buff_id)

class CooldownCondition(EnhancedAttackCondition):
    """Triggers when a cooldown is over."""
    def __init__(self, hero, cooldown_sec, initial_cd_sec=0):
        super().__init__(hero)
        self.cooldown = cooldown_sec * SEC_TO_MS
        self.initial_cd = initial_cd_sec * SEC_TO_MS
        self.last_triggered_time = self.initial_cd

    def init_simulation(self):
        self.last_triggered_time = self.initial_cd

    def is_met(self):
        return self.hero.last_updated >= self.last_triggered_time + self.cooldown

    def on_enhanced_attack(self, t):
        self.last_triggered_time = t

class AndCondition(EnhancedAttackCondition):
    """Composite condition that triggers if ALL sub-conditions are met."""
    def __init__(self, hero, *conditions):
        super().__init__(hero)
        self.conditions = conditions

    def is_met(self):
        # Evaluate all conditions to ensure side effects (like counters) are triggered.
        # Do not use short-circuiting `all()`.
        results = [cond.is_met() for cond in self.conditions]
        return all(results)

    def on_enhanced_attack(self, t):
        # If AndCondition is met, all sub-conditions were also met.
        for cond in self.conditions:
            cond.on_enhanced_attack(t)
    
    def init_simulation(self):
        for cond in self.conditions:
            cond.init_simulation()

class OrCondition(EnhancedAttackCondition):
    """Composite condition that triggers if ANY sub-condition is met."""
    def __init__(self, hero, *conditions):
        super().__init__(hero)
        self.conditions = conditions
        self.last_results = []

    def is_met(self):
        # Evaluate all conditions to ensure side effects (like counters) are triggered.
        # Do not use short-circuiting `any()`.
        self.last_results = [cond.is_met() for cond in self.conditions]
        return any(self.last_results)

    def on_enhanced_attack(self, t):
        # Only call on_enhanced_attack for the sub-conditions that were actually met.
        for i, cond in enumerate(self.conditions):
            if self.last_results and self.last_results[i]:
                cond.on_enhanced_attack(t)

    def init_simulation(self):
        self.last_results = []
        for cond in self.conditions:
            cond.init_simulation()