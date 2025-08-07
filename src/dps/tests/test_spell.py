import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.spell import Spell
from dps.spells import GroupGradeUp, MeditationTime, AromaTherapy
from dps.enums import StatType

def get_total_damage(party):
    """Helper function to calculate total damage for the party."""
    total_damage = 0
    for hero in party.character_list:
        if hero and hasattr(hero, 'damage_records'):
            for damage_type, damage_list in hero.damage_records.items():
                total_damage += sum(dmg for _, dmg in damage_list)
    return total_damage

def test_spell_effects():
    """
    Tests if the '학자' spell correctly applies its stat bonus.
    - Stat Bonus: +3.53% party-wide physic attack and magic attack at level 1.
    """
    # --- Base Case: No Spell ---
    party_no_spell = Party()
    hero_no_spell = SimpleHero("Hero")
    hero_no_spell.upper_skill_cd = 1000000 
    hero_no_spell.sp_recovery_rate = 0
    party_no_spell.add_hero(hero_no_spell, 0)
    party_no_spell.run(max_t=2, num_simulation=1)
    damage_no_spell = get_total_damage(party_no_spell)
    attack_no_spell = hero_no_spell.get_coeff(StatType.AttackPhysic)

    # --- Case: With Spell ---
    party_with_spell = Party()
    hero_with_spell = SimpleHero("Hero")
    hero_with_spell.upper_skill_cd = 1000000
    hero_with_spell.sp_recovery_rate = 0
    party_with_spell.add_hero(hero_with_spell, 0)
    
    # Add the '학자' spell
    spell = Spell(name="학자", level=1)
    party_with_spell.add_spell(spell)
    
    party_with_spell.run(max_t=2, num_simulation=1)
    damage_with_spell = get_total_damage(party_with_spell)
    attack_with_spell = hero_with_spell.get_coeff(StatType.AttackPhysic)

    print("\n--- Spell Effect Test ---")
    print(f"Attack with NO spell: {attack_no_spell}")
    print(f"Attack WITH spell: {attack_with_spell}")
    print(f"Damage with NO spell: {damage_no_spell}")
    print(f"Damage WITH spell: {damage_with_spell}")

    # Verification
    # Expected Attack = BaseAttack * (1 + AttackBonus / 100)
    # AttackBonus from '학자' level 1 is 3.53
    expected_attack = attack_no_spell * (1 + 3.53 / 100)
    assert attack_with_spell == pytest.approx(expected_attack)

    # Damage should increase proportionally to attack
    expected_damage = damage_no_spell * (expected_attack / attack_no_spell)
    
    assert damage_with_spell == pytest.approx(expected_damage), \
        f"Damage with spell is incorrect. Expected: {expected_damage}, Got: {damage_with_spell}"

    print("✅ Spell Effect Test Passed!")


def test_grade_system():
    """학년 시스템 테스트 - 학년에 따른 스탯 증가 확인"""
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)
    
    # 1학년 기본값 확인
    assert hero.grade == 1
    
    # 2학년으로 증가
    hero.increase_grade(1)
    assert hero.grade == 2
    
    # 스탯 계산 적용
    hero._calculate_final_stats()
    
    # 2학년 보너스 확인 (6% 증가)
    expected_attack = 100 * (1 + 6 / 100)  # 기본 공격력 100에 6% 증가
    assert hero.attack_physic == pytest.approx(expected_attack)
    
    # 6학년 딜러 특별 효과
    hero.increase_grade(4)  # 6학년으로
    assert hero.grade == 6
    
    # 스탯 재계산
    hero._calculate_final_stats()
    
    # 6학년 딜러 특별 효과 확인 (100% 증가)
    expected_attack_grade6 = 100 * 2.0  # 기본 공격력 100에 100% 증가
    assert hero.attack_physic == pytest.approx(expected_attack_grade6)
    
    print("✅ Grade System Test Passed!")


def test_grade_increase_spell():
    """단체 월반 스펠 테스트"""
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)
    
    # 스펠 적용 전 학년 확인
    assert hero.grade == 1
    
    # 단체 월반 스펠 추가
    spell = GroupGradeUp(level=1)
    party.add_spell(spell)
    
    # 스펠 설정 효과 적용
    party.init_run()
    
    # 학년이 증가했는지 확인
    assert hero.grade == 2
    
    # 스탯 계산 적용
    hero._calculate_final_stats()
    
    # 2학년 보너스 확인 (6% 증가)
    expected_attack = 100 * (1 + 6 / 100)
    assert hero.attack_physic == pytest.approx(expected_attack)
    
    print("✅ Grade Increase Spell Test Passed!")


def test_sp_recovery_system():
    """SP 회복량 시스템 테스트"""
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)
    party.init_run()
    party.init_simulation()
    
    # 기본 SP 회복량 확인
    assert hero.sp_recovery_rate == 10
    
    # 고정 수치 증가 테스트
    hero.add_sp_recovery_fixed_bonus(5)
    expected_rate = (10 + 5) * (1 + 0 / 100)  # (기본 + 고정) × (1 + %)
    assert hero.get_sp_recovery_rate() == pytest.approx(expected_rate)
    
    # % 증가 테스트
    hero.add_sp_recovery_percent_bonus(20)
    expected_rate = (10 + 5) * (1 + 20 / 100)  # (기본 + 고정) × (1 + %)
    assert hero.get_sp_recovery_rate() == pytest.approx(expected_rate)
    
    print("✅ SP Recovery System Test Passed!")


def test_meditation_time_spell():
    """명상의 시간 스펠 테스트"""
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)
    party.init_run()
    party.init_simulation()
    
    # 스펠 적용 전 SP 회복량 확인
    base_sp_recovery = hero.get_sp_recovery_rate()
    
    # 명상의 시간 스펠 추가
    spell = MeditationTime(level=1)
    party.add_spell(spell)
    
    # 스펠 설정 효과 적용
    party.init_run()
    party.init_simulation()
    
    # 30% 증가 확인
    expected_sp_recovery = base_sp_recovery * (1 + 30 / 100)
    assert hero.get_sp_recovery_rate() == pytest.approx(expected_sp_recovery)
    
    print("✅ Meditation Time Spell Test Passed!")


def test_aroma_therapy_spell():
    """아로마 테라피 스펠 테스트"""
    party = Party()
    
    # 여러 히어로 생성
    hero1 = SimpleHero("Hero1")
    hero2 = SimpleHero("Hero2")
    hero3 = SimpleHero("Hero3")
    
    party.add_hero(hero1, 0)
    party.add_hero(hero2, 1)
    party.add_hero(hero3, 2)

    spell = AromaTherapy(level=1)
    party.add_spell(spell)

    # 초기 SP 설정 (각각 다른 SP 비율)
    hero1.init_sp = 50  # 50% (50/100)
    hero2.init_sp = 20  # 20% (20/100) - 가장 낮음
    hero3.init_sp = 80  # 80% (80/100)

    party.init_run()
    party.init_simulation()
    
    # SP 비율이 가장 낮았던 hero2의 SP가 100%로 회복되었는지 확인
    assert hero2.sp == hero2.max_sp
    assert hero1.sp == 50  # 다른 히어로는 변경되지 않음
    assert hero3.sp == 80  # 다른 히어로는 변경되지 않음
    
    print("✅ Aroma Therapy Spell Test Passed!")


def test_simulation_idempotency():
    """
    Tests if running the simulation multiple times with the same settings yields the exact same result,
    ensuring that the simulation state is properly reset by init_simulation().
    """
    def create_and_setup_party():
        party = Party()
        hero = SimpleHero("IdempotentHero")
        hero.upper_skill_cd = 10 # Use a skill to ensure more complex state changes
        party.add_hero(hero, 0)
        spell = Spell(name="학자", level=1)
        party.add_spell(spell)
        return party
    
    T=60

    # --- Run 1 ---
    party1 = create_and_setup_party()
    party1.run(max_t=T, num_simulation=1)
    damage1 = get_total_damage(party1)
    log1 = [(round(t), m) for t, m in party1.character_list[0].movement_log]

    # --- Run 2 ---: return 2nd simulation result
    party2 = create_and_setup_party()
    party2.run(max_t=T, num_simulation=2)
    damage2 = get_total_damage(party2)
    log2 = [(round(t), m) for t, m in party2.character_list[0].movement_log]

    print("\n--- Simulation Idempotency Test ---")
    print(f"Run 1 Damage: {damage1}")
    print(f"Run 2 Damage: {damage2}")
    print(f"Run 1 Log: {log1}")
    print(f"Run 2 Log: {log2}")

    # Verification
    assert damage1 == damage2, "Total damage should be identical between two identical runs."
    assert log1 == log2, "Movement logs should be identical between two identical runs."

    print("✅ Simulation Idempotency Test Passed!") 