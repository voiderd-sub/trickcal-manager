from PySide6 import QtWidgets
from widgets.ui.main_window import Ui_MainWindow
from widgets.wrapper.account_settings import AccountSettings
from widgets.wrapper.goal_settings import GoalSettings

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
        self.account_settings = AccountSettings(parent=self)
        self.goal_settings = GoalSettings(parent=self)

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
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.executescript(
"""
CREATE TABLE "user_hero" (						-- 유저가 보유한 사도 리스트 (table에 있으면 보유중)
	"hero_id"	INTEGER,						-- 사도 id
	"star_extrinsic"	INTEGER NOT NULL,		-- 현재 별 개수
	PRIMARY KEY("hero_id")
);
CREATE TABLE "user_cur_equip" (                 -- 유저의 현재 장비 장착 상태
    "hero_id"	INTEGER NOT NULL,               -- 사도 id
    "rank"	INTEGER NOT NULL,                   -- 사도의 현재 랭크
    "equips"	TEXT,                           -- 장착한 장비 order값
    PRIMARY KEY("hero_id")
);
CREATE TABLE "user_goal_equip_names" (          -- 유저가 설정한 목표 이름
    "id"	INTEGER PRIMARY KEY,
    "name"	TEXT NOT NULL UNIQUE
);
INSERT INTO "user_goal_equip_names" (id, name) VALUES (1, '기본 목표');
CREATE TABLE "user_goal_equip" (                -- 유저가 설정한 목표 상세 내역
    "goal_id"	INTEGER NOT NULL,               -- 목표 id
    "hero_id"	INTEGER NOT NULL,               -- 사도 id
    "rank"	INTEGER NOT NULL,                   -- 목표 랭크
    "equips"	TEXT,                           -- 목표 장비 order값
    PRIMARY KEY("goal_id","hero_id")
);
PRAGMA journal_mode=wal;
""")
            conn.commit()
            conn.close()

        self.conn_user = sqlite3.connect(db_path)


    def configInit(self):
        config_path = "db/config.yaml"
        if not os.path.isfile(config_path):
            with open(config_path, "w") as f:
                f.write(
"""
account_list:
    - user 1
cur_account_idx: 0
""")
        
        with open("db/config.yaml") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
    
    def updateAccountList(self):
        self.sidebar.updateLocalAccountList()

    def updateGoalList(self):
        self.page_equip_1.updateGoalList()

    def changeAccountCascade(self):
        self.userDBInit()
        self.page_hero.updateTable()
        self.page_equip_1.changeAccount()



app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()