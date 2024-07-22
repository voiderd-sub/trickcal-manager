from widgets.ui.setting_window import Ui_setting_window

from PySide6.QtWidgets import QMainWindow, QPushButton

from functools import partial


class SettingWindow(Ui_setting_window, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("설정")
        self.setInitialState()

    def setInitialState(self):
        # read version from file
        with open("version", "r") as file:
            version = file.read()
        self.label_version.setText(f"v{version}")

        self.loadSettings()

        self.update_btn_program.clicked.connect(self.parent().updateProgram)
        self.update_btn_master.clicked.connect(self.parent().masterDBUpdateCascade)
        self.update_btn_drop.clicked.connect(self.parent().updateDropTable)

        self.save_btn.clicked.connect(self.saveSettings)
        self.exit_btn.clicked.connect(self.close)
    

    def loadSettings(self):
        config_setting = self.parent().config.get("setting", dict())
        for setting_name in config_setting:
            setting = getattr(self, "setting_" + setting_name)
            if type(setting) == QPushButton:
                if config_setting.get(setting_name, False):
                    setting.click()
    

    def saveSettings(self):
        config = self.parent().config
        for attr in dir(self):
            if attr.startswith("setting_"):
                setting = getattr(self, attr)
                if type(setting) == QPushButton:
                    if "setting" not in config:
                        config["setting"] = dict()
                    config["setting"][setting.objectName().lstrip("setting_")] = setting.isChecked()

        self.close()