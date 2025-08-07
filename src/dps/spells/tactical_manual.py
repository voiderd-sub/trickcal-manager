from dps.spell import Spell
from dps.enums import DamageType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class TacticalManual(Spell):
    def __init__(self, level: int = 1):
        super().__init__("전술 교본", level)
    
    def apply_init_effect(self, party: 'Party'):
        damage_bonus = self.effects[0]
        
        for idx in party.active_indices:
            party.character_list[idx].add_amplify(DamageType.ALL, damage_bonus)
