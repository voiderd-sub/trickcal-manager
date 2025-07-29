from dps.spell import Spell
from dps.enums import StatType, DamageType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dps.party import Party

def init_effect_amplify_all_damage(party: 'Party'):
    """
    Initialization effect that increases all damage for the entire party by 100%.
    This is called at the beginning of each simulation.
    """
    for hero in party.character_list:
        if hero:
            hero.add_amplify(DamageType.ALL, 100)

def create_test_spell():
    """
    Creates a test spell with:
    - 5% party-wide attack bonus.
    - 100% all damage amplification init effect.
    """
    return Spell(
        name="Test Spell of Power",
        stat_bonuses={StatType.AttackPhysic: 5},
        init_effect_fn=init_effect_amplify_all_damage
    ) 