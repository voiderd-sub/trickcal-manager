import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.tests.simple_spell import create_test_spell

def get_total_damage(party):
    """Helper function to calculate total damage for the party."""
    total_damage = 0
    for hero in party.character_list:
        if hero and hero.damage_records:
            for damage_type, damage_list in hero.damage_records.items():
                total_damage += sum(dmg for _, dmg in damage_list)
    return total_damage

def test_spell_effects():
    """
    Tests if the test spell correctly applies its stat bonus and unique effect.
    - Stat Bonus: +5% party-wide attack.
    - Unique Effect: +100% all damage amplification.
    """
    # --- Base Case: No Spell ---
    party_no_spell = Party()
    hero_no_spell = SimpleHero("Hero")
    # Disable complexities for predictable damage
    hero_no_spell.upper_skill_cd = 1000000 
    hero_no_spell.sp_recovery_rate = 0
    party_no_spell.add_hero(hero_no_spell, 0)
    party_no_spell.run(max_t=2, num_simulation=1)
    damage_no_spell = get_total_damage(party_no_spell)

    # --- Case: With Spell ---
    party_with_spell = Party()
    hero_with_spell = SimpleHero("Hero")
    hero_with_spell.upper_skill_cd = 1000000
    hero_with_spell.sp_recovery_rate = 0
    party_with_spell.add_hero(hero_with_spell, 0)
    
    # Add the test spell
    spell = create_test_spell()
    party_with_spell.add_spell(spell)
    
    party_with_spell.run(max_t=2, num_simulation=1)
    damage_with_spell = get_total_damage(party_with_spell)

    print("\n--- Spell Effect Test ---")
    print(f"Damage with NO spell: {damage_no_spell}")
    print(f"Damage WITH spell: {damage_with_spell}")

    # Verification
    # Expected damage = BaseDamage * (1 + AttackBonus) * (1 + AmplifyBonus)
    # AttackBonus = 5% = 0.05
    # AmplifyBonus = 100% = 1.00
    # Expected damage = damage_no_spell * 1.05 * 2.0
    expected_damage = damage_no_spell * 1.05 * 2.0
    
    assert damage_with_spell == pytest.approx(expected_damage), \
        f"Damage with spell is incorrect. Expected: {expected_damage}, Got: {damage_with_spell}"

    print("✅ Spell Effect Test Passed!")

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
        spell = create_test_spell()
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