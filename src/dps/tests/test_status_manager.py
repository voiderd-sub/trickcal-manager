import pytest
import numpy as np
from dps.party import Party
from dps.hero import Hero
from dps.status import StatusTemplate, StatusReservation, target_self
from dps.enums import StatType, SEC_TO_MS, MovementType, AttackType
from dps.stat_utils import apply_stat_bonuses

# 테스트용으로 사용할 간단한 상태(버프) 템플릿입니다.
class SimpleStatus(StatusTemplate):
    def __init__(self, caster, duration, max_stack, status_id="test_status"):
        super().__init__(
            status_id=status_id,
            caster=caster,
            target_resolver_fn=target_self,
            max_stack=max_stack,
        )
        self.duration = duration
        self.status_type = "buff"

    def apply_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {StatType.AttackSpeed: 0.1})

    def delete_fn(self, reservation, target_id, current_time):
        target = self.get_target_with_id(target_id)
        apply_stat_bonuses(target, {StatType.AttackSpeed: -0.1})

    def refresh_fn(self, reservation, target_id, current_time):
        pass

# 테스트용으로 사용할 간단한 영웅 클래스입니다.
class SimpleHero(Hero):
    def __init__(self, user_provided_info={}):
        super().__init__(user_provided_info)
        self.attack_type = AttackType.Physic
        self.motion_time = {
            MovementType.AutoAttackBasic: 1.0,
            MovementType.LowerSkill: 1.0,
            MovementType.UpperSkill: 1.0,
        }
        self.lowerskill_level = 0
        self.upperskill_level = 0
        self.init_sp = 0
        self.max_sp = 100
        self.sp_per_aa = 0
        self.sp_recovery_rate = 1
        self.attack_speed = 1.0
        self.upper_skill_cd = 30.0


@pytest.fixture
def party_with_hero():
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    party.init_run()
    party.init_simulation()
    return party, hero

def test_max_stack_zero_extends_duration(party_with_hero):
    """
    max_stack = 0일 때, 버프가 연장되고 최종적으로 제거되는지 테스트합니다.
    """
    party, hero = party_with_hero
    status_manager = party.status_manager
    duration_sec = 10
    duration_ms = duration_sec * SEC_TO_MS

    # t=0에 버프 적용
    status_template = SimpleStatus(hero, duration=duration_sec, max_stack=0, status_id="extend_buff")
    status_reserv = StatusReservation(status_template, 0)
    status_manager.add_status_reserv(status_reserv)
    
    party.current_time = 0
    status_manager.resolve_status_reserv(party.current_time)

    # 버프가 1개 적용되었고, 종료 시간은 duration_ms와 같아야 합니다.
    assert status_manager.get_buff_count(hero.party_idx, "extend_buff") == 1
    statuses = status_manager.get_statuses_by_id("extend_buff")
    assert len(statuses) == 1
    original_end_time = statuses[0].end_time
    assert original_end_time == duration_ms

    # t=5000에 버프 다시 적용 (연장)
    party.current_time = 5000
    status_reserv_2 = StatusReservation(status_template, party.current_time)
    status_manager.add_status_reserv(status_reserv_2)
    status_manager.resolve_status_reserv(party.current_time)

    # 버프 스택은 여전히 1개여야 합니다.
    assert status_manager.get_buff_count(hero.party_idx, "extend_buff") == 1
    statuses = status_manager.get_statuses_by_id("extend_buff")
    assert len(statuses) == 1
    
    new_duration = status_reserv_2.end_time - status_reserv_2.start_time
    expected_new_end_time = original_end_time + new_duration
    final_end_time = statuses[0].end_time
    assert final_end_time == expected_new_end_time

    # 시간이 지나 버프가 제거되는지 확인
    party.current_time = final_end_time + 1
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "extend_buff") == 0
    assert len(status_manager.get_statuses_by_id("extend_buff")) == 0

def test_max_stack_inf_is_individual(party_with_hero):
    """
    max_stack = inf일 때, 버프가 독립적으로 쌓이고 순서대로 제거되는지 테스트합니다.
    """
    party, hero = party_with_hero
    status_manager = party.status_manager
    duration_sec = 10

    status_template = SimpleStatus(hero, duration=duration_sec, max_stack=np.inf, status_id="individual_buff")

    # t=0에 버프 적용
    status_reserv_1 = StatusReservation(status_template, 0)
    status_manager.add_status_reserv(status_reserv_1)
    party.current_time = 0
    status_manager.resolve_status_reserv(party.current_time)
    end_time_1 = status_reserv_1.end_time
    assert status_manager.get_buff_count(hero.party_idx, "individual_buff") == 1

    # t=1000에 버프 재적용
    party.current_time = 1000
    status_reserv_2 = StatusReservation(status_template, party.current_time)
    status_manager.add_status_reserv(status_reserv_2)
    status_manager.resolve_status_reserv(party.current_time)
    end_time_2 = status_reserv_2.end_time
    
    # 버프 스택이 2로 증가해야 합니다.
    assert status_manager.get_buff_count(hero.party_idx, "individual_buff") == 2
    assert len(status_manager.get_statuses_by_id("individual_buff")) == 2
    
    # 첫 번째 버프가 제거되는지 확인
    party.current_time = end_time_1 + 1
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "individual_buff") == 1
    assert len(status_manager.get_statuses_by_id("individual_buff")) == 1

    # 두 번째 버프가 제거되는지 확인
    party.current_time = end_time_2 + 1
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "individual_buff") == 0
    assert len(status_manager.get_statuses_by_id("individual_buff")) == 0

def test_max_stack_N_is_overlap(party_with_hero):
    """
    max_stack = N일 때, 스택 초과 시 오래된 버프가 제거되고 남은 버프들이 순서대로 제거되는지 테스트합니다.
    """
    party, hero = party_with_hero
    status_manager = party.status_manager
    duration_sec = 10
    max_stack = 2

    status_template = SimpleStatus(hero, duration=duration_sec, max_stack=max_stack, status_id="overlap_buff")

    # 1. 첫 번째 버프 적용 (t=0)
    party.current_time = 0
    status_manager.add_status_reserv(StatusReservation(status_template, party.current_time))
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "overlap_buff") == 1

    # 2. 두 번째 버프 적용 (t=1000)
    party.current_time = 1000
    status_manager.add_status_reserv(StatusReservation(status_template, party.current_time))
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "overlap_buff") == 2
    
    # 3. 세 번째 버프 적용 (t=2000), max_stack 초과
    party.current_time = 2000
    status_manager.add_status_reserv(StatusReservation(status_template, party.current_time))
    status_manager.resolve_status_reserv(party.current_time)
    
    # 가장 오래된 버프(t=0)가 제거되고 새로운 버프(t=2000)가 추가되었는지 확인
    assert status_manager.get_buff_count(hero.party_idx, "overlap_buff") == 2
    statuses = status_manager.get_statuses_by_id("overlap_buff")
    assert len(statuses) == 2
    start_times = sorted([s.start_time for s in statuses])
    assert start_times == [1000, 2000]

    end_time_1 = 1000 + duration_sec * SEC_TO_MS  # t=1000에 시작한 버프의 종료 시간
    end_time_2 = 2000 + duration_sec * SEC_TO_MS  # t=2000에 시작한 버프의 종료 시간

    # t=1000에 적용된 버프가 제거되는지 확인
    party.current_time = end_time_1 + 1
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "overlap_buff") == 1
    assert len(status_manager.get_statuses_by_id("overlap_buff")) == 1

    # t=2000에 적용된 버프가 제거되는지 확인
    party.current_time = end_time_2 + 1
    status_manager.resolve_status_reserv(party.current_time)
    assert status_manager.get_buff_count(hero.party_idx, "overlap_buff") == 0
    assert len(status_manager.get_statuses_by_id("overlap_buff")) == 0
