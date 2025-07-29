from typing import TYPE_CHECKING, Dict, Any, Optional, Callable, List, Union

from dps.data.spell_data import SPELL_DATA
from dps.enums import Grade, StatType
from dps.stat_utils import apply_stat_bonuses

if TYPE_CHECKING:
    from .hero import Hero
    from .party import Party


class Spell:
    spell_data = SPELL_DATA

    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level if 1 <= level <= 12 else 1

        data = self.spell_data.get(self.name)
        if not data:
            raise ValueError(f"Spell '{self.name}' not found in spell_data.")

        self.grade: Grade = data["grade"]
        self.stackable: bool = data["is_stackable"]
        self.description: str = data["description"]
        
        # Raw data from file for reference
        self._stat_types: List[Union[StatType, str]] = data["stat_types"]
        self._stats_by_level: List[Optional[List[float]]] = data["stats"]
        self._effects_by_level: List[Optional[List[float]]] = data["effects"]
        self._stat_growth: List[int] = data["stat_growth"]
        self._effect_growth: List[float] = data["effect_growth"]

        # Properties for the current level
        self.base_cost: int = data["cost"]
        self.cost = self._get_cost_for_level()
        self.stat_bonuses = self._get_stats_for_level()
        self.effects = self._get_effects_for_level()
        
        # These should be defined in subclasses for artifacts with unique effects.
        self.setup_effect_fn: Optional[Callable[['Party'], None]] = None
        self.init_effect_fn: Optional[Callable[['Party'], None]] = None

    def _get_stats_for_level(self) -> Dict[StatType, float]:
        """Extracts stat bonuses for the spell's current level."""
        stats = {}
        if self.level - 1 < len(self._stats_by_level) and self._stats_by_level[self.level - 1]:
            level_stats_values = self._stats_by_level[self.level - 1]
            for i, stat_type in enumerate(self._stat_types):
                if stat_type != "Cost" and i < len(level_stats_values):
                    stats[stat_type] = level_stats_values[i]
        return stats

    def _get_cost_for_level(self) -> int:
        """Determines the spell's cost for the current level."""
        cost = self.base_cost
        if "Cost" in self._stat_types:
            try:
                cost_index = self._stat_types.index("Cost")
                if self.level - 1 < len(self._stats_by_level) and self._stats_by_level[self.level - 1]:
                    level_stats = self._stats_by_level[self.level - 1]
                    if cost_index < len(level_stats):
                        cost = int(level_stats[cost_index])
            except ValueError:
                pass
        return cost

    def _get_effects_for_level(self) -> List[float]:
        """Retrieves the special effect values for the spell's current level."""
        if self.level - 1 < len(self._effects_by_level) and self._effects_by_level[self.level - 1]:
            return self._effects_by_level[self.level - 1] or []
        return []

    def apply_stats(self, party: 'Party'):
        """
        Applies the spell's stat bonuses to all heroes in the party.
        """
        for hero in party.character_list:
            if hero:
                apply_stat_bonuses(hero, self.stat_bonuses)

    def apply_setup_effect(self, party: 'Party'):
        """
        Applies the spell's one-time setup effect to the party.
        """
        if self.setup_effect_fn:
            self.setup_effect_fn(party)

    def apply_init_effect(self, party: 'Party'):
        """
        Applies the spell's simulation-specific initial effect to the party.
        """
        if self.init_effect_fn:
            self.init_effect_fn(party) 