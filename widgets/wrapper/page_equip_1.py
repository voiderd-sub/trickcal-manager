from widgets.ui.page_equip_1 import Ui_page_equip_1
from widgets.wrapper.misc import wrapStyle
from widgets.wrapper.goal_settings import GoalSettings

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
        main_window = self.window()
        cur_master: sqlite3.Cursor = main_window.conn_master.cursor()

        # load hero_equip data from master db
        self.hero_name_to_equip_data = dict()
        self.hero_name_to_id = dict()
        self.hero_id_to_name = dict()
        cur_master.execute("SELECT count(DISTINCT(rank)) FROM equipment")
        max_rank = cur_master.fetchone()[0]

        cur_master.execute("""
            select h.id, h.name_kr, he.rank, e.name
            from hero h
            join hero_equip he on (h.id = he.hero_id)
            join equipment e on (he.equipment_id=e.id)
            order by h.personality asc, h.star_intrinsic desc, h.name_kr asc, he.rank asc, e.id asc
        """)
        for (id, hero_name, rank, equip_name) in cur_master:
            if not hero_name in self.hero_name_to_equip_data:
                self.hero_name_to_equip_data[hero_name] = {k: list() for k in range(1, max_rank+1)}
            self.hero_name_to_equip_data[hero_name][rank].append(equip_name)
            self.hero_name_to_id[hero_name] = id
            self.hero_id_to_name[id] = hero_name
        
        # load user_equip data from user db
        self.loadUserEquip()

        # set up rank_table
        table = self.rank_table
        table.setRowCount(max_rank+1)
        table.setColumnCount(7)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        horizontal_header = table.horizontalHeader()
        horizontal_header.hide()
        table.verticalHeader().hide()

        # load names from db (with right order)
        cur_master.execute("""
            select name_kr
            from hero h
            order by name_kr asc
        """)  
        names = ["".join(i) for i in cur_master.fetchall()]

        self.hero_select.addItems(names)
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
        btn.setText(f"MAX")
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
        
        self.user_equip_data_tmp = dict()
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()

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

        self.goal_setting_btn.clicked.connect(self.openGoalSettings)
        self.cur_goal.currentIndexChanged.connect(self.updateCurrentEquipTalbe)

        self.cur_goal.setCurrentIndex(0)
        self.updateGoalList()
        self.radio_cur_mode.setChecked(True)
        self.radio_cur_mode.clicked.connect(self.setCurMode)
        self.radio_goal_mode.clicked.connect(self.setGoalMode)
        


    # Update the table according to the current index of self.hero_select
    def updateCurrentEquipTalbe(self):
        table = self.rank_table
        hero_name = self.hero_select.currentText()

        self.updateUserEquipTmp(hero_name)
        master_equip_data = self.hero_name_to_equip_data[hero_name]
        
        # set text of buttons in the table
        for (rank, item_name_list) in master_equip_data.items():
            for col_idx, equip_name in enumerate(item_name_list):
                mini_btn: QPushButton = table.cellWidget(rank-1, col_idx+1)
                mini_btn.setText(equip_name)

        # enable/disable go_left_btn/go_right_btn
        cur_idx = self.hero_select.currentIndex()
        self.go_left_btn.setEnabled(cur_idx!=0)
        self.go_right_btn.setEnabled(cur_idx!=self.hero_select.count()-1)

        # set checked state of buttons in the table
        if hero_name in self.user_equip_data_tmp:
            load_from = self.user_equip_data_tmp
        elif hero_name in self.user_equip_data:
            load_from = self.user_equip_data
        else:
            table.cellWidget(0,0).click()
            return
        cur_rank, equips = load_from[hero_name]
        table.cellWidget(cur_rank-1, 0).click()
        if equips is None:
            return
        for col_idx in [int(i) for i in equips.split(",")]:
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
    

    # Update user_equip_data_tmp with the previous page's data
    def updateUserEquipTmp(self, hero_name):
        table = self.rank_table

        if not self.last_hero_name is None:
            last_rank = 0
            for row_idx in range(table.rowCount()):
                if table.cellWidget(row_idx, 0).isChecked():
                    last_rank = row_idx+1
                    break
            assert last_rank!=0, "No rank is checked"
            if last_rank==table.rowCount():
                last_equips = None
            else:
                last_equips = ",".join([str(i) for i in range(1, table.columnCount()) if table.cellWidget(row_idx, i).isChecked()])

            if last_equips=="":
                last_equips = None
            
            if self.last_hero_name in self.user_equip_data:
                if self.user_equip_data[self.last_hero_name]==(last_rank, last_equips):
                    if self.last_hero_name in self.user_equip_data_tmp:
                        del self.user_equip_data_tmp[self.last_hero_name]
                else:
                    self.user_equip_data_tmp[self.last_hero_name] = (last_rank, last_equips)
            elif (last_rank, last_equips) != (1, None):
                self.user_equip_data_tmp[self.last_hero_name] = (last_rank, last_equips)
        self.last_hero_name = hero_name
    

    # change user_cur_equip to user_equip_data_tmp, then save it to db
    def saveUserEquipAll(self):
        # save current page data into user_equip_data_tmp
        self.last_hero_name = self.hero_select.currentText()
        self.updateUserEquipTmp(self.hero_select.currentText())

        # transfer changed data from user_equip_data_tmp to user_equip_data
        self.user_equip_data.update(self.user_equip_data_tmp)
        self.user_equip_data_tmp = dict()

        main_window = self.window()
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        data = [(self.hero_name_to_id[hero_name], rank, equips) for (hero_name, (rank, equips)) in self.user_equip_data.items()]
        cur_user.executemany("REPLACE INTO user_cur_equip VALUES (?, ?, ?)", data)
        main_window.conn_user.commit()
    

    # undo all changes in user_equip_data_tmp & page check state
    def undoUserEquipAll(self):
        self.user_equip_data_tmp = dict()
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()
    

    # save current page data into db, then delete it from user_equip_data_tmp
    def saveUserEquipCur(self):
        self.last_hero_name = self.hero_select.currentText()
        self.updateUserEquipTmp(self.hero_select.currentText())

        if self.last_hero_name in self.user_equip_data_tmp:
            self.user_equip_data[self.last_hero_name] = self.user_equip_data_tmp[self.last_hero_name]

            main_window = self.window()
            cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
            hero_name = self.hero_select.currentText()
            rank, equips = self.user_equip_data_tmp[hero_name]
            cur_user.execute("REPLACE INTO user_cur_equip VALUES (?, ?, ?)", (self.hero_name_to_id[hero_name], rank, equips))
            main_window.conn_user.commit()

            del self.user_equip_data_tmp[self.last_hero_name]
    

    # undo change of current pages in user_equip_data_tmp & page check state
    def undoUserEquipCur(self):
        if self.last_hero_name in self.user_equip_data_tmp:
            del self.user_equip_data_tmp[self.last_hero_name]
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()
    

    # Reload user_equip_data from db, then update the table
    def changeAccount(self):
        self.loadUserEquip()
        self.user_equip_data_tmp = dict()
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()


    # Load user_equip_data from db
    def loadUserEquip(self):
        main_window = self.window()
        self.user_equip_data = dict()
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        cur_user.execute("ATTACH DATABASE 'db/master.db' as master")
        cur_user.execute("""
            select h.name_kr, uhe.rank, uhe.equips
            from master.hero h
            join user_cur_equip uhe on (h.id=uhe.hero_id)
        """)
        for (hero_name, rank, equips) in cur_user:
            self.user_equip_data[hero_name] = (rank, equips)
        cur_user.execute("DETACH DATABASE master")
    

    def openGoalSettings(self):
        main_window = self.window()
        new_window: GoalSettings = main_window.goal_settings
        new_window.show()
    

    def updateGoalList(self):
        self.cur_goal.clear()
        main_window = self.window()
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        cur_user.execute("SELECT name FROM user_goal_equip_names order by id asc;")
        self.cur_goal.addItems([name for (name,) in cur_user])
        self.loadCurrentGoalData()
        self.enableRadioGoalMode()
    

    def enableRadioGoalMode(self):
        self.radio_goal_mode.setEnabled(self.cur_goal.count()!=0)
        if self.cur_goal.count()==0:
            self.radio_cur_mode.setChecked(True)


    def loadCurrentGoalData(self):
        if self.cur_goal.count()==0:
            return
        goal_idx = self.cur_goal.currentIndex()
        main_window = self.window()
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        cur_user.execute(f"SELECT hero_id, rank, equips FROM user_goal_equip WHERE goal_id={goal_idx+1};")
        self.hero_name_to_goal_data = dict()
        for (hero_id, rank, equips) in cur_user:
            self.hero_name_to_goal_data[self.hero_id_to_name[hero_id]] = (rank, equips)
    

    def setCurMode(self):
        table = self.rank_table
        num_cols = table.columnCount()
        for row_idx in range(table.rowCount()-1):
            for col_idx in range(1, num_cols):
                table.cellWidget(row_idx, col_idx).setEnabled(True)
        self.last_hero_name = None
        self.updateCurrentEquipTalbe()


    def setGoalMode(self):
        # For the second to last rows in self.rank_table, change the checked button to disabled.
        table = self.rank_table
        num_cols = table.columnCount()
        for row_idx in range(table.rowCount()-1):
            for col_idx in range(1, num_cols):
                btn: QPushButton = table.cellWidget(row_idx, col_idx)
                if btn.isChecked():
                    btn.setEnabled(False)
        
        # load checked state from self.goal_data_tmp
        pass