from widgets.ui.page_crayon_abstract import Ui_page_crayon_abstract

from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PageCrayonAbstract(Ui_page_crayon_abstract, QWidget):
    def __init__(self, parent=None):
        super(PageCrayonAbstract, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        self.reload = {"master": True}

        res = self.window().resource
        stat = res.masterGet("Stat")
        for name_kr, name_en in stat.values():
            container = getattr(self, "container"+name_en)
            container.setIcon(name_en)
            container.setTexts({"name": name_kr})

        icon_size = 40
        for widget in self.currency_widget.findChildren(QLabel):
            if widget.objectName().startswith("Icon"):
                currency_name = widget.objectName()[4:]
                pixmap = QPixmap(f"icon/currency/{currency_name}.png")
                pixmap = pixmap.scaled(icon_size, icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                widget.setPixmap(pixmap)
                widget.setFixedSize(icon_size, icon_size)


    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        res = self.window().resource
        user_board = res.userGet("UserBoard")
        board_type = res.masterGet("BoardType")
        board_cost = res.masterGet("BoardCost")
        hero_id_to_board_data = res.masterGet("HeroIdToBoardData")
        stat = res.masterGet("Stat")
        board_stat = res.masterGet("BoardStat")

        num_board_areas = len(board_type[1]["num_crayon_type"][1])
        num_crayon_types = len(board_type[1]["num_crayon_type"])

        num_painted_board = [[0]*num_crayon_types for _ in range(num_board_areas)]
        num_gateways = [0] * (num_board_areas - 1)
        num_apply_all = [[0]*2 for _ in range(len(stat))]
        for hero_id, user_board_data in user_board.items():
            board_status = user_board_data[0]
            board_id = hero_id_to_board_data[hero_id][0]
            apply_all_stats = hero_id_to_board_data[hero_id][1]
            num_crayon_per_each_area = board_type[board_id]["num_crayon_type"] # (num_crayons * num_areas)
            for (currency_idx, status) in enumerate(board_status):
                if currency_idx == 0:
                    for i, painted in enumerate(status):
                        num_gateways[i] += painted
                else:
                    area_idx = 1
                    for board_cell_idx, painted in enumerate(status, start=1):
                        if board_cell_idx > num_crayon_per_each_area[currency_idx-1][area_idx-1]:
                            area_idx += 1
                        num_painted_board[area_idx-1][currency_idx-1] += painted
                    
                        if currency_idx >= 3:
                            num_apply_all[apply_all_stats[(board_cell_idx-1)%5]-1][currency_idx-3] += painted
        
        gold_paint = 0
        gold_gateway = 0
        crayons = [0] * num_crayon_types
        for area_idx, num in enumerate(num_gateways, start=2):
            gold_gateway += num * board_cost[(area_idx, 0)][0]
        
        for area_idx in range(len(num_painted_board)):
            for crayon_type_idx in range(len(num_painted_board[area_idx])):
                num = num_painted_board[area_idx][crayon_type_idx]
                for k, cost in enumerate(board_cost[(area_idx+1, crayon_type_idx+1)]):
                    if k == 0:
                        gold_paint += num * cost
                    else:
                        crayons[k-1] += num * cost

        self.ValueGold.setText(f"{gold_paint+gold_gateway:,}")
        self.ValueCellGold.setText(f"{gold_paint:,}")
        self.ValueGatewayGold.setText(f"{gold_gateway:,}")
        for idx, num in enumerate(crayons):
            getattr(self, f"ValueCrayon{idx+1}").setText(f"{num:,}")

        num_attack = num_apply_all[1][1] + num_apply_all[2][1]
        num_apply_all[1][1] = num_apply_all[2][1] = num_attack
        
        for idx in range(len(stat)):
            stat_name = stat[idx+1][1]
            num_purple, num_gold = num_apply_all[idx]
            stat_purple = f"+{num_purple * board_stat[(idx+1, True, 3)]}"
            stat_gold = f"×{1 + 0.01 * num_gold * board_stat[(idx+1, True, 4)]:.2f}"
            values = {"num_purple": f"{num_purple}개", "num_gold": f"{num_gold}개", "stat_purple": stat_purple, "stat_gold": stat_gold}
            getattr(self, f"container{stat_name}").setTexts(values)
        
        self.reload = dict()
