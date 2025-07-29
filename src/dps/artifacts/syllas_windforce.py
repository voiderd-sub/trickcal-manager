from dps.artifact import Artifact
from dps.enums import StatType
from dps.stat_utils import apply_stat_bonuses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

class SyllasWindforce(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="실라의 바람살", level=level)
        self.init_effect_fn = self.init_syllas_windforce

    def init_syllas_windforce(self, hero: 'Hero'):
        """
        Initialization effect for Sylla's Windforce:
        - Increases Attack Speed by a percentage based on artifact level.
        This is called at the beginning of each simulation.
        """
        if self.effects:
            apply_stat_bonuses(hero, {StatType.AttackSpeed: self.effects[0]})