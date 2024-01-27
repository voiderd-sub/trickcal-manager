from widgets.ui.page_equip_1 import Ui_page_equip_1
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHeaderView, QSizePolicy, QTableWidgetItem, QWidget, QAbstractItemView,
                                    QPushButton, QToolButton)

import sqlite3
from functools import partial


class PageEquip1(Ui_page_equip_1, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyle("widgets/style/style_page_equip_1.qss")
        self.setInitialState()        # Settings in main.py
        
    
    def setStyle(self, path):
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
        table.setRowCount(max_rank)
        table.setColumnCount(13)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        horizontal_header = table.horizontalHeader()
        horizontal_header.hide()
        table.verticalHeader().hide()

        # load names from db (with right order)
        cur.execute("""
            select name_kr
            from hero h
            order by personality asc, star_intrinsic desc, name_kr asc
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
            btn.setStyleSheet('font: 12pt "ONE Mobile POP";')
            table.setCellWidget(rank-1, 0, btn)
            for col_idx, name in enumerate(item_name_list):
                mini_btn = QToolButton()
                mini_btn.setCheckable(True)
                mini_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                table.setCellWidget(rank-1, col_idx*2+1, mini_btn)
                # when mini_btn clicked, if all mini_btns in the same row are checked, check the button in the first column
                # also, check mini_btn itself
                mini_btn.clicked.connect(partial(self.checkButton, btn))

                item = QTableWidgetItem(name)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(rank-1, col_idx*2+2, item)
            btn.clicked.connect(partial(self.checkAll, btn))
            table.setRowHeight(rank-1, 50)
        self.go_left_btn.setEnabled(False)

        for i in range(13):
            if i%2==0:
                horizontal_header.setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                horizontal_header.setSectionResizeMode(i, QHeaderView.Fixed)
        for col_idx in range(6):
            table.setColumnWidth(col_idx*2+1, 30)

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
                item = QTableWidgetItem(name)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(rank-1, col_idx*2+2, item)

        cur_idx = self.hero_select.currentIndex()
        self.go_left_btn.setEnabled(cur_idx!=0)
        self.go_right_btn.setEnabled(cur_idx!=self.hero_select.count()-1)
    

    # When a button is in the checked state, all checkboxes in the same row are checked.
    # When a button becomes unchecked, all checkboxes in the same row are unchecked.
    def checkAll(self, btn):
        table = self.rank_table
        row = table.indexAt(btn.pos()).row()
        for col_idx in range(1, 13, 2):
            table.cellWidget(row, col_idx).setChecked(btn.isChecked())
    
    def checkButton(self, btn):
        table = self.rank_table
        row = table.indexAt(btn.pos()).row()
        for col_idx in range(1, 13, 2):
            if not table.cellWidget(row, col_idx).isChecked():
                btn.setChecked(False)
                return
        btn.setChecked(True)


    # Change the index only when it is within a valid index range.
    def changeHeroSelectIndex(self, num):
        if 0<=self.hero_select.currentIndex()+num<self.hero_select.count():
            self.hero_select.setCurrentIndex(self.hero_select.currentIndex()+num)