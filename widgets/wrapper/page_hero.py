from widgets.ui.page_hero import Ui_page_hero

from PySide6.QtWidgets import (QComboBox, QHeaderView, QLabel, QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

import sqlite3
from functools import partial

class NonScrollComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()



class HeroWindowComboBox(QWidget):
    def __init__(self, parent=None):
        super(HeroWindowComboBox, self).__init__(parent)
        self.comboBox = NonScrollComboBox(self)

        # Align item to center
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setReadOnly(True)
        self.comboBox.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.comboBox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


    def comboAdd(self, num):
        self.comboBox.addItems(["미보유"]+[str(i) for i in range(num, 6)])
        # Align center
        for i in range(self.comboBox.count()):
            self.comboBox.setItemData(i, Qt.AlignmentFlag.AlignCenter, Qt.UserRole.TextAlignmentRole)


    def comboSetStar(self, star_in, star_ex):
        if star_ex is None:
            self.comboBox.setCurrentIndex(0)
        else:
            self.comboBox.setCurrentIndex(star_ex-star_in+1)



class PageHero(Ui_page_hero, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyle("widgets/style/style_page_hero.qss")
        self.setInitialState()        # Settings in main.py


    def setStyle(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())


    def setInitialState(self):
        table = self.hero_table
        self.hero_name_to_id = dict()
        self.hero_name_to_original_star_ex = dict()
        
        main_window = self.window()
        cur: sqlite3.Cursor = main_window.conn_user.cursor()

        cur.execute(f'attach database "db/master.db" as master_db')
        cur.execute("""
            select id, name_en, name_kr, star_intrinsic, star_extrinsic
            from master_db.hero h
            left outer join user_hero uh
            on (h.id=uh.hero_id)
            order by personality asc, star_intrinsic desc, name_kr asc
        """)

        for idx, (id, name_en, name_kr, star_in, star_ex) in enumerate(cur):
            table.insertRow(idx)
            table.setRowHeight(idx, 130)
            label = QLabel(table)
            label.setText("")
            label.setScaledContents(True)
            label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
            pixmap = QPixmap()
            pixmap.load(f"icon/hero/{name_en}.png")
            label.setPixmap(pixmap)
            table.setCellWidget(idx, 0, label)
            
            item = QTableWidgetItem(name_kr)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(idx, 1, item)

            combo_widget = HeroWindowComboBox()
            combo_widget.comboAdd(star_in)
            combo_widget.comboSetStar(star_in, star_ex)
            table.setCellWidget(idx, 2, combo_widget)

            self.hero_name_to_id[name_kr] = id
            self.hero_name_to_original_star_ex[name_kr] = "미보유" if star_ex is None else str(star_ex)
        
        for col in range(1,3):
            table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table.verticalHeader().hide()
        table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
        table.resizeColumnsToContents()
        table.setColumnWidth(0, 130)

        self.star_1_btn.clicked.connect(partial(self.setSpecificStarValues, 1))
        self.star_2_btn.clicked.connect(partial(self.setSpecificStarValues, 2))
        self.all_check_btn.clicked.connect(self.setAllStarValues)
        self.all_uncheck_btn.clicked.connect(self.uncheckAll)

        self.save_btn.clicked.connect(self.saveExtrinsicStars)
        self.undo_btn.clicked.connect(self.undo)


    def updateTable(self):
        table = self.hero_table
        main_window = self.window()
        cur: sqlite3.Cursor = main_window.conn_user.cursor()

        cur.execute(f'attach database "db/master.db" as master_db')
        cur.execute("""
            select name_kr, star_intrinsic, star_extrinsic
            from master_db.hero h
            left outer join user_hero uh
            on (h.id=uh.hero_id)
            order by personality asc, star_intrinsic desc, name_kr asc
        """)
        for idx, (name_kr, star_in, star_ex) in enumerate(cur):
            table.cellWidget(idx,2).comboSetStar(star_in, star_ex)
            self.hero_name_to_original_star_ex[name_kr] = "미보유" if star_ex is None else str(star_ex)


    def setSpecificStarValues(self, num):
        for i in range(self.hero_table.rowCount()):
            item: NonScrollComboBox = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유" and item.count() + num == 7:
                item.setCurrentIndex(1)
    

    def setAllStarValues(self):
        for i in range(self.hero_table.rowCount()):
            item: NonScrollComboBox = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유":
                item.setCurrentIndex(1)
    

    def saveExtrinsicStars(self):
        conn_user: sqlite3.Connection = self.window().conn_user
        cur = conn_user.cursor()
        for i in range(self.hero_table.rowCount()):
            item: NonScrollComboBox = self.hero_table.cellWidget(i,2).comboBox
            text = item.currentText()
            self.hero_name_to_original_star_ex[self.hero_table.item(i,1).text()] = text
            idx = self.hero_name_to_id[self.hero_table.item(i,1).text()]
            if text=="미보유":
                cur.execute("delete from user_hero where hero_id=?",(idx,))
            else:
                cur.execute("REPLACE INTO user_hero(hero_id, star_extrinsic) VALUES(?,?)",(idx, int(text)))
        conn_user.commit()


    def uncheckAll(self):
        for i in range(self.hero_table.rowCount()):
            item: NonScrollComboBox = self.hero_table.cellWidget(i,2).comboBox
            item.setCurrentIndex(0)


    def undo(self):
        for i in range(self.hero_table.rowCount()):
            item: NonScrollComboBox = self.hero_table.cellWidget(i,2).comboBox
            original_ex = self.hero_name_to_original_star_ex[self.hero_table.item(i,1).text()]
            item.setCurrentText(original_ex)