from dps.enums import *
from dps.status import StatusReservation
from typing import TYPE_CHECKING
import math

if TYPE_CHECKING:
    from dps.hero import Hero


# Base action class with time information
class Action:
    def __init__(self,
                 hero: 'Hero',
                 action_type: ActionType,
                 source_movement: MovementType,
                 damage_type: DamageType,
                 post_fns_on_launch=None):
        self.hero = hero
        self.source_movement = source_movement
        self.damage_type = damage_type if damage_type else MovementType.movement_type_to_dmg_type(source_movement)
        self.action_type = action_type  # Instant, Projectile, Status
        self.post_fns_on_launch = post_fns_on_launch if post_fns_on_launch else []
        
        self.execution_time = 0
        self.delay = 0

    def action_fn(self, current_time):
        """Execute the action"""
        raise NotImplementedError

    def __lt__(self, other):
        return self.execution_time < other.execution_time


def apply_instant_damage(hero, damage_type, time, damage_coeff, movement_type=None):
    movement_type = movement_type if movement_type else damage_type.name
    damage_records = hero.damage_records[movement_type]
    damage = hero.get_damage(damage_coeff, damage_type)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((round(time)/SEC_TO_MS, last_cumulative_damage + damage))


class InstantAction(Action):
    def __init__(self, hero, damage_coeff, source_movement, damage_type, post_fns_on_launch=None):
        super().__init__(hero, ActionType.Instant, source_movement, damage_type, post_fns_on_launch)
        self.damage_coeff = damage_coeff

    def action_fn(self, current_time):
        apply_instant_damage(hero=self.hero,
                             damage_type=self.damage_type,
                             time=current_time,
                             damage_coeff=self.damage_coeff,
                             movement_type=self.source_movement)
        
        for post_fn in self.post_fns_on_launch:
            post_fn(self)


class ProjectileAction(Action):
    def __init__(self, hero, damage_coeff, hit_delay, source_movement, damage_type, post_fns_on_impact=None, post_fns_on_launch=None):
        super().__init__(hero, ActionType.Projectile, source_movement, damage_type, post_fns_on_launch)
        self.damage_coeff = damage_coeff
        self.hit_delay = hit_delay
        self.instant_action = InstantAction(hero, damage_coeff, source_movement, damage_type, post_fns_on_impact)

    def action_fn(self, current_time):
        self.hero.party.action_manager.add_pending_effect(current_time, self.instant_action, self.hit_delay)
        for post_fn in self.post_fns_on_launch:
            post_fn(self)


class StatusAction(Action):
    def __init__(self,
                 hero: 'Hero',
                 source_movement: MovementType,
                 damage_type: DamageType,
                 status_template,
                 post_fns_on_launch=None):
        super().__init__(hero, ActionType.Status, source_movement, damage_type, post_fns_on_launch)
        self.status_template = status_template

    def action_fn(self, current_time):
        """
        Resolves the target dynamically and creates a status object and its reservation just-in-time.
        """

        reservation = StatusReservation(template=self.status_template, start_time=current_time)
        if reservation.get_targets():
            self.hero.party.status_manager.add_status_reserv(reservation)

        for post_fn in self.post_fns_on_launch:
            post_fn(self)
