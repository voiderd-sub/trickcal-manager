from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from widgets.ui.dps_hero_cell import Ui_DpsHeroCell

class DpsHeroCell(Ui_DpsHeroCell, QWidget):
    def __init__(self, parent=None):
        super(DpsHeroCell, self).__init__(parent)
        self.setupUi(self)
        self.setInitialState()
    
    def setInitialState(self):
        self.add_button.clicked.connect(self.addHero)
        self.delete_button.clicked.connect(self.deleteHero)
    

    def addHero(self):
        res = self.window().resource
        idx = self.hero_select.currentIndex()
        if idx < 0:
            return
        self.hero_select.setCurrentIndex(idx)
        hero_name_kr = self.hero_select.currentText()
        hero_id = res.masterGet("HeroNameToId")[hero_name_kr]
        hero_name_en = res.masterGet("HeroIdToMetadata")[hero_id]["name_en"]
        icon = QPixmap(f"icon/hero/{hero_name_en}.png")
        self.hero_icon.setPixmap(icon)
        self.hero_name.setText(hero_name_kr)
        self.stackedWidget.setCurrentIndex(1)

    def deleteHero(self):
        self.stackedWidget.setCurrentIndex(0)
        self.hero_select.setCurrentIndex(-1)