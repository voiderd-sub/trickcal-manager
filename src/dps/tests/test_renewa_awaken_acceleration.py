import pytest
import numpy as np
from functools import partial

from dps.action import InstantAction
from dps.party import Party
from dps.hero import Hero
from dps.heroes.RenewaAwaken import RenewaAwaken
from dps.tests.simple_hero import SimpleHero
from dps.enums import *


@pytest.fixture
def aoe_test_environment(monkeypatch):
    """
    가속 및 어사이드 스킬 테스트를 위한 통합 환경을 설정하는 Pytest fixture.
    'aoe'는 'Acceleration and Aside Effect'의 약자입니다.
    """
    party = Party()

    # 리뉴아 설정
    renewa_info = {
        "name": "RenewaAwaken", "name_kr": "리뉴아(각성)", "attack": 100,
        "lowerskill_level": 1, "upperskill_level": 1, "aside_level": 2, # 기본적으로 L2
        "upper_skill_cd": 20, "attack_type": AttackType.Physic,
        "attack_speed": 100, "init_sp": 0, "sp_recovery_rate": 10,
        "sp_per_aa": 10,
    }
    renewa = RenewaAwaken(renewa_info)
    party.add_hero(renewa, 0)

    # 테스트별 영웅 설정
    aa_only_hero = SimpleHero("AA_Hero")
    aa_only_hero.max_sp = 10000
    party.add_hero(aa_only_hero, 1)

    skill_only_hero = SimpleHero("Skill_Hero")
    skill_only_hero.init_sp = 100
    skill_only_hero.max_sp = 100
    skill_only_hero.sp_recovery_rate = 1000
    skill_only_hero.attack_speed = 10
    party.add_hero(skill_only_hero, 2)

    # --- 로깅 및 패치 설정 ---
    logs = {
        "acceleration": [],
        "motion": [],
        "missile": []
    }

    # 1. 가속 로깅
    original_get_accel = party.get_current_acceleration_factor
    def patched_get_accel(t):
        accel = original_get_accel(t)
        if hasattr(party, 'current_time'):
            current_time_sec = party.current_time / SEC_TO_MS
            if not logs["acceleration"] or logs["acceleration"][-1][1] != accel:
                logs["acceleration"].append((current_time_sec, accel))
        return accel
    monkeypatch.setattr(party, 'get_current_acceleration_factor', patched_get_accel)

    # 2. 모션 로깅
    original_do_movement = Hero.do_movement
    def patched_do_movement(hero_self, movement_type, t):
        motion_time = original_do_movement(hero_self, movement_type, t)
        if hero_self.party.current_time is not None:
            current_time_sec = hero_self.party.current_time / SEC_TO_MS
            logs["motion"].append((current_time_sec, hero_self.name, movement_type, motion_time / SEC_TO_MS))
        return motion_time
    monkeypatch.setattr(Hero, 'do_movement', patched_do_movement)

    # 3. 미사일 로깅
    original_add_action = party.action_manager.add_action_reserv
    def patched_add_action(time, action):
        if action.damage_type == DamageType.AsideSkill:
            logs["missile"].append(time / SEC_TO_MS)
        original_add_action(time, action)
    monkeypatch.setattr(party.action_manager, 'add_action_reserv', patched_add_action)

    # 4. 어사이드 스킬 쿨감 비활성화
    original_aside_effect = renewa._aside_skill_effect
    def patched_aside_effect(fire_time_ms, _=None):
        hit_delay_sec = 0.5
        hit_time = fire_time_ms + (hit_delay_sec * SEC_TO_MS)
        damage_action = InstantAction(
            hero=renewa, damage_coeff=400,
            source_movement=MovementType.AsideSkill,
            damage_type=DamageType.AsideSkill
        )
        renewa.reserv_action(damage_action, hit_time)
        renewa._schedule_next_aside_missile(fire_time_ms)
    monkeypatch.setattr(renewa, '_aside_skill_effect', patched_aside_effect)
    renewa.original_aside_skill_effect = original_aside_effect

    yield party, renewa, aa_only_hero, skill_only_hero, logs


def test_acceleration_effects_on_motion_time(aoe_test_environment):
    """
    매 타임스텝마다 가속 효과가 모션 시간에 정확히 반영되는지 검증합니다.
    (어사이드 스킬 비활성화 상태)
    """
    party, renewa, aa_hero, skill_hero, logs = aoe_test_environment
    renewa.aside_level = 0  # 이 테스트에서는 어사이드 스킬을 비활성화

    party.run(max_t=40, num_simulation=1)

    accel_log = logs["acceleration"]
    motion_log = logs["motion"]

    def get_accel_at_time(t):
        last_accel = 1.0
        for log_t, accel_val in accel_log:
            if log_t <= t:
                last_accel = accel_val
            else:
                break
        return last_accel

    heroes = {hero.name: hero for hero in [renewa, aa_hero, skill_hero]}
    errors = []

    for t, hero_name, move_type, actual_motion_sec in motion_log:
        if move_type == MovementType.AsideSkill: continue
            
        hero = heroes[hero_name]
        accel = get_accel_at_time(t)
        base_motion_sec = hero.motion_time.get(move_type)
        
        expected_motion_sec = -1
        if move_type in [MovementType.LowerSkill, MovementType.UpperSkill]:
            expected_motion_sec = base_motion_sec / accel
        elif move_type in [MovementType.AutoAttackBasic, MovementType.AutoAttackEnhanced]:
            attack_speed_coeff = hero.get_coeff(StatType.AttackSpeed)
            aa_cd_ms = round(300 * SEC_TO_MS / (accel**2 * min(10., attack_speed_coeff) * hero.attack_speed), 0)
            aa_cd_sec = aa_cd_ms / SEC_TO_MS
            expected_motion_sec = min(base_motion_sec, aa_cd_sec)
        
        if expected_motion_sec != -1 and not np.isclose(actual_motion_sec, expected_motion_sec, rtol=0.01):
            errors.append(
                f"T={t:.2f} [{hero_name}-{move_type.name}] | "
                f"가속: {accel:.3f} | "
                f"실제모션: {actual_motion_sec:.3f}s | "
                f"기대모션: {expected_motion_sec:.3f}s"
            )

    assert not errors, "모션 시간 불일치 오류:\n" + "\n".join(errors)
    print("\n\n--- 리뉴아 각성 가속 효과 타임스텝별 검증 완료 ---")
    print("모든 행동의 모션 시간이 기대치와 일치함을 확인했습니다.")


def test_aside_skill_timing(aoe_test_environment):
    """
    어사이드 스킬(미사일)이 가속 효과를 받아 정확한 주기로 발사되는지 검증합니다.
    """
    
    party, renewa, _, _, logs = aoe_test_environment
    renewa.max_sp = 10000  # 저학년 스킬 사용 방지

    party.run(max_t=40, num_simulation=1)
    
    missile_log = logs["missile"]
    accel_log = logs["acceleration"]
    
    assert len(missile_log) > 3, "미사일이 충분히 발사되지 않았습니다."

    def get_accel_at_time(t):
        last_accel = 1.0
        for log_t, accel_val in accel_log:
            if log_t <= t:
                last_accel = accel_val
            else:
                break
        return last_accel

    actual_intervals = np.diff(missile_log)
    errors = []

    assert missile_log[0] == pytest.approx(6.5, abs=0.1)

    for i in range(len(actual_intervals)):
        fire_time = missile_log[i] - 0.5
        accel = get_accel_at_time(fire_time)
        expected_interval = 6.0 / accel
        actual_interval = actual_intervals[i]
        
        if not np.isclose(actual_interval, expected_interval, rtol=0.02):
            errors.append(
                f"구간 {i+1} | 시간: {fire_time:.2f}s | 가속: {accel:.3f} | "
                f"실제 간격: {actual_interval:.3f}s | 기대 간격: {expected_interval:.3f}s"
            )
        else:
            print(f"구간 {i+1} | 시간: {fire_time:.2f}s | 가속: {accel:.3f} | "
                  f"실제 간격: {actual_interval:.3f}s | 기대 간격: {expected_interval:.3f}s")

    assert not errors, "어사이드 스킬 발사 간격 불일치:\n" + "\n".join(errors)
    print("\n\n--- 리뉴아 어사이드 스킬 타이밍 검증 완료 ---")
    print("모든 미사일 발사 간격이 가속에 따라 정확하게 조절됨을 확인했습니다.")


def test_upper_skill_cd_reduction():
    # 미사일 쿨 6초 -> 25초 내에 3번 떨어짐 (25//8 == 3) -> 6초 쿨감 -> 첫 고학은 19초
    from dps.skill_conditions import CooldownReadyCondition
    hero = RenewaAwaken({
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 3,
        'attack': 100,
    })

    party = Party()
    party.add_hero(hero, 0)

    hero.max_sp = 10000

    rules = [None]* 9
    rules[0] = CooldownReadyCondition([
        MovementType.LowerSkill,
        MovementType.AutoAttackBasic,
        MovementType.AutoAttackEnhanced
    ])

    party.run(max_t=40, num_simulation=1, rules=rules)

    print(hero.movement_log)

    for t, m in hero.movement_log:
        if t == pytest.approx(19000, abs=10):
            assert m == MovementType.UpperSkill
            break
    else:
        assert False, "19초에 고학년 나가지 않음"