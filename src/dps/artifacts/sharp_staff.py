from dps.artifact import Artifact
from dps.enums import DamageType

class SharpStaff(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="날카로운 지팡이", level=level)

    def apply_init_effect(self, hero):
        """
        Applies the skill damage increase effect.
        """
        effect_value = self.effects[0]
        hero.add_amplify(DamageType.Skill, effect_value) 