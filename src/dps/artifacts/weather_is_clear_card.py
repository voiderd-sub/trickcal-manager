from dps.artifact import Artifact
from dps.enums import DamageType, MovementType, StatType
from dps.action import InstantAction
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

class WeatherIsClearCard(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="날씨는 맑음 카드", level=level)
        self.setup_effect_fn = self.setup_weather_is_clear_card
        self.init_effect_fn = self.init_weather_is_clear_card

    def setup_weather_is_clear_card(self, hero: 'Hero'):
        """
        Setup effect for Clear Weather Card:
        - Modifies the hero's aa_post_fn to add a counter and a lightning strike effect.
        This is called once per run.
        """
        if not hasattr(hero, 'original_aa_post_fn_cwc'):
            hero.original_aa_post_fn_cwc = hero.aa_post_fn
        
        def enhanced_aa_post_fn():
            hero.original_aa_post_fn_cwc()
            
            hero.artifact_counters['weather_is_clear_card_counter'] += 1
            
            if hero.artifact_counters['weather_is_clear_card_counter'] >= 3:
                hero.artifact_counters['weather_is_clear_card_counter'] = 0
                
                if self.effects:
                    lightning_action = InstantAction(
                        hero=hero,
                        damage_coeff=self.effects[0],
                        source_movement=MovementType.Artifact,
                        damage_type=DamageType.Artifact
                    )
                    hero.reserv_action(lightning_action, hero.party.current_time)
        
        hero.aa_post_fn = enhanced_aa_post_fn

    def init_weather_is_clear_card(self, hero: 'Hero'):
        """
        Initialization effect for Clear Weather Card:
        - Resets the basic attack counter for the lightning strike effect.
        This is called at the beginning of each simulation.
        """
        hero.artifact_counters['weather_is_clear_card_counter'] = 0 