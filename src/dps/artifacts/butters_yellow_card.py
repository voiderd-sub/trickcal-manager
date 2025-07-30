from dps.artifact import Artifact
from dps.enums import DamageType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero


class ButtersYellowCard(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="버터의 옐로카드", level=level)

    def apply_init_effect(self, hero: "Hero"):
        """
        Initialization effect for Butter's Yellow Card:
        - Increases enhanced attack damage dealt by the hero by a percentage based on artifact level.
        This is called at the beginning of each simulation.
        """
        hero.add_amplify(DamageType.AutoAttackEnhanced, self.effects[0]) 