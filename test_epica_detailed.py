#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from widgets.dps.party import Party
from db.dps.hero.Epica import Epica
import pandas as pd

def test_epica_detailed():
    """에피카의 상세한 시뮬레이션 테스트"""
    
    # 파티 생성
    party = Party()
    
    # 에피카 캐릭터 정보 설정
    epica_info = {
        "aside_level": 2,
        "lowerskill_level": 5,
        "upperskill_level": 3,
    }
    
    # 에피카 생성 및 파티에 추가
    epica = Epica(epica_info)
    party.add_hero(epica, 0)
    
    print("=== 에피카 상세 시뮬레이션 테스트 ===")
    print(f"캐릭터: {epica.name_kr} (Epica)")
    print(f"어사이드 레벨: {epica_info['aside_level']}")
    print(f"저학년 스킬 레벨: {epica_info['lowerskill_level']}")
    print(f"고학년 스킬 레벨: {epica_info['upperskill_level']}")
    print()
    
    # 시뮬레이션 실행 (240초, 1회)
    print("시뮬레이션 실행 중... (240초, 1회)")
    result_df = party.run(max_t=240, num_simulation=1)
    
    # 결과 출력
    print("\n=== 시뮬레이션 결과 ===")
    
    # 에피카의 결과만 필터링
    epica_results = result_df[result_df['name'].str.startswith('에피카_0')]
    
    if not epica_results.empty:
        print("데미지 타입별 결과:")
        for _, row in epica_results.iterrows():
            dmg_type = row['dmg_type']
            dmg_value = row['dmg']
            
            dmg_label = {
                "AutoAttackBasic": "기본공격",
                "AutoAttackEnhanced": "강화공격", 
                "LowerSkill": "저학년 스킬",
                "UpperSkill": "고학년 스킬",
                "Total": "총합"
            }.get(dmg_type, dmg_type)
            
            print(f"  {dmg_label}: {dmg_value:,.0f}")
        
        total_damage = epica_results[epica_results['dmg_type'] == 'Total']['dmg'].iloc[0]
        print(f"\n총 데미지: {total_damage:,.0f}")
        print(f"DPS: {total_damage/240:,.0f}")
        
    # 행동 통계 분석
    print("\n=== 행동 통계 ===")
    movement_counts = {}
    for _, movement in epica.movement_log:
        movement_counts[movement] = movement_counts.get(movement, 0) + 1
    
    movement_names = {
        "AutoAttackBasic": "기본공격",
        "AutoAttackEnhanced": "강화공격",
        "LowerSkill": "저학년 스킬",
        "UpperSkill": "고학년 스킬",
        "Wait": "대기"
    }
    
    for movement, count in movement_counts.items():
        name = movement_names.get(movement, movement)
        print(f"  {name}: {count}회")
    
    # 스킬 사용 횟수 확인
    print(f"\n저학년 스킬 사용 횟수: {len(epica.movement_timestamps['LowerSkill'])}")
    print(f"고학년 스킬 사용 횟수: {len(epica.movement_timestamps['UpperSkill'])}")
    
    # 버프 상태 확인
    print("\n=== 버프 상태 확인 ===")
    has_lower_buff = epica.has_buff(f"에피카_0_저학년")
    has_upper_buff = epica.has_buff(f"에피카_0_고학년")
    print(f"저학년 버프 보유: {has_lower_buff}")
    print(f"고학년 버프 보유: {has_upper_buff}")
    
    # 액션 큐 상태 확인
    print("\n=== 액션 큐 상태 ===")
    action_manager = party.action_manager
    print(f"대기 중인 액션 수: {len(action_manager.action_queue)}")
    
    # StatusManager 상태 확인
    print("\n=== StatusManager 상태 ===")
    status_manager = party.status_manager
    print(f"대기 중인 상태 수: {len(status_manager.status_queue)}")
    
    party.action_manager.resolve_all_actions(party.current_time)
    
    return result_df

def test_epica_short_simulation():
    """짧은 시뮬레이션으로 상세한 로그 확인"""
    
    party = Party()
    epica_info = {"aside_level": 2, "lowerskill_level": 5, "upperskill_level": 3}
    epica = Epica(epica_info)
    party.add_hero(epica, 0)
    
    print("=== 15초 상세 시뮬레이션 ===")
    
    party.init_simulation()
    step_count = 0
    
    while party.current_time < int(15 * 1000) and step_count < 100:  # 15초 또는 최대 100스텝
        step_count += 1
        all_min_indices = party.next_update.argmin()
        party.current_time = party.next_update[all_min_indices]
        
        print(f"\n--- 스텝 {step_count} (시간: {party.current_time/1000:.2f}초) ---")
        print(f"다음 업데이트: 인덱스 {all_min_indices}")
        
        if all_min_indices < 9:
            hero = party.character_list[all_min_indices]
            if hero is not None:
                print(f"캐릭터 {all_min_indices} 행동 실행")
                new_t = hero.step(party.current_time)
                party.next_update[all_min_indices] = new_t
                print(f"다음 행동 시간: {new_t/1000:.2f}초")
        elif all_min_indices == 9:
            print("액션 해결")
            before_count = len(party.action_manager.action_queue)
            party.action_manager.resolve_action_reserv(party.current_time)
            after_count = len(party.action_manager.action_queue)
            print(f"액션 큐: {before_count} -> {after_count}")
        else:
            print("상태 해결")
            before_count = len(party.status_manager.status_queue)
            party.status_manager.resolve_status_reserv(party.current_time)
            after_count = len(party.status_manager.status_queue)
            print(f"상태 큐: {before_count} -> {after_count}")
    
    print(f"\n총 스텝 수: {step_count}")
    print(f"최종 시간: {party.current_time/1000:.2f}초")

if __name__ == "__main__":
    # 상세 테스트 실행
    result = test_epica_detailed()
    
    print("\n" + "="*60)
    
    # 짧은 시뮬레이션 테스트
    test_epica_short_simulation() 