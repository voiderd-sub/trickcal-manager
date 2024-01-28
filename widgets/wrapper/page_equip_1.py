from widgets.ui.page_equip_1 import Ui_page_equip_1
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHeaderView, QSizePolicy, QWidget, QAbstractItemView,
                                    QPushButton, QButtonGroup)

import sqlite3
from functools import partial

from widgets.wrapper.misc import wrapStyle


class PageEquip1(Ui_page_equip_1, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyleFromPath("widgets/style/style_page_equip_1.qss")
        self.setInitialState()        # Settings in main.py
        
    
    def setStyleFromPath(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())

    def setInitialState(self):
        main_window = self.window()
        cur: sqlite3.Cursor = main_window.conn_master.cursor()

        # load hero_equip data from db
        self.name_to_equip_data = dict()
        cur.execute("SELECT count(DISTINCT(rank)) FROM equipment")
        max_rank = cur.fetchone()[0]

        cur.execute("""
            select h.name_kr, he.rank, he."order", e.name
            from hero h
            join hero_equip he on (h.id = he.hero_id)
            join equipment e on (he.equipment_id=e.id)
            order by h.personality asc, h.star_intrinsic desc, h.name_kr asc, he.rank asc, e.id asc
        """)
        for (hero_name, rank, order, equip_name) in cur:
            if not hero_name in self.name_to_equip_data:
                self.name_to_equip_data[hero_name] = {k: list() for k in range(1, max_rank+1)}
            self.name_to_equip_data[hero_name][rank].append(equip_name)

        # set up rank_table
        table = self.rank_table
        table.setRowCount(max_rank+1)
        table.setColumnCount(7)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        horizontal_header = table.horizontalHeader()
        horizontal_header.hide()
        table.verticalHeader().hide()

        # load names from db (with right order)
        cur.execute("""
            select name_kr
            from hero h
            order by name_kr asc
        """)  
        names = ["".join(i) for i in cur.fetchall()]

        self.hero_select.addItems(names)
        self.hero_select.currentIndexChanged.connect(self.updateCurrentEquipTalbe)

        # set current equip table
        data = self.name_to_equip_data[self.hero_select.currentText()]
        for (rank, item_name_list) in data.items():
            btn = QPushButton()
            btn.setText(f"Rank {rank}")
            btn.setCheckable(True)
            btn.setStyleSheet('font: 14pt "ONE Mobile POP";')
            table.setCellWidget(rank-1, 0, btn)
            for col_idx, name in enumerate(item_name_list):
                mini_btn = QPushButton()
                mini_btn.setStyle(wrapStyle())
                mini_btn.setStyleSheet('font: 11pt "ONE Mobile POP";')
                mini_btn.setCheckable(True)
                mini_btn.setText(name)
                mini_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                table.setCellWidget(rank-1, col_idx+1, mini_btn)
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

        # When you click self.go_left_btn/self.go_right_btn,
        # increment/decrement self.hero_select's index by 1
        self.go_left_btn.clicked.connect(partial(self.changeHeroSelectIndex, -1))
        self.go_right_btn.clicked.connect(partial(self.changeHeroSelectIndex, 1))

        # Pressing the right/left arrow key while focusing on the table
        # has the same effect as clicking go_right/left_btn
        table.keyPressEvent = lambda event: self.changeHeroSelectIndex(1) if event.key()==Qt.Key.Key_Right else self.changeHeroSelectIndex(-1) if event.key()==Qt.Key.Key_Left else None


    # Update the table according to the current index of self.hero_select
    def updateCurrentEquipTalbe(self):
        data = self.name_to_equip_data[self.hero_select.currentText()]
        table = self.rank_table

        for (rank, item_name_list) in data.items():
            for col_idx, name in enumerate(item_name_list):
                mini_btn: QPushButton = table.cellWidget(rank-1, col_idx+1)
                mini_btn.setText(name)

        cur_idx = self.hero_select.currentIndex()
        self.go_left_btn.setEnabled(cur_idx!=0)
        self.go_right_btn.setEnabled(cur_idx!=self.hero_select.count()-1)
    

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