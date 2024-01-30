from widgets.ui.page_home import Ui_page_home

from PySide6.QtWidgets import QWidget

class PageHome(Ui_page_home, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        pass