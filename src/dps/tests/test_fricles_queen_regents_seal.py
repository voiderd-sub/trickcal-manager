import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.fricles_queen_regents_seal import FriclesQueenRegentsSeal
from dps.enums import DamageType, StatType


def test_fricles_queen_regents_seal_stats():
    """Test that Fricle's Queen Regent's Seal correctly applies stat bonuses."""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    
    artifact = FriclesQueenRegentsSeal()
    party.add_artifact(artifact, 0)
    
    party.init_run(None, None)
    party.init_simulation()
    
    # Base coeff is 1.0, bonus is 17.84 / 100
    expected_coeff = 1.0 + 17.84 / 100
    assert hero.get_coeff(StatType.AttackMagic) == pytest.approx(expected_coeff)
    assert hero.get_coeff(StatType.CriticalMult) == pytest.approx(expected_coeff)


def test_seal_non_stackable_on_same_hero():
    """Test that the seal's amplify effect does not stack if the same hero equips two."""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)

    # Add two seals to the same hero
    party.add_artifact(FriclesQueenRegentsSeal(), 0)
    party.add_artifact(FriclesQueenRegentsSeal(), 0)

    party.init_run(None, None)
    party.init_simulation()

    # The init_effect_fn is non-stackable, so it should only be applied once per hero.
    # Base amplify is 1.0, bonus is 41%
    expected_amplify = 1.0 + 0.41
    for dt in DamageType.get_leaf_members(DamageType.Skill):
        assert hero.get_amplify(dt) == pytest.approx(expected_amplify)


def test_seal_stacks_on_different_heroes_in_same_row():
    """Test that the seal's amplify effect stacks when equipped by different heroes in the same row."""
    party = Party()
    hero1 = SimpleHero()
    hero2 = SimpleHero()
    hero3 = SimpleHero() # a hero in a different row

    # hero1 and hero2 are in the same row (row 0), hero3 is in another row (row 1)
    party.add_hero(hero1, 0)
    party.add_hero(hero2, 1)
    party.add_hero(hero3, 3)

    # Each hero in the same row equips one seal
    party.add_artifact(FriclesQueenRegentsSeal(), 0)
    party.add_artifact(FriclesQueenRegentsSeal(), 1)

    party.init_run(None, None)
    party.init_simulation()

    # The effect from hero1's seal applies to hero1 and hero2.
    # The effect from hero2's seal also applies to hero1 and hero2.
    # So, the 41% bonus should be applied twice.
    expected_amplify_stacked = 1.0 + 0.41 + 0.41
    for dt in DamageType.get_leaf_members(DamageType.Skill):
        assert hero1.get_amplify(dt) == pytest.approx(expected_amplify_stacked)
        assert hero2.get_amplify(dt) == pytest.approx(expected_amplify_stacked)

    # hero3 is in a different row, so it should not receive any bonus.
    expected_amplify_unaffected = 1.0
    for dt in DamageType.get_leaf_members(DamageType.Skill):
        assert hero3.get_amplify(dt) == pytest.approx(expected_amplify_unaffected) 