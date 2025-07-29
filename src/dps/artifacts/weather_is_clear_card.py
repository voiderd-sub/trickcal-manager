from dps.artifact import Artifact
from dps.enums import DamageType, MovementType, StatType
from dps.action import InstantAction
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party


def setup_weather_is_clear_card(hero: 'Hero'):
    """
    Setup effect for Clear Weather Card:
    - Modifies the hero's aa_post_fn to add a counter and a lightning strike effect.
    This is called once per run.
    """
    # Store reference to the original aa_post_fn if it hasn't been stored yet.
    if not hasattr(hero, 'original_aa_post_fn_cwc'):
        hero.original_aa_post_fn_cwc = hero.aa_post_fn
    
    def enhanced_aa_post_fn():
        # Call original function first
        hero.original_aa_post_fn_cwc()
        
        # Increment counter
        hero.artifact_counters['weather_is_clear_card_counter'] += 1
        
        # Check if lightning should strike (every 3 attacks)
        if hero.artifact_counters['weather_is_clear_card_counter'] >= 3:
            # Reset counter
            hero.artifact_counters['weather_is_clear_card_counter'] = 0
            
            # Create lightning damage action
            lightning_action = InstantAction(
                hero=hero,
                damage_coeff=150,
                source_movement=MovementType.Artifact,
                damage_type=DamageType.Artifact
            )
            
            # Schedule lightning damage immediately
            hero.reserv_action(lightning_action, hero.party.current_time)
    
    # Replace the aa_post_fn with our enhanced version
    hero.aa_post_fn = enhanced_aa_post_fn

def init_weather_is_clear_card(hero: 'Hero', artifact: 'Artifact'):
    """
    Initialization effect for Clear Weather Card:
    - Resets the basic attack counter for the lightning strike effect.
    This is called at the beginning of each simulation.
    """
    hero.artifact_counters['weather_is_clear_card_counter'] = 0


class WeatherIsClearCard(Artifact):
    def __init__(self):
        super().__init__(
            name="날씨는 맑음 카드",
            stat_bonuses={
                StatType.AttackSpeed: 17.98,
                StatType.CriticalRate: 17.98
            },
            setup_effect_fn=setup_weather_is_clear_card,
            init_effect_fn=init_weather_is_clear_card,
            stackable=False,  # This effect does not stack
        ) 