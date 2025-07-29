import pytest
from dps.party import Party
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.dayas_diamond_cutter import DayasDiamondCutter
from dps.status import StatusTemplate
from dps.enums import MovementType, DamageType

# # A simple debuff for testing purposes
# dummy_debuff_template = StatusTemplate(
#     status_id="dummy_debuff",
#     is_buff=False,
#     max_stack=1,
#     duration_ms=10000,
#     apply_fn=lambda *args: None,
#     delete_fn=lambda *args: None,
# )

def apply_dummy_debuff(party):
    """Helper function to apply a debuff to the enemy."""
    # debuff = Status(
    #     template=dummy_debuff_template,
    #     source_hero_id=0,
    #     target_hero_ids=[9] # 9 is the enemy ID
    # )
    party.status_manager.active_debuffs[9] = {0: "debuff"}

def test_dayas_diamond_cutter_conditional_damage():
    """Tests that damage increases by 35% only when the enemy has a debuff."""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    party.add_artifact(DayasDiamondCutter(), 0)
    
    party.init_run(None, None)
    party.init_simulation()

    # 1. Get damage without any debuffs
    damage_no_debuff = hero.get_damage(100, DamageType.AutoAttackBasic)

    # 2. Apply a debuff and get damage again
    apply_dummy_debuff(party)
    damage_with_debuff = hero.get_damage(100, DamageType.AutoAttackBasic)

    # 3. Verify that damage increased by 35%
    # The base amplify is 1.0, with debuff it becomes 1.0 + 0.35 = 1.35
    assert damage_with_debuff == pytest.approx(damage_no_debuff * 1.35)
    print("✅ Conditional damage test passed!")

def test_dayas_diamond_cutter_stacking():
    """Tests that the damage bonus stacks when multiple artifacts are equipped."""
    party = Party()
    hero = SimpleHero()
    party.add_hero(hero, 0)
    # Equip two artifacts
    party.add_artifact(DayasDiamondCutter(), 0)
    party.add_artifact(DayasDiamondCutter(), 0)
    
    party.init_run(None, None)
    party.init_simulation()

    # 1. Get damage without any debuffs
    damage_no_debuff = hero.get_damage(100, DamageType.AutoAttackBasic)

    # 2. Apply a debuff and get damage
    apply_dummy_debuff(party)
    damage_with_debuff = hero.get_damage(100, DamageType.AutoAttackBasic)
    
    # 3. Verify that damage increased by 70% (35% from each artifact)
    # Base amplify is 1.0, with two stacking effects it becomes 1.0 + 0.35 + 0.35 = 1.70
    assert damage_with_debuff == pytest.approx(damage_no_debuff * 1.70)
    print("✅ Stacking effect test passed!")

if __name__ == "__main__":
    test_dayas_diamond_cutter_conditional_damage()
    test_dayas_diamond_cutter_stacking()
    print("✅ All DayasDiamondCutter tests passed!") 