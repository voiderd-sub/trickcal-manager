from dps.artifact import Artifact
from dps.enums import StatType, SEC_TO_MS
from typing import TYPE_CHECKING
import math

if TYPE_CHECKING:
    from dps.hero import Hero
    from dps.party import Party

class DragonLightSword(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="용광검", level=level)
        self.setup_effect_fn = self.setup_dragonlightsword
        self.init_effect_fn = self.init_dragonlightsword

    def setup_dragonlightsword(self, hero: 'Hero'):
        """Setup effect for DragonLightSword. This is called once per run."""
        if not hasattr(hero, 'original_get_coeff_dls'):
            hero.original_get_coeff_dls = hero.get_coeff
        
        def enhanced_get_coeff(stat_type: StatType):
            base_coeff = hero.original_get_coeff_dls(stat_type)
            
            if stat_type == StatType.AttackSpeed and self.effects:
                last_reset_time = hero.artifact_counters.get('dragonlightsword_last_reset_time', 0)
                current_time = hero.party.current_time
                
                stacks = math.floor(current_time / SEC_TO_MS) - math.floor(last_reset_time / SEC_TO_MS)
                dls_as_bonus = stacks * (self.effects[0] / 100)
                
                return base_coeff + dls_as_bonus
            
            return base_coeff

        hero.get_coeff = enhanced_get_coeff

        if not hasattr(hero, 'original_LowerSkill_dls'):
            hero.original_LowerSkill_dls = hero.LowerSkill

        def enhanced_LowerSkill(t):
            hero.artifact_counters['dragonlightsword_last_reset_time'] = t
            hero.original_LowerSkill_dls(t)

        hero.LowerSkill = enhanced_LowerSkill

    def init_dragonlightsword(self, hero: 'Hero'):
        """Initialization effect for DragonLightSword. Called at the start of each simulation."""
        hero.artifact_counters['dragonlightsword_last_reset_time'] = 0 