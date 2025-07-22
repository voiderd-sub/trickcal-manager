#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dps.party import Party
from db.dps.hero.Epica import Epica
import pandas as pd

def test_epica_simulation():
    """에피카 하나만으로 시뮬레이션을 테스트하는 함수"""
    
    # 파티 생성
    party = Party()
    
    # 에피카 캐릭터 정보 설정
    epica_info = {
        "aside_level": 2,  # 어사이드 레벨
        "lowerskill_level": 5,  # 저학년 스킬 레벨
        "upperskill_level": 3,  # 고학년 스킬 레벨
    }
    
    # 에피카 생성 및 파티에 추가 (인덱스 0번에 배치)
    epica = Epica(epica_info)
    party.add_hero(epica, 0)
    
    print("=== 에피카 시뮬레이션 테스트 ===")
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
            
            # 한국어 라벨로 변환
            dmg_label = {
                "AutoAttackBasic": "기본공격",
                "AutoAttackEnhanced": "강화공격", 
                "LowerSkill": "저학년 스킬",
                "UpperSkill": "고학년 스킬",
                "Total": "총합"
            }.get(dmg_type, dmg_type)
            
            print(f"  {dmg_label}: {dmg_value:,.0f}")
        
        # 총 데미지 계산
        total_damage = epica_results[epica_results['dmg_type'] == 'Total']['dmg'].iloc[0]
        print(f"\n총 데미지: {total_damage:,.0f}")
        print(f"DPS: {total_damage/240:,.0f}")
        
    else:
        print("에피카의 결과를 찾을 수 없습니다.")
    
    # 디버깅을 위한 추가 정보
    print("\n=== 디버깅 정보 ===")
    print(f"전체 결과 행 수: {len(result_df)}")
    print(f"에피카 결과 행 수: {len(epica_results)}")
    
    if not epica_results.empty:
        print("에피카 결과 데이터:")
        print(epica_results.to_string(index=False))
    
    return result_df

def test_epica_movement_log():
    """에피카의 행동 로그를 확인하는 함수"""
    
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
    
    # 짧은 시뮬레이션 실행 (10초)
    print("=== 에피카 행동 로그 테스트 ===")
    print("10초간 시뮬레이션 실행...")
    
    party.init_simulation()
    while party.current_time < int(10 * 1000):  # 10초
        all_min_indices = party.next_update.argmin()
        party.current_time = party.next_update[all_min_indices]
        
        if all_min_indices < 9:
            hero = party.character_list[all_min_indices]
            if hero is not None:
                new_t = hero.step(party.current_time)
                party.next_update[all_min_indices] = new_t
        elif all_min_indices == 9:
            party.action_manager.resolve_all_actions(party.current_time)
        else:
            party.status_manager.resolve_status_reserv(party.current_time)
    
    # 행동 로그 출력
    print("\n=== 에피카 행동 로그 (처음 20개) ===")
    movement_log = epica.movement_log[:20]
    
    for timestamp, movement in movement_log:
        movement_name = {
            "AutoAttackBasic": "기본공격",
            "AutoAttackEnhanced": "강화공격",
            "LowerSkill": "저학년 스킬",
            "UpperSkill": "고학년 스킬",
            "Wait": "대기"
        }.get(movement, movement)
        
        print(f"  {timestamp:.2f}초: {movement_name}")
    
    print(f"\n총 행동 수: {len(epica.movement_log)}")

if __name__ == "__main__":
    # 메인 테스트 실행
    result = test_epica_simulation()
    
    print("\n" + "="*50)
    
    # 행동 로그 테스트
    test_epica_movement_log() 