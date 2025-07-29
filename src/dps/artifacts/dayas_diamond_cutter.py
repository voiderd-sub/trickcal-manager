from dps.artifact import Artifact
from dps.enums import StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

def init_dayas_diamond_cutter(hero: 'Hero', artifact: 'Artifact'):
    """
    Initialization effect for Daya's Diamond Cutter:
    - Adds an amplify modifier to the hero for this simulation.
    """
    def amplify_modifier(damage_type):
        """
        Returns a conditional amplify value.
        Increases damage by 35% if the enemy has any debuff.
        """
        enemy_id = 9
        debuffs = hero.party.status_manager.active_debuffs[enemy_id]
        if debuffs:
            return 0.35
        return 0.0

    hero.amplify_modifiers[id(artifact)] = amplify_modifier

class DayasDiamondCutter(Artifact):
    def __init__(self):
        super().__init__(
            name="다야의 다이아몬드 커터",
            stat_bonuses={
                StatType.AttackMagic: 22.74,
                StatType.CriticalRate: 27.66
            },
            setup_effect_fn=None,
            init_effect_fn=init_dayas_diamond_cutter,
            stackable=True
        ) 