# Artifacts package
from .weather_is_clear_card import WeatherIsClearCard
from .belitas_staff import BelitasStaff
from .syllas_windforce import SyllasWindforce
from .dayas_diamond_cutter import DayasDiamondCutter
from .rims_scythe import RimsScythe
from .dragonlightsword import DragonLightSword
from .fricles_queen_regents_seal import FriclesQueenRegentsSeal
from .kettlebell_30kg import Kettlebell30kg
from .leets_earth_smasher import LeetsEarthSmasher
from .sharp_staff import SharpStaff
from .jade_magic_book import JadeMagicBook
from .pendant_of_healing import PendantOfHealing
from .rusty_red_sword import RustyRedSword
from .toy_telescope import ToyTelescope

# A dictionary to easily access artifact classes by their name.
# The keys should match the artifact names defined in artifact_data.py.
ARTIFACT_CLASS_MAP = {
    "벨리타의 지팡이": BelitasStaff,
    "다야의 다이아몬드 커터": DayasDiamondCutter,
    "용광검": DragonLightSword,
    "프리클의 여왕 대리 인장": FriclesQueenRegentsSeal,
    "30KG 케틀벨": Kettlebell30kg,
    "림의 낫": RimsScythe,
    "실라의 바람살": SyllasWindforce,
    "날씨는 맑음 카드": WeatherIsClearCard,
    "리츠의 대지 뽀개기": LeetsEarthSmasher,
    "날카로운 지팡이": SharpStaff,
    "옥빛 마법서": JadeMagicBook,
    "치유의 펜던트": PendantOfHealing,
    "녹슨 붉은 검": RustyRedSword,
    "장난감 망원경": ToyTelescope,
}

__all__ = [
    "WeatherIsClearCard",
    "BelitasStaff",
    "SyllasWindforce",
    "DayasDiamondCutter",
    "RimsScythe",
    "DragonLightSword",
    "FriclesQueenRegentsSeal",
    "Kettlebell30kg",
    "LeetsEarthSmasher",
    "SharpStaff",
    "JadeMagicBook",
    "PendantOfHealing",
    "RustyRedSword",
    "ToyTelescope",
    "ARTIFACT_CLASS_MAP"
] 