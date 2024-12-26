from .enums import *
from .buff import BuffManager
from .step_function import StepFunction
import matplotlib.pyplot as plt

import numpy as np


class Party:
    def __init__(self):
        self.character_list = [None] * 9
        self.buff_manager = BuffManager(self)

    def init_simulation(self):
        self.current_time = 0  # 밀리초 단위
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

    def run(self, max_t):
        self.init_simulation()
        while self.current_time < max_t * MS_IN_SEC:
            all_min_indices = np.where(self.next_update == self.current_time)[0]
            for idx in all_min_indices:
                if idx == 9:  # BuffManager
                    self.buff_manager.apply_buffs(self.current_time)
                    self.next_update[9] = self.buff_manager.buff_heap[0].time if self.buff_manager.buff_heap else np.inf
                else:
                    hero = self.character_list[idx]
                    new_t = hero.step(self.current_time)
                    self.next_update[idx] = new_t
            self.current_time = int(self.next_update.min())
        for idx in range(9):
            character = self.character_list[idx]
            if character != None:
                print("Result of", character)
                print(character.action_log)
                print(character.action_timestamps)
                print(character.damage_records)
                # cumulative_damage_dict = character.calculate_cumulative_damage(max_t+0.5)
                # StepFunction.plot_multiple(*reversed(list(zip(*cumulative_damage_dict.items()))))
                # plt.legend()
                # plt.show()
                                
                