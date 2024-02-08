from widgets.ui.page_equip_abstract import Ui_page_equip_abstract
from widgets.wrapper.resource_manager import ResourceManager
from widgets.wrapper.misc import FlowLayout

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from collections import defaultdict


class PageEquipAbstract(QWidget, Ui_page_equip_abstract):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        for name_kr, name_en in self.window().resource.masterGet("Stat").values():
            pixmap = QPixmap()
            pixmap.load(f"icon/status/Icon_{name_en}.png")
            
            label: QLabel = getattr(self, f"icon{name_en}")
            label.setPixmap(pixmap)
        
        self.updateEquipStatAbstract()
        self.containerAll_2.setStyleSheet("background-color: white; border-radius: 8px;")

        self.vertical_layout = QVBoxLayout(self.scroll_container)
        self.vertical_layout.setContentsMargins(10, 10, 10, 10)
        self.vertical_layout.setSpacing(10)
        self.goal_list.currentIndexChanged.connect(self.updateEquipState)
        self.updateGoalList()


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
        all_cnt = len(hero_id_to_rank_stat_type) * max_rank * 2
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


    def reloadAll(self):
        self.updateEquipStatAbstract()
        self.updateEquipState()
    

    def updateGoalList(self):
        goal_list = self.window().resource.userGet("GoalList")
        self.goal_list.blockSignals(True)
        self.goal_list.clear()
        self.goal_list.blockSignals(False)
        self.goal_list.addItems(["현재 랭크"] + goal_list)
    

    def updateEquipState(self):
        if self.goal_list.currentIndex() == 0:
            self.goal_rate_label_left.hide()
            self.goal_rate_label_right.hide()
        else:
            self.goal_rate_label_left.show()
            self.goal_rate_label_right.show()
        
        res = self.window().resource
        max_rank = res.masterGet("MaxRank")
        user_equip = res.userGet("CurEquip")
        hero_id_to_metadata = res.masterGet("HeroIdToMetadata")

        # Treat MAX (=max_rank +1) as max_rank
        rank_to_hero_list = {idx: [] for idx in range(max_rank+1)}
        if self.goal_list.currentIndex() == 0:
            for hero_id in hero_id_to_metadata.keys():
                rank, equips = user_equip.get(hero_id, (1, set()))
                if rank > max_rank:
                    rank = max_rank
                    equips = {1, 2, 3, 4, 5, 6}
                rank_to_hero_list[rank].append((hero_id, equips))
        else:
            goal_idx = self.goal_list.currentIndex()
            cur = self.window().conn_user.cursor()
            cur.execute("SELECT hero_id, rank, equips FROM user_goal_equip WHERE goal_id = ?", (goal_idx,))
            for hero_id, rank, equips in cur:
                if equips is not None:
                    equips = set(map(int, equips.split(",")))
                else:
                    equips = set()
                if rank > max_rank:
                    rank = max_rank
                    equips = {1, 2, 3, 4, 5, 6}
                cur_rank, cur_equips = user_equip.get(hero_id, (1, set()))
                if (self.check_show_completed.isChecked() is False and
                    (cur_rank > rank or (cur_rank == rank and cur_equips & equips == equips))):
                    continue
                rank_to_hero_list[rank].append((hero_id, equips))
            
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

            hero_list = rank_to_hero_list[rank]
            rank_container = QWidget(row_container)
            rank_container.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred))
            # layout = QHBoxLayout(rank_container)
            layout = FlowLayout(rank_container, 0)
            for hero_id, equips in hero_list:
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

                label = QLabel(metadata["name_kr"], hero_container)
                label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                label.setFixedWidth(80)
                label.setWordWrap(True)
                hero_container_layout.addWidget(label)

                layout.addWidget(hero_container)


            horizontal_layout.addWidget(rank_container)
            self.vertical_layout.addWidget(row_container)
