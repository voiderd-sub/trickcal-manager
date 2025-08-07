from dps.spell import Spell
from dps.enums import DamageType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class IgnoreWeak(Spell):
    def __init__(self, level: int = 1):
        super().__init__("약자무시", level)
    
    def apply_init_effect(self, party: 'Party'):
        damage_bonus = self.effects[0]
        
        for idx in party.active_indices:
            hero = party.character_list[idx]
            hero.add_amplify(DamageType.AutoAttack, damage_bonus)
