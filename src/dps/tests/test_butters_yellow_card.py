import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.butters_yellow_card import ButtersYellowCard
from dps.enums import DamageType

def test_butters_yellow_card_damage_increase():
    """
    Tests that Butter's Yellow Card increases enhanced attack damage.
    """
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    party.add_artifact(ButtersYellowCard(level=1), 0)
    
    party.init_run(None, None)
    party.init_simulation()

    # Get damage for a basic auto attack
    basic_attack_damage = hero.get_damage(100, DamageType.AutoAttackBasic)

    # Get damage for an enhanced auto attack
    enhanced_attack_damage = hero.get_damage(100, DamageType.AutoAttackEnhanced)

    # Effect at level 1 is 69%
    expected_damage = basic_attack_damage * 1.69

    assert enhanced_attack_damage == pytest.approx(expected_damage)

def test_butters_yellow_card_stacking():
    """
    Tests that the damage bonus from Butter's Yellow Card stacks.
    """
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    party.add_artifact(ButtersYellowCard(level=1), 0)
    party.add_artifact(ButtersYellowCard(level=1), 0)
    
    party.init_run(None, None)
    party.init_simulation()

    # Get damage for a basic auto attack
    basic_attack_damage = hero.get_damage(100, DamageType.AutoAttackBasic)

    # Get damage for an enhanced auto attack
    enhanced_attack_damage = hero.get_damage(100, DamageType.AutoAttackEnhanced)

    # Effect at level 1 is 69%, so two artifacts should be 138%
    expected_damage = basic_attack_damage * 2.38

    assert enhanced_attack_damage == pytest.approx(expected_damage)

if __name__ == "__main__":
    test_butters_yellow_card_damage_increase()
    test_butters_yellow_card_stacking() 