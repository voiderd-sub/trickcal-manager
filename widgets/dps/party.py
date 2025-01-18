from widgets.dps.enums import *
from widgets.dps.status_manager import StatusManager

from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Party:
    def __init__(self):
        self.character_list = [None] * 9
        self.buff_manager = StatusManager(self)

    def init_simulation(self):
        self.current_time = 0  # 밀리초 단위
        self.simulation_result = dict()
        self.damage_records = []
        self.action_log = []
        self.next_update = self.next_update = np.full(10, np.inf)       # idx=0 for buff manager
        for i in range(9):
            if self.character_list[i] is not None:
                self.character_list[i].init_simulation()
                self.next_update[i] = 0

    def add_hero(self, hero, idx):
        self.character_list[idx] = hero
        hero.party = self
        hero.party_idx = idx

    def get_target_indices(self, target, idx):
        active_flags = sum(1 << i for i in range(9) if self.character_list[i] is not None)

        match target:
            case TargetHero.Self:
                return 1 << idx
            case TargetHero.AllWOSelf:
                return active_flags & ~(1 << idx)
            case TargetHero.All:
                return active_flags
            case _:
                raise ValueError("Unsupported target type")
    
    def get_amplify(self, hero):
        return 0.
    
    def get_additional_coeff(self, hero):
        return 1.

    def run(self, max_t, num_simulation):
        hero_name_to_dmg = defaultdict(lambda: defaultdict(list))
        for _ in range(num_simulation):
            self.init_simulation()
            while self.current_time < int(max_t * MS_IN_SEC):
                all_min_indices = np.where(self.next_update == self.current_time)[0]
                for idx in all_min_indices:
                    if idx == 0:  # BuffManager
                        self.buff_manager.resolve_status_reserv(self.current_time)
                    else:
                        hero = self.character_list[idx]
                        new_t = hero.step(self.current_time)
                        self.next_update[idx] = new_t
                self.current_time = int(self.next_update.min())
            for idx in range(9):
                character = self.character_list[idx]
                if character != None:
                    character.calculate_cumulative_damage(max_t)
                    for dmg_type, value in character.damage_records.items():
                        hero_name_to_dmg[character.name][dmg_type].append(value)
                    # hero_name_to_dmg[character.name]["Total"].append(sum(character.damage_records.values()))
            
        self.plot_boxplot(hero_name_to_dmg["Daya"])
            
    def plot_boxplot(self, data):
        df = pd.DataFrame([
            {"Damage type": key, "value": value} 
            for key, values in data.items() 
            # for key, values in [("Total", data["Total"])]
            for value in values
        ])

        plt.figure(figsize=(8, 6))
        
        # Boxplot 생성
        sns.boxplot(data=df, x="Damage type", y="value", color="skyblue")
        
        # Labeling
        plt.title("Total Damage", fontsize=16)
        plt.xlabel("Damage type", fontsize=14)
        plt.ylabel("", fontsize=14)
        
        # Show the plot
        plt.grid(axis="x", linestyle="--", alpha=0.7)
        plt.show()