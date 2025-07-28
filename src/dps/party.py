from dps.enums import *
from dps.status_manager import StatusManager
from dps.action_manager import ActionManager
from dps.upper_skill_manager import UpperSkillManager
from dps.skill_conditions import CooldownReadyCondition, MovementTriggerCondition

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
        self.next_update = np.full(12, np.inf)       # idx=9:action manager, 10:status manager, 11:upper skill manager

        self.active_indices = [i for i, c in enumerate(self.character_list[:9]) if c is not None]

        # Initialize all heroes first, and set their next update time
        for i in self.active_indices:
            self.character_list[i].init_simulation()
            self.next_update[i] = 0

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

        # Connect movement triggers
        hero_map = {h.get_unique_name(): h for h in self.character_list if h is not None}
        for i, rule in enumerate(self.upper_skill_rules):
            if isinstance(rule, MovementTriggerCondition):
                target_hero = self.character_list[i]
                target_hero.set_upper_skill_rule(rule) # Set rule for the target hero

                trigger_hero_name = rule.trigger_hero_unique_name
                if trigger_hero_name in hero_map:
                    trigger_hero = hero_map[trigger_hero_name]
                    trigger_hero.add_movement_trigger(
                        rule.trigger_movement,
                        i, # target_hero_id
                        rule.delay_min_seconds,
                        rule.delay_max_seconds
                    )
            elif self.character_list[i]: # Set rules for non-trigger heroes
                self.character_list[i].set_upper_skill_rule(rule)
            
        self.status_manager.init_simulation()
        self.action_manager.init_simulation()
        self.upper_skill_manager.init_simulation()
        

    def add_hero(self, hero, idx):
        self.character_list[idx] = hero
        hero.party = self
        hero.party_idx = idx
        hero._setup_status_templates()
        hero._setup_all_movement_actions()

    def add_artifact(self, artifact, hero_idx):
        hero = self.character_list[hero_idx]
        if hero:
            hero.add_artifact(artifact)

    def set_global_upper_skill_lock(self, current_time):
        self.upper_skill_manager.locked_until = current_time + GLOBAL_UPPER_SKILL_LOCK_MS
        self.next_update[11] = self.upper_skill_manager.locked_until

    def is_global_upper_skill_ready(self, current_time):
        return current_time >= self.upper_skill_manager.locked_until

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
            prev_time = 0
            while self.current_time < int(max_t * SEC_TO_MS):
                assert self.current_time >= prev_time, "time paradox!"
                prev_time = self.current_time

                all_min_indices = np.where(self.next_update == self.current_time)[0]

                # --- Step A: Update timers and request skills for all active heroes ---
                for idx in all_min_indices:
                    if idx < 9:
                        hero = self.character_list[idx]
                        hero.update_timers_and_request_skill(self.current_time)

                all_min_indices = np.where(self.next_update == self.current_time)[0]

                # --- Step B: Managers resolve requests and set flags ---
                # Run UpperSkillManager first as it can influence other heroes' actions
                if 11 in all_min_indices:
                    self.upper_skill_manager.resolve_request(self.current_time)
                if 9 in all_min_indices:
                    self.action_manager.resolve_all_actions(self.current_time)
                if 10 in all_min_indices:
                    self.status_manager.resolve_status_reserv(self.current_time)

                all_min_indices = np.where(self.next_update == self.current_time)[0]

                # --- Step C: All active heroes choose and execute their movement ---
                for idx in all_min_indices:
                    if idx < 9:
                        hero = self.character_list[idx]
                        new_t = hero.choose_and_execute_movement(self.current_time)
                        self.next_update[idx] = new_t
                
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