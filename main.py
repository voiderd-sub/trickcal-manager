from PySide6 import QtWidgets
from ui.main_window import Ui_MainWindow
from functools import partial


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.set_initial_state()
        self.stacked_window.setCurrentIndex(0)
    
    def set_initial_state(self):
        # Connect btns with pages with each page
        for i, name in enumerate(self.sidebar.btn_with_pages):
            btn=getattr(self.sidebar, name)
            btn.clicked.connect(partial(self.stacked_window.setCurrentIndex, i))

    def closeEvent(self, event):
        self.hero_window.closeDBconn()
        event.accept()


app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()