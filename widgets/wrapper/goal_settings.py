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
        self.name_list = list(name for (name, goal_type) in res.userGet("GoalIdToName").values())


    def saveCurrentState(self):
        main = self.parent()
        res = main.resource

        old_name_to_id_and_type = {goal_name: (goal_idx, goal_type) for (goal_idx, (goal_name, goal_type))
                          in res.userGet("GoalIdToName").items()}
        old_id_to_type = {goal_idx: goal_type for (goal_idx, (goal_name, goal_type))
                          in res.userGet("GoalIdToName").items()}
        goal_id_to_name = res.userGet("GoalIdToName")
        
        update_list = []
        remaining_old_idx_list = []

        for i in range(self.table.rowCount()):
            old_name, new_name = self.table.item(i, 0).text(), self.table.item(i, 1).text()
            if old_name != self.placeholder_name:       # old goal
                old_idx = old_name_to_id_and_type[old_name][0]
                if new_name == "":
                    new_name = old_name
                update_list.append((old_idx, new_name))
                remaining_old_idx_list.append(old_idx)
            elif new_name == "":
                QMessageBox.critical(self, 'Error', "신규 목표명을 모두 입력해주세요.", QMessageBox.Ok)
                return
            else:
                update_list.append((0, new_name))
        
        remaining_old_idx_list = set(remaining_old_idx_list)
        deleted_old_idx_list = list(set(range(1, len(goal_id_to_name)+1)) - remaining_old_idx_list)
        
        # check whether there is duplicated name
        new_names = [name for (idx, name) in update_list]
        if len(new_names) != len(set(new_names)):
            QMessageBox.critical(self, 'Error', "중복된 목표명이 있습니다.", QMessageBox.Ok)
            return
        
        # Update GoalIdToName
        old_id_to_new_id = dict()
        goal_id_to_name.clear()
        for (idx, (old_idx, new_name)) in enumerate(update_list, start=1):
            if old_idx == 0:
                goal_id_to_name[idx] = (new_name, "User")
            else:
                goal_id_to_name[idx] = (new_name, old_id_to_type[old_idx])
                old_id_to_new_id[old_idx] = idx

        # Update GoalEquip
        goal_equip = res.userGet("GoalEquip")
        new_goal_equip = dict()
        for (goal_idx, equip_list) in goal_equip.items():
            if goal_idx in old_id_to_new_id:
                new_goal_equip[old_id_to_new_id[goal_idx]] = equip_list
        
        goal_equip.clear()
        goal_equip.update(new_goal_equip)

        main.updateGoalList()

        self.close()