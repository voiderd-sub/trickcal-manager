from widgets.ui.set_goal_with_stat import Ui_SetGoalWithStat

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

import os


class SetGoalWithStat(QMainWindow, Ui_SetGoalWithStat):
    def __init__(self, *args, **kwargs):
        super(SetGoalWithStat, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setInitialState()
    

    def setInitialState(self):
        # make list of stat names. name of icon file is in icon\status
        stat_list = os.listdir('icon/status')
        self.stat_list = [stat.split('.')[0].lstrip("Icon_") for stat in stat_list]

        # set icon
        for stat in self.stat_list:
            getattr(self, stat).setIcon(QIcon(f"icon/status/Icon_{stat}.png"))

        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.sendGoalStat)
    

    def sendGoalStat(self):
        checked_stat = []
        for stat in self.stat_list:
            btn = getattr(self, stat)
            if btn.isChecked():
                checked_stat.append(btn.text())
        self.close()
        if len(checked_stat) != 0:
            self.parent().setGoalStat(checked_stat)