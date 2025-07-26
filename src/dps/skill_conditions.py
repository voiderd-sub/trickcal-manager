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
        super().__init__(cancel_current_movement)

    def should_request(self, hero) -> bool:
        return False 