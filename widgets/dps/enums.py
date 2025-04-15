from enum import Enum, auto, IntFlag

VERY_BIG_NUMBER = 1e10
SEC_TO_MS = 1000
DELTA_T = 0.1
SP_INTERVAL = 1 * SEC_TO_MS

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

    @classmethod
    def act_type_to_dmg_type(cls, action_type):
        return getattr(DamageType, action_type.name)

class TargetHero(StrEnum):
    Self = auto()
    All = auto()
    AllWOSelf = auto()
    FrontLine = auto()
    MiddleLine = auto()
    BackLine = auto()

class EffectType(StrEnum):
    Instant = auto()
    Delayed = auto()
    Debuff = auto()
    Buff = auto()

# class for damage amplifier
class DamageType(IntFlag):
    NONE                = 0
    LowerSkill          = auto()
    UpperSkill          = auto()
    AutoAttackBasic     = auto()
    AutoAttackEnhanced  = auto()
    Debuff              = auto()
    Artifact            = auto()

    Skill      = LowerSkill | UpperSkill
    AutoAttack = AutoAttackBasic | AutoAttackEnhanced
    ALL        = Skill | AutoAttack | Debuff | Artifact

    @classmethod
    def get_leaf_members(cls, damage_type):
        return {dt for dt in cls.leaf_types() if (damage_type & dt) == dt}
    
    @classmethod
    def leaf_types(cls):
        return {
            cls.LowerSkill, cls.UpperSkill,
            cls.AutoAttackBasic, cls.AutoAttackEnhanced,
            cls.Debuff, cls.Artifact
        }

class Personality(StrEnum):
    Naive = auto()
    Mad = auto()
    Cool = auto()
    Jolly = auto()
    Gloomy = auto()

DMG_TYPE_LABELS_KR = {
    "AutoAttackBasic": "평타",
    "AutoAttackEnhanced": "강평",
    "LowerSkill": "저학년",
    "UpperSkill": "고학년",
    "Artifact": "아티팩트",
    "Debuff": "디버프",
}
