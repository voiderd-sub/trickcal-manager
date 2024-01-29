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
        main_window = self.parent()
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        cur_user.execute("SELECT id, name FROM user_goal_equip_names;")

        self.old_name_to_id = {name: idx for idx, name in cur_user}

        self.name_list = list(self.old_name_to_id.keys())
        self.deleted_name_list = []


    def saveCurrentState(self):
        main_window = self.parent()

        old_name_to_new_name = dict()
        old_idx_to_tmp_idx = dict()
        tmp_idx_to_new_idx = dict()

        new_goal_list = []
        for i in range(self.table.rowCount()):
            old_name, new_name = self.table.item(i, 0).text(), self.table.item(i, 1).text()
            if old_name != self.placeholder_name:
                old_idx_to_tmp_idx[self.old_name_to_id[old_name]] = 1000 + i
                tmp_idx_to_new_idx[1000 + i] = i
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
        deleted_idx_list = [self.old_name_to_id[name] for name in self.deleted_name_list]

        # check whether there is duplicated name
        if len(new_goal_list) != len(set(new_goal_list)):
            QMessageBox.critical(self, 'Error', "중복된 목표명이 있습니다.", QMessageBox.Ok)
            return
        
        # update table user_goal_equip_names
        cur_user: sqlite3.Cursor = main_window.conn_user.cursor()
        cur_user.execute("DELETE FROM user_goal_equip_names;")
        cur_user.executemany("INSERT INTO user_goal_equip_names VALUES (?, ?);", enumerate(new_goal_list, start=1))

        # update table user_goal_equip
        for idx in deleted_idx_list:
            cur_user.execute("DELETE FROM user_goal_equip WHERE goal_id=?;", (idx,))
        for old_idx, tmp_idx in old_idx_to_tmp_idx.items():
            cur_user.execute("UPDATE user_goal_equip SET goal_id=? WHERE goal_id=?;", (tmp_idx, old_idx))
        for tmp_idx, new_idx in tmp_idx_to_new_idx.items():
            cur_user.execute("UPDATE user_goal_equip SET goal_id=? WHERE goal_id=?;", (new_idx, tmp_idx))
        main_window.conn_user.commit()

        # set cur_goal index
        main_window.updateGoalList()

        self.close()