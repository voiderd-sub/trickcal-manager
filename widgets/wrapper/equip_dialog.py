from widgets.ui.equip_dialog import Ui_Dialog

from PySide6.QtWidgets import QDialog



class EquipDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 40px; font-size: 13pt;}")
        self.tabWidget.tabBar().expanding = True
        self.ok_btn.clicked.connect(self.close)

    def setResultValues(self, result):
        for idx, txt in enumerate(result, 1):
            getattr(self, f"text_{idx}").setText(txt)