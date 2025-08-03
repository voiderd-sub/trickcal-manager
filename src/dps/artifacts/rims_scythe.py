from dps.artifact import Artifact
from dps.enums import StatType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.hero import Hero

class RimsScythe(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="림의 낫", level=level)

    def apply_setup_effect(self, hero: 'Hero'):
        """
        Setup effect for Rim's Scythe:
        - Adds an execution effect to the hero's basic attack post-function subscribers.
        This is called once per run.
        """
        def execution_effect():
            # --- Placeholder for Execution Logic ---
            # TODO: Implement the execution logic.
            # This requires access to the enemy object targeted by the auto-attack.
            # 1. Get the target of the last auto-attack.
            # 2. Check if the target is a 'normal monster'.
            # 3. Check if target.current_hp / target.max_hp <= 0.18.
            # 4. If all conditions are met, set target.current_hp = 0 or apply fatal damage.
            pass

        hero.aa_post_fns.append(execution_effect) 