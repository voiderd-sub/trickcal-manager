#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from widgets.dps.party import Party
from db.dps.hero.TestHero import TestHero
from widgets.dps.enums import MovementType
import pandas as pd
import numpy as np

def test_simple_hero():
    """단순화된 테스트용 Hero로 시뮬레이션 테스트"""
    
    # 파티 생성
    party = Party()
    
    # TestHero 캐릭터 정보 설정
    hero_info = {
        "aside_level": 0,  # 어사이드 없음
        "lowerskill_level": 1,
        "upperskill_level": 1,
    }
    
    # TestHero 생성 및 파티에 추가
    test_hero = TestHero(hero_info)
    party.add_hero(test_hero, 0)
    
    print("=== 단순화된 테스트용 Hero 시뮬레이션 ===")
    print(f"캐릭터: {test_hero.name_kr} (TestHero)")
    print("데미지 설정:")
    print("  - 기본공격: 1")
    print("  - 저학년 스킬: 1,000")
    print("  - 고학년 스킬: 1,000,000")
    print()
    
    # 시뮬레이션 실행 (30초, 1회)
    print("시뮬레이션 실행 중... (30초, 1회)")
    result_df = party.run(max_t=30, num_simulation=1)
    
    # 결과 출력
    print("\n=== 시뮬레이션 결과 ===")
    
    # TestHero의 결과만 필터링
    hero_results = result_df[result_df['name'].str.startswith('테스트영웅_0')]
    
    if not hero_results.empty:
        print("데미지 타입별 결과:")
        for _, row in hero_results.iterrows():
            dmg_type = row['dmg_type']
            dmg_value = row['dmg']
            
            # 한국어 라벨로 변환
            dmg_label = {
                "AutoAttackBasic": "기본공격",
                "AutoAttackEnhanced": "강화공격", 
                "LowerSkill": "저학년 스킬",
                "UpperSkill": "고학년 스킬",
                "Total": "총합"
            }.get(str(dmg_type), str(dmg_type))
            
            print(f"  {dmg_label}: {dmg_value:,.0f}")
        
        # 총 데미지 계산
        total_damage_row = hero_results[hero_results['dmg_type'] == 'Total']
        if len(total_damage_row) > 0:
            dmg_val = np.array(total_damage_row['dmg'])
            total_damage = dmg_val[0]
        else:
            total_damage = 0
        print(f"\n총 데미지: {total_damage:,.0f}")
        print(f"DPS: {total_damage/30:,.0f}")
        
        # 각 무브먼트 실행 횟수 계산
        print("\n=== 무브먼트 실행 횟수 분석 ===")
        basic_attacks_row = hero_results[hero_results['dmg_type'] == 'AutoAttackBasic']
        lower_skills_row = hero_results[hero_results['dmg_type'] == 'LowerSkill']
        upper_skills_row = hero_results[hero_results['dmg_type'] == 'UpperSkill']
        if len(basic_attacks_row) > 0:
            dmg_val = np.array(basic_attacks_row['dmg'])
            basic_attacks = dmg_val[0]
        else:
            basic_attacks = 0
        if len(lower_skills_row) > 0:
            dmg_val = np.array(lower_skills_row['dmg'])
            lower_skills = dmg_val[0]
        else:
            lower_skills = 0
        if len(upper_skills_row) > 0:
            dmg_val = np.array(upper_skills_row['dmg'])
            upper_skills = dmg_val[0]
        else:
            upper_skills = 0
        
        print(f"기본공격 실행 횟수: {basic_attacks / 0.8:.0f}회")
        print(f"저학년 스킬 실행 횟수: {lower_skills / 800:.0f}회")
        print(f"고학년 스킬 실행 횟수: {upper_skills / 800000:.0f}회")
        
        # pending effect(투사체 적중) 발생 시점 출력
        before_pending = len(party.action_manager.pending_effect_queue)
        party.action_manager.resolve_all_actions(party.current_time)
        after_pending = len(party.action_manager.pending_effect_queue)
        if before_pending > after_pending:
            print(f"[Projectile Hit] time: {party.current_time/1000:.2f}s")
            # 적중된 액션 정보 출력 (여기서는 가장 최근에 실행된 액션을 추정)
            # 실제 데미지 기록은 hero.damage_records에서 확인 가능
            for movement, records in test_hero.damage_records.items():
                if records:
                    last_time, last_dmg = records[-1]
                    print(f"  movement: {movement}, hit_time: {last_time}, cumulative_damage: {last_dmg}")
        
    else:
        print("TestHero의 결과를 찾을 수 없습니다.")
    
    # 행동 통계 분석
    print("\n=== 행동 통계 ===")
    movement_counts = {}
    for _, movement in test_hero.movement_log:
        movement_counts[movement] = movement_counts.get(movement, 0) + 1
    
    movement_names = {
        MovementType.AutoAttackBasic: "기본공격",
        MovementType.AutoAttackEnhanced: "강화공격",
        MovementType.LowerSkill: "저학년 스킬",
        MovementType.UpperSkill: "고학년 스킬",
        MovementType.Wait: "대기"
    }
    
    for movement, count in movement_counts.items():
        name = movement_names.get(movement, str(movement))
        print(f"  {name}: {count}회")
    
    # 스킬 사용 횟수 확인
    print(f"\n저학년 스킬 사용 횟수: {len(test_hero.movement_timestamps[MovementType.LowerSkill])}")
    print(f"고학년 스킬 사용 횟수: {len(test_hero.movement_timestamps[MovementType.UpperSkill])}")
    
    # 각 무브먼트별 액션(데미지) 실행 횟수 확인
    print("\n=== 각 무브먼트별 액션(데미지) 실행 횟수 ===")
    for movement in [MovementType.AutoAttackBasic, MovementType.AutoAttackEnhanced, MovementType.LowerSkill, MovementType.UpperSkill]:
        records = test_hero.damage_records.get(movement, [])
        if isinstance(records, list):
            count = len(records)
        elif records:
            count = 1
        else:
            count = 0
        print(f"{movement_names.get(movement, str(movement))}: {count}회 (2개 이상이어야 정상)")
    
    return result_df

def test_simple_hero_detailed():
    """TestHero의 상세한 행동 로그 확인 및 액션 실행 횟수 카운트"""
    party = Party()
    hero_info = {"aside_level": 0, "lowerskill_level": 1, "upperskill_level": 1}
    test_hero = TestHero(hero_info)
    party.add_hero(test_hero, 0)
    print("=== TestHero 상세 행동 로그 (30초) ===")
    party.init_simulation()
    step_count = 0
    total_action_executed = 0
    while party.current_time < int(30 * 1000):
        step_count += 1
        all_min_indices = party.next_update.argmin()
        party.current_time = party.next_update[all_min_indices]
        if all_min_indices < 9:
            hero = party.character_list[all_min_indices]
            if hero is not None:
                print(f"\n--- 스텝 {step_count} (시간: {party.current_time/1000:.2f}초) ---")
                print(f"캐릭터 {all_min_indices} 무브먼트 실행")
                new_t = hero.step(party.current_time)
                party.next_update[all_min_indices] = new_t
                print(f"다음 행동 시간: {new_t/1000:.2f}초")
        elif all_min_indices == 9:
            print(f"step {step_count} (time: {party.current_time/1000:.2f}s)")
            if party.action_manager.action_queue and party.action_manager.action_queue[0][0] == party.current_time:
                print(f"current action: {party.action_manager.action_queue[0][2].action_type} from {party.action_manager.action_queue[0][2].source_movement}")
                before = len(party.action_manager.action_queue)
                party.action_manager.resolve_all_actions(party.current_time)
                after = len(party.action_manager.action_queue)
                executed = before - after if before > after else 0
                total_action_executed += executed
            if party.action_manager.pending_effect_queue and party.action_manager.pending_effect_queue[0][0] == party.current_time:
                print(f"current pending effect: {party.action_manager.pending_effect_queue[0][2].action_type} from {party.action_manager.pending_effect_queue[0][2].source_movement}")
                party.action_manager.resolve_all_actions(party.current_time)

            else:
                pass
        else:
            print(f"step {step_count} (time: {party.current_time/1000:.2f}s)")
            print(f"current status: {party.status_manager.status_queue[0].template.status_id}")
            party.status_manager.resolve_status_reserv(party.current_time)
    # 행동 로그 출력
    print("\n=== TestHero 행동 로그 ===")
    movement_log = test_hero.movement_log
    for timestamp, movement in movement_log:
        movement_name = {
            "AutoAttackBasic": "기본공격",
            "AutoAttackEnhanced": "강화공격",
            "LowerSkill": "저학년 스킬",
            "UpperSkill": "고학년 스킬",
            "Wait": "대기"
        }.get(movement, movement)
        print(f"  {timestamp:.2f}초: {movement_name}")
    print(f"\n총 행동 수: {len(test_hero.movement_log)}")
    print(f"최종 시간: {party.current_time/1000:.2f}초")
    print(f"총 액션 실행 횟수: {total_action_executed}회 (2개 이상이어야 정상)")

if __name__ == "__main__":
    # 메인 테스트 실행
    # result = test_simple_hero()
    
    print("\n" + "="*60)
    
    # 상세 행동 로그 테스트
    test_simple_hero_detailed() 