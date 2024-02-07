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
        main = self.window()
        res = main.resource

        # load hero_equip data from master db
        max_rank = res.masterGet("MaxRank")

        # load user_equip data from user db
        self.loadUserEquip()

        # set up rank_table
        table = self.rank_table
        table.clearContents()
        table.setRowCount(max_rank+1)
        table.setColumnCount(7)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        horizontal_header = table.horizontalHeader()
        horizontal_header.hide()
        table.verticalHeader().hide()

        # hero name with asc order
        self.hero_select.setCompleterFont(15)
        self.updateHeroList()
        self.hero_select.currentIndexChanged.connect(self.updateCurrentEquipTalbe)

        # set current equip table
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

        self.go_left_btn.setEnabled(False)

        # make qbuttongroup with all buttons in the first column
        rank_btn_group = QButtonGroup(self)
        for row_idx in range(max_rank+1):
            rank_btn_group.addButton(table.cellWidget(row_idx, 0))

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

        # Connect save/undo buttons
        self.save_all_btn.clicked.connect(self.saveUserEquipAll)
        self.save_cur_btn.clicked.connect(self.saveUserEquipCur)
        self.undo_all_btn.clicked.connect(self.undoUserEquipAll)
        self.undo_cur_btn.clicked.connect(self.undoUserEquipCur)

        self.last_mode = True   # True: cur_mode, False: goal_mode
        self.radio_cur_mode.setChecked(True)
        self.radio_cur_mode.toggled.connect(self.updateCurrentEquipTalbe)

        # Settings for goal mode
        self.updateGoalNameList()
        self.cur_goal.setCurrentIndex(0)
        self.goal_setting_btn.clicked.connect(self.openGoalSettings)
        self.cur_goal.currentIndexChanged.connect(self.loadCurrentGoalData)

        self.combo_set_goal.clear()
        self.combo_set_goal.addItems(["선택"] + [str(i) for i in range(1, max_rank+1)] + ["MAX"])
        self.set_check_btn.clicked.connect(self.setCheckAllWithRank)

        # Settings for set_goal_with_stat
        self.set_goal_with_stat = SetGoalWithStat(self)
        self.set_goal_w_stat_btn.clicked.connect(self.set_goal_with_stat.show)

    def updateHeroList(self):
        self.hero_select.blockSignals(True)
        res = self.window().resource
        hero_name_to_equip_names = res.masterGet("HeroNameToId")
        names = list(sorted(hero_name_to_equip_names.keys()))
        self.hero_select.clear()
        self.hero_select.addItems(names)
        self.hero_select.blockSignals(False)
        

    # Update the table according to the current index of self.hero_select
    def updateCurrentEquipTalbe(self):
        table = self.rank_table
        num_rows = table.rowCount()
        num_cols = table.columnCount()

        hero_name = self.hero_select.currentText()
        is_goal = self.radio_goal_mode.isChecked()

        self.updateUserEquipTmp()
        hero_name_to_equip_names = self.window().resource.masterGet("HeroNameToEquipNames")
        master_equip_data = hero_name_to_equip_names[hero_name]
        
        # set text of buttons in the table
        for (rank, item_name_list) in master_equip_data.items():
            for col_idx, equip_name in enumerate(item_name_list):
                mini_btn: QPushButton = table.cellWidget(rank-1, col_idx+1)
                mini_btn.setText(equip_name)

        # enable/disable go_left_btn/go_right_btn
        cur_idx = self.hero_select.currentIndex()
        self.go_left_btn.setEnabled(cur_idx!=0)
        self.go_right_btn.setEnabled(cur_idx!=self.hero_select.count()-1)

        # set enabled state of buttons in the table (only in goal mode)
        # Determine whether to disable using equip_data(_tmp)
        if is_goal:
            if hero_name in self.user_equip_data_tmp:
                load_from = self.user_equip_data_tmp
            elif hero_name in self.user_equip_data:
                load_from = self.user_equip_data
            else:
                load_from = None
            if load_from is None:
                for row_idx in range(num_rows-1):
                    for col_idx in range(num_cols):
                        table.cellWidget(row_idx, col_idx).setEnabled(True)
            else:
                cur_rank, equips = load_from[hero_name]
                for row_idx in range(num_rows-1):
                    for col_idx in range(1, num_cols):
                        if equips is None:
                            table.cellWidget(row_idx, col_idx).setDisabled(row_idx<cur_rank-1)
                        else:
                            table.cellWidget(row_idx, col_idx).setDisabled(row_idx<cur_rank-1 or (row_idx==cur_rank-1 and col_idx in equips))
                for row_idx in range(num_rows-1):
                    table.cellWidget(row_idx, 0).setDisabled(row_idx<cur_rank-1)
        else:
            for row_idx in range(num_rows-1):
                for col_idx in range(num_cols):
                    table.cellWidget(row_idx, col_idx).setEnabled(True)

        # set checked state of buttons in the table
        # In current mode, check the buttons according to user_equip_data(_tmp)
        # In goal mode, check the buttons according to hero_name_to_goal_data(_tmp)
        load_from = None  
        if is_goal:
            if hero_name in self.hero_name_to_goal_data_tmp:
                load_from = self.hero_name_to_goal_data_tmp
            elif hero_name in self.hero_name_to_goal_data:
                load_from = self.hero_name_to_goal_data
        else:
            if hero_name in self.user_equip_data_tmp:
                load_from = self.user_equip_data_tmp
            elif hero_name in self.user_equip_data:
                load_from = self.user_equip_data
        
        if load_from is None:
            for row_idx in range(num_rows):
                btn = table.cellWidget(row_idx, 0)
                if btn.isEnabled():
                    btn.click()
                    break
            return
        cur_rank, equips = load_from[hero_name]
        table.cellWidget(cur_rank-1, 0).click()
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
    

    # Update user_equip_data_tmp & hero_name_to_goal_data_tmp with the previous page's data
    def updateUserEquipTmp(self):
        table = self.rank_table

        # In Current mode, checked cells are checked and stored in user_equip_data tmp.
        # In goal mode, cells that are enabled and checked at the same time
        # are checked and stored in hero_name_to_goal_data_tmp.
        db_data_dict = self.user_equip_data if self.last_mode else self.hero_name_to_goal_data
        save_to = self.user_equip_data_tmp if self.last_mode else self.hero_name_to_goal_data_tmp

        if not self.last_hero_name is None:
            # Find the last checked rank
            # The method for finding rank is the same for both cur_mode and goal_mode
            last_rank = 0
            for row_idx in range(table.rowCount()):
                if table.cellWidget(row_idx, 0).isChecked():
                    last_rank = row_idx+1
                    break
            assert last_rank!=0, "No rank is checked"
            if last_rank==table.rowCount():
                last_equips = set()
            else:
            # Meanwhile, in goal_mode, the button in the same row as the enabled top button
            # among the first rows can be checked/unchecked in a disabled state.
            # Therefore, both cases must be considered separately.
                if self.last_mode:
                    last_equips = set([i for i in range(1, table.columnCount()) if table.cellWidget(last_rank-1, i).isChecked()])
                else:
                    last_equips = set([i for i in range(1, table.columnCount()) if table.cellWidget(last_rank-1, i).isChecked() or not table.cellWidget(last_rank-1, i).isEnabled()])

            if last_equips=="":
                last_equips = set()
            
            db_data = db_data_dict.get(self.last_hero_name, None)

            # If same data already exists in db, delete from tmp
            if db_data == (last_rank, last_equips):
                save_to.pop(self.last_hero_name, None)

            # If it is not in db, save to tmp
            else:
                save_to[self.last_hero_name] = (last_rank, last_equips)

        self.last_hero_name = self.hero_select.currentText()
        self.last_mode = self.radio_cur_mode.isChecked()
    

    # change user_cur_equip to user_equip_data_tmp, then save it to db
    def saveUserEquipAll(self):
        # save current page data into user_equip_data_tmp
        self.last_hero_name = self.hero_select.currentText()
        self.updateUserEquipTmp()

        # transfer changed data from tmp to each dict
        self.user_equip_data.update(self.user_equip_data_tmp)
        self.user_equip_data_tmp = dict()
        self.hero_name_to_goal_data.update(self.hero_name_to_goal_data_tmp)
        self.hero_name_to_goal_data_tmp = dict()

        main = self.window()
        res = main.resource
        cur_user: sqlite3.Cursor = main.conn_user.cursor()
        hero_name_to_id = res.masterGet("HeroNameToId")

        data = [(hero_name_to_id[hero_name], rank, ",".join((str(i) for i in equips)) if len(equips)!=0 else None) for (hero_name, (rank, equips)) in self.user_equip_data.items()]
        cur_user.executemany("REPLACE INTO user_cur_equip VALUES (?, ?, ?)", data)

        if self.cur_goal.count()!=0:
            cur_goal_idx = self.cur_goal.currentIndex()
            data = [(cur_goal_idx+1, hero_name_to_id[hero_name], rank, ",".join((str(i) for i in equips)) if len(equips)!=0 else None) for (hero_name, (rank, equips)) in self.hero_name_to_goal_data.items()]
            cur_user.executemany("REPLACE INTO user_goal_equip(goal_id, hero_id, rank, equips) VALUES (?, ?, ?, ?)", data)

        main.conn_user.commit()
        _ = main.resource.getCurEquip()
    

    # undo all changes in tmp
    def undoUserEquipAll(self):
        self.user_equip_data_tmp = dict()
        self.hero_name_to_goal_data_tmp = dict()
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()
    

    # save current page data into db, then delete it from user_equip_data_tmp
    def saveUserEquipCur(self):
        self.last_hero_name = self.hero_select.currentText()
        self.updateUserEquipTmp()
        main = self.window()
        res = main.resource
        cur_user: sqlite3.Cursor = main.conn_user.cursor()

        hero_name_to_id = res.masterGet("HeroNameToId")
        hero_name = self.hero_select.currentText()

        if self.last_hero_name in self.user_equip_data_tmp:
            self.user_equip_data[self.last_hero_name] = self.user_equip_data_tmp[self.last_hero_name]
            rank, equips = self.user_equip_data_tmp[hero_name]
            equips = ",".join([str(i) for i in list(equips)]) if len(equips)!=0 else None
            cur_user.execute("REPLACE INTO user_cur_equip VALUES (?, ?, ?)",
                             (hero_name_to_id[hero_name], rank, equips))
            main.conn_user.commit()
            del self.user_equip_data_tmp[self.last_hero_name]

        if self.last_hero_name in self.hero_name_to_goal_data_tmp:
            self.hero_name_to_goal_data[self.last_hero_name] = self.hero_name_to_goal_data_tmp[self.last_hero_name]
            rank, equips = self.hero_name_to_goal_data_tmp[hero_name]
            equips = ",".join([str(i) for i in list(equips)]) if len(equips)!=0 else None
            cur_user.execute("REPLACE INTO user_goal_equip VALUES (?, ?, ?, ?)",
                             (self.cur_goal.currentIndex()+1, hero_name_to_id[hero_name], rank, equips))
            main.conn_user.commit()
            del self.hero_name_to_goal_data_tmp[self.last_hero_name]
        _ = main.resource.getCurEquip()
    

    # undo tmp changes of current page
    def undoUserEquipCur(self):
        if self.radio_cur_mode.isChecked():
            self.user_equip_data_tmp.pop(self.last_hero_name, None)
        else:
            self.hero_name_to_goal_data_tmp.pop(self.last_hero_name, None)
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()
    

    # Reload equip & goal data from db, then update the table
    def changeAccount(self):
        self.loadUserEquip()
        self.updateGoalNameList()


    # Load user_equip_data from db
    def loadUserEquip(self):
        main = self.window()
        res = main.resource
        self.user_equip_data = dict()

        id_to_equip = res.userGet("CurEquip")
        id_to_meta = res.masterGet("HeroIdToMetadata")
        for (id, equip_data) in id_to_equip.items():
            self.user_equip_data[id_to_meta[id]["name_kr"]] = equip_data

        self.user_equip_data_tmp = dict()
        self.last_hero_name = None
    

    def openGoalSettings(self):
        main_window = self.window()
        new_window: GoalSettings = main_window.goal_settings
        new_window.show()
    

    def updateGoalNameList(self):
        self.cur_goal.clear()
        main = self.window()
        self.cur_goal.addItems(main.resource.userGet("GoalList"))
        self.enableRadioGoalMode()
        self.loadCurrentGoalData()
    

    def enableRadioGoalMode(self):
        self.radio_goal_mode.setEnabled(self.cur_goal.count()!=0)
        if self.cur_goal.count()==0:
            self.radio_cur_mode.setChecked(True)


    def loadCurrentGoalData(self):
        if self.cur_goal.count()==0:
            return
        goal_idx = self.cur_goal.currentIndex()
        main = self.window()
        hero_id_to_metadata = main.resource.masterGet("HeroIdToMetadata")
        cur_user: sqlite3.Cursor = main.conn_user.cursor()
        cur_user.execute(f"SELECT hero_id, rank, equips FROM user_goal_equip WHERE goal_id={goal_idx+1};")
        self.hero_name_to_goal_data = dict()
        for (hero_id, rank, equips) in cur_user:
            equips = set([int(i) for i in equips.split(",")]) if equips is not None else set()
            self.hero_name_to_goal_data[hero_id_to_metadata[hero_id]["name_kr"]] = (rank, equips)
        self.hero_name_to_goal_data_tmp = dict()
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()

    
    # Edit each tmp file and refresh table
    def setCheckAllWithRank(self):
        is_goal = self.radio_goal_mode.isChecked()
        table = self.rank_table
        cur_rank = self.combo_set_goal.currentIndex()
        hero_name_to_equip_names = self.window().resource.masterGet("HeroNameToEquipNames")

        if cur_rank==0:
            return
        for name in hero_name_to_equip_names.keys():
            if is_goal:
                self.hero_name_to_goal_data_tmp[name] = (cur_rank, None)
            else:
                self.user_equip_data_tmp[name] = (cur_rank, None)
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()
    

    def setGoalStat(self, stat_list):
        assert len(stat_list) >= 1, "stat_list must have at least one element"
        
        main_window = self.window()
        cur_master: sqlite3.Cursor = main_window.conn_master.cursor()
        cur_master.execute("SELECT id, name from stat")
        stat_name_to_id = {name: id for (id, name) in cur_master}
        stat_ids = "("+",".join([str(stat_name_to_id[stat]) for stat in stat_list])+")"

        cur_master.execute("SELECT MAX(DISTINCT(rank)) FROM equipment")
        max_rank = cur_master.fetchone()[0]

        cur_master.execute(f"""
            select id, max(rank)
            from rank_stat_type rst
            where (stat_1_id in {stat_ids} or stat_2_id in {stat_ids})
            and rank <= {max_rank}
			group by id
        """)

        rank_type_id_to_rank = {id: rank for (id, rank) in cur_master}

        if not hasattr(self, "hero_name_to_rank_type"):
            self.hero_name_to_rank_type = dict()
            cur_master.execute("select * from hero_rank_stat_type")
            for (hero_id, rank_type_id) in cur_master:
                self.hero_name_to_rank_type[self.hero_id_to_name[hero_id]] = rank_type_id

        for hero_name in self.hero_name_to_rank_type:
            rank_type_id = self.hero_name_to_rank_type[hero_name]
            rank = rank_type_id_to_rank[rank_type_id]
            self.hero_name_to_goal_data_tmp[hero_name] = (rank, None)
        
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()