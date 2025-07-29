from dps.artifact import Artifact
from dps.enums import DamageType, StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact


class BelitasStaff(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="벨리타의 지팡이", level=level)
        self.init_effect_fn = self.init_effect

    def init_effect(self, hero: 'Hero'):
        """
        Initialization effect for Belita's Staff:
        - Increases all damage dealt by the hero by a percentage based on artifact level.
        This is called at the beginning of each simulation.
        """
        if self.effects:
            hero.add_amplify(DamageType.ALL, self.effects[0]) 