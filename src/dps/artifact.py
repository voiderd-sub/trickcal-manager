from typing import TYPE_CHECKING, Dict, Any, Optional, Callable, List, Union

from .data.artifact_data import ARTIFACT_DATA
from .enums import Grade, StatType
from .stat_utils import apply_stat_bonuses

if TYPE_CHECKING:
    from .hero import Hero


class Artifact:
    """
    Base class for all artifacts.

    This class is designed to be subclassed for each specific artifact.
    It handles loading all the statistical data from the central artifact_data file.
    Subclasses are responsible for implementing the unique effects of the artifact
    by providing `setup_effect_fn` or `init_effect_fn`.
    """
    artifact_data = ARTIFACT_DATA

    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level if 1 <= level <= 12 else 1

        data = self.artifact_data.get(self.name)
        if not data:
            raise ValueError(f"Artifact '{self.name}' not found in artifact_data.")

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
        self.setup_effect_fn: Optional[Callable[['Hero'], None]] = None
        self.init_effect_fn: Optional[Callable[['Hero'], None]] = None

    def _get_stats_for_level(self) -> Dict[StatType, float]:
        """Extracts stat bonuses for the artifact's current level."""
        stats = {}
        if self.level - 1 < len(self._stats_by_level) and self._stats_by_level[self.level - 1]:
            level_stats_values = self._stats_by_level[self.level - 1]
            for i, stat_type in enumerate(self._stat_types):
                if stat_type != "Cost" and i < len(level_stats_values):
                    stats[stat_type] = level_stats_values[i]
        return stats

    def _get_cost_for_level(self) -> int:
        """Determines the artifact's cost for the current level."""
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
        """Retrieves the special effect values for the artifact's current level."""
        if self.level - 1 < len(self._effects_by_level) and self._effects_by_level[self.level - 1]:
            return self._effects_by_level[self.level - 1] or []
        return []

    def apply_stats(self, hero: 'Hero'):
        """Applies the artifact's stat bonuses to a hero."""
        apply_stat_bonuses(hero, self.stat_bonuses)

    def apply_setup_effect(self, hero: 'Hero'):
        """
        Applies the artifact's one-time setup effect to a hero.
        This is meant to be implemented in subclasses for specific artifacts.
        """
        if self.setup_effect_fn:
            self.setup_effect_fn(hero)

    def apply_init_effect(self, hero: 'Hero'):
        """
        Applies the artifact's simulation-specific initial effect to a hero.
        This is meant to be implemented in subclasses for specific artifacts.
        """
        if self.init_effect_fn:
            self.init_effect_fn(hero) 