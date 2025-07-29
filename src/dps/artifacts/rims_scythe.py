from dps.artifact import Artifact
from dps.enums import StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero

def setup_rims_scythe(hero: 'Hero'):
    """
    Setup effect for Rim's Scythe:
    - Modifies the hero's aa_post_fn to add an execution effect.
    This is called once per run.
    """
    if not hasattr(hero, 'original_aa_post_fn_rs'):
        hero.original_aa_post_fn_rs = hero.aa_post_fn
    
    def enhanced_aa_post_fn():
        # Call original function first
        hero.original_aa_post_fn_rs()
        
        # --- Placeholder for Execution Logic ---
        # TODO: Implement the execution logic.
        # This requires access to the enemy object targeted by the auto-attack.
        # 1. Get the target of the last auto-attack.
        # 2. Check if the target is a 'normal monster'.
        # 3. Check if target.current_hp / target.max_hp <= 0.18.
        # 4. If all conditions are met, set target.current_hp = 0 or apply fatal damage.
        pass

    hero.aa_post_fn = enhanced_aa_post_fn

class RimsScythe(Artifact):
    def __init__(self):
        super().__init__(
            name="림의 낫",
            stat_bonuses={
                StatType.AttackPhysic: 22.47,
                StatType.CriticalRate: 27.66
            },
            setup_effect_fn=setup_rims_scythe,
            init_effect_fn=None,
            stackable=False # Execution effect logic does not stack.
        ) 