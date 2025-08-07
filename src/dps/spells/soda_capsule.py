from dps.spell import Spell

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class SodaCapsule(Spell):
    def __init__(self, level: int = 1):
        super().__init__("소다맛 캡슐", level)
    
    def apply_init_effect(self, party: 'Party'):
        sp_recovery = self.effects[0]
        
        for idx in party.active_indices:
            hero = party.character_list[idx]
            hero.sp = min(hero.max_sp, hero.sp + sp_recovery)
