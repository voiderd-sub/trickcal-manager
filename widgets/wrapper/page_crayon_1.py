from widgets.ui.page_crayon_1 import Ui_page_crayon_1

from PySide6.QtWidgets import QWidget

class PageCrayon1(Ui_page_crayon_1, QWidget):
    def __init__(self, parent=None):
        super(PageCrayon1, self).__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        pass