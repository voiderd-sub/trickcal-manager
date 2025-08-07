from dps.artifact import Artifact
from dps.enums import DamageType

class LeetsEarthSmasher(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="리츠의 대지 뽀개기", level=level)

    def apply_init_effect(self, hero):
        """
        Applies the damage reduction effect to all allies in the same row.
        """
        effect_value = self.effects[0]
        
        # This artifact affects all heroes in the same row as the wearer.
        # The wearer is 'hero'. We need to find other heroes in the same row from hero.party
        
        hero_row = hero.party_idx // 3
        for ally_idx in hero.party.active_indices:
            ally = hero.party.character_list[ally_idx]
            if ally and ally.party_idx // 3 == hero_row:
                ally.reduce_damage_taken(DamageType.ALL, effect_value) 