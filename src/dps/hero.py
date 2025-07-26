from dps.enums import *
from dps.skill_conditions import *

import numpy as np
from collections import defaultdict
from functools import partial


def find_valid_skill_level(L, i):
    for j in range(i-1, -1, -1):
        if L[j] is not None:
            return j+1
    return 0


class Hero:
    def __init__(self, user_provided_info):
        for key, value in user_provided_info.items():
            setattr(self, key, value)
        
        # Action templates for each movement type
        self._action_templates = {}
        self.status_templates = {}
    
    def __repr__(self):
        return self.name if hasattr(self, "name") else "HeroNameDefault"

    def init_simulation(self):
        # Check skill level data is exists.
        # If not, use the value of the level that has data but is lower than the user's skill level.
        for skill_type in ["lowerskill", "upperskill"]:
            skill_values = getattr(self, skill_type+"_value", None)
            if not skill_values:
                user_level = getattr(self, skill_type+"_level")
                valid_level = find_valid_skill_level(skill_values, user_level)
                if user_level != valid_level:
                    setattr(self, skill_type+"_level", valid_level)
                    print(f"Data for {skill_type} level {user_level} is not exists.")
                    print(f"Use data of level {valid_level} instead.")

        self._initialize_eac()
        self._setup_status_templates()
        self._setup_all_movement_actions()

        self.aa_cd = round(300 * SEC_TO_MS / self.attack_speed)
        self.sp = self.init_sp
        self.sp_timer = 0
        self.upper_skill_timer = round(self.upper_skill_cd * SEC_TO_MS * 0.5)
        self.aa_timer = 0
        self.last_updated = 0
        self.last_movement = MovementType.Wait
        self.last_movement_time = 0
        self.upper_skill_flag = False
        self.upper_skill_rule = None
        self.next_t_without_interrupt = 0
        if not hasattr(self, "atk"):
            self.atk = 100
        self.amplify_dict = {dt: 1.0 for dt in DamageType.leaf_types()}
        self.atk_coeff = 1.
        self.attack_speed_coeff = 1.
        self.acceleration = 1.

        self.movement_log = []
        self.movement_timestamps = {MovementType.AutoAttackBasic: [],
                                  MovementType.AutoAttackEnhanced: [],
                                  MovementType.LowerSkill: [],
                                  MovementType.UpperSkill: [],
                                  }
        self.damage_records = defaultdict(list)

        self.last_motion_time = 0

    def _setup_all_movement_actions(self):
        """Pre-generates and sorts action templates for all movement types."""
        self._action_templates[MovementType.AutoAttackBasic] = self._setup_basic_attack_actions()
        self._action_templates[MovementType.AutoAttackEnhanced] = self._setup_enhanced_attack_actions()
        self._action_templates[MovementType.LowerSkill] = self._setup_lower_skill_actions()
        self._action_templates[MovementType.UpperSkill] = self._setup_upper_skill_actions()

        # Sort all templates by their t_ratio (the second element in the tuple)
        for template in self._action_templates.values():
            if template:
                template.sort(key=lambda x: x[1])

    def _setup_basic_attack_actions(self):
        """Returns a list of (action, t_ratio) for basic attacks."""
        return []

    def _setup_enhanced_attack_actions(self):
        """Returns a list of (action, t_ratio) for enhanced attacks."""
        return []

    def _setup_lower_skill_actions(self):
        """Returns a list of (action, t_ratio) for lower skill."""
        return []

    def _setup_upper_skill_actions(self):
        """Returns a list of (action, t_ratio) for upper skill."""
        return []

    def _setup_status_templates(self):
        """Initializes status templates for the hero. Should be overridden by subclasses."""
        pass

    def choose_movement(self):
        if self.upper_skill_flag:
            return MovementType.UpperSkill
        
        # Rare case: dt = upper_skill_cd in the previous step
        # Use the if statement below to use UpperSkill first
        can_cast_upper = self.upper_skill_rule and self.upper_skill_rule.should_request(self)
        if self.upper_skill_timer == 0 and can_cast_upper:
            return MovementType.Wait

        if self.sp == self.max_sp:
            return MovementType.LowerSkill
        elif self.aa_timer == 0:
            if self.is_enhanced(): return MovementType.AutoAttackEnhanced
            else:                  return MovementType.AutoAttackBasic
        return MovementType.Wait

    def update(self, t):
        # update sp
        dt = t - self.last_updated
        if self.last_movement not in (MovementType.LowerSkill, MovementType.UpperSkill):
            self.sp_timer += dt
            if self.sp_timer >= SP_INTERVAL:
                num_sp_recover, self.sp_timer = divmod(self.sp_timer, SP_INTERVAL)
                self.sp = min(self.max_sp, self.sp + self.sp_recovery_rate * num_sp_recover)

        # update cd
        self.aa_timer = max(0, self.aa_timer - dt)
        
        prev_upper_skill_timer = self.upper_skill_timer
        self.upper_skill_timer = max(0, self.upper_skill_timer - dt)
        if prev_upper_skill_timer > 0 and self.upper_skill_timer == 0:
            if self.upper_skill_rule and self.upper_skill_rule.should_request(self):
                self.party.upper_skill_manager.add_request(self.party_idx)

        self.aa_cd = self.get_aa_cd()

        self.last_updated = t

    def step(self, t):
        if self.next_t_without_interrupt:
            return_value = self.next_t_without_interrupt
            self.next_t_without_interrupt = 0
            self.update(t)
            return return_value

        self.update(t)
        movement = self.choose_movement()
        
        if movement == MovementType.Wait:
            wait_time = min(SP_INTERVAL - self.sp_timer, self.aa_timer, self.upper_skill_timer)
            dt = max(1, round(wait_time))
        else:
            # Start the movement and get its full duration
            match movement:
                case MovementType.AutoAttackBasic | MovementType.AutoAttackEnhanced:
                    self.aa_timer = self.aa_cd
                case MovementType.LowerSkill:
                    self.sp = 0
                case MovementType.UpperSkill:
                    self.upper_skill_timer = round(self.upper_skill_cd * SEC_TO_MS)
                    self.upper_skill_flag = False
            
            dt = round(self.do_movement(movement, t))
            self.movement_timestamps[movement].append(round(t) / SEC_TO_MS)
            
            # Decide the actual time step
            if self.upper_skill_timer < dt:
                self.next_t_without_interrupt = t + dt
                dt = self.upper_skill_timer

        self.last_movement = movement
        self.movement_log.append((t, movement))
        return t + dt
    
    def calculate_cumulative_damage(self, max_T):
        for key, record in self.damage_records.items():
            for i in range(len(record) - 1, -1, -1):
                if record[i][0] < max_T:
                    self.damage_records[key] = record[i][1]
                    break
        
    def do_movement(self, movement_type, t):
        motion_time = self.get_motion_time(movement_type)
        self.last_motion_time = motion_time
        self.last_updated = t
        
        # Dispatch to specific movement methods
        if movement_type == MovementType.AutoAttackBasic:
            self.BasicAttack(t)
        elif movement_type == MovementType.AutoAttackEnhanced:
            self.EnhancedAttack(t)
            self.eac.on_enhanced_attack(t)      # self.eac is not None here.
        elif movement_type == MovementType.LowerSkill:
            self.LowerSkill(t)
        elif movement_type == MovementType.UpperSkill:
            self.UpperSkill(t)
        
        return motion_time

    def _reserv_actions_from_template(self, movement_type, t):
        """Helper to create and reserve actions from a template."""
        motion_time = self.get_motion_time(movement_type)
        action_tuples = []
        template = self._action_templates.get(movement_type, [])
        for action, t_ratio in template:
            action_tuples.append((action, t + motion_time * t_ratio))
        
        if not action_tuples:
            return
        
        self.reserv_action_chain(action_tuples)

    def BasicAttack(self, t):
        self._reserv_actions_from_template(MovementType.AutoAttackBasic, t)

    def EnhancedAttack(self, t):
        self._reserv_actions_from_template(MovementType.AutoAttackEnhanced, t)

    def LowerSkill(self, t):
        self._reserv_actions_from_template(MovementType.LowerSkill, t)

    def UpperSkill(self, t):
        self._reserv_actions_from_template(MovementType.UpperSkill, t)

    def is_enhanced(self):
        return self.eac and self.eac.is_met()

    def reserv_action(self, action, t):
        self.party.action_manager.add_action_reserv(t, action)

    def reserv_action_chain(self, action_tuples):
        """
        Reserves a chain of actions. The next action is reserved in the post_fn of the previous action.
        Assumes that the actions in the chain (except possibly the last one) do not have a pre-existing post_fn.
        :param action_tuples: A list of (action, execution_time) tuples.
        """
        if not action_tuples:
            return
        # Iterate backwards from the second to last action to chain them up.
        for i in range(len(action_tuples) - 2, -1, -1):
            # Get the current action which needs its post_fn set.
            current_action, _ = action_tuples[i]
            
            # Get the next action that should be scheduled by the current one.
            next_action, next_time = action_tuples[i+1]
            
            # Set the post_fn of the current action to reserve the next action.
            # We use functools.partial to capture the correct action and time.
            partial_fn = partial(self.reserv_action, next_action, next_time)
            current_action.post_fn = lambda _,p=partial_fn: p()
        
        # Schedule the first action in the chain.
        first_action, first_time = action_tuples[0]
        self.reserv_action(first_action, first_time)

    def aa_post_fn(self):
        self.sp = min(self.max_sp, self.sp + self.sp_per_aa)

    def get_aa_cd(self):
        return round(300 * SEC_TO_MS / (self.acceleration**2 * min(10., self.attack_speed_coeff) * self.attack_speed), 0)
    
    def get_motion_time(self, movement_type: MovementType):
        base_motion_time_sec = self.motion_time.get(movement_type)
        if base_motion_time_sec is None:
            raise ValueError(f"Motion time for {movement_type} is not defined.")
        
        motion_time_ms = base_motion_time_sec * SEC_TO_MS

        match movement_type:
            case MovementType.AutoAttackBasic | MovementType.AutoAttackEnhanced:
                return min(motion_time_ms, self.get_aa_cd())
            case MovementType.LowerSkill | MovementType.UpperSkill:
                return motion_time_ms / self.acceleration
        
        raise ValueError(f"Invalid movement type: {movement_type}")
    

    def get_amplify(self, damage_type):
        return self.amplify_dict[damage_type]

    def add_amplify(self, damage_type: DamageType, value: float):
        for dt in DamageType.get_leaf_members(damage_type):
            self.amplify_dict[dt] += value
    
    def get_damage(self, damage, movement_type):
        enemy_amplify = self.party.get_amplify(self)
        additional_coeff = self.party.get_additional_coeff(self)  # include type_effectiveness, hidden damage decrease, etc.
        applying_amplify = max(0.25, self.get_amplify(movement_type) + enemy_amplify)
        applying_atk_coeff = max(0.2, self.atk_coeff)
        return 0.8 * (self.atk * applying_atk_coeff) * applying_amplify * (damage/100) * additional_coeff

    def get_name(self):
        return self.name_kr

    def get_unique_name(self):
        return f"{self.name}_{self.party_idx}"

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
        return np.random.rand() < self.probability

class PeriodicCondition(EnhancedAttackCondition):
    """Triggers every N attacks."""
    def __init__(self, hero, cycle):
        super().__init__(hero)
        if cycle <= 0:
            raise ValueError("Cycle must be positive.")
        self.cycle = cycle

    def is_met(self):
        timestamps = self.hero.movement_timestamps
        num_attacks = len(timestamps[MovementType.AutoAttackBasic]) + len(timestamps[MovementType.AutoAttackEnhanced])
        return (num_attacks + 1) % self.cycle == 0

class BuffCondition(EnhancedAttackCondition):
    """Triggers if the hero has a specific buff."""
    def __init__(self, hero, buff_id):
        super().__init__(hero)
        self.buff_id = buff_id

    def is_met(self):
        return self.hero.has_buff(self.buff_id)

class CooldownCondition(EnhancedAttackCondition):
    """Triggers when a cooldown is over."""
    def __init__(self, hero, cooldown_sec):
        super().__init__(hero)
        self.cooldown = cooldown_sec * SEC_TO_MS
        self.last_triggered_time = -self.cooldown # Allow first attack to be enhanced

    def init_simulation(self):
        self.last_triggered_time = -self.cooldown

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
        return all(cond.is_met() for cond in self.conditions)

    def on_enhanced_attack(self, t):
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

    def is_met(self):
        return any(cond.is_met() for cond in self.conditions)

    def on_enhanced_attack(self, t):
        for cond in self.conditions:
            if cond.is_met():
                cond.on_enhanced_attack(t)

    def init_simulation(self):
        for cond in self.conditions:
            cond.init_simulation()