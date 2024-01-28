from widgets.ui.account_settings import Ui_AccountSettings
from PySide6.QtWidgets import QMainWindow, QCheckBox, QListWidgetItem
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

class AccountSettings(Ui_AccountSettings, QMainWindow):
    def __init__(self):
        super(AccountSettings, self).__init__()
        self.setupUi(self)
        self.setStyleFromPath("widgets/style/style_account_settings.qss")
        self.setInitialState()

    def setStyleFromPath(self, path):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())
    
    def setInitialState(self):
        regex = QRegularExpression("[ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9 ]+")
        validator = QRegularExpressionValidator(regex, self.account_name_line)
        self.account_name_line.setValidator(validator)

        self.add_btn.clicked.connect(self.addAccount)
        self.cancel_btn.clicked.connect(self.cancelUpdate)
        self.save_btn.clicked.connect(self.saveAccountSettings)
    
    def updateLocalAccountList(self, account_list):
        self.account_list.clear()
        for name in account_list:
            item = QCheckBox(name)
            list_item = QListWidgetItem()
            self.account_list.addItem(list_item)
            self.account_list.setItemWidget(list_item, item)
    
    def saveAccountSettings(self):
        self.main.config["account_list"] = self.tmp_account_list
        self.main.updateAccountList()
        self.close()
    
    def addAccount(self):
        name = self.account_name_line.text()
        if len(name)>=1:
            self.tmp_account_list.append(name)
            self.account_name_line.clear()
            self.updateLocalAccountList(self.tmp_account_list)
    
    def cancelUpdate(self):
        self.updateLocalAccountList(self.main.config["account_list"])
        self.account_name_line.clear()
        self.close()
    
    def set_tmp_account_list(self, account_list):
        self.tmp_account_list = account_list
