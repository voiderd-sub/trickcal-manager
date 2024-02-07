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

        f = lambda x: [x[0]+"_sub_btn_"+str(i) for i in range(1, x[1]+1)]
        self.btn_with_pages = ["home_btn", "hero_btn", "equip_sub_btn_abstract"]\
                            +f(("equip",3)) + f(("crayon",2)) + f(("food",3)) + f(("lab",3))
        
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
        
        self.updateLocalAccountList(False)
        # connect changeAccount with account_list only when user select account from account_list
        self.account_list.activated.connect(self.changeAccount)

        # self.account_list.currentIndexChanged.connect(self.changeAccount)
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


    def changeAccount(self, account_list_changed=False):
        main_window = self.window()
        config = main_window.config
        selected_idx = self.account_list.currentIndex()
        if selected_idx != config["cur_account_idx"] or account_list_changed:
            config["cur_account_idx"] = selected_idx
            main_window.conn_user.close()
            del main_window.conn_user
            main_window.changeAccountCascade()


    def updateLocalAccountList(self, is_not_init):
        config = self.window().config
        self.account_list.clear()
        self.account_list.addItems(config["account_list"])
        self.account_list.setCurrentIndex(config["cur_account_idx"])
        self.changeAccount(is_not_init)


    def openAccountSettings(self):
        main_window = self.window()
        new_window: AccountSettings = main_window.account_settings
        new_window.show()