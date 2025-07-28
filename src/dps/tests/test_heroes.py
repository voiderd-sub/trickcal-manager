import pytest
from dps.party import Party
from dps.heroes.Epica import Epica

@pytest.fixture
def epica_party():
    """
    Provides a Party instance with a single, configured Epica hero.
    """
    user_info = {
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 3,
        'attack': 100,
    }
    
    epica_hero = Epica(user_info)
    party = Party()
    party.add_hero(epica_hero, 4)
    return party

def test_epica_simulation(epica_party):
    """
    Tests a 4-minute simulation with Epica to ensure it runs without crashing.
    """
    try:
        # Simulate for 4 minutes (240,000 ms)
        epica_party.run(max_t=240, num_simulation=1)
        # print log
        print("Epica simulation result:")
        epica = epica_party.character_list[4]
        print(epica.movement_timestamps)
        print(epica.damage_records)
        # get damage time per movement
        for movement_type, actions in epica.movement_timestamps.items():
            total_actions = len(actions)
            total_damage_timestamps = len(epica.damage_records[movement_type])
            print(f"{movement_type}: {total_actions} actions, {total_damage_timestamps} damage timestamps")
    except Exception as e:
        pytest.fail(f"Epica simulation failed with an exception: {e}") 