from widgets.wrapper.combobox_editor import ComboBoxEditor
from PySide6.QtWidgets import QMessageBox

import os



class AccountSettings(ComboBoxEditor):
    def __init__(self, *args, **kwargs):
        self.placeholder_name = "새 계정 (계정 이름을 바꿔주세요!)"
        super(AccountSettings, self).__init__(*args, **kwargs)
        self.setWindowTitle('계정 설정')
        

    def loadList(self):
        self.name_list = self.parent().config["account_list"].copy()


    def saveCurrentState(self):
        main = self.parent()
        table = self.table
        old_name_to_new_name = dict()

        new_account_list = []
        remaining_account_list = []
        for i in range(table.rowCount()):
            old_name, new_name = table.item(i, 0).text(), table.item(i, 1).text()
            if new_name =="":
                if old_name == self.placeholder_name:
                    QMessageBox.critical(self, 'Error', "신규 계정 이름을 모두 입력해주세요.", QMessageBox.Ok)
                    return
                else:
                    remaining_account_list.append(old_name)
                    new_account_list.append(old_name)
                    continue

            # New account or changed name : insert new name
            new_account_list.append(new_name)

            # if old name is not in old_name_set, it is a new account
            if old_name != self.placeholder_name:
                old_name_to_new_name[old_name] = new_name
                remaining_account_list.append(old_name)
        deleted_name_list = list(set(self.name_list) - set(remaining_account_list))

        # check whether there is duplicated name
        if len(new_account_list) != len(set(new_account_list)):
            QMessageBox.critical(self, 'Error', "중복된 계정 이름이 있습니다.", QMessageBox.Ok)
            return
        
        # update config
        main.config["account_list"] = new_account_list
        main.config["cur_account_idx"] = 0

        # Before reflecting the changes, save user data
        main.saveLastPageData()
        main.resource.saveAllUserResource()

        # disconnect userDB
        main.conn_user.close()

        # delete old dbs first
        for deleted_name in deleted_name_list:
            path = f"db/{deleted_name}.db"
            if os.path.isfile(path):
                os.remove(path)
        
        # then rename old dbs to temporary names
        for old_name, new_name in old_name_to_new_name.items():
            os.rename(f"db/{old_name}.db", f"db/{new_name}++tmp.db")
        
        # finally, rename temporary dbs to new names
        for new_name in sorted(new_account_list, key=lambda x: len(x)):
            # check if the file already exists
            if os.path.isfile(f"db/{new_name}++tmp.db"):
                os.rename(f"db/{new_name}++tmp.db", f"db/{new_name}.db")

        
        main.updateAccountList()
        self.close()