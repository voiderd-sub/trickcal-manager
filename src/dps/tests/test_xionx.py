import pytest

from dps.party import Party
from dps.heroes.xXionx import xXionx
from dps.enums import MovementType, DamageType, StatType, SEC_TO_MS
from dps.status import StatusReservation

@pytest.fixture
def party_with_xionx():
    """Pytest fixture to set up a Party with xXionx."""
    def _setup(hero_info):
        party = Party()
        xion = xXionx(hero_info)
        party.add_hero(xion, 6)
        party.init_run()
        party.init_simulation()
        return party, xion
    return _setup

def test_run_xionx(party_with_xionx):
    hero_info = {"attack": 100, "aside_level": 0}
    party, xion = party_with_xionx(hero_info)
    party.run(max_t=30, num_simulation=1)
    
    # print movement log
    # print(xion.movement_log)
    # print(xion.movement_timestamps)
    # print(xion.damage_records)

def test_darkbullet_attack_buff(party_with_xionx):
    hero_info = {"attack": 100, "aside_level": 0}
    party, xion = party_with_xionx(hero_info)

    # 1. '마탄' 스택 0개일 때의 대미지 계산
    base_attack_coeff = xion.get_coeff(StatType.AttackPhysic)
    base_damage = xion.get_damage(175, DamageType.AutoAttackBasic)

    assert base_attack_coeff == 1.0
    assert base_damage == pytest.approx(0.8 * 100 * 1.0 * 1.75)  # 140

    # 2. '마탄' 스택 1개 부여
    name = xion.get_unique_name()
    buff_template = xion.status_templates[name + "_마탄"]
    reservation = StatusReservation(template=buff_template, start_time=party.current_time)
    party.status_manager.add_status_reserv(reservation)
    party.status_manager.resolve_status_reserv(party.current_time)

    # 3. 스택 카운트 및 공격력 계수 확인
    stack_count = party.status_manager.get_buff_count(xion.party_idx, name + "_마탄")
    assert stack_count == 1
    
    buffed_attack_coeff = xion.get_coeff(StatType.AttackPhysic)
    assert buffed_attack_coeff == pytest.approx(1.0 + 0.05) # Note: apply_stat_bonuses adds 5, which is 0.05 as coeff

    # 4. '마탄' 스택 1개일 때의 대미지 계산 및 검증
    buffed_damage = xion.get_damage(175, DamageType.AutoAttackBasic)
    assert buffed_damage == pytest.approx(0.8 * 100 * (1.0 + 0.05) * 1.75)
    assert buffed_damage > base_damage

    # 5. 마탄을 10번 부여
    for i in range(10):
        reservation = StatusReservation(template=buff_template, start_time=party.current_time)
        party.status_manager.add_status_reserv(reservation)
    party.status_manager.resolve_status_reserv(party.current_time)
    
    # 6. 공격력이 마탄 최대 스택(6)과 같은지 확인
    max_buff_attack_coeff = xion.get_coeff(StatType.AttackPhysic)
    assert max_buff_attack_coeff == pytest.approx(1.0 + 6 * 0.05)
    
    max_buffed_damage = xion.get_damage(175, DamageType.AutoAttackBasic)
    assert max_buffed_damage == pytest.approx(0.8 * 100 * (1.0 + 6 * 0.05) * 1.75)


def test_aside_l2_buff_scenarios():
    # 1. xion만 있는 파티를 생성한다. 이때 xion의 aisde level은 2이며, 
    # 고학년 사용 조건은 CooldownReadyCondition이고, UpperSkill을 제외한 모든 movement가 cancelable하다.
    
    # CooldownReadyCondition 설정
    from dps.skill_conditions import CooldownReadyCondition
    from dps.enums import MovementType
    
    # UpperSkill을 제외한 모든 movement가 cancelable
    cancelable_movements = [
        MovementType.AutoAttackBasic,
        MovementType.AutoAttackEnhanced,
        MovementType.LowerSkill,
        MovementType.AsideSkill,
    ]

    hero_info = {"attack": 100, "aside_level": 2}
    party = Party()
    xion = xXionx(hero_info)
    xion.upper_skill_cd = 10
    party.add_hero(xion, 6)
    party.init_run(rules=[
        None, None, None, None, None, None,
        CooldownReadyCondition(cancelable_movements=cancelable_movements),
        None, None
    ])
    party.init_simulation()


    # 2. t = 20까지 manual하게 party.step()을 진행한다.
    print("=== Aside L2 Buff Scenarios Test ===")
    print(f"Initial time: {party.current_time}ms")
    print(f"Xion aside_level: {xion.aside_level}")
    print(f"Cancelable movements: {cancelable_movements}")
    xion.sp = xion.max_sp
    
    step_count = 0
    while party.current_time <= 20 * SEC_TO_MS:
        step_count += 1
        print(f"Step {step_count}: t = {party.current_time}ms")
        
        # 현재 상태 출력
        if hasattr(xion, 'last_movement'):
            print(f"  Last movement: {xion.last_movement}")
        if hasattr(xion, 'upper_skill_flag'):
            print(f"  Upper skill flag: {xion.upper_skill_flag}")
        if hasattr(xion, '_pending_aside_l2_buff_times'):
            print(f"  Pending aside L2 buff times: {xion._pending_aside_l2_buff_times}")
        print(f"  AS: {xion.get_coeff(StatType.AttackSpeed)}")
        
        # 파티 스텝 실행
        party.step()

        print(f"Do {xion.last_movement.name}")
        
        # 버프 상태 확인
        name = xion.get_unique_name()
        aside_buff_name = name + "_A2_공속"
        buff_count = party.status_manager.get_buff_count(xion.party_idx, aside_buff_name)
        if buff_count > 0:
            print(f"  Active aside L2 buffs: {buff_count}")
        
        print()
    
    print("=== Test Complete ===")
    print("테스트가 완료되었습니다. 위의 로그를 확인하여 정상 작동 여부를 판단하세요.")