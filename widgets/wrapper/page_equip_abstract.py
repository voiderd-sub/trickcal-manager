from widgets.ui.page_equip_abstract import Ui_page_equip_abstract
from widgets.wrapper.resource_manager import ResourceManager
from widgets.wrapper.misc import FlowLayout

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt

from collections import defaultdict


class PageEquipAbstract(QWidget, Ui_page_equip_abstract):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        self.reload = {"account": True}

        for name_kr, name_en in self.window().resource.masterGet("Stat").values():
            pixmap = QPixmap()
            pixmap.load(f"icon/status/Icon_{name_en}.png")
            
            label: QLabel = getattr(self, f"icon{name_en}")
            label.setPixmap(pixmap)
        
        self.containerAll_2.setStyleSheet("background-color: white; border-radius: 8px;")

        self.vertical_layout = QVBoxLayout(self.scroll_container)
        self.vertical_layout.setContentsMargins(10, 10, 10, 10)
        self.vertical_layout.setSpacing(10)
        self.goal_list.currentIndexChanged.connect(self.updateEquipState)
        self.check_show_completed.stateChanged.connect(self.showModeChanged)
        self.radio_equip_show.toggled.connect(self.updateEquipState)
        # self.updateGoalList()
        # self.updateEquipState()


    def updateEquipStatAbstract(self):
        # load current equip state
        res: ResourceManager = self.window().resource
        user_equip = res.userGet("CurEquip")
        rank_stat_type = res.masterGet("RankStatType")
        hero_id_to_rank_stat_type = res.masterGet("HeroIdToRankStatType")
        max_rank = res.masterGet("MaxRank")
        stat = res.masterGet("Stat")

        cur_stats = defaultdict(int)
        all_stats = defaultdict(int)
        cur_cnt = 0
        all_cnt = len(hero_id_to_rank_stat_type) * (max_rank-1) * 2
        for hero_id in hero_id_to_rank_stat_type.keys():
            hero_rank = user_equip[hero_id][0]
            stat_type = hero_id_to_rank_stat_type[hero_id]
            for rank_idx in range(1, max_rank+1):
                for stat_id, value in rank_stat_type[stat_type][rank_idx].items():
                    all_stats[stat_id] += value
                    if rank_idx <= hero_rank:
                        cur_stats[stat_id] += value
                        cur_cnt += 1
        
        for id, (name_kr, name_en) in stat.items():
            if cur_stats[id] == all_stats[id]:
                ratio = "완료!"
            else:
                ratio = f"{cur_stats[id] * 100 / all_stats[id] if all_stats[id] != 0 else 0:.1f}%"            
            text = f"{cur_stats[id]} / {all_stats[id]}"
            getattr(self, f"stat{name_en}").setText(text)
            getattr(self, f"rate{name_en}").setText(f"({ratio})")
        
        self.rateAll.setText(f"{cur_cnt * 100 / all_cnt:.1f}%")
    

    def updateGoalList(self):
        goal_list = list(name for (name, type) in self.window().resource.userGet("GoalIdToName").values())
        self.goal_list.blockSignals(True)
        self.goal_list.clear()
        self.goal_list.addItems(["현재 랭크"] + goal_list)
        self.goal_list.blockSignals(False)
    

    def updateEquipState(self):
        no_goal = self.goal_list.currentIndex() == 0
        if no_goal:
            self.goal_rate_label_left.hide()
            self.goal_rate_label_right.hide()
        else:
            self.goal_rate_label_left.show()
            self.goal_rate_label_right.show()
        
        res: ResourceManager = self.window().resource
        max_rank = res.masterGet("MaxRank")
        user_equip = res.userGet("CurEquip")
        hero_id_to_metadata = res.masterGet("HeroIdToMetadata")
        hero_id_to_name_order = res.masterGet("HeroIdToNameOrder")

        # Treat MAX (=max_rank +1) as max_rank
        rank_to_hero_dict = {idx: dict() for idx in range(max_rank+1)}
        if not no_goal:
            cnt_tot = 0
            cnt_complete = 0
            goal_idx = self.goal_list.currentIndex()
            goal_equip = res.userGet("GoalEquip")[goal_idx]

        for hero_id in hero_id_to_metadata.keys():
            cur_rank, cur_equips = user_equip.get(hero_id, (1, set()))
            if cur_rank > max_rank:
                cur_rank = max_rank
                cur_equips = set(range(1,7))
            if no_goal:
                rank_to_hero_dict[cur_rank][hero_id] = (f"{len(cur_equips)}/6", False)
            else:
                goal_rank, goal_equips = goal_equip.get(hero_id, (1, set()))
                cnt_tot += (goal_rank-1) * 6 + len(goal_equips)
                if goal_rank > max_rank:
                    goal_rank = max_rank
                    goal_equips = set(range(1,7))
                completed = cur_rank > goal_rank or (cur_rank == goal_rank and cur_equips & goal_equips == goal_equips)
                not_compl_same_rank = not completed and cur_rank == goal_rank
                equip_complete_numerator = (len(cur_equips & goal_equips)
                                            if not_compl_same_rank
                                            else len(cur_equips))
                equip_complete_denominator = len(goal_equips) if not_compl_same_rank else 6
                if completed:
                    cnt_complete += (goal_rank-1) * 6 + len(goal_equips)
                else:
                    cnt_complete += (cur_rank-1) * 6 + (
                        len(cur_equips & goal_equips) if cur_rank == goal_rank else len(cur_equips))
                ratio_text = f"{equip_complete_numerator}/{equip_complete_denominator}"
                rank_to_hero_dict[goal_rank][hero_id] = (ratio_text, completed)

        if not no_goal:
            if cnt_tot == 0:
                self.goal_rate_label_right.setText("목표 없음")
            else:
                self.goal_rate_label_right.setText(f"{cnt_complete * 100 / cnt_tot:.1f}%")
            
        # clear all widgets in self.contents_layout
        for i in reversed(range(self.vertical_layout.count())):
            self.vertical_layout.itemAt(i).widget().deleteLater()

        for rank in range(max_rank, 0, -1):
            # Make container for each rank
            row_container = QWidget(self.scroll_container)
            color = "#f8f8f8" if rank % 2 == 0 else "#e8e8e8"
            row_container.setStyleSheet(f"background-color: {color}; border-radius: 20px;")
            horizontal_layout = QHBoxLayout(row_container)

            # rank label
            label = QLabel(f"Rank {rank}", row_container)
            font = label.font()
            font.setPointSize(15)
            label.setFont(font)
            horizontal_layout.addWidget(label)

            hero_dict = rank_to_hero_dict[rank]
            rank_container = QWidget(row_container)
            rank_container.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred))
            layout = FlowLayout(rank_container, 0)
            for hero_id, (ratio_text, completed) in sorted(hero_dict.items(), key=lambda x: hero_id_to_name_order[x[0]]):
                if completed and not self.check_show_completed.isChecked():
                    continue
                metadata = hero_id_to_metadata[hero_id]

                hero_container = QWidget(rank_container)
                hero_container.setFixedWidth(80)
                hero_container.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))
                hero_container_layout = QVBoxLayout(hero_container)
                hero_container_layout.setContentsMargins(0, 0, 0, 0)
                hero_container_layout.setSpacing(5)

                pixmap = QPixmap()
                pixmap.load(f"icon/hero/{metadata['name_en']}.png")
                pixmap = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)

                label = QLabel()
                label.setFixedSize(80, 80)
                label.setPixmap(pixmap)
                label.setScaledContents(True)
                hero_container_layout.addWidget(label)
                label.setStyleSheet("border: 1px solid black; border-radius: 0px;")

                text = metadata["name_kr"]
                label = QLabel(text, hero_container)
                label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                label.setFixedWidth(80)
                label.setWordWrap(True)
                hero_container_layout.addWidget(label)

                text = []
                if not no_goal or self.radio_equip_show.isChecked():
                    label = QLabel(hero_container)
                    if not no_goal:
                        cur_rank = min(user_equip[hero_id][0], max_rank)
                        text.append(f"{cur_rank}")
                    if self.radio_equip_show.isChecked():
                        text.append(f"{ratio_text}")
                    text = " - ".join(text)
                    label.setText(text)
                    label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                    label.setFixedWidth(80)
                    label.setWordWrap(True)
                    font = label.font()
                    font.setPointSize(11)
                    label.setFont(font)
                    hero_container_layout.addWidget(label)
                layout.addWidget(hero_container)

            horizontal_layout.addWidget(rank_container)
            self.vertical_layout.addWidget(row_container)


    def showModeChanged(self):
        if self.goal_list.currentIndex() != 0:
            self.updateEquipState()
    

    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        if self.reload.get("goal", False) or self.reload.get("account", False):
            self.updateGoalList()
        
        self.updateEquipStatAbstract()
        self.updateEquipState()
        self.reload = dict()