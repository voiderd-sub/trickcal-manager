from dps.artifact import Artifact
from dps.enums import SEC_TO_MS

class PendantOfHealing(Artifact):
    def __init__(self, level: int = 1):
        super().__init__(name="치유의 펜던트", level=level)
        # For now, do nothing. (Health recovery mechanisms not implemented)
        self.cooldown = 5 * SEC_TO_MS

    def apply_setup_effect(self, hero):
        """
        Setup effect for Pendant of Healing:
        - Modifies the hero's aa_post_fn to add a life steal effect with a cooldown.
        This is called once per run.
        """
        return
        if not hasattr(hero, 'original_aa_post_fn_poh'):
            hero.original_aa_post_fn_poh = hero.aa_post_fn
        
        def new_aa_post_fn():
            hero.original_aa_post_fn_poh()
            
            current_time = hero.party.action_manager.current_time
            last_proc_time = hero.artifact_counters.get('pendant_of_healing_last_proc', -self.cooldown)
            
            if current_time >= last_proc_time + self.cooldown:
                hero.artifact_counters['pendant_of_healing_last_proc'] = current_time
                
                # Placeholder for the healing effect.
                # The actual healing logic would need access to the damage dealt by the auto-attack.
                # effect_value = self.effects[0]
                # heal_amount = damage_dealt * (effect_value / 100)
                # hero.heal(heal_amount)
                pass

        hero.aa_post_fn = new_aa_post_fn

    def apply_init_effect(self, hero):
        """
        Initialization effect for Pendant of Healing:
        - Resets the last proc time for the life steal effect.
        This is called at the beginning of each simulation.
        """
        hero.artifact_counters['pendant_of_healing_last_proc'] = -self.cooldown 