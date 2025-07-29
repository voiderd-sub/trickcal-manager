from typing import TYPE_CHECKING, Dict, Any, Optional, Callable
from dps.stat_utils import apply_stat_bonuses

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

class Artifact:
    def __init__(self, name: str, stat_bonuses: Dict[str, Any], 
                 setup_effect_fn: Optional[Callable[['Hero'], None]] = None,
                 init_effect_fn: Optional[Callable[['Hero', 'Artifact'], None]] = None,
                 stackable: bool = True):
        """
        Initializes an artifact.

        :param name: The name of the artifact.
        :param stat_bonuses: A dictionary where keys are StatType enum names (str)
                             and values are the bonuses to apply.
        :param setup_effect_fn: Optional function for one-time setup effects (e.g., monkey-patching). Called once per run.
        :param init_effect_fn: Optional function for effects that need re-initialization every simulation.
        :param stackable: Whether this artifact's unique effect can stack with duplicates.
        """
        self.name = name
        self.stat_bonuses = stat_bonuses
        self.setup_effect_fn = setup_effect_fn
        self.init_effect_fn = init_effect_fn
        self.stackable = stackable

    def apply_stats(self, hero: 'Hero'):
        """
        Applies the artifact's stat bonuses to a hero.
        """
        apply_stat_bonuses(hero, self.stat_bonuses) 

    def apply_setup_effect(self, hero: 'Hero'):
        """
        Applies the artifact's one-time setup effect to a hero.
        """
        if self.setup_effect_fn:
            self.setup_effect_fn(hero)

    def apply_init_effect(self, hero: 'Hero'):
        """
        Applies the artifact's simulation-specific initial effect to a hero.
        """
        if self.init_effect_fn:
            self.init_effect_fn(hero, self) 