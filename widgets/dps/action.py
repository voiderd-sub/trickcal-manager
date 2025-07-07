from widgets.dps.enums import *
import random
from widgets.dps.status import StatusReservation

# Tree structure classes for action templates
class ActionNode:
    """Base class for action tree nodes"""
    def __init__(self):
        pass

    def evaluate(self, hero, t, motion_time):
        """Evaluate the node and return list of (timing_ratio, delay, action) tuples"""
        raise NotImplementedError


class ActionLeafNode(ActionNode):
    """Leaf node that holds a pre-made action object"""
    def __init__(self, timing_ratio: float, delay: float, action):
        super().__init__()
        self.timing_ratio = timing_ratio
        self.delay = delay
        self.action = action

    def evaluate(self, hero, t, motion_time):
        # 미리 만들어진 action 객체를 반환
        return [(self.timing_ratio, self.delay, self.action)]


class ConditionNode(ActionNode):
    """Node that evaluates a condition and branches"""
    def __init__(self, condition: dict, true_branch: ActionNode, false_branch: ActionNode):
        super().__init__()
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def evaluate(self, hero, t, motion_time):
        if self._evaluate_condition(hero, self.condition):
            return self.true_branch.evaluate(hero, t, motion_time)
        else:
            return self.false_branch.evaluate(hero, t, motion_time)

    def _evaluate_condition(self, hero, condition):
        """Evaluate a condition"""
        condition_type = condition["type"]
        
        if condition_type == "has_buff":
            return hero.has_buff(condition["buff_id"])
        elif condition_type == "random":
            return random.random() < condition["probability"]
        # 다른 조건 타입들도 추가 가능
        
        return False


class SequenceNode(ActionNode):
    """Node that executes multiple actions in sequence"""
    def __init__(self, children: list[ActionNode]):
        super().__init__()
        self.children = children

    def evaluate(self, hero, t, motion_time):
        actions = []
        for child in self.children:
            actions.extend(child.evaluate(hero, t, motion_time))
        return actions


# Factory functions for creating tree nodes from dictionaries
def create_action_node_from_dict(node_data: dict) -> ActionNode:
    """Create an ActionNode from dictionary data"""
    node_type = node_data.get("type")
    
    if node_type == "action":
        return ActionLeafNode(
            timing_ratio=node_data["timing_ratio"],
            delay=node_data["delay"],
            action=node_data["action"]
        )
    
    elif node_type == "condition":
        return ConditionNode(
            condition=node_data["condition"],
            true_branch=create_action_node_from_dict(node_data["true_branch"]),
            false_branch=create_action_node_from_dict(node_data["false_branch"])
        )
    
    elif node_type == "sequence":
        children = [create_action_node_from_dict(child) for child in node_data["children"]]
        return SequenceNode(children)
    
    else:
        raise ValueError(f"Unknown node type: {node_type}")


# Base action class with time information
class Action:
    def __init__(self,
                 hero,   # Hero
                 action_type: ActionType,
                 source_movement: MovementType,
                 damage_type: DamageType):
        self.hero = hero
        self.source_movement = source_movement
        self.damage_type = damage_type if damage_type else MovementType.movement_type_to_dmg_type(source_movement)
        self.action_type = action_type  # Instant, Projectile, Status
        
        # Time information (set by schedule_action_template)
        self.execution_time = 0
        self.delay = 0

    def action_fn(self, current_time):
        """Execute the action"""
        raise NotImplementedError

    def __lt__(self, other):
        return self.execution_time < other.execution_time


def apply_instant_damage(hero, damage_type, time, damage_coeff, movement_type=None):
    time = int(time)
    movement_type = movement_type if movement_type else damage_type.name
    damage_records = hero.damage_records[movement_type]
    damage = hero.get_damage(damage_coeff, damage_type)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((int(time // SEC_TO_MS), last_cumulative_damage + damage))


# Wrong implementation. Damage is applied at the time of the action, not at the time of the hit.

# def apply_delayed_damage(hero, damage_type, time, damage_coeff, hit_delay, movement_type=None):
#     movement_type = movement_type if movement_type else damage_type.name
#     damage_records = hero.damage_records[movement_type]
#     damage = hero.get_damage(damage_coeff, damage_type)
#     last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
#     damage_records.append((int((time + hit_delay) // SEC_TO_MS), last_cumulative_damage + damage))


class InstantAction(Action):
    def __init__(self, hero, damage_coeff, source_movement, damage_type):
        super().__init__(hero, ActionType.Instant, source_movement, damage_type)
        self.damage_coeff = damage_coeff

    def action_fn(self, current_time):
        apply_instant_damage(hero = self.hero,
                             damage_type = self.damage_type,
                             time = current_time,
                             damage_coeff = self.damage_coeff,
                             movement_type = self.source_movement)
        self._handle_post_action_effects()

    def _handle_post_action_effects(self):
        """Handle post-action effects like SP recovery"""
        if self.source_movement in [MovementType.AutoAttackBasic, MovementType.AutoAttackEnhanced]:
            self.hero.aa_post_fn()


class ProjectileAction(Action):
    def __init__(self, hero, damage_coeff, hit_delay, source_movement, damage_type):
        super().__init__(hero, ActionType.Projectile, source_movement, damage_type)
        self.damage_coeff = damage_coeff
        self.hit_delay = hit_delay
        self.instant_action = InstantAction(hero, damage_coeff, source_movement, damage_type)

    def action_fn(self, current_time):
        effect_time = current_time + int(self.hit_delay)
        self.hero.party.action_manager.add_pending_effect(effect_time, self.instant_action, 0)
    
    def _handle_post_action_effects(self):
        """Handle post-action effects like SP recovery"""
        if self.source_movement in [MovementType.AutoAttackBasic, MovementType.AutoAttackEnhanced]:
            self.hero.aa_post_fn()


class StatusAction(Action):
    def __init__(self, hero, status, source_movement, damage_type):
        super().__init__(hero, ActionType.Status, source_movement, damage_type)
        self.status = status  # StatusTemplate

    def action_fn(self, current_time):
        # StatusReservation을 생성해서 넘긴다
        start_time = current_time
        duration = getattr(self.status, 'duration', 0)
        end_time = start_time + int(duration * SEC_TO_MS)
        reservation = StatusReservation(self.status, start_time, end_time)
        self.hero.party.status_manager.add_status_reserv(reservation)