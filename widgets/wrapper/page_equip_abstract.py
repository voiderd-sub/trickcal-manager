from widgets.ui.page_equip_abstract import Ui_page_equip_abstract

from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap

import os


class PageEquipAbstract(QWidget, Ui_page_equip_abstract):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        stat_list = os.listdir('icon/status')
        self.stat_list = [stat.split('.')[0].lstrip("Icon_") for stat in stat_list]
        for stat in self.stat_list:
            pixmap = QPixmap()
            pixmap.load(f"icon/status/Icon_{stat}.png")
            
            label: QLabel = getattr(self, f"icon{stat}")
            label.setPixmap(pixmap)
        
        self.updateEquipStatAbstract()


    def updateEquipStatAbstract(self):
        # load current equip state
        main_window = self.window()
        cur = main_window.conn_user.cursor()