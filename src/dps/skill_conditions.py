from dps.enums import *

class UpperSkillCastCondition:
    """Base class for upper skill casting conditions."""
    def __init__(self, cancel_current_movement: bool = False):
        self.cancel_current_movement = cancel_current_movement

    def should_request(self, hero) -> bool:
        """Determines if the hero should request to use their upper skill."""
        raise NotImplementedError

class CooldownReadyCondition(UpperSkillCastCondition):
    """Casts the upper skill as soon as the cooldown is over."""
    def __init__(self, cancel_current_movement: bool = False):
        super().__init__(cancel_current_movement)
        
    def should_request(self, hero) -> bool:
        return True

class NeverCastCondition(UpperSkillCastCondition):
    """Never casts the upper skill."""
    def __init__(self, cancel_current_movement: bool = False):
        super().__init__(False)     # never cast, never cancel current movement

    def should_request(self, hero) -> bool:
        return False

class MovementTriggerCondition(UpperSkillCastCondition):
    """
    Casts the upper skill after a specific movement from another hero,
    within a defined time window.
    """
    def __init__(self, trigger_hero_unique_name: str, trigger_movement: MovementType, 
                 delay_min_seconds: float, delay_max_seconds: float, 
                 cancel_current_movement: bool = False):
        super().__init__(cancel_current_movement)
        self.trigger_hero_unique_name = trigger_hero_unique_name
        self.trigger_movement = trigger_movement
        self.delay_min_seconds = delay_min_seconds
        self.delay_max_seconds = delay_max_seconds

    def should_request(self, hero) -> bool:
        # This condition is handled by the UpperSkillManager's delayed request queue,
        # not by the hero's direct request mechanism.
        return False 