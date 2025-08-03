import pytest
from dps.party import Party
from dps.heroes.Sylla import Sylla
from dps.artifact import Artifact
from dps.enums import MovementType, MAX_MOTION_TIME

@pytest.fixture
def sylla_party(request):
    """
    Provides a Party instance with a single, configured Sylla hero.
    Exclusive weapon level can be passed as a parameter.
    If ew_level > 0, the exclusive weapon artifact is added to the hero.
    """
    ew_level = request.param if hasattr(request, 'param') else 0
    
    user_info = {
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 1,
        'attack': 100,
    }
    
    sylla_hero = Sylla(user_info)
    
    if ew_level > 0:
        ew_artifact = Artifact("실라의 바람살", level=ew_level)
        sylla_hero.add_artifact(ew_artifact)

    party = Party()
    party.add_hero(sylla_hero, 4)
    return party, sylla_hero

@pytest.mark.parametrize('sylla_party', [0], indirect=True)
def test_sylla_no_ew(sylla_party):
    """
    Tests Sylla without exclusive weapon.
    """
    party, sylla = sylla_party
    party.init_run() # Initialize the party and hero for the run

    assert sylla.motion_time[MovementType.AutoAttackBasic] == 1.0
    
    # In no_ew case, _setup_basic_attack_actions is called inside hero._setup_all_movement_actions
    # which is called when party.add_hero.
    # The actions are stored in _action_templates.
    actions = sylla._action_templates[MovementType.AutoAttackBasic]
    assert len(actions) == 1
    action, _ = actions[0]
    assert action.damage_coeff == 70

@pytest.mark.parametrize('sylla_party', [1], indirect=True)
def test_sylla_ew_l1(sylla_party):
    """
    Tests Sylla with level 1 exclusive weapon.
    The exclusive weapon effect is applied during party.init_run().
    """
    party, sylla = sylla_party
    
    # Before init_run, the ew effect is not applied yet.
    assert sylla.motion_time[MovementType.AutoAttackBasic] == 1.0

    # init_run will detect the exclusive weapon and call setup_exclusive_weapon_effects
    party.init_run()

    # After init_run, the motion time should be updated by _setup_ew_l1
    assert sylla.motion_time[MovementType.AutoAttackBasic] == MAX_MOTION_TIME

    # And the actions should be replaced
    actions = sylla._action_templates[MovementType.AutoAttackBasic]
    assert len(actions) == 2
    
    # Actions are sorted by t_ratio, so we can check them in order.
    action1, _ = actions[0]
    action2, _ = actions[1]
    assert action1.damage_coeff == 80
    assert action2.damage_coeff == 80

@pytest.mark.parametrize('sylla_party', [3], indirect=True)
def test_sylla_ew_l3(sylla_party):
    """
    Tests Sylla with level 3 exclusive weapon.
    """
    party, sylla = sylla_party

    party.init_run()
    party.init_simulation()
    assert sylla.attack_speed_coeff == 1.125


@pytest.mark.parametrize('sylla_party', [3], indirect=True)
def test_sylla_simulation(sylla_party):
    """
    Tests a short simulation with Sylla to ensure it runs without crashing.
    """
    party, _ = sylla_party
    # Use a very short simulation time to just check for crashes
    party.run(max_t=1, num_simulation=1)
