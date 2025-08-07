from dps.spell import Spell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party

class MeditationTime(Spell):
    def __init__(self, level: int = 1):
        super().__init__("명상의 시간", level)

    def apply_init_effect(self, party: 'Party'):
        sp_recovery_bonus = self.effects[0]
        
        for idx in party.active_indices:
            party.character_list[idx].add_sp_recovery_percent_bonus(sp_recovery_bonus)