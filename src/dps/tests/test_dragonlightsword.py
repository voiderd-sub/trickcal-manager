import pytest
import numpy as np
import math
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.dragonlightsword import DragonLightSword
from dps.enums import MovementType, StatType, SEC_TO_MS

def test_dragonlightsword_precise_attack_timing_with_motion():
    """
    Tests DragonLightSword with a precise, direct comparison method,
    explicitly accounting for the motion time of the interrupting LowerSkill.
    """
    party = Party()
    hero = SimpleHero("TestHero")
    hero.upper_skill_cd = 1000000 
    hero.sp_per_aa = 0 # Ensure SP gain is only from time
    party.add_hero(hero, 0)
    party.add_artifact(DragonLightSword(), 0)

    party.run(max_t=20, num_simulation=1)

    # --- Analysis ---
    movement_log = hero.movement_log
    basic_attack_times = [t for t, m in movement_log if m == MovementType.AutoAttackBasic]
    lower_skill_time = next((t for t, m in movement_log if m == MovementType.LowerSkill), None)

    # --- Verification ---
    def predict_aa_cd(t, last_reset_time):
        stacks = math.floor(t / SEC_TO_MS) - math.floor(last_reset_time / SEC_TO_MS)
        dls_as_bonus = stacks * 0.08
        base_as_coeff = hero.attack_speed_coeff 
        total_as_coeff = base_as_coeff + dls_as_bonus
        return round(300 * SEC_TO_MS / (hero.acceleration**2 * min(10., total_as_coeff) * hero.attack_speed), 0)

    last_reset_time = 0
    interrupting_interval_idx = -1
    if lower_skill_time:
        for i in range(len(basic_attack_times) - 1):
            if basic_attack_times[i] < lower_skill_time < basic_attack_times[i+1]:
                interrupting_interval_idx = i
                break
    
    print("\n--- DragonLightSword Precise Attack Timing Test (with Motion) ---")

    for i in range(len(basic_attack_times) - 1):
        current_attack_time = basic_attack_times[i]
        
        if i == interrupting_interval_idx:
            # Special case: The interval interrupted by the Lower Skill
            # The next basic attack should start right after the Lower Skill's motion is finished.
            expected_next_attack_time = lower_skill_time + hero.get_motion_time(MovementType.LowerSkill)
            actual_next_attack_time = basic_attack_times[i+1]
            
            print(f"Checking interrupt at {current_attack_time/1000:.3f}s: Expected next attack after LS motion at ~{expected_next_attack_time/1000:.3f}s, Actual: {actual_next_attack_time/1000:.3f}s")
            assert actual_next_attack_time == pytest.approx(expected_next_attack_time, abs=1)
            
            last_reset_time = lower_skill_time
        else:
            # Normal case: The interval should match the calculated attack cooldown
            expected_cd = predict_aa_cd(current_attack_time, last_reset_time)
            actual_interval = basic_attack_times[i+1] - current_attack_time
            
            print(f"Attack at {current_attack_time/1000:.3f}s: Expected CD: {expected_cd}ms, Actual Interval: {actual_interval}ms")
            assert actual_interval == pytest.approx(expected_cd, abs=1)

    print("\n✅ DragonLightSword precise timing test with motion considered passed!")

if __name__ == "__main__":
    test_dragonlightsword_precise_attack_timing_with_motion() 