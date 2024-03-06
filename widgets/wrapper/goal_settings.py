from widgets.wrapper.combobox_editor import ComboBoxEditor
from PySide6.QtWidgets import QMessageBox

import os
import sqlite3



class GoalSettings(ComboBoxEditor):
    def __init__(self, *args, **kwargs):
        self.placeholder_name = "새 목표 (이름을 바꿔주세요!)"
        super(GoalSettings, self).__init__(*args, **kwargs)
        self.setWindowTitle('랭크작 목표 설정')
        

    def loadList(self):
        res = self.parent().resource

        self.name_list = list(res.userGet("GoalIdToName").values())
        self.deleted_name_list = []


    def saveCurrentState(self):
        main = self.parent()
        res = main.resource

        old_name_to_id = {goal_name: goal_idx for (goal_idx, goal_name)
                          in res.userGet("GoalIdToName").items()}
        old_name_to_new_name = dict()
        old_idx_to_tmp_idx = dict()
        tmp_idx_to_new_idx = dict()

        new_goal_list = []
        for i in range(self.table.rowCount()):
            old_name, new_name = self.table.item(i, 0).text(), self.table.item(i, 1).text()
            if old_name != self.placeholder_name:
                old_idx_to_tmp_idx[old_name_to_id[old_name]] = 1000 + (i+1)
                tmp_idx_to_new_idx[1000 + (i+1)] = (i+1)
                if new_name == "":
                    new_goal_list.append(old_name)
                else:
                    new_goal_list.append(new_name)
                    old_name_to_new_name[old_name] = new_name
            elif new_name == "":
                QMessageBox.critical(self, 'Error', "신규 목표명을 모두 입력해주세요.", QMessageBox.Ok)
                return
            else:
                new_goal_list.append(new_name)
        deleted_idx_list = [old_name_to_id[name] for name in self.deleted_name_list]

        # check whether there is duplicated name
        if len(new_goal_list) != len(set(new_goal_list)):
            QMessageBox.critical(self, 'Error', "중복된 목표명이 있습니다.", QMessageBox.Ok)
            return
        
        goal_id_to_name = res.userGet("GoalIdToName")
        goal_id_to_name.clear()
        for (idx, name) in enumerate(new_goal_list, start=1):
            goal_id_to_name[idx] = name

        goal_equip = res.userGet("GoalEquip")
        # update table user_goal_equip
        for idx in deleted_idx_list:
            del goal_equip[idx]
        for old_idx, tmp_idx in old_idx_to_tmp_idx.items():
            goal_equip[tmp_idx] = goal_equip[old_idx]
            del goal_equip[old_idx]
        for tmp_idx, new_idx in tmp_idx_to_new_idx.items():
            goal_equip[new_idx] = goal_equip[tmp_idx]
            del goal_equip[tmp_idx]

        main.updateGoalList()

        self.close()