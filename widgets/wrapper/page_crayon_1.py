from widgets.ui.page_crayon_1 import Ui_page_crayon_1
from widgets.wrapper.misc import DragCheckableButton

from PySide6.QtWidgets import (QWidget, QAbstractItemView, QPushButton, QTableWidgetItem,
                               QLabel, QTableWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from functools import partial


class PageCrayon1(Ui_page_crayon_1, QWidget):
    def __init__(self, parent=None):
        super(PageCrayon1, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        self.reload = {"master": True}
        main = self.window()
        res = main.resource

        self.purple_style = """QPushButton{
    border-width: 1px;
    border-style: solid;
    border-color: rgb(208,208,208);
	border-radius:5px;
	background-color: rgb(241,220,255);
}

QPushButton:hover{
	background-color: rgb(216,212,255);
    border-color: rgb(0,120,212);
}

QPushButton:pressed, QPushButton:checked{
	background-color: rgb(193,204,255);
    border-color: rgb(0,84,153);
}"""

        self.gold_style = """QPushButton{
    border-width: 1px;
    border-style: solid;
    border-color: rgb(208,208,208);
	border-radius:5px;
	background-color: rgb(255, 255, 127);
}

QPushButton:hover{
	background-color: rgb(229,243,198);
    border-color: rgb(0,120,212);
}

QPushButton:pressed, QPushButton:checked{
	background-color: rgb(204,232,204);
    border-color: rgb(0,84,153);
}"""
            

        board_sequence = res.masterGet("BoardType")[1]["seq"]
        rows, cols = len(board_sequence[0]), len(board_sequence)

        table = self.board_table
        table.setRowCount(rows)
        table.setColumnCount(cols)
        self.setupTable()
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        table.horizontalHeader().hide()
        table.verticalHeader().hide()
        # set all cell size to 50*50
        for i in range(cols):
            table.setColumnWidth(i, 50)
        for i in range(rows):
            table.setRowHeight(i, 50)

        self.last_hero_name = None

        # setup hero select & currency_widget
        self.hero_select.currentIndexChanged.connect(self.updateCurrentBoardTable)

        icon_size = 40
        for widget in self.currency_widget.findChildren(QLabel):
            if widget.objectName().startswith("Icon"):
                currency_name = widget.objectName()[4:]
                pixmap = QPixmap(f"icon/currency/{currency_name}.png")
                pixmap = pixmap.scaled(icon_size, icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                widget.setPixmap(pixmap)
                widget.setFixedSize(icon_size, icon_size)

        # same as page_equip_1
        self.go_left_btn.clicked.connect(partial(self.changeHeroSelectIndex, -1))
        self.go_right_btn.clicked.connect(partial(self.changeHeroSelectIndex, 1))


        # change wheel event of table to scroll horizontally; scroll 6 cells per 1 scroll
        table.setHorizontalScrollMode(QTableWidget.ScrollMode.ScrollPerPixel)
        table.wheelEvent = lambda event: table.horizontalScrollBar().setValue(
            table.horizontalScrollBar().value() - event.angleDelta().y() / 120 * 50 * 12)

        # initialize data for drag-to-select
        self.dragging = False
        self.drag_mode = None
        # set table's mouseMoveEvent to trigger drag-to-select
        table.mouseMoveEvent = self.mouseMoveEvent

        for i in range(1, 4):
            for target in ["normal", "special", "all"]:
                btn = getattr(self, f"select_{target}_{i}_btn")
                btn.clicked.connect(partial(self.easy_select, i, target))


    def setupTable(self):
        num_rows, num_cols = self.board_table.rowCount(), self.board_table.columnCount()
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem()
                self.board_table.setItem(i, j, item)
                item.setTextAlignment(Qt.AlignCenter)


    def updateCurrentBoardTable(self):
        res = self.window().resource
        hero_name = self.hero_select.currentText()
        hero_name_to_id = res.masterGet("HeroNameToId")
        if hero_name in hero_name_to_id:
            hero_id = hero_name_to_id[hero_name]            # last hero name may be None
        else:
            hero_id = hero_name_to_id[self.last_hero_name]  # last hero name != None
        board_id, purple_crayon, gold_crayon = res.masterGet("HeroIdToBoardData")[hero_id]
        board_sequence = res.masterGet("BoardType")[board_id]["seq"]
        num_cols = len(board_sequence)
        num_rows = len(board_sequence[0])
        statshort = res.masterGet("StatShort")
        user_board = res.userGet("UserBoard")
        board_cost = res.masterGet("BoardCost")

        if self.last_hero_name is not None:
            self.updateBoundary()

        # Initialize cur_hero_board_data
        if hero_id not in user_board:
            cnt_crayon = [-1, 0, 0, 0, 0]            # gateway, white, blue, purple, gold
            for i in range(num_cols):
                for j in range(num_rows):
                    seq = board_sequence[i][j]
                    if seq != 0:
                        cnt_crayon[seq%10] += 1
            user_board[hero_id] = (tuple([0] * cnt for cnt in cnt_crayon), [])

        table = self.board_table

        table.clearContents()
        self.setupTable()
        for i in range(num_rows):
            for j in range(num_cols):
                item = table.item(i, j)
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
        
        board_level = 0
        crayon_indices = [0] * 5
        self.costs = [0] * 5
        self.cost_gateway = 0
        self.board_buttons = [list() for _ in range(3)]     # HARD CODED
        board_cnt = 0

        for j in range(num_cols):
            for i in range(num_rows):
                seq = board_sequence[j][i]

                if seq == 0:
                    continue

                if seq == 10:
                    board_level += 1
                    if board_level == 1:
                        item = table.item(6-i, j)
                        item.setText("→")
                        font = item.font()
                        font.setPointSize(20)
                        item.setFont(font)
                        item.setFlags((item.flags() | Qt.ItemIsEnabled) & ~Qt.ItemIsEditable)
                    else:
                        btn = DragCheckableButton(parent=self, key=(board_level-1, 0))
                        board_cnt = 1
                        self.board_buttons[board_level-1].append((btn, seq))
                        table.setCellWidget(6-i, j, btn)
                        icon = QPixmap("icon/board/Gateway.png")
                        icon = icon.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                        btn.setIcon(icon)
                        btn.setIconSize(icon.rect().size())
                        if user_board[hero_id][0][0][crayon_indices[0]] == 1:
                            btn.setChecked(True)
                            self.cost_gateway += board_cost[(board_level, 0)][0]

                        clicked_fn = partial(self.updateResource, hero_id, board_level, 0, crayon_indices[0])
                        btn.toggled.connect(clicked_fn)
                        crayon_indices[0] += 1

                else:
                    btn = DragCheckableButton(parent=self, key=(board_level-1, board_cnt))
                    board_cnt += 1
                    self.board_buttons[board_level-1].append((btn, seq))
                    table.setCellWidget(6-i, j, btn)
                    if user_board[hero_id][0][seq][crayon_indices[seq]] == 1:
                        btn.setChecked(True)
                        for idx, item in enumerate(board_cost[(board_level, seq)]):
                            self.costs[idx] += item

                    if seq == 3:
                        btn.setText(f"{statshort[purple_crayon[crayon_indices[seq]]]}")
                        btn.setStyleSheet(self.purple_style)
                    elif seq == 4:
                        stat_idx = gold_crayon[crayon_indices[seq]]
                        if stat_idx == 2 or stat_idx == 3:
                            stat_name = "공격력"
                        else:
                            stat_name = statshort[stat_idx]
                        btn.setText(f"{stat_name}")
                        btn.setStyleSheet(self.gold_style)
                    clicked_fn = partial(self.updateResource, hero_id, board_level, seq, crayon_indices[seq])
                    btn.toggled.connect(clicked_fn)
                    crayon_indices[seq] += 1

        self.changeCostLabels()
        
        # 유효성 검사 및 last_hero_name 업데이트
        current_hero_name = self.hero_select.currentText()
        if current_hero_name in hero_name_to_id:
            self.last_hero_name = current_hero_name
        else:
            # Invalid hero name detected; changing text to last hero name
            self.hero_select.setCurrentText(self.last_hero_name)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down:
            self.changeHeroSelectIndex(1)
        elif event.key() == Qt.Key.Key_Up:
            self.changeHeroSelectIndex(-1)
        elif event.key() == Qt.Key.Key_Right:
            self.board_table.horizontalScrollBar().setValue(self.board_table.horizontalScrollBar().value() + 600)
        elif event.key() == Qt.Key.Key_Left:
            self.board_table.horizontalScrollBar().setValue(self.board_table.horizontalScrollBar().value() - 600)

    
    def buttonPressed(self, key):
        board_level, idx = key
        btn, seq = self.board_buttons[board_level][idx]
        btn.setChecked(not btn.isChecked())
        self.dragging = True
        self.drag_mode = 'select' if btn.isChecked() else 'deselect'
    
    def buttonReleased(self, key):
        self.dragging = False
        self.drag_mode = None
    
    def mouseMoveEvent(self, event):
        if self.dragging:
            button = self.board_table.childAt(event.position().toPoint())
            # check button is real button or not
            if button and isinstance(button, DragCheckableButton):
                if self.drag_mode == 'select':
                    button.setChecked(True)
                elif self.drag_mode == 'deselect':
                    button.setChecked(False)
    
    def easy_select(self, board_level, target):
        target_seqs = [1, 2, 3, 4] if target == "all" else ([3, 4] if target == "special" else [1, 2])
        if board_level >= 2 and target != "special":
            target_seqs.append(10)
        target_btns = [btn for btn, seq in self.board_buttons[board_level-1] if seq in target_seqs]
        
        toCheck = not all(btn.isChecked() for btn in target_btns)
        for btn in target_btns:
            btn.setChecked(toCheck)


    def changeHeroSelectIndex(self, num):
        if 0<=self.hero_select.currentIndex()+num<self.hero_select.count():
            self.hero_select.setCurrentIndex(self.hero_select.currentIndex()+num)
        self.board_table.horizontalScrollBar().setValue(0)


    def updateHeroList(self):
        self.hero_select.blockSignals(True)
        hero_name_to_id = self.window().resource.masterGet("HeroNameToId")
        names = list(sorted(hero_name_to_id.keys()))
        self.hero_select.clear()
        self.hero_select.addItems(names)
        self.hero_select.setCurrentIndex(0)
        self.hero_select.blockSignals(False)


    def updateResource(self, hero_id, level, crayon_type, idx, value):
        res = self.window().resource
        user_board = res.userGet("UserBoard")
        board_cost = res.masterGet("BoardCost")
        old_value = user_board[hero_id][0][crayon_type][idx]
        user_board[hero_id][0][crayon_type][idx] = int(value)
        if crayon_type == 0:
            self.cost_gateway += board_cost[(level, 0)][0] * (value - old_value)
        else:
            for i in range(len(self.costs)):
                self.costs[i] += board_cost[(level, crayon_type)][i] * (value - old_value)
        self.changeCostLabels()


    def changeCostLabels(self):
        for idx, cost in enumerate(self.costs):
            if idx==0:
                self.ValueGold.setText(f"{cost + self.cost_gateway:,}")
                self.ValueEraserGold.setText("0")
            else:
                getattr(self, f"ValueCrayon{idx}").setText(f"{cost:,}")


    def updateBoundary(self):
        # boundary : The current cell is selected & there are unselected cells among neighboring cells
        res = self.window().resource
        table = self.board_table
        table_rows, table_cols = table.rowCount(), table.columnCount()
        last_hero_id = res.masterGet("HeroNameToId")[self.last_hero_name]
        last_hero_board_id = res.masterGet("HeroIdToBoardData")[last_hero_id][0]
        first_gate_coordinate = res.masterGet("BoardType")[last_hero_board_id]["gates"][0]
        user_board = res.userGet("UserBoard")
        boundary_coordinates = []
        hero_name = res.masterGet("HeroIdToMetadata")[last_hero_id]["name_kr"]

        def is_valid(x, y):
            return 0 <= x < table_rows and 0 <= y < table_cols and table.cellWidget(x, y) is not None
        
        def is_checked(x, y):
            if (y, 6-x) == first_gate_coordinate:
                return True
            widget = table.cellWidget(x, y)
            if widget is None:
                return False
            return widget.isChecked()

        for i in range(table_rows): #7
            for j in range(table_cols): #37
                if is_checked(i, j):
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if is_valid(x, y) and not is_checked(x, y):
                            boundary_coordinates.append((j, 6-i))
                            break

        user_board[last_hero_id][1].clear()
        user_board[last_hero_id][1].extend(boundary_coordinates)



    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        if self.reload.get("master", False):
            self.last_hero_name = None
            self.updateHeroList()
            self.updateCurrentBoardTable()

        elif self.reload.get("account", False):
            self.last_hero_name = None
            self.updateCurrentBoardTable()
        
        self.reload = dict()
    

    def savePageData(self):
        # save current pages' boundary data

        current_hero_name = self.hero_select.currentText()
        hero_name_to_id = self.window().resource.masterGet("HeroNameToId")
        
        if current_hero_name in hero_name_to_id:
            self.last_hero_name = current_hero_name
        else:
            # Invalid hero name detected; changing text to last hero name
            self.hero_select.setCurrentText(self.last_hero_name)

        self.updateBoundary()
        
        main = self.window()
        main.changeBoardCascade()