from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QLabel,
                               QTableWidgetItem, QVBoxLayout, QWidget, QComboBox)

from ui.sidebar import Ui_sidebar
from ui.hero_window import Ui_hero_window
from ui.equip_window_1 import Ui_equip_window_1

from functools import partial
import sqlite3

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
    
    def combo_add(self, num):
        self.comboBox.addItems(["미보유"]+[str(i) for i in range(num, 6)])

        # Align center
        for i in range(self.comboBox.count()):
            self.comboBox.setItemData(i, Qt.AlignmentFlag.AlignCenter, Qt.UserRole.TextAlignmentRole)
    
    def combo_set_star(self, star_in, star_ex):
        if star_ex is None:
            return
        else:
            self.comboBox.setCurrentIndex(star_ex-star_in+1)


class Sidebar(Ui_sidebar, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)              # Settings in Qt Designer
        self.set_initial_state()        # Settings in main.py
        self.set_style("ui/style_sidebar.qss")
        self.setParent(parent)
    
    def set_style(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())
    
    def set_initial_state(self):
        # define main buttons & sub buttons
        self.main_btn_dict = dict()
        self.sub_menu_dict = dict()
        self.menu_names = ["home", "hero", "equip", "crayon", "food", "lab"]

        f = lambda x: [x[0]+"_sub_btn_"+str(i) for i in range(1, x[1]+1)]
        self.btn_with_pages = ["home_btn", "hero_btn"]\
                            + f(("equip",3)) + f(("crayon",2)) + f(("food",3)) + f(("lab",3))
        
        for name in self.menu_names:
            self.main_btn_dict[name] = getattr(self, name+"_btn")
            self.sub_menu_dict[name] = getattr(self, name+"_sub") if hasattr(self, name+"_sub") else None

        self.home_btn.setChecked(True)
        for name in self.menu_names:
            btn = self.main_btn_dict[name]
            sub = self.sub_menu_dict[name]

            if not sub is None:
                sub.hide()
            btn.clicked.connect(partial(self.show_submenu, clicked_menu_name=name))
    
    def show_submenu(self, clicked_menu_name):
        for name in self.menu_names:
            sub = self.sub_menu_dict[name]
            if sub is None:
                pass
            elif name==clicked_menu_name:
                # Turn off the property exclusive temporary to uncheck all submenus
                group = getattr(self, name+"_group")
                group.setExclusive(False)
                for btn in group.buttons():
                    btn.setChecked(False)
                group.setExclusive(True)
                sub.show()
            else:
                sub.hide()



class HeroWindow(Ui_hero_window, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)              # Settings in Qt Designer
        self.set_initial_state()        # Settings in main.py
        self.set_style("ui/style_hero_window.qss")
        self.setParent(parent)
    
    def set_style(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())
    
    def set_initial_state(self):
        table = self.hero_table
        self.hero_name_to_id = dict()
        self.hero_name_to_original_star_ex = dict()

        self.conn_master = sqlite3.connect("db/master.db")
        self.conn_user = sqlite3.connect("db/userdata.db")
        cur = self.conn_master.cursor()

        cur.execute('attach database "db/userdata.db" as user_db')
        cur.execute("""
            select id, name_en, name_kr, star_intrinsic, star_extrinsic
            from hero h
            left outer join user_db.user_hero uh
            on (h.id=uh.hero_id)
            order by personality asc, star_intrinsic desc, name_kr asc
        """)

        for idx, (id, name_en, name_kr, star_in, star_ex) in enumerate(cur):
            table.insertRow(idx)
            label = QLabel(table)
            label.setText("")
            label.setScaledContents(True)
            pixmap = QPixmap()
            pixmap.load(f"icon/hero/{name_en}.png")
            label.setPixmap(pixmap)
            table.setCellWidget(idx, 0, label)
            
            item = QTableWidgetItem(name_kr)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(idx, 1, item)

            combo_widget = HeroWindowComboBox()
            combo_widget.combo_add(star_in)
            combo_widget.combo_set_star(star_in, star_ex)
            table.setCellWidget(idx, 2, combo_widget)

            self.hero_name_to_id[name_kr] = id
            self.hero_name_to_original_star_ex[name_kr] = "미보유" if star_ex is None else str(star_ex)

        table.setColumnWidth(0, 100)
        for col in range(1,3):
            table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)

        self.star_1_btn.clicked.connect(partial(self.setSpecificStarValues, 1))
        self.star_2_btn.clicked.connect(partial(self.setSpecificStarValues, 2))
        self.all_check_btn.clicked.connect(self.setAllStarValues)
        self.all_uncheck_btn.clicked.connect(self.uncheckAll)

        self.save_btn.clicked.connect(self.saveExtrinsicStars)
        self.undo_btn.clicked.connect(self.undo)
        
    
    def setSpecificStarValues(self, num):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유" and item.count() + num == 7:
                item.setCurrentIndex(1)
    
    def setAllStarValues(self):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유":
                item.setCurrentIndex(1)
    
    def saveExtrinsicStars(self):
        cur = self.conn_user.cursor()
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            text = item.currentText()
            self.hero_name_to_original_star_ex[self.hero_table.item(i,1).text()] = text
            idx = self.hero_name_to_id[self.hero_table.item(i,1).text()]
            if text=="미보유":
                cur.execute("delete from user_hero where hero_id=?",(idx,))
            else:
                cur.execute("REPLACE INTO user_hero(hero_id, star_extrinsic) VALUES(?,?)",(idx, int(text)))
        self.conn_user.commit()

    def uncheckAll(self):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            item.setCurrentIndex(0)

    def undo(self):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            original_ex = self.hero_name_to_original_star_ex[self.hero_table.item(i,1).text()]
            item.setCurrentText(original_ex)
    
    def closeDBconn(self):
        if hasattr(self, "conn_user"):
            cur = self.conn_user.cursor()
            cur.execute("vacuum")
        
        for conn in ["conn_master", "conn_user"]:
            if hasattr(self, conn):
                getattr(self, conn).close()


class EquipWindow1(Ui_equip_window_1, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)              # Settings in Qt Designer
        # self.set_initial_state()        # Settings in main.py
        # self.set_style("ui/style_hero_window.qss")
        self.setParent(parent)