from dps.artifact import Artifact
from dps.enums import DamageType, MovementType, StatType
from dps.action import InstantAction
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party


def weather_is_clear_card_effect(hero: 'Hero'):
    """
    Unique effect for Clear Weather Card:
    - Every 3 basic attacks, lightning strikes for 150% attack damage
    """
    # Initialize counter for basic attacks
    if 'weather_is_clear_card_counter' not in hero.artifact_counters:
        hero.artifact_counters['weather_is_clear_card_counter'] = 0
    
    # Store reference to the original aa_post_fn
    original_aa_post_fn = hero.aa_post_fn
    
    def enhanced_aa_post_fn():
        # Call original function first
        original_aa_post_fn()
        
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


class WeatherIsClearCard(Artifact):
    def __init__(self):
        super().__init__(
            name="날씨는 맑음 카드",
            stat_bonuses={
                StatType.AttackSpeed: 17.98,
                StatType.CriticalRate: 17.98
            },
            unique_effect_fn=weather_is_clear_card_effect,
            stackable=False,  # This effect does not stack
            column_wide=False  # This effect only applies to the wearer
        ) 