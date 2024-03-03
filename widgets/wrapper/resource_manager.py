from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QMovie

from collections import defaultdict
import sqlite3
import pandas as pd
import numpy as np

class ResourceManager:
    def __init__(self, main):
        self.main = main
        self._resourceMaster = dict()
        self._resourceUser = dict()

        self.masterInit()

    def userGet(self, resource_name):
        if resource_name in self._resourceUser:
            return self._resourceUser[resource_name]
        else:
            return getattr(self, f"get{resource_name}")()

    def masterGet(self, resource_name):
        return self._resourceMaster[resource_name]

    def delete(self, resource_name):
        if resource_name in self._resourceUser:
            del self._resourceUser[resource_name]
        elif resource_name in self._resourceMaster:
            del self._resourceMaster[resource_name]
    
    def deleteAll(self, user=False, master=False):
        if user:
            self._resourceUser.clear()
        if master:
            self._resourceMaster.clear()

    
    def getHeroIdToStarExtrinsic(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT hero_id, star_extrinsic FROM user_hero")
        star_extrinsic = {idx: star for (idx, star) in cur_user}
        self._resourceUser["HeroIdToStarExtrinsic"] = star_extrinsic
        return star_extrinsic
        

    def getCurEquip(self):
        user_equip = dict()

        cur_master = self.main.conn_master.cursor()
        cur_master.execute("SELECT max(_rowid_) FROM hero")
        max_hero_id = cur_master.fetchone()[0]

        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_cur_equip")
        for (idx, rank, equips) in cur_user:
            user_equip[idx] = (rank, set((int(i) for i in equips.split(",")))
                                if equips is not None else set())
        
        for i in range(1, max_hero_id+1):
            if i not in user_equip:
                user_equip[i] = (1, set())
        
        self._resourceUser["CurEquip"] = user_equip
        return user_equip
    

    def getGoalList(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT name FROM user_goal_equip_names order by id asc;")
        goal_list = [name for (name,) in cur_user]
        self._resourceUser["goal_list"] = goal_list
        return goal_list
    

    def getGoalEquip(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_goal_equip")
        goal_equip = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
        for (goal_id, hero_id, rank, equips) in cur_user:
            goal_equip[goal_id][hero_id] = (rank, set((int(i) for i in equips.split(","))) if equips is not None else set())
        self._resourceUser["GoalEquip"] = goal_equip
        return goal_equip
    

    def getCalcSettings(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM calc_settings")
        calc_settings = {name: value for (name, value) in cur_user}
        self._resourceUser["CalcSettings"] = calc_settings
        return calc_settings
    

    def getBagEquips(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_bag_equips")
        bag_equips = {id: count for (id, count) in cur_user}
        self._resourceUser["BagEquips"] = bag_equips
        return bag_equips
    
    # user_items means "materials"
    def getUserItems(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_items")
        user_items = {name: count for (name, count) in cur_user}
        self._resourceUser["UserItems"] = user_items
        return user_items
    

    def masterInit(self):
        cur = self.main.conn_master.cursor()

        # MaxRank
        cur.execute("SELECT MAX(rank) FROM equipment")
        max_rank = cur.fetchone()[0]
        self._resourceMaster["MaxRank"] = max_rank

        # HeroNameToId, HeroIdToMetadata
        hero_name_to_id = dict()
        hero_id_to_metadata = dict()
        meta_names = ["name_kr", "name_en", "star_in", "attack_type", "pos", "class", "personality", "race"]
        cur.execute("SELECT * FROM hero") # idx, name_kr, name_en, star_in, attack_type, pos, class, personality, race
        for data in cur:
            idx = data[0]
            hero_name_to_id[data[1]] = idx
            hero_id_to_metadata[idx] = dict()
            for meta_name, meta_val in zip(meta_names, data[1:]):
                hero_id_to_metadata[idx][meta_name] = meta_val

        self._resourceMaster["HeroNameToId"] = hero_name_to_id
        self._resourceMaster["HeroIdToMetadata"] = hero_id_to_metadata


        # HeroIdToEquipNames, HeroIdToEquipIds, HeroNameToEquipNames
        hero_id_to_equip_names = defaultdict(lambda: defaultdict(list))
        hero_id_to_equip_ids = defaultdict(lambda: defaultdict(list))
        hero_name_to_equip_names = defaultdict(lambda: defaultdict(list))
        cur.execute("""SELECT h.id, h.name_kr, he.rank, e.id, e.name
                        FROM hero h
                        JOIN hero_equip he ON (h.id = he.hero_id)
                        JOIN equipment e ON (he.equipment_id = e.id)
                        ORDER BY he.rank ASC, e.id ASC
                    """)
        for (hero_id, hero_name_kr, rank, equip_id, equip_name) in cur:
            hero_id_to_equip_names[hero_id][rank].append(equip_name)
            hero_id_to_equip_ids[hero_id][rank].append(equip_id)
            hero_name_to_equip_names[hero_name_kr][rank].append(equip_name)
        self._resourceMaster["HeroIdToEquipNames"] = hero_id_to_equip_names
        self._resourceMaster["HeroIdToEquipIds"] = hero_id_to_equip_ids
        self._resourceMaster["HeroNameToEquipNames"] = hero_name_to_equip_names

        # EquipIdToName, EquipNameToId, EquipDefaultOrder
        equip_id_to_rank_n_type = dict()
        equip_id_to_name = dict()
        equip_name_to_id = dict()
        equip_default_order = dict()
        equip_name_default_order = list()
        cur.execute("SELECT id, name, rank, type FROM equipment ORDER BY rank ASC, type ASC, name ASC")
        for (id, name, rank, type) in cur:
            equip_id_to_rank_n_type[id] = (rank, type)
            equip_id_to_name[id] = name
            equip_name_to_id[name] = id
            equip_default_order[id] = len(equip_default_order) + 1
            equip_name_default_order.append(name)
        self._resourceMaster["EquipIdToRankAndType"] = equip_id_to_rank_n_type
        self._resourceMaster["EquipIdToName"] = equip_id_to_name
        self._resourceMaster["EquipNameToId"] = equip_name_to_id
        self._resourceMaster["EquipDefaultOrder"] = equip_default_order
        self._resourceMaster["EquipNameDefaultOrder"] = equip_name_default_order

        # Recipe
        cur.execute("SELECT * from equipment_recipe")
        recipe = defaultdict(lambda: defaultdict(int))
        for row in cur:
            rank, type = row[:2]
            for i in range(2, len(row), 2):
                name, count = row[i], row[i+1]
                if name is None:
                    continue
                recipe[(rank, type)][name] = count
        self._resourceMaster["Recipe"] = recipe

        # RankToStandard
        cur.execute("SELECT rank, standard FROM rank_standard")
        rank_to_standard = {rank: standard for (rank, standard) in cur}
        self._resourceMaster["RankToStandard"] = rank_to_standard

        # RankStatType
        cur.execute("SELECT id, rank, stat_1_id, stat_1_value, stat_2_id, stat_2_value FROM rank_stat_type")
        rank_stat_type = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for (id, rank, stat_1_id, stat_1_value, stat_2_id, stat_2_value) in cur:
            rank_stat_type[id][rank][stat_1_id] = stat_1_value
            rank_stat_type[id][rank][stat_2_id] = stat_2_value
        self._resourceMaster["RankStatType"] = rank_stat_type

        # HeroIdToRankStatType
        cur.execute("SELECT hero_id, rank_stat_type FROM hero_rank_stat_type")
        hero_rank_stat_type = {hero_id: stat_type for (hero_id, stat_type) in cur}
        self._resourceMaster["HeroIdToRankStatType"] = hero_rank_stat_type

        # Stat
        cur.execute("SELECT * FROM stat")
        stat = {id: (name_kr, name_en) for (id, name_kr, name_en) in cur}
        self._resourceMaster["Stat"] = stat

        # StageToDrop
        cur.execute("SELECT * FROM drop_table")
        stage_to_drop = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for (stage, item_1, item_1_drop_rate, item_2, item_2_drop_rate) in cur:
            stage_to_drop[stage][item_1] = item_1_drop_rate
            stage_to_drop[stage][item_2] = item_2_drop_rate
            stage_to_drop[stage].pop(None, None)
        self._resourceMaster["StageToDrop"] = stage_to_drop

        # HeroDefaultOrder
        hero_default_order = list()
        cur.execute("SELECT id FROM hero ORDER BY personality ASC, star_intrinsic DESC, name_kr ASC")
        for (idx,) in cur:
            hero_default_order.append(idx)
        self._resourceMaster["HeroDefaultOrder"] = hero_default_order

        # HeroIdToNameOrder
        hero_name_order = dict()
        cur.execute("SELECT id FROM hero ORDER BY name_kr ASC")
        for (idx,) in cur:
            hero_name_order[idx] = len(hero_name_order) + 1
        self._resourceMaster["HeroIdToNameOrder"] = hero_name_order
    

    def updateDropTable(self):
        path_item_table = self.main.config["path_item_table"]
        url=f'https://docs.google.com/spreadsheet/ccc?key={path_item_table}&output=xlsx'

        # make dict of drop item list
        drop_item_list = dict()
        stage_to_drop = dict()
        df = pd.read_excel(url, sheet_name="아이템 이름", usecols="A,E:F")
        df = df.replace({np.nan: None})
        for (_, row) in df.iterrows():
            stage_name, item_1, item_2 = row
            drop_item_list[stage_name] = (item_1, item_2)

        df = pd.read_excel(url, sheet_name="드랍률", header=2, usecols="A:B,K:L")
        for (_, row) in df.iterrows():
            stage_name, count, prob_1, prob_2 = row
            if count < 100:
                continue
            prob_1 = None if type(prob_1)==str else prob_1
            prob_2 = None if type(prob_2)==str else prob_2
            item_1, item_2 = drop_item_list[stage_name]
            stage_to_drop[stage_name] = dict()
            stage_to_drop[stage_name][item_1] = prob_1
            stage_to_drop[stage_name][item_2] = prob_2
            stage_to_drop[stage_name].pop(None, None)

        data = []
        for stage_name, item_dict in stage_to_drop.items():
            item_1, item_2 = drop_item_list[stage_name]
            data.append((stage_name, item_1, item_dict.get(item_1, None), item_2, item_dict.get(item_2, None)))

        conn = sqlite3.connect("db/master.db")
        cur = conn.cursor()
        cur.executemany("""INSERT OR REPLACE INTO
                            drop_table(area, item_1_name, item_1_drop_rate, item_2_name, item_2_drop_rate)
                            VALUES (?, ?, ?, ?, ?)""", data)
        conn.commit()
        conn.close()

        self._resourceMaster["StageToDrop"] = stage_to_drop



class UpdateDropTableDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(400, 300)
        self.setWindowTitle("로딩중...")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowTitleHint)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        label = QLabel()
        self.movie = QMovie("icon/loading.gif")
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setScaledSize(self.movie.scaledSize() * 0.75)
        label.setMovie(self.movie)
        label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label)

        layout.addSpacing(20)
        
        label = QLabel("드랍 테이블 로딩중...학교. 푸흡.")
        label.setStyleSheet('font: 18pt "ONE Mobile POP";')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addWidget(label)

        label = QLabel("교주님, 10초 정도 걸려요.")
        label.setStyleSheet('font: 12pt "ONE Mobile POP";')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        layout.addWidget(label)

        self.setLayout(layout)
    

    def showEvent(self, event):
        super().showEvent(event)
        self.movie.start()
    
    def closeEvent(self, event):
        self.movie.stop()
        super().closeEvent(event)

        