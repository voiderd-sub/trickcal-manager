from dps.spell import Spell
from dps.enums import DamageType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class HowToGetHitPainlessly(Spell):
    def __init__(self, level: int = 1):
        super().__init__("안 아프게 맞는 법", level)
    
    def apply_init_effect(self, party: 'Party'):
        damage_reduction = self.effects[0]
        
        for idx in party.active_indices:
            hero = party.character_list[idx]
            hero.reduce_damage_taken(DamageType.ALL, damage_reduction)
