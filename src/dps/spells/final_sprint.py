from dps.spell import Spell
from dps.enums import StatType, SEC_TO_MS
from dps.action import Action
from dps.stat_utils import apply_stat_bonuses

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class FinalSprintAction(Action):    
    def __init__(self, party: 'Party', attack_speed_bonus: float):
        super().__init__(
            hero=None,
            action_type=None,
            source_movement=None,
            damage_type=None
        )
        self.party = party
        self.attack_speed_bonus = attack_speed_bonus
    
    def action_fn(self, current_time):
        for idx in self.party.active_indices:
            hero = self.party.character_list[idx]
            apply_stat_bonuses(hero, {StatType.AttackSpeed: self.attack_speed_bonus})


class FinalSprint(Spell):    
    def __init__(self, level: int = 1):
        super().__init__("막판 스퍼트", level)
        self.stackable = False
    
    def apply_init_effect(self, party: 'Party'):
        final_sprint_start_time = max(0, party.max_t - 40 * SEC_TO_MS)
        
        attack_speed_bonus = self.effects[0]
        
        final_sprint_action = FinalSprintAction(party, attack_speed_bonus)
        party.action_manager.add_pending_effect(final_sprint_start_time, final_sprint_action)
