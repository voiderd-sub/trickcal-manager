import pytest
from dps.party import Party
from dps.enums import DamageType
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.toy_telescope import ToyTelescope

@pytest.fixture
def setup_hero():
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)
    return party, hero

def test_toy_telescope_effects(setup_hero):
    """
    Tests the damage amplification effect of the Toy Telescope artifact.
    """
    party, hero = setup_hero
    
    # Temporarily add SimpleHero to the distance factor map for testing
    ToyTelescope.DISTANCE_FACTOR_MAP[hero.name_kr] = 0.5

    # --- Case 1: No artifact ---
    party.init_run(None, None)
    party.init_simulation()
    amp_no_artifact_basic = hero.get_amplify(DamageType.AutoAttackBasic)
    amp_no_artifact_enhanced = hero.get_amplify(DamageType.AutoAttackEnhanced)

    assert amp_no_artifact_basic == 1.0, "Initial basic attack amplify should be 1.0"
    assert amp_no_artifact_enhanced == 1.0, "Initial enhanced attack amplify should be 1.0"

    # --- Case 2: One artifact ---
    artifact1 = ToyTelescope(level=1)
    print(hero.amplify_dict)
    hero.add_artifact(artifact1)
    print(hero.amplify_dict)

    party.init_run(None, None)
    print(hero.amplify_dict)

    party.init_simulation()
    print(hero.amplify_dict)


    # Calculation based on artifact logic with a=0.5
    # effect_value = 10.0 (level 1)
    # basic_amp = 40 * 0.5 * 10.0 = 200%
    # enhanced_amp = 10 * 0.5 * 10.0 = 50%
    expected_amp_basic_1 = 1.0 + (200 / 100)
    expected_amp_enhanced_1 = 1.0 + (50 / 100)

    amp_with_1_artifact_basic = hero.get_amplify(DamageType.AutoAttackBasic)
    amp_with_1_artifact_enhanced = hero.get_amplify(DamageType.AutoAttackEnhanced)

    print("\n--- Toy Telescope Test (1 Artifact) ---")
    print(f"Basic Attack Amplify: Expected={expected_amp_basic_1}, Got={amp_with_1_artifact_basic}")
    print(f"Enhanced Attack Amplify: Expected={expected_amp_enhanced_1}, Got={amp_with_1_artifact_enhanced}")

    assert amp_with_1_artifact_basic == pytest.approx(expected_amp_basic_1)
    assert amp_with_1_artifact_enhanced == pytest.approx(expected_amp_enhanced_1)

    # --- Case 3: One artifact on an Eldain hero ---
    hero.is_eldain = True
    party.init_run(None, None)
    party.init_simulation()
    
    # Basic amp should be doubled for Eldain
    expected_amp_basic_eldain = 1.0 + (200 * 2 / 100)
    amp_eldain_basic = hero.get_amplify(DamageType.AutoAttackBasic)

    print("\n--- Toy Telescope Test (1 Artifact on Eldain) ---")
    print(f"Eldain Basic Attack Amplify: Expected={expected_amp_basic_eldain}, Got={amp_eldain_basic}")
    assert amp_eldain_basic == pytest.approx(expected_amp_basic_eldain)
    hero.is_eldain = False # Reset for next test case

    # --- Case 4: Two stackable artifacts ---
    artifact2 = ToyTelescope(level=1)
    hero.add_artifact(artifact2)
    party.init_run(None, None)
    party.init_simulation()

    # Effects should stack, so double the amplification from Case 2
    expected_amp_basic_2 = 1.0 + (200 / 100) * 2
    expected_amp_enhanced_2 = 1.0 + (50 / 100) * 2

    amp_with_2_artifacts_basic = hero.get_amplify(DamageType.AutoAttackBasic)
    amp_with_2_artifacts_enhanced = hero.get_amplify(DamageType.AutoAttackEnhanced)

    print("\n--- Toy Telescope Test (2 Artifacts) ---")
    print(f"Basic Attack Amplify (2): Expected={expected_amp_basic_2}, Got={amp_with_2_artifacts_basic}")
    print(f"Enhanced Attack Amplify (2): Expected={expected_amp_enhanced_2}, Got={amp_with_2_artifacts_enhanced}")

    assert amp_with_2_artifacts_basic == pytest.approx(expected_amp_basic_2)
    assert amp_with_2_artifacts_enhanced == pytest.approx(expected_amp_enhanced_2)

    # Cleanup the map
    del ToyTelescope.DISTANCE_FACTOR_MAP[hero.name_kr]
    
    print("\n✅ Toy Telescope effect test passed!") 