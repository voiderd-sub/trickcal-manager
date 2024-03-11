from widgets.ui.page_equip_1 import Ui_page_equip_1
from widgets.wrapper.misc import wrapStyle
from widgets.wrapper.goal_settings import GoalSettings
from widgets.wrapper.set_goal_with_stat import SetGoalWithStat

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHeaderView, QSizePolicy, QWidget, QAbstractItemView,
                                    QPushButton, QButtonGroup)

import sqlite3
from functools import partial



class PageEquip1(Ui_page_equip_1, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setInitialState()        # Settings in main.py
        

    def setInitialState(self):
        self.reload = {"account": True}
        main = self.window()
        res = main.resource

        # load hero_equip data from master db
        max_rank = res.masterGet("MaxRank")

        # load user_equip data from user db
        # self.user_equip_data_tmp = dict()
        self.last_hero_name = None
        self.last_goal_idx = 0

        # set up rank_table
        table = self.rank_table
        self.setupTable()
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        horizontal_header = table.horizontalHeader()
        horizontal_header.hide()
        table.verticalHeader().hide()

        # hero name with asc order
        self.hero_select.setCompleterFont(15)
        self.updateHeroList()
        self.hero_select.currentIndexChanged.connect(self.updateCurrentEquipTable)

        horizontal_header.setSectionResizeMode(0, QHeaderView.Fixed)
        for col_idx in range(1, 7):
            horizontal_header.setSectionResizeMode(col_idx, QHeaderView.Stretch)

        # When you click self.go_left_btn/self.go_right_btn,
        # increment/decrement self.hero_select's index by 1
        self.go_left_btn.clicked.connect(partial(self.changeHeroSelectIndex, -1))
        self.go_right_btn.clicked.connect(partial(self.changeHeroSelectIndex, 1))

        # Pressing the right/left arrow key while focusing on the table
        # has the same effect as clicking go_right/left_btn
        table.keyPressEvent = lambda event: self.changeHeroSelectIndex(1) if event.key()==Qt.Key.Key_Right else self.changeHeroSelectIndex(-1) if event.key()==Qt.Key.Key_Left else None

        self.last_mode = True   # True: cur_mode, False: goal_mode
        self.radio_cur_mode.setChecked(True)
        self.radio_cur_mode.toggled.connect(self.updateCurrentEquipTable)

        # Settings for goal mode
        self.cur_goal.currentIndexChanged.connect(self.updateCurrentEquipTable)
        self.goal_setting_btn.clicked.connect(self.openGoalSettings)
        self.set_check_btn.clicked.connect(self.setCheckAllWithRank)

        # Settings for set_goal_with_stat
        self.set_goal_with_stat = SetGoalWithStat(self)
        self.set_goal_w_stat_btn.clicked.connect(self.set_goal_with_stat.show)


    def setupTable(self):
        max_rank = self.window().resource.masterGet("MaxRank")
        table = self.rank_table
        table.clearContents()
        table.setRowCount(max_rank+1)
        table.setColumnCount(7)
        for rank in range(1, max_rank+1):
            btn = QPushButton()
            btn.setText(f"Rank {rank}")
            btn.setCheckable(True)
            btn.setStyleSheet('font: 14pt "ONE Mobile POP";')
            table.setCellWidget(rank-1, 0, btn)
            for col_idx in range(1, 7):
                mini_btn = QPushButton()
                mini_btn.setStyle(wrapStyle())
                mini_btn.setStyleSheet('font: 11pt "ONE Mobile POP";')
                mini_btn.setCheckable(True)
                mini_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                table.setCellWidget(rank-1, col_idx, mini_btn)
                mini_btn.clicked.connect(partial(self.checkButton, mini_btn))
            btn.clicked.connect(partial(self.checkAll, rank-1))
            table.setRowHeight(rank-1, 50)
        btn = QPushButton()
        btn.setText("MAX")
        btn.setCheckable(True)
        btn.setStyleSheet('font: 14pt "ONE Mobile POP";')
        table.setCellWidget(max_rank, 0, btn)
        btn.clicked.connect(partial(self.checkAll, max_rank))
        table.setRowHeight(max_rank, 50)

        # make qbuttongroup with all buttons in the first column
        rank_btn_group = QButtonGroup(self)
        for row_idx in range(max_rank+1):
            rank_btn_group.addButton(table.cellWidget(row_idx, 0))

        # update combo_set_goal to reflect new max_rank
        self.combo_set_goal.clear()
        self.combo_set_goal.addItems(["선택"] + [str(i) for i in range(1, max_rank+1)] + ["MAX"])


    def updateHeroList(self):
        self.hero_select.blockSignals(True)
        hero_name_to_id = self.window().resource.masterGet("HeroNameToId")
        names = list(sorted(hero_name_to_id.keys()))
        self.hero_select.clear()
        self.hero_select.addItems(names)
        self.hero_select.blockSignals(False)
        

    # Update the table according to the current index of self.hero_select
    def updateCurrentEquipTable(self):
        table = self.rank_table
        res = self.window().resource
        num_rows = table.rowCount()
        num_cols = table.columnCount()

        hero_name = self.hero_select.currentText()
        hero_id = res.masterGet("HeroNameToId")[hero_name]
        is_goal = self.radio_goal_mode.isChecked()
        cur_equip = res.userGet("CurEquip")
        goal_equip = res.userGet("GoalEquip")

        self.updateResourceLastUserEquip()
        hero_id_to_equip_names = res.masterGet("HeroIdToEquipNames")
        master_equip_data = hero_id_to_equip_names[hero_id]
        
        # set text of buttons in the table
        for (rank, item_name_list) in master_equip_data.items():
            for col_idx, equip_name in enumerate(item_name_list):
                mini_btn: QPushButton = table.cellWidget(rank-1, col_idx+1)
                mini_btn.setText(equip_name)

        # enable/disable go_left_btn/go_right_btn
        cur_herolist_idx = self.hero_select.currentIndex()
        self.go_left_btn.setEnabled(cur_herolist_idx!=0)
        self.go_right_btn.setEnabled(cur_herolist_idx!=self.hero_select.count()-1)

        # set enabled state of buttons in the table (only in goal mode)
        if is_goal:
            if not hero_id in cur_equip:
                for row_idx in range(num_rows-1):
                    for col_idx in range(num_cols):
                        table.cellWidget(row_idx, col_idx).setEnabled(True)
            else:
                cur_rank, equips = cur_equip[hero_id]
                for row_idx in range(num_rows-1):
                    for col_idx in range(1, num_cols):
                        table.cellWidget(row_idx, col_idx).setDisabled(row_idx<cur_rank-1 or (row_idx==cur_rank-1 and col_idx in equips))
                for row_idx in range(num_rows-1):
                    table.cellWidget(row_idx, 0).setDisabled(row_idx<cur_rank-1)
        else:
            for row_idx in range(num_rows-1):
                for col_idx in range(num_cols):
                    table.cellWidget(row_idx, col_idx).setEnabled(True)

        # set checked state of buttons in the table
        # In current mode, check the buttons according to CurEquip
        # In goal mode, check the buttons according to GoalEquip
        load_from = None  
        if is_goal and hero_id in goal_equip[self.cur_goal.currentIndex()+1]:
            load_from = goal_equip[self.cur_goal.currentIndex()+1]
        elif not is_goal and hero_id in cur_equip:
            load_from = cur_equip

        if load_from is None:
            cur_rank, equips = 1, set()
        else:
            cur_rank, equips = load_from[hero_id]

        min_enabled_rank = 1
        for row_idx in range(num_rows):
            btn = table.cellWidget(row_idx, 0)
            if btn.isEnabled():
                min_enabled_rank = row_idx+1
                break
        table.cellWidget(max(min_enabled_rank, cur_rank)-1, 0).click()
        if len(equips) == 0:
            return
        for col_idx in list(equips):
            table.cellWidget(cur_rank-1, col_idx).setChecked(True)
        
    

    # Function for button in the first column (set rank)
    def checkAll(self, row_idx):
        table = self.rank_table
        num_cols = table.columnCount()
        for col_idx in range(1, num_cols):
            for row in range(row_idx):
                table.cellWidget(row, col_idx).setChecked(True)
            for row in range(row_idx, table.rowCount()-1):
                table.cellWidget(row, col_idx).setChecked(False)
        table.cellWidget(table.rowCount()-1, 0).setChecked(False)
    
    
    # Function for buttons in 2nd to last column
    def checkButton(self, btn):
        table = self.rank_table
        cur_row = table.indexAt(btn.pos()).row()
        num_cols = table.columnCount()
        if btn.isChecked():
            for col_idx in range(1, num_cols):
                for row_idx in range(cur_row):
                    table.cellWidget(row_idx, col_idx).setChecked(True)
            for col_idx in range(1, num_cols):
                if not table.cellWidget(cur_row, col_idx).isChecked():
                    table.cellWidget(cur_row, 0).setChecked(True)
                    return
            table.cellWidget(cur_row+1, 0).setChecked(True)
        else:
            table.cellWidget(cur_row, 0).setChecked(True)
            for col_idx in range(1, num_cols):
                for row_idx in range(cur_row+1, table.rowCount()-1):
                    table.cellWidget(row_idx, col_idx).setChecked(False)


    # Change the index only when it is within a valid index range.
    def changeHeroSelectIndex(self, num):
        if 0<=self.hero_select.currentIndex()+num<self.hero_select.count():
            self.hero_select.setCurrentIndex(self.hero_select.currentIndex()+num)
    

    # Reflect last page's data to resource manager
    def updateResourceLastUserEquip(self):
        table = self.rank_table
        res = self.window().resource

        save_to = (res.userGet("CurEquip") if self.last_mode
                        else res.userGet("GoalEquip")[self.last_goal_idx+1])

        if not self.last_hero_name is None:
            # Find the last checked rank
            # Method for finding rank is the same for both cur_mode and goal_mode
            last_rank = 0
            for row_idx in range(table.rowCount()):
                if table.cellWidget(row_idx, 0).isChecked():
                    last_rank = row_idx+1
                    break
            assert last_rank!=0, "No rank is checked"
            if last_rank==table.rowCount():
                last_equips = set()
            else:
                # Find the last checked equips
                # Method for finding equips is different for cur_mode and goal_mode
                if self.last_mode:
                    last_equips = set([i for i in range(1, table.columnCount()) if table.cellWidget(last_rank-1, i).isChecked()])
                else:
                    last_equips = set([i for i in range(1, table.columnCount()) if table.cellWidget(last_rank-1, i).isChecked() or not table.cellWidget(last_rank-1, i).isEnabled()])
            
            last_hero_idx = res.masterGet("HeroNameToId")[self.last_hero_name]
            save_to[last_hero_idx] = (last_rank, last_equips)

        self.last_hero_name = self.hero_select.currentText()
        self.last_mode = self.radio_cur_mode.isChecked()
        self.last_goal_idx = self.cur_goal.currentIndex()


    def saveUserEquipAll(self):
        self.last_hero_name = self.hero_select.currentText()
        self.updateResourceLastUserEquip()
        main = self.window()
        res = main.resource

        # transfer changed data from tmp to each dict
        cur_equip = res.userGet("CurEquip")
        cur_goal_idx = self.cur_goal.currentIndex() + 1
        goal_equip = res.userGet("GoalEquip")[cur_goal_idx]

        cur_equip.update(self.user_equip_data_tmp)
        self.user_equip_data_tmp = dict()
        goal_equip.update(self.hero_name_to_goal_data_tmp)
        self.hero_name_to_goal_data_tmp = dict()

        cur_user: sqlite3.Cursor = main.conn_user.cursor()

        data = [(hero_id, rank, ",".join((str(i) for i in list(equips))) if len(equips)!=0 else None) for (hero_id, (rank, equips)) in cur_equip.items()]
        cur_user.executemany("REPLACE INTO user_cur_equip VALUES (?, ?, ?)", data)

        if self.cur_goal.count()!=0:
            data = [(cur_goal_idx, hero_id, rank, ",".join((str(i) for i in list(equips))) if len(equips)!=0 else None) for (hero_id, (rank, equips)) in goal_equip.items()]
            cur_user.executemany("REPLACE INTO user_goal_equip(goal_id, hero_id, rank, equips) VALUES (?, ?, ?, ?)", data)

        main.conn_user.commit()
        main.changeEquipCascade()
    

    # undo all changes in tmp
    def undoUserEquipAll(self):
        self.user_equip_data_tmp = dict()
        self.hero_name_to_goal_data_tmp = dict()
        self.updateEquipTableAtInit()
    

    # save current page data into db, then delete it from user_equip_data_tmp
    def saveUserEquipCur(self):
        self.last_hero_name = self.hero_select.currentText()
        self.updateResourceLastUserEquip()
        main = self.window()
        res = main.resource
        cur_user: sqlite3.Cursor = main.conn_user.cursor()

        hero_id = res.masterGet("HeroNameToId")[self.last_hero_name]

        if hero_id in self.user_equip_data_tmp:
            res.userGet("CurEquip")[hero_id] = self.user_equip_data_tmp[hero_id]
            rank, equips = self.user_equip_data_tmp[hero_id]
            equips = ",".join([str(i) for i in list(equips)]) if len(equips)!=0 else None
            cur_user.execute("REPLACE INTO user_cur_equip VALUES (?, ?, ?)",
                             (hero_id, rank, equips))
            main.conn_user.commit()
            del self.user_equip_data_tmp[hero_id]

        if hero_id in self.hero_name_to_goal_data_tmp:
            goal_idx = self.cur_goal.currentIndex() + 1
            res.userGet("GoalEquip")[goal_idx][hero_id] = self.hero_name_to_goal_data_tmp[hero_id]
            rank, equips = self.hero_name_to_goal_data_tmp[hero_id]
            equips = ",".join([str(i) for i in list(equips)]) if len(equips)!=0 else None
            cur_user.execute("REPLACE INTO user_goal_equip VALUES (?, ?, ?, ?)",
                             (goal_idx, hero_id, rank, equips))
            main.conn_user.commit()
            del self.hero_name_to_goal_data_tmp[hero_id]
        
        main.changeEquipCascade()
    

    # undo tmp changes of current page
    def undoUserEquipCur(self):
        last_hero_id = self.window().resource.masterGet("HeroNameToId")[self.last_hero_name]
        if self.radio_cur_mode.isChecked():
            self.user_equip_data_tmp.pop(last_hero_id, None)
        else:
            self.hero_name_to_goal_data_tmp.pop(last_hero_id, None)
        self.updateEquipTableAtInit()
    

    def openGoalSettings(self):
        self.updateResourceLastUserEquip()

        main_window = self.window()
        new_window: GoalSettings = main_window.goal_settings
        new_window.show()
    

    def updateGoalNameList(self):
        main = self.window()
        self.cur_goal.blockSignals(True)
        self.cur_goal.clear()
        self.cur_goal.addItems(main.resource.userGet("GoalIdToName").values())
        self.cur_goal.setCurrentIndex(0)
        self.last_goal_idx = 0
        self.cur_goal.blockSignals(False)
        self.enableRadioGoalMode()
        self.updateEquipTableAtInit()
    

    def enableRadioGoalMode(self):
        self.radio_goal_mode.setEnabled(self.cur_goal.count()!=0)
        if self.cur_goal.count()==0:
            self.radio_cur_mode.setChecked(True)


    def updateEquipTableAtInit(self):
        self.last_hero_name = None
        self.updateCurrentEquipTable()

    
    # Edit each tmp file and refresh table
    def setCheckAllWithRank(self):
        is_goal = self.radio_goal_mode.isChecked()
        cur_rank = self.combo_set_goal.currentIndex()
        res = self.window().resource
        hero_id_to_equip_names = res.masterGet("HeroIdToEquipNames")

        if cur_rank==0:
            return
        for hero_id in hero_id_to_equip_names.keys():
            if is_goal:
                res.userGet("GoalEquip")[self.cur_goal.currentIndex()+1][hero_id] = (cur_rank, set())
            else:
                res.userGet("CurEquip")[hero_id] = (cur_rank, set())
        self.updateEquipTableAtInit()
    

    def setGoalStat(self, stat_list):
        assert len(stat_list) >= 1, "stat_list must have at least one element"
        
        main = self.window()
        res = main.resource
        stat_name_to_id = {name_kr: id for (id, (name_kr, name_en)) in res.masterGet("Stat").items()}
        goal_stat_ids = {stat_name_to_id[stat_name] for stat_name in stat_list}
        max_rank = res.masterGet("MaxRank")
        rank_type_id_to_goal_rank = dict()

        for rank_type_id, rank_to_stat_dict in res.masterGet("RankStatType").items():
            goal_rank = 1
            for rank, stat_dict in rank_to_stat_dict.items():
                if rank > max_rank:
                    break
                if len(goal_stat_ids.intersection(stat_dict.keys())) > 0:
                    rank_type_id_to_goal_rank[rank_type_id] = rank

        hero_id_to_rank_stat_type = res.masterGet("HeroIdToRankStatType")

        for hero_id, rank_type_id in hero_id_to_rank_stat_type.items():
            goal_rank = rank_type_id_to_goal_rank[rank_type_id]
            res.userGet("GoalEquip")[self.cur_goal.currentIndex()+1][hero_id] = (goal_rank, set())
        
        self.updateEquipTableAtInit()


    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        if self.reload.get("master", False):
            self.setupTable()
            self.updateHeroList()
        
        self.updateGoalNameList()
        
        self.reload = dict()
    

    def savePageData(self):
        self.updateResourceLastUserEquip()
        self.window().changeEquipCascade()
