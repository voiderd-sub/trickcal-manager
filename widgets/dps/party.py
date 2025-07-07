from widgets.dps.enums import *
from widgets.dps.status_manager import StatusManager
from widgets.dps.action_manager import ActionManager
from widgets.dps.event import *

import numpy as np
import pandas as pd
import heapq

from tqdm import tqdm


class Party:
    def __init__(self):
        self.character_list = [None] * 11    # idx=9 : action manager, idx=10 : status manager
        self.action_manager = ActionManager(self)
        self.status_manager = StatusManager(self)


    def init_simulation(self):
        self.current_time = 0  # ms
        self.simulation_result = dict()
        self.damage_records = []
        self.movement_log = []
        self.active_indices = [i for i, c in enumerate(self.character_list) if c is not None]
        self.next_update = np.full(11, np.inf)       # idx=9 : action manager, idx=10 : status manager
        for i in range(9):
            if self.character_list[i] is not None:
                self.character_list[i].init_simulation()
                self.next_update[i] = 0
        self.upper_skill_cooldown = [np.inf] * 9
        self.upper_skill_lock_until = 0
        self.status_manager.init_simulation()
        self.action_manager.init_simulation()
        

    def add_hero(self, hero, idx):
        self.character_list[idx] = hero
        hero.party = self
        hero.party_idx = idx

    def get_target_indices(self, target, idx):
        match target:
            case TargetHero.Self:
                return [idx]
            case TargetHero.AllWOSelf:
                return [i for i in self.active_indices if i != idx]
            case TargetHero.All:
                return self.active_indices
            case _:
                raise ValueError("Unsupported target type")

    def get_amplify(self, hero):
        # TODO : NEED TO REVISE
        return 0.
    
    def get_additional_coeff(self, hero):
        # TODO : NEED TO REVISE
        return 1.

    def run(self, max_t, num_simulation):
        rows = []
        for _ in tqdm(range(num_simulation)):
            self.init_simulation()
            while self.current_time < int(max_t * SEC_TO_MS):
                all_min_indices = np.where(self.next_update == self.current_time)[0]

                # TODO : Use Upper skill

                
                for idx in all_min_indices:
                    if idx < 9:
                        # Add actions into action queue
                        hero = self.character_list[idx]
                        new_t = hero.step(self.current_time)
                        self.next_update[idx] = new_t
                    elif idx == 9:
                        # Resolve actions; this includes damage and buff/debuff reservations.
                        self.action_manager.resolve_all_actions(self.current_time)
                    else:
                        self.status_manager.resolve_status_reserv(self.current_time)
                
                # Go to next timestep
                self.current_time = int(self.next_update.min())

            # Simulation terminated; extract results
            for idx in range(9):
                character = self.character_list[idx]
                if character != None:
                    name = character.get_name() + "_" + str(idx)
                    character.calculate_cumulative_damage(max_t)
                    total_dmg = 0
                    for dmg_type, value in character.damage_records.items():
                        rows.append({
                            "name": name,
                            "dmg_type": dmg_type,
                            "dmg": value
                        })
                        total_dmg += value
                    rows.append({
                        "name": name,
                        "dmg_type": "Total",
                        "dmg": total_dmg
                    })
        df = pd.DataFrame(rows)
            
        return df