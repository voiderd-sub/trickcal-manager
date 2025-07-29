from typing import TYPE_CHECKING, Dict, Any, Optional, Callable
from dps.stat_utils import apply_stat_bonuses

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

class Spell:
    def __init__(self, name: str, stat_bonuses: Dict[str, Any],
                 setup_effect_fn: Optional[Callable[['Party'], None]] = None,
                 init_effect_fn: Optional[Callable[['Party'], None]] = None,
                 stackable: bool = True):
        """
        Initializes a spell.

        :param name: The name of the spell.
        :param stat_bonuses: A dictionary where keys are StatType enum names (str)
                             and values are the bonuses to apply.
        :param setup_effect_fn: Optional function for one-time setup effects. Called once per run.
        :param init_effect_fn: Optional function for effects that need re-initialization every simulation.
        :param stackable: Whether this spell's unique effect can stack with duplicates.
        """
        self.name = name
        self.stat_bonuses = stat_bonuses
        self.setup_effect_fn = setup_effect_fn
        self.init_effect_fn = init_effect_fn
        self.stackable = stackable

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