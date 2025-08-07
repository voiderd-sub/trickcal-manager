from dps.spell import Spell
from dps.enums import DamageType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class Vanguard(Spell):
    def __init__(self, level: int = 1):
        super().__init__("선봉대", level)
    
    def apply_init_effect(self, party: 'Party'):
        damage_bonus, damage_reduction = self.effects
        
        for idx in party.active_indices:
            if idx < 3:  # 전열 (0, 1, 2)
                hero = party.character_list[idx]
                hero.add_amplify(DamageType.ALL, damage_bonus)
                hero.reduce_damage_taken(DamageType.ALL, damage_reduction)
