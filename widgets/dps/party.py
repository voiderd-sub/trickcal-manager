from widgets.dps.enums import *
from widgets.dps.buff import BuffManager

import numpy as np
import plotly.graph_objects as go


class Party:
    def __init__(self):
        self.character_list = [None] * 9
        self.buff_manager = BuffManager(self)

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
                cumulative_damage_dict = character.calculate_cumulative_damage(max_t)
                timesteps = cumulative_damage_dict["Timestep"]
                total_dmg = np.zeros_like(timesteps)
                for v in cumulative_damage_dict.values():
                    total_dmg += v
                cumulative_damage_dict["Total"] = total_dmg
                self.simulation_result[character.name] = cumulative_damage_dict
        self.plot_combined()

    def plot_combined(self):
        timesteps = next(iter(self.simulation_result.values()))["Timestep"]

        # 1. 시간에 따른 총 대미지 계산
        total_damage_timeline = sum(
            damage_info["Total"] for damage_info in self.simulation_result.values()
        )

        # 2. 각 캐릭터별 총 대미지와 비율 계산
        total_damage = {
            character_name: damage_info["Total"].sum()
            for character_name, damage_info in self.simulation_result.items()
        }
        overall_total_damage = sum(total_damage.values())
        percentage_damage = {
            name: (damage / overall_total_damage) * 100
            for name, damage in total_damage.items()
        }

        # 3. 각 캐릭터별 절대 대미지와 요소별 대미지 비율 계산
        character_damage_traces = []
        damage_percentage_traces = []
        for character_name, damage_info in self.simulation_result.items():
            # 캐릭터별 총 대미지
            character_damage_traces.append(go.Scatter(
                x=timesteps,
                y=damage_info["Total"],
                mode="lines",
                name=f"{character_name} Total Damage"
            ))

            # 각 캐릭터 요소별 대미지 비율
            damage_keys = [k for k in damage_info.keys() if k not in ["Timestep", "Total"]]
            for key in damage_keys:
                damage_percentage_traces.append(go.Scatter(
                    x=timesteps,
                    y=(damage_info[key] / damage_info["Total"]) * 100,
                    mode="lines",
                    name=f"{character_name} {key} (%)"
                ))

        # Plotly 그래프 생성
        fig = go.Figure()

        # 초기 그래프: 시간에 따른 총 대미지
        fig.add_trace(go.Scatter(
            x=timesteps,
            y=total_damage_timeline,
            mode="lines",
            name="Total Damage Over Time",
            visible=True  # 처음에 표시
        ))

        # 다른 그래프는 초기 상태에서 숨김
        for trace in character_damage_traces + damage_percentage_traces:
            trace.visible = False
            fig.add_trace(trace)

        # 버튼 설정
        fig.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="right",
                    x=0.1,
                    y=1.15,
                    buttons=[
                        dict(
                            label="Total Damage Over Time",
                            method="update",
                            args=[
                                {"visible": [True] + [False] * (len(character_damage_traces) + len(damage_percentage_traces))},
                                {"title": "Total Damage Over Time"}
                            ]
                        ),
                        dict(
                            label="Percentage Damage per Character",
                            method="update",
                            args=[
                                {"visible": [False] + [False] * len(character_damage_traces) + [True] * len(damage_percentage_traces)},
                                {"title": "Percentage Damage per Character"}
                            ]
                        ),
                        dict(
                            label="Character Damage Breakdown (Absolute)",
                            method="update",
                            args=[
                                {"visible": [False] + [True] * len(character_damage_traces) + [False] * len(damage_percentage_traces)},
                                {"title": "Character Damage Breakdown (Absolute)"}
                            ]
                        ),
                        dict(
                            label="Character Damage Breakdown (Percentage)",
                            method="update",
                            args=[
                                {"visible": [False] + [False] * len(character_damage_traces) + [True] * len(damage_percentage_traces)},
                                {"title": "Character Damage Breakdown (Percentage)"}
                            ]
                        ),
                    ]
                )
            ]
        )

        # 레이아웃 설정
        fig.update_layout(
            title="Damage Analysis",
            xaxis_title="Timestep",
            yaxis_title="Damage",
            showlegend=True
        )

        # 그래프 표시
        fig.show()