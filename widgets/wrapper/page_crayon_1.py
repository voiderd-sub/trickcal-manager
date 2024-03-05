from widgets.ui.page_crayon_1 import Ui_page_crayon_1

from PySide6.QtWidgets import QWidget, QAbstractItemView, QPushButton, QTableWidgetItem, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class PageCrayon1(Ui_page_crayon_1, QWidget):
    def __init__(self, parent=None):
        super(PageCrayon1, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        self.reload = dict()
        main = self.window()
        res = main.resource

        table = self.board_table
        table.setRowCount(7)
        table.setColumnCount(37)
        self.setupTable()
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        table.horizontalHeader().hide()
        table.verticalHeader().hide()
        # set all cell size to 50*50
        for i in range(37):
            table.setColumnWidth(i, 50)
        for i in range(7):
            table.setRowHeight(i, 50)

        # setup hero select & currency_widget
        self.hero_select.currentIndexChanged.connect(self.updateCurrentBoardTable)
        self.updateHeroList()
        self.hero_select.setCurrentIndex(0)

        icon_size = 40
        for widget in self.currency_widget.findChildren(QLabel):
            if widget.objectName().startswith("Icon"):
                currency_name = widget.objectName()[4:]
                pixmap = QPixmap(f"icon/currency/{currency_name}.png")
                pixmap = pixmap.scaled(icon_size, icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                widget.setPixmap(pixmap)
                widget.setFixedSize(icon_size, icon_size)

        self.updateCurrentBoardTable()


    def setupTable(self):
        for i in range(7):
            for j in range(37):
                item = QTableWidgetItem()
                self.board_table.setItem(i, j, item)
                item.setTextAlignment(Qt.AlignCenter)


    def updateCurrentBoardTable(self):
        res = self.window().resource
        hero_name = self.hero_select.currentText()
        hero_id = res.masterGet("HeroNameToId")[hero_name]
        board_id, board_stats = res.masterGet("HeroIdToBoardData")[hero_id]
        board_sequence = res.masterGet("BoardType")[board_id]
        statshort = res.masterGet("StatShort")

        table = self.board_table
        table.clearContents()
        self.setupTable()
        for i in range(7):
            for j in range(37):
                item = table.item(i, j)
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
        
        col_idx = 0
        purple_idx = 0
        gold_idx = 0
        for i, seq in enumerate(board_sequence):
            if i % 2 == 0:
                if col_idx == 0:
                    item = table.item(7-int(seq), col_idx)
                    item.setText("→")
                    # set font size 20
                    font = item.font()
                    font.setPointSize(20)
                    item.setFont(font)
                    item.setFlags((item.flags() | Qt.ItemIsEnabled) & ~Qt.ItemIsEditable)
                else:
                    btn = QPushButton()
                    btn.setCheckable(True)
                    table.setCellWidget(int(seq)-1, col_idx, btn)
                    btn.setText("관문")
                col_idx += 1
            else:
                for (idx, cell_type) in enumerate(seq):
                    if cell_type != "0":
                        btn = QPushButton()
                        btn.setCheckable(True)
                        row_idx = 6 - idx % 7
                        tmp_col_idx = col_idx + idx // 7
                        table.setCellWidget(row_idx, tmp_col_idx, btn)
                        if cell_type == "3":
                            btn.setText(f"보크\n{statshort[board_stats[purple_idx]]}")
                            purple_idx = (purple_idx + 1) % 5
                        elif cell_type == "4":
                            stat_idx = board_stats[gold_idx]
                            if stat_idx == 2 or stat_idx == 3:
                                stat_name = "공격력"
                            else:
                                stat_name = statshort[stat_idx]
                            btn.setText(f"황크\n{stat_name}")
                            gold_idx = (gold_idx + 1) % 5
                col_idx += len(seq) // 7




    def updateHeroList(self):
        self.hero_select.blockSignals(True)
        hero_name_to_id = self.window().resource.masterGet("HeroNameToId")
        names = list(sorted(hero_name_to_id.keys()))
        self.hero_select.clear()
        self.hero_select.addItems(names)
        self.hero_select.blockSignals(False)


    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        if self.reload.get("account", False):
            self.user_equip_data_tmp = dict()
            self.last_hero_name = None
            self.updateGoalNameList()
        
        elif self.reload.get("master", False):
            self.setupTable()
            self.updateHeroList()
        
        elif self.reload.get("goal", False):
            self.updateGoalNameList()
        
        self.reload = dict()