from dps.enums import *
from dps.status_manager import StatusManager
from dps.action_manager import ActionManager
from dps.upper_skill_manager import UpperSkillManager
from dps.skill_conditions import CooldownReadyCondition

import numpy as np
import pandas as pd

from tqdm import tqdm


class Party:
    def __init__(self):
        self.character_list = [None] * 12    # idx=9 : action manager, idx=10 : status manager, idx=11 : upper skill manager
        self.action_manager = ActionManager(self)
        self.status_manager = StatusManager(self)
        self.upper_skill_manager = UpperSkillManager(self)


    def init_simulation(self, priority, rules):
        self.current_time = 0  # ms
        self.simulation_result = dict()
        self.damage_records = []
        self.movement_log = []

        self.active_indices = [i for i, c in enumerate(self.character_list[:9]) if c is not None]
        # Set priorities and rules
        self.upper_skill_priorities = [10] * 9
        if priority:
            for i, p in enumerate(priority):
                if self.character_list[i] is not None:
                    self.upper_skill_priorities[i] = p
        
        self.upper_skill_rules = [None] * 9
        if rules:
            self.upper_skill_rules = rules
        else:
            self.upper_skill_rules = [CooldownReadyCondition() if c else None for c in self.character_list[:9]]

        self.next_update = np.full(12, np.inf)       # idx=9:action manager, 10:status manager, 11:upper skill manager
        for i in self.active_indices:
            self.character_list[i].init_simulation()
            self.character_list[i].set_upper_skill_rule(self.upper_skill_rules[i])
            self.next_update[i] = 0
            
        self.status_manager.init_simulation()
        self.action_manager.init_simulation()
        self.upper_skill_manager.init_simulation()
        

    def add_hero(self, hero, idx):
        self.character_list[idx] = hero
        hero.party = self
        hero.party_idx = idx

    def get_amplify(self, hero):
        # TODO : NEED TO REVISE
        return 0.
    
    def get_additional_coeff(self, hero):
        # TODO : NEED TO REVISE
        return 1.

    def run(self, max_t, num_simulation, priority=None, rules=None):
        rows = []
        import time
        for _ in tqdm(range(num_simulation)):
            self.init_simulation(priority, rules)
            while self.current_time < int(max_t * SEC_TO_MS):
                all_min_indices = np.where(self.next_update == self.current_time)[0]

                print("party.current_time", self.current_time, all_min_indices)
    
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
                    elif idx == 10:
                        self.status_manager.resolve_status_reserv(self.current_time)
                    else: # 11
                        self.upper_skill_manager.resolve_request(self.current_time)
                
                # Go to next timestep
                self.current_time = int(self.next_update.min())
        return
        #     # Simulation terminated; extract results
        #     for idx in range(9):
        #         character = self.character_list[idx]
        #         if character != None:
        #             name = character.get_unique_name()
        #             print(name, character.damage_records)
        #             character.calculate_cumulative_damage(max_t)

        #             total_dmg = 0
        #             for dmg_type, value in character.damage_records.items():
        #                 rows.append({
        #                     "name": name,
        #                     "dmg_type": dmg_type,
        #                     "dmg": value
        #                 })
        #                 total_dmg += value
        #             rows.append({
        #                 "name": name,
        #                 "dmg_type": "Total",
        #                 "dmg": total_dmg
        #             })
        # df = pd.DataFrame(rows)
            
        # return df