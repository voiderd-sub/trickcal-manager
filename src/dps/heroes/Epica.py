from dps.action import *
from dps.hero import Hero, ProbabilisticCondition, BuffCondition, OrCondition
from dps.status import BuffAttackSpeed, BuffAmplify


class Epica(Hero):
    lowerskill_value = [(60 + 3 * level, 8 + 0.5 * level) for level in range(13)]
    upperskill_value = [72 + 6 * level for level in range(13)]

    def __init__(self, user_provided_info):
        super().__init__(user_provided_info)

        self.hero_id = 17
        self.name = "Epica"
        self.name_kr = "에피카"

        self.attack_type = AttackType.Physic
        self.personality = Personality.Jolly
        self.attack_speed = 102
        self.init_sp = 100
        self.max_sp = 450
        self.sp_recovery_rate = 20
        self.sp_per_aa = 0
        self.upper_skill_cd = 54

        self.motion_time = {
            MovementType.AutoAttackBasic: 1.690,
            MovementType.AutoAttackEnhanced: 1.667,
            MovementType.LowerSkill: 2.900,
            MovementType.UpperSkill: 10.00,
        }

    def setup_eac(self):
        prob = 0.25 + (0.15 if self.aside_level >= 2 else 0)
        prob_cond = ProbabilisticCondition(self, prob)
        buff_cond = BuffCondition(self, f"{self.get_unique_name()}_저학년")
        return OrCondition(self, prob_cond, buff_cond)

    def BasicAttack(self, t):
        motion_time = self.get_motion_time(MovementType.AutoAttackBasic)
        hit_delay = 0.5

        actions_info = [(0.65, 100)]
        if self.aside_level >= 2:
            actions_info.append((0.71, 100))

        action_tuples = []
        for t_ratio, damage_coeff in actions_info:
            action = ProjectileAction(
                hero=self,
                damage_coeff=damage_coeff,
                hit_delay=hit_delay,
                source_movement=MovementType.AutoAttackBasic,
                damage_type=DamageType.AutoAttackBasic,
            )
            action_tuples.append((action, t + motion_time * t_ratio))
        
        self.reserv_action_chain(action_tuples)
        return motion_time

    def EnhancedAttack(self, t):
        motion_time = self.get_motion_time(MovementType.AutoAttackEnhanced)
        hit_delay = 1.05

        actions_info = [(0.95, 200)]
        if self.aside_level >= 2:
            actions_info.append((0.71, 200))

        action_tuples = []
        for t_ratio, damage_coeff in actions_info:
            action = ProjectileAction(
                hero=self,
                damage_coeff=damage_coeff,
                hit_delay=hit_delay,
                source_movement=MovementType.AutoAttackEnhanced,
                damage_type=DamageType.AutoAttackEnhanced,
            )
            action_tuples.append((action, t + motion_time * t_ratio))
            
        self.reserv_action_chain(action_tuples)
        return motion_time

    def LowerSkill(self, t):
        motion_time = self.get_motion_time(MovementType.LowerSkill)
        buff_time = t + motion_time * 0.55
        duration = 10.0
        self_as_buff_val, other_as_buff_val = self.lowerskill_value[self.lowerskill_level - 1]

        # Self buff
        self_buff = BuffAttackSpeed(
            status_id=f"{self.get_unique_name()}_저학년",
            caster=self,
            target=self.party.get_target_indices(TargetHero.Self, self.party_idx),
            duration=duration,
            value=self_as_buff_val,
        )
        
        # Other party members buff
        other_buff = BuffAttackSpeed(
            status_id=f"{self.get_unique_name()}_저학년_other",
            caster=self,
            target=self.party.get_target_indices(TargetHero.AllWOSelf, self.party_idx),
            duration=duration,
            value=other_as_buff_val,
        )

        action_tuples = [
            (StatusAction(hero=self,
                          status=self_buff,
                          source_movement=MovementType.LowerSkill,
                          damage_type=DamageType.NONE),
                          buff_time),
            (StatusAction(hero=self,
                          status=other_buff,
                          source_movement=MovementType.LowerSkill,
                          damage_type=DamageType.NONE),
                          buff_time)
        ]
        
        self.reserv_action_chain(action_tuples)
        return motion_time

    def UpperSkill(self, t):
        motion_time = self.get_motion_time(MovementType.UpperSkill)
        action_tuples = []

        # Buff Action
        buff_time = t + motion_time * 0.09
        duration = 8.0
        buff_all = BuffAmplify(
            status_id=f"{self.get_unique_name()}_고학년",
            caster=self,
            target=self.party.get_target_indices(TargetHero.All, self.party_idx),
            duration=duration,
            value=27,
            applying_dmg_type=DamageType.ALL,
        )
        action_tuples.append(
            (StatusAction(hero=self,
                          status=buff_all,
                          source_movement=MovementType.UpperSkill,
                          damage_type=DamageType.NONE),
                          buff_time)
        )

        # Damage Actions
        damage = self.upperskill_value[self.upperskill_level - 1]
        hit_delay = 0.35

        for j in range(3):
            for i in range(8):
                t_ratio = 0.28 + 0.013 * i + 0.12 * j
                action = ProjectileAction(
                    hero=self,
                    damage_coeff=damage,
                    hit_delay=hit_delay,
                    source_movement=MovementType.UpperSkill,
                    damage_type=DamageType.AutoAttackBasic,
                )
                action_tuples.append((action, t + motion_time * t_ratio))
        self.reserv_action_chain(action_tuples)
        return motion_time
