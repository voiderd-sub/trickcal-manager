from widgets.ui.page_crayon_2 import Ui_page_crayon_2

from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QTabWidget, QLabel


class PageCrayon2(Ui_page_crayon_2, QWidget):
    def __init__(self, parent=None):
        super(PageCrayon2, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()


    def setInitialState(self):
        self.reload = {"master": True}
        res = self.window().resource
        stat = res.masterGet("Stat")

        for tab_name in ("gold", "purple"):
            tab = getattr(self, f"tab_{tab_name}")
            layout = QVBoxLayout(tab)
            layout.setContentsMargins(0, 10, 0, 0)

            # add another tab widget in layout
            subtab = QTabWidget(tab)
            font = subtab.font()
            font.setPointSize(13)
            subtab.setFont(font)

            stat_names = [stat[i][0] for i in range(1, len(stat)+1)]
            if tab_name == "gold":
                stat_names = stat_names[:1] + ["공격력"] + stat_names[3:]
            for i, stat_name in enumerate(stat_names):
                subwidget = QScrollArea()
                subwidget.setWidgetResizable(True)
                subtab.addTab(subwidget, stat_name)
                scroll_container = QWidget(self)
                subwidget.setWidget(scroll_container)
                sublayout = QVBoxLayout(scroll_container)
                scroll_container.setLayout(sublayout)
                sublayout.setContentsMargins(10, 10, 10, 10)
                sublayout.setSpacing(10)
                setattr(self, f"scroll_{tab_name}_{i}", scroll_container)
            layout.addWidget(subtab)
            setattr(self, f"subtab_{tab_name}", subtab)


    def getMinPath(self, start, level, boundary, gate_points, gate_selected, board_type_id):
        res = self.window().resource
        board_min_cost_path = res.masterGet("BoardMinCostPath")
        cost_path_list = []
        for end in boundary:
            level_end = 1 if end[0] < gate_points[1][0] else 2 if end[0] < gate_points[2][0] else 3
            if level == level_end:
                cost, path = board_min_cost_path[board_type_id][start][end]
                cost_path_list.append((cost, path))
            elif level > level_end:
                cost = 0
                path = []
                path_points = [start]
                for lv_cursor in range(level, level_end, -1):
                    path_points.append(gate_points[lv_cursor-1])
                    cost += (1-gate_selected[lv_cursor-2]) * (lv_cursor-1) * 100  # adjust cost with opened gates
                path_points.append(end)
                for i in range(len(path_points)-1):
                    partial_cost, partial_path = board_min_cost_path[board_type_id][path_points[i]][path_points[i+1]]
                    cost += partial_cost
                    path.extend(partial_path[:-1])
                cost_path_list.append((cost, path))
            else: # level < level_end
                continue # Never gonna be minimum path
        
        cost_path_list.sort(key=lambda x: x[0])
        return cost_path_list[0]


    def updateGoldCrayon(self):
        res = self.window().resource
        stat = res.masterGet("Stat")
        board_type = res.masterGet("BoardType")
        board_cost = res.masterGet("BoardCost")
        hero_id_to_metadata = res.masterGet("HeroIdToMetadata")
        hero_id_to_board_data = res.masterGet("HeroIdToBoardData")
        user_board = res.userGet("UserBoard")
        
        # clear all widgets in all scroll area (in gold tab)
        for i in range(0, self.subtab_gold.count()):
            subtab = getattr(self, f"scroll_gold_{i}")
            sublayout = subtab.layout()
            for j in reversed(range(sublayout.count())):
                sublayout.itemAt(j).widget().deleteLater()
        
        # make data for each stat
        min_paths = [list() for _ in range(self.subtab_gold.count())]
        already_selected = [list() for _ in range(self.subtab_gold.count())]
    
        for hero_id in hero_id_to_metadata:
            hero_name = hero_id_to_metadata[hero_id]["name_kr"]
            hero_board_type_id, purple_crayon_list, gold_crayon_list = hero_id_to_board_data[hero_id]
            hero_board_type_data = board_type[hero_board_type_id]
            start_points = hero_board_type_data["start_points"][4]      # 4 is for gold
            gate_points = hero_board_type_data["gates"]
            point_to_idx = hero_board_type_data["point_to_idx"]
            if hero_id in user_board:
                board_selected, boundary = user_board[hero_id]
                # if boundary is empty, it means that the hero's board is completed; so, skip this hero
                if not boundary:
                    # print(f"{hero_name} is completed")
                    continue
            else:
                board_selected = [[0]*2] + [[0] * i[-1] for i in hero_board_type_data["num_crayon_type"]]
                boundary = gate_points[:1]
            gate_selected = board_selected[0]
            board_selected = board_selected[4]      # 4 is for gold

            stat_cursor = 0
            for level, point_list in enumerate(start_points, 1):
                for point in point_list:
                    stat_idx = gold_crayon_list[stat_cursor]
                    stat_idx -= 2 if stat_idx >= 3 else 1       # 공격력 하나로 합치고, 나머지는 하나씩 땡겨짐
                    # already selected
                    if board_selected[point_to_idx[point]] == 1:
                        already_selected[stat_idx].append((hero_name, level, stat_cursor))
                    else:
                        # get min path (cost of starting point is not included in cost)
                        cost, path = self.getMinPath(point, level, boundary, gate_points, gate_selected, hero_board_type_id)
                        # Translate cost to readable form
                        crayon_4, crayon_3, gold = cost//10000000, (cost%10000000)//10000, (cost%10000)/2
                        # cost_start = board_cost[(level, 4)]
                        # crayon_4 += cost_start[4]
                        # crayon_3 += cost_start[3]
                        # gold += cost_start[0] / 10000
                        min_paths[stat_idx].append((hero_name, stat_cursor+1, (crayon_4, crayon_3, gold), path))
                    stat_cursor += 1
        
        # sort min_paths by cost (crayon_4, crayon_3, gold) ascending
        for i in range(len(min_paths)):
            min_paths[i].sort(key=lambda x: x[2])
        
        # update widgets
        for i in range(len(min_paths)):
            subwidget = getattr(self, f"scroll_gold_{i}")
            sublayout = subwidget.layout()
            font = subwidget.font()
            for hero_name, stat_cursor, (crayon_4, crayon_3, gold), path in min_paths[i]:
                label = QLabel(f"{hero_name}, {stat_cursor}번째 칸 : 황크 {crayon_4}개, 보크 {crayon_3}개, 골드 {gold:.1f}만")
                sublayout.addWidget(label)
                font.setPointSize(13)
                label.setFont(font)

                # label = QLabel(str(path))
                # label.setWordWrap(True)
                # font.setPointSize(10)
                # label.setFont(font)
                # sublayout.addWidget(label)

                # add empty widget for spacing
                empty_widget = QWidget()
                sublayout.addWidget(empty_widget)


    def updatePurpleCrayon(self):
        res = self.window().resource
        stat = res.masterGet("Stat")
        board_type = res.masterGet("BoardType")
        board_cost = res.masterGet("BoardCost")
        hero_id_to_metadata = res.masterGet("HeroIdToMetadata")
        hero_id_to_board_data = res.masterGet("HeroIdToBoardData")
        user_board = res.userGet("UserBoard")
        
        # clear all widgets in all scroll area (in purple tab)
        for i in range(0, self.subtab_purple.count()):
            subtab = getattr(self, f"scroll_purple_{i}")
            sublayout = subtab.layout()
            for j in reversed(range(sublayout.count())):
                sublayout.itemAt(j).widget().deleteLater()
        
        # make data for each stat
        min_paths = [list() for _ in range(self.subtab_purple.count())]
        already_selected = [list() for _ in range(self.subtab_purple.count())]

        for hero_id in hero_id_to_metadata:
            hero_name = hero_id_to_metadata[hero_id]["name_kr"]
            hero_board_type_id, purple_crayon_list, gold_crayon_list = hero_id_to_board_data[hero_id]
            hero_board_type_data = board_type[hero_board_type_id]
            start_points = hero_board_type_data["start_points"][3]      # 3 is for purple
            gate_points = hero_board_type_data["gates"]
            point_to_idx = hero_board_type_data["point_to_idx"]
            if hero_id in user_board:
                board_selected, boundary = user_board[hero_id]
                # if boundary is empty, it means that the hero's board is completed; so, skip this hero
                if not boundary:
                    # print(f"{hero_name} is completed")
                    continue
            else:
                board_selected = [[0]*2] + [[0] * i[-1] for i in hero_board_type_data["num_crayon_type"]]
                boundary = gate_points[:1]
            gate_selected = board_selected[0]
            board_selected = board_selected[3]      # 3 is for purple

            stat_cursor = 0
            for level, point_list in enumerate(start_points, 1):
                for point in point_list:
                    stat_idx = purple_crayon_list[stat_cursor] - 1
                    # already selected
                    if board_selected[point_to_idx[point]] == 1:
                        already_selected[stat_idx].append((hero_name, level, stat_cursor))
                    else:
                        # get min path (cost of starting point is not included in cost)
                        cost, path = self.getMinPath(point, level, boundary, gate_points, gate_selected, hero_board_type_id)
                        # Translate cost to readable form
                        crayon_4, crayon_3, gold = cost//10000000, (cost%10000000)//10000, (cost%10000)/2
                        # cost_start = board_cost[(level, 5)]
                        # crayon_4 += cost_start[4]
                        # crayon_3 += cost_start[3]
                        # gold += cost_start[0] / 10000
                        min_paths[stat_idx].append((hero_name, stat_cursor+1, (crayon_4, crayon_3, gold), path))
                    stat_cursor += 1

        # sort min_paths by cost (crayon_4, crayon_3, gold) ascending
        for i in range(len(min_paths)):
            min_paths[i].sort(key=lambda x: x[2])

        # update widgets
        for i in range(len(min_paths)):
            subwidget = getattr(self, f"scroll_purple_{i}")
            sublayout = subwidget.layout()
            font = subwidget.font()
            for hero_name, stat_cursor, (crayon_4, crayon_3, gold), path in min_paths[i]:
                label = QLabel(f"{hero_name}, {stat_cursor}번째 칸 : 황크 {crayon_4}개, 보크 {crayon_3}개, 골드 {gold:.1f}만")
                sublayout.addWidget(label)
                font.setPointSize(13)
                label.setFont(font)

                # label = QLabel(str(path))
                # label.setWordWrap(True)
                # font.setPointSize(10)
                # label.setFont(font)
                # sublayout.addWidget(label)

                # add empty widget for spacing
                empty_widget = QWidget()
                sublayout.addWidget(empty_widget)
                    
                    

    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        self.updateGoldCrayon()
        self.updatePurpleCrayon()
        self.reload = dict()
