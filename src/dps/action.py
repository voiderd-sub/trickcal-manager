from dps.enums import *
import random
from dps.status import StatusReservation

# Base action class with time information
class Action:
    def __init__(self,
                 hero,   # Hero
                 action_type: ActionType,
                 source_movement: MovementType,
                 damage_type: DamageType,
                 post_fn=None):  # 추가: post_fn 인자
        self.hero = hero
        self.source_movement = source_movement
        self.damage_type = damage_type if damage_type else MovementType.movement_type_to_dmg_type(source_movement)
        self.action_type = action_type  # Instant, Projectile, Status
        self.post_fn = post_fn  # 추가: post_fn 저장
        
        # Time information (set by schedule_action_template)
        self.execution_time = 0
        self.delay = 0

    def action_fn(self, current_time):
        """Execute the action"""
        raise NotImplementedError

    def __lt__(self, other):
        return self.execution_time < other.execution_time


def apply_instant_damage(hero, damage_type, time, damage_coeff, movement_type=None):
    time = int(time)
    movement_type = movement_type if movement_type else damage_type.name
    damage_records = hero.damage_records[movement_type]
    damage = hero.get_damage(damage_coeff, damage_type)
    last_cumulative_damage = damage_records[-1][-1] if len(damage_records) >=1 else 0
    damage_records.append((int(time // SEC_TO_MS), last_cumulative_damage + damage))


class InstantAction(Action):
    def __init__(self, hero, damage_coeff, source_movement, damage_type, post_fn=None):
        super().__init__(hero, ActionType.Instant, source_movement, damage_type, post_fn)
        self.damage_coeff = damage_coeff

    def action_fn(self, current_time):
        apply_instant_damage(hero=self.hero,
                             damage_type=self.damage_type,
                             time=current_time,
                             damage_coeff=self.damage_coeff,
                             movement_type=self.source_movement)
        self._handle_post_action_effects()
        
        # post_fn 실행 (추가)
        if self.post_fn:
            self.post_fn()

    def _handle_post_action_effects(self):
        """Handle post-action effects like SP recovery"""
        if self.source_movement in [MovementType.AutoAttackBasic, MovementType.AutoAttackEnhanced]:
            self.hero.aa_post_fn()


class ProjectileAction(Action):
    def __init__(self, hero, damage_coeff, hit_delay, source_movement, damage_type, post_fn=None):
        super().__init__(hero, ActionType.Projectile, source_movement, damage_type, post_fn)
        self.damage_coeff = damage_coeff
        self.hit_delay = hit_delay
        self.instant_action = InstantAction(hero, damage_coeff, source_movement, damage_type)

    def action_fn(self, current_time):
        effect_time = current_time + int(self.hit_delay)
        self.hero.party.action_manager.add_pending_effect(effect_time, self.instant_action, 0)
        
        # post_fn 실행 (추가)
        if self.post_fn:
            self.post_fn()


class StatusAction(Action):
    def __init__(self, hero, status, source_movement, damage_type, post_fn=None):
        super().__init__(hero, ActionType.Status, source_movement, damage_type, post_fn)
        self.status = status  # StatusTemplate

    def action_fn(self, current_time):
        # StatusReservation을 생성해서 넘긴다
        start_time = current_time
        duration = getattr(self.status, 'duration', 0)
        end_time = start_time + int(duration * SEC_TO_MS)
        reservation = StatusReservation(self.status, start_time, end_time)
        self.hero.party.status_manager.add_status_reserv(reservation)
        
        # post_fn 실행 (추가)
        if self.post_fn:
            self.post_fn()