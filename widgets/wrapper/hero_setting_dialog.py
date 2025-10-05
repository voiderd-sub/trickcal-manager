from PySide6.QtWidgets import QDialog
from widgets.ui.hero_setting_dialog import Ui_HeroSettingDialog

class HeroSettingDialog(Ui_HeroSettingDialog, QDialog):
    def __init__(self, hero_name, parent=None):
        super(HeroSettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.hero_name = hero_name
        self.setInitialState()
        
    def setInitialState(self):
        # Set hero name
        self.hero_name_label.setText(self.hero_name)
        
        # Connect button signals
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Set default values
        self.setDefaultValues()
        
    def setDefaultValues(self):
        """Set default values for all spinboxes"""
        # Skill levels
        self.lower_skill_spinbox.setValue(1)
        self.upper_skill_spinbox.setValue(1)
        self.aside_skill_spinbox.setValue(0)
        
        # Stats
        self.attack_spinbox.setValue(1000)
        self.defense_spinbox.setValue(500)
        self.hp_spinbox.setValue(10000)
        self.attack_speed_spinbox.setValue(100)
        self.crit_rate_spinbox.setValue(5)
        self.crit_damage_spinbox.setValue(150)
        
    def loadSettings(self, settings):
        """Load settings from a dictionary"""
        if not settings:
            return
            
        # Load skill levels
        if 'lower_skill_level' in settings:
            self.lower_skill_spinbox.setValue(settings['lower_skill_level'])
        if 'upper_skill_level' in settings:
            self.upper_skill_spinbox.setValue(settings['upper_skill_level'])
        if 'aside_skill_level' in settings:
            self.aside_skill_spinbox.setValue(settings['aside_skill_level'])
            
        # Load stats
        if 'attack' in settings:
            self.attack_spinbox.setValue(settings['attack'])
        if 'defense' in settings:
            self.defense_spinbox.setValue(settings['defense'])
        if 'hp' in settings:
            self.hp_spinbox.setValue(settings['hp'])
        if 'attack_speed' in settings:
            self.attack_speed_spinbox.setValue(settings['attack_speed'])
        if 'crit_rate' in settings:
            self.crit_rate_spinbox.setValue(settings['crit_rate'])
        if 'crit_damage' in settings:
            self.crit_damage_spinbox.setValue(settings['crit_damage'])
            
    def getSettings(self):
        """Get current settings as a dictionary"""
        return {
            'hero_name': self.hero_name,
            'lower_skill_level': self.lower_skill_spinbox.value(),
            'upper_skill_level': self.upper_skill_spinbox.value(),
            'aside_skill_level': self.aside_skill_spinbox.value(),
            'attack': self.attack_spinbox.value(),
            'defense': self.defense_spinbox.value(),
            'hp': self.hp_spinbox.value(),
            'attack_speed': self.attack_speed_spinbox.value(),
            'crit_rate': self.crit_rate_spinbox.value(),
            'crit_damage': self.crit_damage_spinbox.value(),
        }
