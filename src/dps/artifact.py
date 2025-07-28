from typing import TYPE_CHECKING, Dict, Any, Optional, Callable
from dps.stat_utils import apply_stat_bonuses

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

class Artifact:
    def __init__(self, name: str, stat_bonuses: Dict[str, Any], 
                 unique_effect_fn: Optional[Callable[['Hero'], None]] = None,
                 stackable: bool = True, column_wide: bool = False):
        """
        Initializes an artifact.

        :param name: The name of the artifact.
        :param stat_bonuses: A dictionary where keys are StatType enum names (str)
                             and values are the bonuses to apply.
        :param unique_effect_fn: Optional function for unique effects.
        :param stackable: Whether this artifact's unique effect can stack with duplicates.
        :param column_wide: Whether this artifact's unique effect applies to the entire column.
        """
        self.name = name
        self.stat_bonuses = stat_bonuses
        self.unique_effect_fn = unique_effect_fn
        self.stackable = stackable
        self.column_wide = column_wide

    def apply_stats(self, hero: 'Hero'):
        """
        Applies the artifact's stat bonuses to a hero.
        This method is called once at the beginning of a simulation.
        """
        apply_stat_bonuses(hero, self.stat_bonuses) 


    def apply_unique_effect(self, hero: 'Hero'):
        """
        Applies the artifact's unique effect to a hero.
        This method is called once at the beginning of a simulation.
        """
        if self.unique_effect_fn:
            self.unique_effect_fn(hero) 