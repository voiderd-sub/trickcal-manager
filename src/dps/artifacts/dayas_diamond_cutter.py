from dps.artifact import Artifact
from dps.enums import StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

class DayasDiamondCutter(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="다야의 다이아몬드 커터", level=level)
        self.init_effect_fn = self.init_effect
        
    def init_effect(self, hero: 'Hero'):
        """
        Initialization effect for Daya's Diamond Cutter:
        - Adds an amplify modifier to the hero for this simulation.
        """
        def amplify_modifier(damage_type):
            """
            Returns a conditional amplify value.
            Increases damage if the enemy has any debuff.
            """
            enemy_id = 9 # Assuming a single enemy for now
            debuffs = hero.party.status_manager.active_debuffs[enemy_id]
            if debuffs and self.effects:
                return self.effects[0]
            return 0.0

        hero.amplify_modifiers[id(self)] = amplify_modifier 