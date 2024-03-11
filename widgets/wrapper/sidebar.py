from widgets.ui.sidebar import Ui_sidebar
from widgets.wrapper.account_settings import AccountSettings

from functools import partial
from PySide6.QtWidgets import QWidget, QMainWindow

class Sidebar(Ui_sidebar, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)              # Settings in Qt Designer
        self.setInitialState()        # Settings in main.py


    def setInitialState(self):
        # define main buttons & sub buttons
        self.main_btn_dict = dict()
        self.sub_menu_dict = dict()
        self.menu_names = ["home", "hero", "equip", "crayon", "food", "lab"]

        f = lambda x: [f"{x[0]}_{i}_btn" for i in range(1, x[1]+1)]
        self.btn_with_pages = ["home_btn", "hero_btn", "equip_abstract_btn"]\
                            +f(("equip",3)) + ["crayon_abstract_btn"]\
                            +f(("crayon",2)) + f(("food",3)) + f(("lab",3))
        
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
        
        self.updateAccountList()
        self.account_list.activated.connect(self.changeAccount)
        self.account_setting_btn.clicked.connect(self.openAccountSettings)
        self.setting_btn.clicked.connect(self.openSettings)


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
        main = self.window()
        config = main.config
        selected_idx = self.account_list.currentIndex()
        if selected_idx != config["cur_account_idx"]:
            main.saveLastPageData()
            main.resource.saveAllUserResource()
            config["cur_account_idx"] = selected_idx
            main.changeAccountCascade()


    def updateAccountList(self):
        config = self.window().config
        self.account_list.blockSignals(True)
        self.account_list.clear()
        self.account_list.addItems(config["account_list"])
        self.account_list.setCurrentIndex(config["cur_account_idx"])
        self.account_list.blockSignals(False)


    def openAccountSettings(self):
        self.window().account_settings.show()
    

    def openSettings(self):
        self.window().setting_window.show()