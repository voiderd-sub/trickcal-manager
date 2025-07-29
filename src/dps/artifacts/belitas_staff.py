from dps.artifact import Artifact
from dps.enums import DamageType, StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

def init_belitas_staff(hero: 'Hero', artifact: 'Artifact'):
    """
    Initialization effect for Belita's Staff:
    - Increases all damage dealt by the hero by 25%.
    This is called at the beginning of each simulation.
    """
    hero.add_amplify(DamageType.ALL, 25)

class BelitasStaff(Artifact):
    def __init__(self):
        super().__init__(
            name="벨리타의 지팡이",
            stat_bonuses={
                StatType.AttackMagic: 17.29,
                StatType.CriticalMult: 17.29
            },
            setup_effect_fn=None,
            init_effect_fn=init_belitas_staff,
            stackable=True,
        ) 