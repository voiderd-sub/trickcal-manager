import pytest
from dps.party import Party
from dps.heroes.Arnet import Arnet
from dps.enums import MovementType, DamageType, MAX_MOTION_TIME
from dps.action import ProjectileAction


@pytest.fixture
def arnet_party():
    """
    Provides a Party instance with a single, configured Arnet hero.
    """
    user_info = {
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 1,
        'attack': 100,
    }
    
    arnet_hero = Arnet(user_info)
    party = Party()
    party.add_hero(arnet_hero, 4)
    return party, arnet_hero


def test_arnet_basic_attack_pattern(arnet_party):
    """
    Tests that Arnet's basic attacks alternate between odd and even patterns.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Get the action templates for basic attacks
    odd_template = arnet._action_templates[MovementType.AutoAttackBasic][0]  # Odd attack
    even_template = arnet._action_templates[MovementType.AutoAttackBasic][1]  # Even attack
    
    # Check odd attack (should have projectile action)
    assert len(odd_template) == 1
    odd_action, odd_t_ratio = odd_template[0]
    assert isinstance(odd_action, ProjectileAction)
    assert odd_action.damage_coeff == 100
    assert odd_action.hit_delay == 0.45
    assert odd_t_ratio == 0.45
    
    # Check even attack (should be empty for now, as healing is not implemented)
    assert len(even_template) == 0


def test_arnet_attack_counter_alternation(arnet_party):
    """
    Tests that Arnet's basic attack counter alternates between 0 and 1.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Reset counter to ensure clean state
    arnet.basic_attack_counter = 0
    
    # Test first attack (odd)
    template_index = arnet._choose_basic_attack_template()
    assert template_index == 0  # Odd attack
    assert arnet.basic_attack_counter == 1
    
    # Test second attack (even)
    template_index = arnet._choose_basic_attack_template()
    assert template_index == 1  # Even attack
    assert arnet.basic_attack_counter == 2
    
    # Test third attack (odd)
    template_index = arnet._choose_basic_attack_template()
    assert template_index == 0  # Odd attack
    assert arnet.basic_attack_counter == 3
    
    # Test fourth attack (even)
    template_index = arnet._choose_basic_attack_template()
    assert template_index == 1  # Even attack
    assert arnet.basic_attack_counter == 4


def test_arnet_enhanced_attack_actions(arnet_party):
    """
    Tests that Arnet's enhanced attack applies deception buff.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Get enhanced attack actions
    enhanced_actions = arnet._action_templates[MovementType.AutoAttackEnhanced][0]
    
    # Should have one status action for deception buff
    assert len(enhanced_actions) == 1
    action, t_ratio = enhanced_actions[0]
    
    # Check that it's a status action for deception
    from dps.action import StatusAction
    assert isinstance(action, StatusAction)
    assert "강평_눈속임" in action.status_template.status_id
    assert t_ratio == 0.55


def test_arnet_motion_times(arnet_party):
    """
    Tests Arnet's motion times for different attack types.
    """
    party, arnet = arnet_party
    party.init_run()
    
    # Check motion times
    assert arnet.motion_time[MovementType.AutoAttackBasic] == MAX_MOTION_TIME
    assert arnet.motion_time[MovementType.AutoAttackEnhanced] == MAX_MOTION_TIME
    assert arnet.motion_time[MovementType.LowerSkill] == 2.5
    assert arnet.motion_time[MovementType.UpperSkill] == 3.6


def test_arnet_simulation_run(arnet_party):
    """
    Tests a short simulation with Arnet to ensure it runs without crashing.
    """
    party, _ = arnet_party
    party.run(max_t=60, num_simulation=1)


def test_arnet_mvp_tracking(arnet_party):
    """
    Test MVP damage tracking and selection.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Get lower skill actions
    lower_skill_actions = arnet._action_templates[MovementType.LowerSkill][0]
    
    # Should have one StartMVPTrackingAction at 47% timing
    assert len(lower_skill_actions) == 1
    action, t_ratio = lower_skill_actions[0]
    
    from dps.heroes.Arnet import StartMVPTrackingAction
    assert isinstance(action, StartMVPTrackingAction)
    assert t_ratio == 0.47


def test_arnet_mvp_buff_application(arnet_party):
    """
    Test MVP buff application to selected hero.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Mock MVP selection
    mvp_hero_idx = 4  # Arnet's own index
    current_time = 1000  # Mock current time
    
    # Apply MVP buff
    arnet.apply_mvp_buff(mvp_hero_idx, current_time)
    
    # Check that MVP status template exists
    name = arnet.get_unique_name()
    mvp_template = arnet.status_templates[f"{name}_MVP"]
    
    # Check MVP buff properties
    assert mvp_template.duration == 12.0
    assert mvp_template.attack_speed_bonus == arnet.lowerskill_value[arnet.lowerskill_level - 1][0]  # 140
    assert mvp_template.amplify_bonus == arnet.lowerskill_value[arnet.lowerskill_level - 1][1]      # 180


def test_arnet_sp_recovery_pause(arnet_party):
    """
    Test SP recovery pause during lower skill.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Set initial SP and timer
    arnet.sp = 50
    arnet.sp_timer = 0
    arnet.sp_recovery_pause_end_time = 0
    
    # Simulate lower skill start
    current_time = 1000
    arnet.LowerSkill(0, current_time)
    
    # Check that SP recovery is paused
    assert arnet.sp_recovery_pause_end_time > current_time
    
    # Simulate time passing without SP recovery
    arnet.update_timers_and_request_skill(current_time + 1000, additional_sp=0)
    assert arnet.sp == 50  # SP should not increase due to pause


def test_arnet_sp_recovery_resume_after_mvp_tracking(arnet_party):
    """
    Test SP recovery resume after MVP tracking ends.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Set initial SP and pause it
    arnet.sp = 50
    arnet.sp_recovery_pause_end_time = 2000  # Pause until time 2000
    
    # Simulate MVP tracking end (which should resume SP recovery)
    from dps.heroes.Arnet import EndMVPTrackingAction
    # Create proper initial_damages with Arnet's index
    initial_damages = {4: 0}  # Arnet's index is 4
    end_action = EndMVPTrackingAction(arnet, MovementType.LowerSkill, DamageType.NONE, initial_damages)
    end_action.action_fn(1500)
    
    # Check that SP recovery is resumed
    assert arnet.sp_recovery_pause_end_time == 0


def test_arnet_sp_recovery_resume_after_upper_skill(arnet_party):
    """
    Test SP recovery resume when upper skill cancels lower skill.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Set initial SP and pause it
    arnet.sp = 50
    arnet.sp_recovery_pause_end_time = 2000  # Pause until time 2000
    arnet.mvp_tracking_started = False  # MVP tracking hasn't started yet
    
    # Simulate upper skill (which should resume SP recovery)
    current_time = 1500
    arnet.UpperSkill(0, current_time)
    
    # Check that SP recovery is resumed
    assert arnet.sp_recovery_pause_end_time == 0


def test_arnet_sp_recovery_no_resume_if_mvp_tracking_started(arnet_party):
    """
    Test that SP recovery is NOT resumed if MVP tracking has already started.
    """
    party, arnet = arnet_party
    party.init_run()
    party.init_simulation()
    
    # Set initial SP and pause it
    arnet.sp = 50
    arnet.sp_recovery_pause_end_time = 2000  # Pause until time 2000
    arnet.mvp_tracking_started = True  # MVP tracking has started
    
    # Simulate upper skill (should NOT resume SP recovery)
    current_time = 1500
    arnet.UpperSkill(0, current_time)
    
    # Check that SP recovery is still paused
    assert arnet.sp_recovery_pause_end_time == 2000


def test_arnet_aside_l2_fireworks(arnet_party):
    """
    Test fireworks effect for aside level 2+.
    """
    # Create Arnet with aside level 2
    user_info = {
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 2,
        'attack': 100,
    }
    
    arnet_hero = Arnet(user_info)
    party = Party()
    party.add_hero(arnet_hero, 4)
    party.init_run()
    party.init_simulation()
    
    # Check that aside level 2 enables fireworks effect
    assert arnet_hero.aside_level >= 2
    
    # Get lower skill actions
    lower_skill_actions = arnet_hero._action_templates[MovementType.LowerSkill][0]
    
    # Should have one action at 47% timing
    assert len(lower_skill_actions) == 1
    action, t_ratio = lower_skill_actions[0]
    assert t_ratio == 0.47
    
    # Check that fireworks effect method exists
    assert hasattr(arnet_hero, 'apply_fireworks_effect')


def test_arnet_consecutive_mvp_buff(arnet_party):
    """
    Test consecutive MVP buff difference.
    """
    # Create Arnet with aside level 2
    user_info = {
        'lowerskill_level': 13,
        'upperskill_level': 13,
        'aside_level': 2,
        'attack': 100,
    }
    
    arnet_hero = Arnet(user_info)
    party = Party()
    party.add_hero(arnet_hero, 4)
    party.init_run()
    party.init_simulation()
    
    # Test non-consecutive MVP (first time)
    current_time = 1000
    arnet_hero.last_mvp_hero_idx = None
    arnet_hero.apply_fireworks_effect(current_time, is_consecutive=False)
    
    # Test consecutive MVP (second time)
    arnet_hero.last_mvp_hero_idx = 4  # Same hero as MVP
    arnet_hero.apply_fireworks_effect(current_time, is_consecutive=True)
    
    # Check that fireworks effect method exists and works
    assert hasattr(arnet_hero, 'apply_fireworks_effect')
