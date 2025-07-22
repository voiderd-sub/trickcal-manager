from widgets.ui.page_dps_1 import Ui_page_dps_1
from widgets.wrapper.dps_graph_window import DpsGraphWindow

from PySide6.QtWidgets import QWidget
from dps.party import Party

import importlib, os


class PageDps1(Ui_page_dps_1, QWidget):
    def __init__(self, parent=None):
        super(PageDps1, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        self.reload = {"master": True}
        main = self.window()
        res = main.resource

        # Update hero_list of dps_hero_cell
        hero_list_for_each_pos = [list() for _ in range(3)]

        for val in res.masterGet("HeroIdToMetadata").values():
            name = val["name_kr"]
            pos = val["pos"]        # 1 : Front, 2 : Mid, 3 : Back, 4 : All
            if pos == 4:
                for idx in range(3):
                    hero_list_for_each_pos[idx].append(name)
            else:
                hero_list_for_each_pos[pos-1].append(name)

        for pos_idx, position in enumerate(("Front", "Mid", "Back")):
            hero_name_list = hero_list_for_each_pos[pos_idx]
            for idx in range(1, 4):
                cell = getattr(self, f"HeroCell{position}{idx}")
                cell.hero_select.blockSignals(True)
                cell.hero_select.addItems(hero_name_list)
                cell.hero_select.setCurrentIndex(-1)
                cell.setStyleSheet(u"QGroupBox{border: 1.5px solid; border-radius: 10px;}")
                cell.hero_select.blockSignals(False)
        
        self.calculate_btn.clicked.connect(self.calculate)

        self.graph_window = DpsGraphWindow(self.window())


    def calculate(self):
        # Create Party and run simulation
        res = self.window().resource
        hero_name_to_id = res.masterGet("HeroNameToId")
        hero_id_to_meta = res.masterGet("HeroIdToMetadata")
        party = Party()
        for pos_idx, position in enumerate(("Front", "Mid", "Back")):
            for idx in range(1, 4):
                cell = getattr(self, f"HeroCell{position}{idx}")
                cell_idx = cell.stackedWidget.currentIndex()
                if cell_idx == 1:
                    hero_name = cell.hero_select.currentText()
                    hero_id = hero_name_to_id[hero_name]
                    hero_name_en = hero_id_to_meta[hero_id]["name_en"]
                    hero_cls = self.dynamic_import(f"db/dps/hero/{hero_name_en}.py")
                    hero = hero_cls({
                        "aside_level": 0,
                        "lowerskill_level": 13,
                        "upperskill_level": 13,
                        "atk": 100.,
                    })
                    party.add_hero(hero, pos_idx*3 + idx - 1)
        hero_name_to_dmg = party.run(240, 100)
        
        self.graph_window.showGraph(hero_name_to_dmg)

        return


    def dynamic_import(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_path}")

        module_name = os.path.splitext(os.path.basename(file_path))[0]

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            raise ImportError(f"모듈 spec 생성 실패: {file_path}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        return getattr(module, module_name)


    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        self.reload = dict()
    

    def savePageData(self):
        # self.window().changeEquipCascade()
        pass