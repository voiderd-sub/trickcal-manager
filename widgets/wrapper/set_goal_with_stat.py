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
        stat = self.parent().window().resource.masterGet("Stat")
        stat_list_en = []
        for name_kr, name_en in stat.values():
            stat_list_en.append(name_en)

        # set icon
        for stat in stat_list_en:
            getattr(self, stat).setIcon(QIcon(f"icon/status/Icon_{stat}.png"))

        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.sendGoalStat)
    

    def sendGoalStat(self):
        checked_stat = []
        for name_kr, name_en in self.parent().window().resource.masterGet("Stat").values():
            btn = getattr(self, name_en)
            if btn.isChecked():
                checked_stat.append(btn.text())
                btn.setChecked(False)
        
        over_max_rank = self.over_max_rank_box.isChecked()
        self.over_max_rank_box.setChecked(False)

        self.close()

        if len(checked_stat) != 0:
            self.parent().setGoalStat(checked_stat, over_max_rank)