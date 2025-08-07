from dps.spell import Spell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party

class GroupGradeUp(Spell):
    def __init__(self, level: int = 1):
        super().__init__("단체 월반", level)
        self.stackable = False
    
    def apply_setup_effect(self, party: 'Party'):
        for idx in party.active_indices:
            party.character_list[idx].increase_grade(1)