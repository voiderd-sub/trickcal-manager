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
        self.stackable: bool = True # If false, you must explicitly modify this value after inheriting it.
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

        # If different spells have the same unique effect
        # and the unique effect cannot be duplicated,
        # this attribute should be overridden with the same value for them.
        self.effect_id = type(self).__name__

    def _get_stats_for_level(self) -> Dict[StatType, float]:
        """
        Extracts stat bonuses for the spell's current level.
        If data for the current level is missing, it estimates the values based on level 1 stats and growth rates.
        """
        stats = {}
        level_idx = self.level - 1

        # Check if data for the current level exists
        if level_idx < len(self._stats_by_level) and self._stats_by_level[level_idx]:
            level_stats_values = self._stats_by_level[level_idx]
            for i, stat_type_str in enumerate(self._stat_types):
                if stat_type_str != "Cost" and i < len(level_stats_values):
                    stats[stat_type_str] = level_stats_values[i]
        # If data is missing, estimate it
        elif self._stats_by_level and self._stats_by_level[0]:
            level_1_stats = self._stats_by_level[0]
            for i, stat_type_str in enumerate(self._stat_types):
                if stat_type_str != "Cost" and i < len(level_1_stats) and i < len(self._stat_growth):
                    level_1_value = level_1_stats[i]
                    growth = self._stat_growth[i]
                    
                    estimated_value = level_1_value * (1 + (self.level - 1) / 11 * growth / 100)
                    stats[stat_type_str] = round(estimated_value, 2)
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
        """
        Retrieves the special effect values for the spell's current level.
        If data for the current level is missing, it estimates the values based on level 1 effects and growth rates.
        """
        level_idx = self.level - 1

        # Check if data for the current level exists
        if level_idx < len(self._effects_by_level) and self._effects_by_level[level_idx] is not None:
            return self._effects_by_level[level_idx] or []
        
        # If data is missing, estimate it
        estimated_effects = []
        if self._effects_by_level and self._effects_by_level[0] is not None:
            level_1_effects = self._effects_by_level[0]
            for i, effect_val in enumerate(level_1_effects):
                if i < len(self._effect_growth):
                    growth = self._effect_growth[i]
                    
                    estimated_value = effect_val + (self.level - 1) * growth
                    
                    # Rounding rule based on level 1 value type
                    if effect_val == int(effect_val):
                        estimated_effects.append(round(estimated_value))
                    else:
                        estimated_effects.append(round(estimated_value, 2))
                else:
                     estimated_effects.append(effect_val)
        
        return estimated_effects

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
        pass

    def apply_init_effect(self, party: 'Party'):
        """
        Applies the spell's simulation-specific initial effect to the party.
        """
        pass