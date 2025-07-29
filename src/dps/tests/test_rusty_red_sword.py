import pytest
import pandas as pd
from dps.party import Party
from dps.enums import SEC_TO_MS
from dps.tests.simple_hero import SimpleHero
from dps.artifacts.rusty_red_sword import RustyRedSword
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dps.status import StatusReservation

def test_rusty_red_sword_cycle():
    """
    Tests if the Rusty Red Sword artifact correctly applies its buff
    in a repeating cycle of 6 seconds on, 2 seconds off.
    """
    party = Party()
    hero = SimpleHero("TestHero")
    party.add_hero(hero, 0)

    # Level 1 Rusty Red Sword, set to always be active for testing
    artifact = RustyRedSword(level=1, always_active=True)
    hero.add_artifact(artifact)

    # --- Monkey-patch StatusManager to log buff applications and deletions ---
    status_log = []
    original_add_status = party.status_manager._add_status
    original_delete_status = party.status_manager._delete_status

    def logging_add_status(status: 'StatusReservation', current_time: float):
        print(f"Adding status {status.template.status_id} at time {current_time}")
        status_log.append({
            'time': current_time,
            'event': 'add',
            'status_id': status.template.status_id,
        })
        original_add_status(status, current_time)

    def logging_delete_status(status: 'StatusReservation', current_time: float):
        print(f"Deleting status {status.template.status_id} at time {current_time}")
        status_log.append({
            'time': current_time,
            'event': 'delete',
            'status_id': status.template.status_id,
        })
        original_delete_status(status, current_time)

    party.status_manager._add_status = logging_add_status
    party.status_manager._delete_status = logging_delete_status
    # --- End of Monkey-patch ---

    # Run simulation for a duration that covers several buff cycles
    party.run(max_t=20, num_simulation=1)

    # --- Analysis ---
    df = pd.DataFrame(status_log)
    df['time_sec'] = (df['time'] / SEC_TO_MS).round(1)

    print("\n--- Rusty Red Sword Buff Cycle Test ---")
    print("Status Log:")
    print(df)

    # Filter for the specific buffs from our artifact instance
    aspd_buff_id = artifact.aspd_buff.status_id
    amp_buff_id = artifact.amp_buff.status_id

    aspd_adds = df[(df['status_id'] == aspd_buff_id) & (df['event'] == 'add')]['time_sec'].tolist()
    aspd_deletes = df[(df['status_id'] == aspd_buff_id) & (df['event'] == 'delete')]['time_sec'].tolist()
    
    amp_adds = df[(df['status_id'] == amp_buff_id) & (df['event'] == 'add')]['time_sec'].tolist()
    amp_deletes = df[(df['status_id'] == amp_buff_id) & (df['event'] == 'delete')]['time_sec'].tolist()

    # The buff is applied at t=0, then re-applied 2s after each deletion.
    # Deletion happens after 6s duration. Cycle time is 6s+2s=8s.
    expected_adds = [0.0, 8.0, 16.0]
    expected_deletes = [6.0, 14.0]

    assert aspd_adds == expected_adds, "Attack speed buff application times are incorrect."
    assert aspd_deletes == expected_deletes, "Attack speed buff deletion times are incorrect."
    
    assert amp_adds == expected_adds, "Damage amplify buff application times are incorrect."
    assert amp_deletes == expected_deletes, "Damage amplify buff deletion times are incorrect."
    
    print("\n✅ Rusty Red Sword buff cycle test passed!") 