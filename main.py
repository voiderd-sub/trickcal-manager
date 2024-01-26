from PySide6 import QtWidgets
from ui.main_window import Ui_MainWindow
from ui.wrapper import AccountSettings

from functools import partial
import sqlite3, yaml, os.path

"""
!WARNING!
If you converted the .ui file to a .py file with the pyside6-uic command,
you must pass "self.stacked_widget" as an argument to each custom widget
constructor of stackedwindow in main_window.py.
"""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # open db & config     
        self.configInit()   
        self.masterDBInit()
        self.userDBInit()

        # generate subwindows
        self.account_settings = AccountSettings()
        self.account_settings.updateLocalAccountList(self.config["account_list"])
        self.account_settings.main = self

        self.setupUi(self)
        self.setInitialState()
        self.stacked_window.setCurrentIndex(0)
    
    def setInitialState(self):
        # Connect btns with pages with each page
        for i, name in enumerate(self.sidebar.btn_with_pages):
            btn=getattr(self.sidebar, name)
            btn.clicked.connect(partial(self.stacked_window.setCurrentIndex, i))

    def closeEvent(self, event):
        self.conn_master.close()
        self.conn_user.close()
        with open('db/config.yaml', 'w') as f:
            yaml.dump(self.config, f)
        event.accept()
    
    def masterDBInit(self):
        db_path = "db/master.db"
        if not os.path.isfile(db_path):
            ### 대충 db 다운로드 하는 코드 ###
            pass
        self.conn_master = sqlite3.connect(db_path)

    def userDBInit(self):
        user_name = self.config["account_list"][self.config["cur_account_idx"]]
        db_path = f"db/{user_name}.db"

        if not os.path.isfile(db_path):
            with sqlite3.connect(db_path) as conn:
                cur = conn.cursor()
                cur.executescript(
"""
CREATE TABLE "user_hero" (						-- 유저가 보유한 사도 리스트 (table에 있으면 보유중)
	"hero_id"	INTEGER,						-- 사도 id
	"star_extrinsic"	INTEGER NOT NULL,		-- 현재 별 개수
	PRIMARY KEY("hero_id")
);
PRAGMA journal_mode=wal;
""")
                conn.commit()

        self.conn_user = sqlite3.connect(db_path)
    
    def configInit(self):
        config_path = "db/config.yaml"
        if not os.path.isfile(config_path):
            with open(config_path, "w") as f:
                f.write(
"""
account_list:
    - user 1
cur_user_idx: 0
""")
        
        with open("db/config.yaml") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
    
    def updateAccountList(self):
        new_account_list = self.config["account_list"]
        self.account_settings.updateLocalAccountList(new_account_list)
        self.sidebar.updateLocalAccountList(new_account_list)
    
    def changeAccount(self):
        self.userDBInit()
        self.page_hero.updateTable()




app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()