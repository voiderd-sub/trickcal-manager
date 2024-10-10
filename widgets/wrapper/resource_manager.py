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
    
    
    def saveAllUserResource(self):
        # For each key in _resourceUser, save the value to the database
        conn = self.main.conn_user
        cur = conn.cursor()
        for userdata_name, userdata in self._resourceUser.items():
            match userdata_name:
                case "HeroIdToStarExtrinsic":
                    cur.executemany("INSERT OR REPLACE INTO user_hero(hero_id, star_extrinsic) VALUES(?,?)",
                                    userdata.items())
                    
                case "CurEquip":
                    data = [(idx, rank, ",".join(str(i) for i in equips) if equips else None)
                            for idx, (rank, equips) in userdata.items()]
                    cur.executemany("INSERT OR REPLACE INTO user_cur_equip(hero_id, rank, equips) VALUES(?,?,?)", data)

                case "GoalIdToName":
                    cur.execute("DELETE FROM user_goal_equip_names")
                    cur.executemany("INSERT INTO user_goal_equip_names(id, name, goal_type) VALUES(?,?,?)",
                                    [(id, name, goal_type) for id, (name, goal_type) in userdata.items()])
                    
                case "GoalEquip":
                    cur.execute("DELETE FROM user_goal_equip")
                    data = [(goal_id, hero_id, rank, ",".join(str(i) for i in equips) if equips else None) for goal_id, hero_dict in userdata.items() for hero_id, (rank, equips) in hero_dict.items()]
                    cur.executemany("INSERT INTO user_goal_equip(goal_id, hero_id, rank, equips) VALUES(?,?,?,?)", data)

                case "CalcSettings":
                    cur.executemany("INSERT OR REPLACE INTO calc_settings(setting_name, value) VALUES(?,?)",
                                    userdata.items())
                
                case "BagEquips":
                    cur.execute("DELETE FROM user_bag_equips")
                    cur.executemany("INSERT INTO user_bag_equips(id, count) VALUES(?,?)",
                                    userdata.items())
                
                case "UserItems":
                    cur.executemany("REPLACE INTO user_items(name, count) VALUES(?,?)",
                                    userdata.items())
                    
                case "UserBoard":
                    user_board = [(hero_id,
                                   ";".join("".join(str(i) for i in checked_list)
                                            for checked_list in board_status_tuple))
                                  for hero_id, (board_status_tuple, boundary) in userdata.items()]
                    cur.executemany("INSERT OR REPLACE INTO user_board(hero_id, board_status) VALUES(?,?)",
                                    user_board)

        conn.commit()
    

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
    

    def getGoalIdToName(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT id, name, goal_type FROM user_goal_equip_names order by id asc;")
        goal_id_to_name = {id: (name, goal_type) for (id, name, goal_type) in cur_user}
        self._resourceUser["GoalIdToName"] = goal_id_to_name
        return goal_id_to_name
    

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
    

    def getUserBoard(self):
        # {hero_id : (gateways, crayon1, ..., crayon4)}
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_board")
        user_board = {hero_id: tuple([int(checked_char) for checked_char in checked_str]
                      for checked_str in board_status.split(";"))
                      for (hero_id, board_status) in cur_user}
        
        # construct board array for each boardtype
        board_type = self.masterGet("BoardType")
        hero_id_to_board_data = self.masterGet("HeroIdToBoardData")

        for hero_id, board_status_tuple in user_board.items():
            # if no cell is selected, set boundary to (0, start_point)
            # find start_point by using index of board_type_data[0]'s item is 10
            crayon_indices = [0] * 5
            boundary = []
            board_type_id = hero_id_to_board_data[hero_id][0]
            board_type_data = board_type[board_type_id]["seq"]

            if sum(sum(row) for row in board_status_tuple) == 0:
                for col, cell in enumerate(board_type_data[0]):
                    if cell == 10:
                        boundary.append((0, col))
                        break
                user_board[hero_id] = (board_status_tuple, boundary)
                continue

            for row in range(1, len(board_type_data)):
                for col in range(len(board_type_data[row])):
                    cell_type = board_type_data[row][col]
                    if cell_type != 0:
                        is_selected = board_status_tuple[cell_type%10][crayon_indices[cell_type%10]]
                        if is_selected:
                            # check is there any unselected cell in (x+-1, y) and (x, y+-1)
                            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                if 0 <= row+dx < len(board_type_data) and 0 <= col+dy < len(board_type_data[row]):
                                    if board_type_data[row+dx][col+dy] == 0:
                                        boundary.append((row, col))
                                        break
                        crayon_indices[cell_type%10] += 1
            
            user_board[hero_id] = (board_status_tuple, boundary)
        self._resourceUser["UserBoard"] = user_board
        return user_board


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
        for board_seq in cur:
            idx = board_seq[0]
            hero_name_to_id[board_seq[1]] = idx
            hero_id_to_metadata[idx] = dict()
            for meta_name, meta_val in zip(meta_names, board_seq[1:]):
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
        cur.execute("SELECT id, name_kr, name_en FROM stat")
        stat = {id: (name_kr, name_en) for (id, name_kr, name_en) in cur}
        self._resourceMaster["Stat"] = stat
        cur.execute("SELECT id, short FROM stat")
        stat_short = {id: short for (id, short) in cur}
        self._resourceMaster["StatShort"] = stat_short

        # StageToDrop
        cur.execute("SELECT * FROM drop_table")
        stage_to_drop = defaultdict(lambda: defaultdict(int))
        for (stage, item_1, item_1_drop_rate, item_2, item_2_drop_rate) in cur:
            stage_to_drop[stage][item_1] = item_1_drop_rate
            stage_to_drop[stage][item_2] = item_2_drop_rate
            stage_to_drop[stage].pop(None, None)
        self._resourceMaster["StageToDrop"] = stage_to_drop


        # BoardType
        cur.execute("""SELECT id, board, board_type.is_star_1, num_crayon_type
                    FROM board_type JOIN board_num_each_crayon
                    ON (board_type.is_star_1=board_num_each_crayon.is_star_1)""")
        board_type = dict()
        for (id, board, is_star_1, num_crayon_type) in cur:
            data = dict()
            board_seq = list()
            start_points = {3 : list(), 4 : list()}
            point_to_idx = dict()
            crayon_indices = [0] * 4
            gates = []
            for level, seq in enumerate(board.split(";"), start=1):
                if len(seq) == 1:
                    board_seq.append([0] * 7)
                    board_seq[-1][int(seq)-1] = 10
                    gates.append((len(board_seq)-1, int(seq)-1))
                    for type in start_points:
                        start_points[type].append([])
                else:
                    for seq_idx, type in enumerate(seq):
                        type = int(type)
                        col = seq_idx % 7
                        if col == 0:
                            board_seq.append([0] * 7)
                        board_seq[-1][col] = type
                        if type > 0:
                            point_to_idx[(len(board_seq)-1, col)] = crayon_indices[type-1]
                            crayon_indices[type-1] += 1
                        if type >= 3:
                            start_points[type][-1].append((len(board_seq)-1, col))

            data["seq"] = board_seq
            data["is_star_1"] = bool(is_star_1)
            data["start_points"] = start_points
            data["gates"] = gates
            data["point_to_idx"] = point_to_idx

            num_crayon_types = [list() for _ in range(4)]
            for num_types in num_crayon_type.split(";"):
                for idx, num_type in enumerate(num_types.split(",")):
                    num_crayon_types[idx].append(int(num_type) + num_crayon_types[idx][-1] if num_crayon_types[idx] else int(num_type))
            for idx, num_type in enumerate(num_crayon_types):
                num_crayon_types[idx] = tuple(num_type)
            data["num_crayon_type"] = tuple(num_crayon_types)
            board_type[id] = data
        self._resourceMaster["BoardType"] = board_type


        # BoardCost
        cur.execute("SELECT level, type, gold, crayons FROM board_cost")
        board_cost = dict()
        for (level, type, gold, crayons) in cur:
            board_cost[(level, type)] = (gold, *(int(i) for i in crayons.split(";")))
        self._resourceMaster["BoardCost"] = board_cost


        # BoardStat
        cur.execute("SELECT stat_id, is_star_1, crayon_type, value FROM board_stats")
        board_stat = dict()
        for (stat_id, is_star_1, crayon_type, value) in cur:
            if is_star_1 > 1:
                board_stat[(stat_id, False, crayon_type)] = board_stat[(stat_id, True, crayon_type)] = value
            else:
                board_stat[(stat_id, bool(is_star_1), crayon_type)] = value
        self._resourceMaster["BoardStat"] = board_stat


        # BoardMinCostPath
        cur.execute("SELECT * FROM board_min_cost_path")
        min_cost_path = defaultdict(lambda: defaultdict(lambda: dict()))
        for (board_id, start_point, end_point, cost, path) in cur:
            start_point = tuple(int(i) for i in start_point.split(","))
            end_point = tuple(int(i) for i in end_point.split(","))
            path = tuple(tuple(int(i) for i in point.split(",")) for point in path.split(";"))
            min_cost_path[board_id][start_point][end_point] = (cost, path)
        self._resourceMaster["BoardMinCostPath"] = min_cost_path


        # HeroIdToBoardData
        cur.execute("SELECT * FROM hero_board_type")
        hero_id_to_board_data = {hero_id: (board_type, tuple(int(i) for i in purple.split(",")), tuple(int(i) for i in gold.split(","))) for (hero_id, board_type, purple, gold) in cur}
        self._resourceMaster["HeroIdToBoardData"] = hero_id_to_board_data


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

        