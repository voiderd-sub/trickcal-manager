from dps.artifact import Artifact
from dps.enums import StatType
from dps.stat_utils import apply_stat_bonuses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

def init_syllas_windforce(hero: 'Hero', artifact: 'Artifact'):
    """
    Initialization effect for Sylla's Windforce:
    - Increases Attack Speed by 60%.
    This is called at the beginning of each simulation.
    """
    # The logic is same as 'stat bonus',
    # but since it is a unique effect, it is implemented separately like this.
    apply_stat_bonuses(hero, {StatType.AttackSpeed: 60})

class SyllasWindforce(Artifact):
    def __init__(self):
        super().__init__(
            name="실라의 바람살",
            stat_bonuses={
                StatType.CriticalRate: 24.2
            },
            setup_effect_fn=None,
            init_effect_fn=init_syllas_windforce,
            stackable=True
        )