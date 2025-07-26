class UpperSkillCastCondition:
    """Base class for upper skill casting conditions."""
    def should_request(self, hero) -> bool:
        """Determines if the hero should request to use their upper skill."""
        raise NotImplementedError

class CooldownReadyCondition(UpperSkillCastCondition):
    """Casts the upper skill as soon as the cooldown is over."""
    def should_request(self, hero) -> bool:
        return True

class NeverCastCondition(UpperSkillCastCondition):
    """Never casts the upper skill."""
    def should_request(self, hero) -> bool:
        return False 