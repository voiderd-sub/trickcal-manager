from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from widgets.ui.dps_hero_cell import Ui_DpsHeroCell
from widgets.wrapper.hero_setting_dialog import HeroSettingDialog

class DpsHeroCell(Ui_DpsHeroCell, QWidget):
    def __init__(self, parent=None):
        super(DpsHeroCell, self).__init__(parent)
        self.setupUi(self)
        self.hero_settings = {}  # Store hero settings
        self.setInitialState()
    
    def setInitialState(self):
        self.add_button.clicked.connect(self.addHero)
        self.delete_button.clicked.connect(self.deleteHero)
        self.setting_button.clicked.connect(self.openHeroSettings)  # Connect '?' button
        self.hero_select.currentIndexChanged.connect(self.addHero)
    

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
        self.hero_settings = {}  # Clear settings when hero is deleted
        
    def openHeroSettings(self):
        """Open hero settings dialog when '?' button is clicked"""
        if not self.hero_name.text() or self.hero_name.text() == "name":
            return  # No hero selected
            
        hero_name = self.hero_name.text()
        
        # Create and show settings dialog
        dialog = HeroSettingDialog(hero_name, self)
        
        # Load existing settings if available
        if hero_name in self.hero_settings:
            dialog.loadSettings(self.hero_settings[hero_name])
            
        # Show dialog and handle result
        if dialog.exec() == HeroSettingDialog.Accepted:
            # Save settings
            self.hero_settings[hero_name] = dialog.getSettings()
            
    def getHeroSettings(self):
        """Get current hero settings"""
        hero_name = self.hero_name.text()
        if hero_name and hero_name != "name" and hero_name in self.hero_settings:
            return self.hero_settings[hero_name]
        return None
        
    def setHeroSettings(self, settings):
        """Set hero settings from external source"""
        if settings and 'hero_name' in settings:
            self.hero_settings[settings['hero_name']] = settings