from dps.spell import Spell
import random

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class AromaTherapy(Spell):    
    def __init__(self, level: int = 1):
        super().__init__("아로마 테라피", level)
    
    def apply_init_effect(self, party: 'Party'):
        lowest_sp_ratio = float('inf')
        lowest_sp_heroes = []

        for idx in party.active_indices:
            hero = party.character_list[idx]
            sp_ratio = hero.sp / hero.max_sp

            if sp_ratio < lowest_sp_ratio:
                lowest_sp_ratio = sp_ratio
                lowest_sp_heroes = [hero]
            elif sp_ratio == lowest_sp_ratio:
                lowest_sp_heroes.append(hero)

        if lowest_sp_heroes:
            target_hero = random.choice(lowest_sp_heroes)
            target_hero.sp = target_hero.max_sp







