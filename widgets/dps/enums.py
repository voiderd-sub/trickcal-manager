from enum import Enum, auto

VERY_BIG_NUMBER = 1e10
MS_IN_SEC = 1000
DELTA_T = 0.1
SP_INTERVAL = 1 * MS_IN_SEC

class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class AttackType(StrEnum):
    Physic = auto()
    Magic = auto()

class ActionType(StrEnum):
    AutoAttackBasic = auto()
    AutoAttackEnhanced = auto()
    LowerSkill = auto()
    UpperSkill = auto()
    Wait = auto()

class BuffType(StrEnum):
    TriggerEnhanced = auto()
    AttackSpeedAdd = auto()

class TargetHero(StrEnum):
    Self = auto()
    All = auto()
    AllWOSelf = auto()
    FrontLine = auto()
    MiddleLine = auto()
    BackLine = auto()

class EffectType(StrEnum):
    INSTANT = auto()
    PROJECTILE = auto()
    DEBUFF = auto()
    BUFF = auto()

class BuffType(StrEnum):
    ATTACK_SPEED_ADD = auto()
    DAMAGE_INCREASE = auto()

class DebuffType(StrEnum):
    Sting = auto()          # 쓰라림 : 틱당 10%; 치감 50% (구현 X)
    Burn = auto()           # 화상 : 틱당 30%
    Frostbite = auto()      # 동상 : 틱당 10%; 받피증 효과는 버프로 처리
    Poisoning = auto()      # 중독 : 틱당 7.5%; 공깎 30% (구현 X)