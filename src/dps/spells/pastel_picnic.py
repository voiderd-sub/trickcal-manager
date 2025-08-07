from dps.spell import Spell
from dps.enums import DamageType, Class

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.party import Party


class PastelPicnic(Spell):
    def __init__(self, level: int = 1):
        super().__init__("파스텔빛 소풍", level)
    
    def apply_init_effect(self, party: 'Party'):
        eldain_count = 0
        for idx in party.active_indices:
            hero = party.character_list[idx]
            if hero.is_eldain:
                eldain_count += 1
        
        if eldain_count >= 3:
            for idx in party.active_indices:
                hero = party.character_list[idx]
                hero.add_sp_recovery_percent_bonus(20)
        
        # TODO: 꽃잎 바람과 간식 효과 구현
        # 꽃잎 바람: 12초마다 (첫 쿨타임 6초)
        # - 피해량: (가장 높은 아군 공격력 × effects[0]% × 0.8)
        # - 엘다인 1명당 90% 추가 피해
        # - 피해량 증가 적용 안됨
        
        # 간식: 15초마다 (첫 쿨타임 12초)
        # - 8초 동안 모든 아군 HP 2초마다 2% 회복
        # - 엘다인 1명당 회복량 1% 추가
        # - HP 회복 시스템 미구현으로 스킵
