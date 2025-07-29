from dps.artifact import Artifact
from dps.enums import StatType, DamageType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.artifact import Artifact

class FriclesQueenRegentsSeal(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="프리클의 여왕 대리 인장", level=level)
        self.init_effect_fn = self.init_fricles_queen_regents_seal

    def init_fricles_queen_regents_seal(self, hero: 'Hero'):
        """
        Initializes the effect for Fricle's Queen Regent's Seal.
        This effect increases the skill damage of all allies in the same row.
        """
        if not self.effects:
            return
            
        party = hero.party
        hero_row = hero.party_idx // 3

        for idx in party.active_indices:
            ally = party.character_list[idx]
            if ally.party_idx // 3 == hero_row:
                ally.add_amplify(DamageType.Skill, self.effects[0]) 