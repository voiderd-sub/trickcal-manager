from dps.artifact import Artifact
from dps.enums import DamageType, StatType
from dps.stat_utils import apply_stat_bonuses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

class Kettlebell30kg(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="30KG 케틀벨", level=level)

    def apply_init_effect(self, hero: 'Hero'):
        """
        Initialization effect for 30KG Kettlebell:
        - Increases the hero's skill damage by a percentage based on level.
        - Decreases the hero's attack speed by 30%.
        """
        if self.effects:
            hero.add_amplify(DamageType.Skill, self.effects[0])
        apply_stat_bonuses(hero, {StatType.AttackSpeed: -30}) 