from typing import TYPE_CHECKING, Dict, Any
from dps.enums import StatType

if TYPE_CHECKING:
    from dps.hero import Hero


def apply_stat_bonuses(hero: 'Hero', stat_bonuses: Dict[str, Any]):
    """
    Applies stat bonuses to a hero. This function can be reused by artifacts, spells, etc.
    
    :param hero: The hero to apply stats to
    :param stat_bonuses: Dictionary mapping stat names to bonus values
    """
    for stat_type, value in stat_bonuses.items():
        value_percent = value / 100.0
        attr_name = stat_type.to_hero_attr(is_coeff=True)
        current_value = getattr(hero, attr_name, 1.0)
        setattr(hero, attr_name, current_value + value_percent)