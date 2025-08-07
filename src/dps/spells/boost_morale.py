from dps.spell import Spell
from dps.enums import StatType
from dps.stat_utils import apply_stat_bonuses

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class BoostMorale(Spell):
    def __init__(self, level: int = 1):
        super().__init__("사기진작", level)
    
    def apply_init_effect(self, party: 'Party'):
        attack_speed_bonus = self.effects[0]
        
        for idx in party.active_indices:
            hero = party.character_list[idx]
            apply_stat_bonuses(hero, {StatType.AttackSpeed: attack_speed_bonus})
