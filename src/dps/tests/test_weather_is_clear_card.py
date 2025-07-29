import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.weather_is_clear_card import WeatherIsClearCard


def test_weather_is_clear_card_stats():
    """Test that WeatherIsClearCard correctly applies stat bonuses"""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    
    # Add WeatherIsClearCard
    artifact = WeatherIsClearCard()
    party.add_artifact(artifact, 0)
    
    # Initialize simulation to apply stats
    party.init_run(None, None)
    party.init_simulation()
    
    # Check that stats are applied correctly
    assert hero.attack_speed_coeff == pytest.approx(1.1798), f"Expected attack_speed_coeff to be 1.1798, got {hero.attack_speed_coeff}"
    assert hero.critical_rate_coeff == pytest.approx(1.1798), f"Expected critical_rate_coeff to be 1.1798, got {hero.critical_rate_coeff}"


def test_weather_is_clear_card_lightning_effect():
    """Test that WeatherIsClearCard triggers lightning damage every 3 basic attacks"""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    
    # Add WeatherIsClearCard
    artifact = WeatherIsClearCard()
    party.add_artifact(artifact, 0)
    
    # Run simulation for enough time to get multiple basic attacks
    party.run(max_t=10, num_simulation=1)
    
    # Check that lightning damage was recorded
    artifact_damage_records = hero.damage_records.get("Artifact", [])
    basic_attack_records = hero.damage_records.get("AutoAttackBasic", [])
    
    print(f"Basic attack records: {basic_attack_records}")
    print(f"Artifact damage records: {artifact_damage_records}")
    
    # Should have lightning damage (every 3 basic attacks)
    assert len(artifact_damage_records) > 0, "No lightning damage was recorded"
    
    # Verify lightning damage timing (should occur after every 3rd basic attack)
    basic_attack_times = [record[0] for record in basic_attack_records]
    lightning_times = [record[0] for record in artifact_damage_records]
    
    print(f"Basic attack times: {basic_attack_times}")
    print(f"Lightning times: {lightning_times}")
    
    # Lightning should occur after every 3rd basic attack
    expected_lightning_count = len(basic_attack_times) // 3
    assert len(lightning_times) == expected_lightning_count, \
        f"Expected {expected_lightning_count} lightning strikes, got {len(lightning_times)}"


def test_weather_is_clear_card_non_stackable():
    """Test that WeatherIsClearCard effect does not stack when multiple are equipped"""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    
    # Add two WeatherIsClearCards
    artifact1 = WeatherIsClearCard()
    artifact2 = WeatherIsClearCard()
    party.add_artifact(artifact1, 0)
    party.add_artifact(artifact2, 0)
    
    # Run simulation
    party.run(max_t=10, num_simulation=1)
    
    # Check that only one lightning effect is active (non-stackable)
    # The effect should still work, but not be duplicated
    artifact_damage_records = hero.damage_records.get("Artifact", [])
    basic_attack_records = hero.damage_records.get("AutoAttackBasic", [])
    
    # Should still have lightning damage, but not more than with one artifact
    expected_lightning_count = len(basic_attack_records) // 3
    assert len(artifact_damage_records) == expected_lightning_count, \
        f"Expected {expected_lightning_count} lightning strikes, got {len(artifact_damage_records)}"


if __name__ == "__main__":
    test_weather_is_clear_card_stats()
    test_weather_is_clear_card_lightning_effect()
    test_weather_is_clear_card_non_stackable()
    print("✅ All WeatherIsClearCard tests passed!") 