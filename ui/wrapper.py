from PySide6.QtCore import Qt, QRegularExpression, QSortFilterProxyModel
from PySide6.QtGui import QPixmap, QValidator, QRegularExpressionValidator
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QLabel, QCheckBox,
                               QTableWidgetItem, QVBoxLayout, QWidget, QComboBox, QMainWindow,
                               QListWidgetItem, QCompleter, QAbstractItemView,
                               QPushButton, QToolButton)

from ui.sidebar import Ui_sidebar
from ui.page_hero import Ui_page_hero
from ui.page_equip_1 import Ui_page_equip_1
from ui.account_settings import Ui_AccountSettings

from functools import partial
import sqlite3


"""
!WARNING!
Be sure to call in the following order: setParent -> setupUi -> setStyle -> setInitialState
Fatal bugs occur when the order is changed
"""


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


class Sidebar(Ui_sidebar, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyle("ui/style_sidebar.qss")
        self.setInitialState()        # Settings in main.py
        
    
    def setStyle(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())
    
    def setInitialState(self):
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
            btn.clicked.connect(partial(self.showSubmenu, clicked_menu_name=name))
        
        config = self.window().config
        self.updateLocalAccountList(config["account_list"], config["cur_account_idx"])
        self.account_select_btn.clicked.connect(self.changeAccount)
        self.account_setting_btn.clicked.connect(self.openAccountSettings)
        
    def showSubmenu(self, clicked_menu_name):
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
    
    def changeAccount(self):
        main_window = self.window()
        config = main_window.config
        selected_idx = self.account_list.currentIndex()
        if selected_idx != config["cur_account_idx"]:
            config["cur_account_idx"] = selected_idx
            main_window.conn_user.close()
            del main_window.conn_user
            main_window.changeAccount()
    
    def updateLocalAccountList(self, account_list, idx=0):
        self.account_list.clear()
        self.account_list.addItems(account_list)
        self.account_list.setCurrentIndex(idx)

    def openAccountSettings(self):
        main_window = self.window()
        new_window: QMainWindow = main_window.account_settings
        new_window.tmp_account_list = main_window.config["account_list"].copy()
        new_window.show()


class AccountSettings(Ui_AccountSettings, QMainWindow):
    def __init__(self):
        super(AccountSettings, self).__init__()
        self.setupUi(self)
        self.setStyle("ui/style_account_settings.qss")
        self.setInitialState()

    def setStyle(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())
    
    def setInitialState(self):
        regex = QRegularExpression("[ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9 ]+")
        validator = QRegularExpressionValidator(regex, self.account_name_line)
        self.account_name_line.setValidator(validator)

        self.add_btn.clicked.connect(self.addAccount)
        self.cancel_btn.clicked.connect(self.cancelUpdate)
        self.save_btn.clicked.connect(self.saveAccountSettings)
    
    def updateLocalAccountList(self, account_list):
        self.account_list.clear()
        for name in account_list:
            item = QCheckBox(name)
            list_item = QListWidgetItem()
            self.account_list.addItem(list_item)
            self.account_list.setItemWidget(list_item, item)
    
    def saveAccountSettings(self):
        self.main.config["account_list"] = self.tmp_account_list
        self.main.updateAccountList()
        self.close()
    
    def addAccount(self):
        name = self.account_name_line.text()
        if len(name)>=1:
            self.tmp_account_list.append(name)
            self.account_name_line.clear()
            self.updateLocalAccountList(self.tmp_account_list)
    
    def cancelUpdate(self):
        self.updateLocalAccountList(self.main.config["account_list"])
        self.account_name_line.clear()
        self.close()


class PageHero(Ui_page_hero, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyle("ui/style_page_hero.qss")
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
            item = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유" and item.count() + num == 7:
                item.setCurrentIndex(1)
    
    def setAllStarValues(self):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            if item.currentText() == "미보유":
                item.setCurrentIndex(1)
    
    def saveExtrinsicStars(self):
        conn_user: sqlite3.Connection = self.window().conn_user
        cur = conn_user.cursor()
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
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
            item = self.hero_table.cellWidget(i,2).comboBox
            item.setCurrentIndex(0)

    def undo(self):
        for i in range(self.hero_table.rowCount()):
            item = self.hero_table.cellWidget(i,2).comboBox
            original_ex = self.hero_name_to_original_star_ex[self.hero_table.item(i,1).text()]
            item.setCurrentText(original_ex)


class PageEquip1(Ui_page_equip_1, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setStyle("ui/style_page_equip_1.qss")
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

        for i in range(13):
            if i%2==0:
                horizontal_header.setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                horizontal_header.setSectionResizeMode(i, QHeaderView.Fixed)

        for col_idx in range(6):
            table.setColumnWidth(col_idx*2+1, 30)

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