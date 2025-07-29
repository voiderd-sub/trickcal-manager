from dps.artifact import Artifact
from dps.enums import StatType, SEC_TO_MS
from typing import TYPE_CHECKING
import math

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

def setup_dragonlightsword(hero: 'Hero'):
    """Setup effect for DragonLightSword. This is called once per run."""
    # 1. Monkey-patch get_coeff to dynamically add attack speed
    if not hasattr(hero, 'original_get_coeff_dls'):
        hero.original_get_coeff_dls = hero.get_coeff
    
    def enhanced_get_coeff(stat_type: StatType):
        # First, get the base coefficient value from the original function
        base_coeff = hero.original_get_coeff_dls(stat_type)
        
        # Only modify the coefficient if it's for AttackSpeed
        if stat_type == StatType.AttackSpeed:
            last_reset_time = hero.artifact_counters.get('dragonlightsword_last_reset_time')
            current_time = hero.party.current_time
            
            stacks = math.floor(current_time / SEC_TO_MS) - math.floor(last_reset_time / SEC_TO_MS)
            dls_as_bonus = stacks * 0.08
            
            return base_coeff + dls_as_bonus
        
        # For all other stats, return the original value
        return base_coeff

    hero.get_coeff = enhanced_get_coeff

    # 2. Monkey-patch LowerSkill to reset stacks by updating the last reset time
    if not hasattr(hero, 'original_LowerSkill_dls'):
        hero.original_LowerSkill_dls = hero.LowerSkill

    def enhanced_LowerSkill(t):
        hero.artifact_counters['dragonlightsword_last_reset_time'] = t
        hero.original_LowerSkill_dls(t)

    hero.LowerSkill = enhanced_LowerSkill

def init_dragonlightsword(hero: 'Hero', artifact: 'Artifact'):
    """Initialization effect for DragonLightSword. Called at the start of each simulation."""
    hero.artifact_counters['dragonlightsword_last_reset_time'] = 0


class DragonLightSword(Artifact):
    def __init__(self):
        super().__init__(
            name="DragonLightSword",
            stat_bonuses={
                StatType.AttackSpeed: 8.74,
                StatType.CriticalMult: 17.48
            },
            setup_effect_fn=setup_dragonlightsword,
            init_effect_fn=init_dragonlightsword,
            stackable=False
        ) 