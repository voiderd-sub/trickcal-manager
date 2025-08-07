from dps.artifact import Artifact
from dps.status import BuffStatCoeff, BuffAmplify, target_self, StatusReservation
from dps.enums import DamageType, StatType, SEC_TO_MS

class RustyRedSword(Artifact):
    def __init__(self, level: int = 1, always_active: bool = False):
        super().__init__(name="녹슨 붉은 검", level=level)
        self.always_active = always_active

        if self.always_active:
            # Create buff templates once and store them as instance attributes.
            # This makes them unique to this specific artifact instance.
            self.aspd_buff = BuffStatCoeff(
                status_id=f"rusty_red_sword_aspd_buff_{id(self)}",
                caster=None,  # Caster will be set when the effect is applied
                target_resolver_fn=target_self,
                duration=6,
                stat_bonuses={StatType.AttackSpeed: self.effects[0]}
            )
            
            self.amp_buff = BuffAmplify(
                status_id=f"rusty_red_sword_amp_buff_{id(self)}",
                caster=None,
                target_resolver_fn=target_self,
                duration=6,
                applying_dmg_type=DamageType.ALL,
                value=self.effects[1]
            )
            
            # Store original delete functions before patching
            self._original_aspd_delete = self.aspd_buff.delete_fn
            self._original_amp_delete = self.amp_buff.delete_fn
            
            # Monkey-patch the delete functions to re-apply the buff after a delay
            self.aspd_buff.delete_fn = self._patched_aspd_delete
            self.amp_buff.delete_fn = self._patched_amp_delete



    def apply_init_effect(self, hero):
        """Kicks off the periodic buff cycle for the hero."""
        # Set the actual caster on the template before the first application
        self.aspd_buff.caster = hero
        self.amp_buff.caster = hero

        # Start the buff cycle
        current_time = hero.party.current_time
        aspd_reservation = StatusReservation(template=self.aspd_buff, start_time=current_time)
        amp_reservation = StatusReservation(template=self.amp_buff, start_time=current_time)
        hero.party.status_manager.add_status_reserv(aspd_reservation)
        hero.party.status_manager.add_status_reserv(amp_reservation)

    def _patched_aspd_delete(self, reservation, target_id, current_time):
        # 1. Apply the original effect removal logic
        self._original_aspd_delete(reservation, target_id, current_time)
        aspd_reservation = StatusReservation(template=self.aspd_buff, start_time=current_time + 2 * SEC_TO_MS)
        # 2. Re-schedule the buff to apply again after the 2s cooldown
        target = self.aspd_buff.get_target_with_id(target_id)
        target.party.status_manager.add_status_reserv(aspd_reservation)

    def _patched_amp_delete(self, reservation, target_id, current_time):
        # 1. Apply the original effect removal logic
        self._original_amp_delete(reservation, target_id, current_time)
        amp_reservation = StatusReservation(template=self.amp_buff, start_time=current_time + 2 * SEC_TO_MS)
        # 2. Re-schedule the buff to apply again after the 2s cooldown
        target = self.amp_buff.get_target_with_id(target_id)
        target.party.status_manager.add_status_reserv(amp_reservation) 