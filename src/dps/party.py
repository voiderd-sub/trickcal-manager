from dps.enums import *
from dps.status_manager import StatusManager
from dps.action_manager import ActionManager
from dps.upper_skill_manager import UpperSkillManager
from dps.skill_conditions import CooldownReadyCondition, MovementTriggerCondition
from dps.spell import Spell

import numpy as np
import pandas as pd

from tqdm import tqdm


class Party:
    def __init__(self):
        self.character_list = [None] * 12    # idx=9 : action manager, idx=10 : status manager, idx=11 : upper skill manager
        self.action_manager = ActionManager(self)
        self.status_manager = StatusManager(self)
        self.upper_skill_manager = UpperSkillManager(self)
        self.spells = []
        self.applied_spell_effects = set()


    def init_run(self, priority=None, rules=None):
        """Initializes settings that are constant for the entire run."""
        self.active_indices = [i for i, c in enumerate(self.character_list[:9]) if c is not None]
        self.applied_spell_effects = set()

        # 1. Initialize hero base settings for the run.
        for i in self.active_indices:
            self.character_list[i].init_run()

        # 2. Apply party-wide one-time setup effects from spells, checking for stackability.
        for spell in self.spells:
            if spell.setup_effect_fn:
                effect_key = spell.setup_effect_fn.__name__
                if not spell.stackable:
                    if effect_key in self.applied_spell_effects:
                        continue # Skip already-applied non-stackable setup effect
                    self.applied_spell_effects.add(effect_key)
                spell.apply_setup_effect(self)

        # 3. Set priorities and rules for the run.
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

        # 4. Connect movement triggers
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


    def init_simulation(self):
        """Initializes/resets the state for a single simulation."""
        self.current_time = 0  # ms
        self.simulation_result = dict()
        self.damage_records = []
        self.movement_log = []
        self.next_update = np.full(12, np.inf)

        # 1. Initialize/reset hero state for the simulation.
        for i in self.active_indices:
            self.character_list[i].init_simulation()
            self.next_update[i] = 0
        
        # 2. Apply party-wide stat bonuses from spells for this simulation.
        for spell in self.spells:
            spell.apply_stats(self)

        # 3. Initialize/reset managers for the simulation.
        self.status_manager.init_simulation()
        self.action_manager.init_simulation()
        self.upper_skill_manager.init_simulation()

        # 4. Apply artifact initialization effects for all heroes
        applied_artifact_init_effects_this_sim = set()
        for i in self.active_indices:
            hero = self.character_list[i]
            for artifact in hero.artifacts:
                if artifact.init_effect_fn:
                    effect_key = (hero.party_idx, artifact.init_effect_fn.__name__)
                    if not artifact.stackable:
                        if effect_key in applied_artifact_init_effects_this_sim:
                            continue
                        applied_artifact_init_effects_this_sim.add(effect_key)
                    artifact.apply_init_effect(hero)
        
        # 5. Apply party-wide initialization effects from spells for this simulation, checking for stackability.
        applied_spell_init_effects_this_sim = set()
        for spell in self.spells:
            if spell.init_effect_fn:
                effect_key = spell.init_effect_fn.__name__
                if not spell.stackable:
                    if effect_key in applied_spell_init_effects_this_sim:
                        continue # Skip already-applied non-stackable init effect
                    applied_spell_init_effects_this_sim.add(effect_key)
                spell.apply_init_effect(self)
        

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

    def add_spell(self, spell: Spell):
        self.spells.append(spell)

    def set_global_upper_skill_lock(self, current_time):
        self.upper_skill_manager.locked_until = current_time + GLOBAL_UPPER_SKILL_LOCK_MS
        self.next_update[11] = self.upper_skill_manager.locked_until

    def is_global_upper_skill_ready(self, current_time):
        return current_time >= self.upper_skill_manager.locked_until

    def get_amplify(self, hero):
        # NOT FOR HERO. (this is the function that calculates enemy-wise amplify)
        return 0.
    
    def get_additional_coeff(self, hero):
        # TODO : NEED TO REVISE
        return 1.

    def run(self, max_t, num_simulation, priority=None, rules=None):
        self.init_run(priority, rules)
        
        for _ in tqdm(range(num_simulation)):
            self.init_simulation()
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