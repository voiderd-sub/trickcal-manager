from widgets.ui.page_equip_2 import Ui_page_equip_2
from widgets.wrapper.misc import ExtendedComboBox, NumberDelegate

from PySide6.QtWidgets import QWidget, QAbstractItemView, QTableWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt

import sqlite3
from functools import partial



class PageEquip2(Ui_page_equip_2, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        # load db data
        main = self.window()
        res = main.resource
        cur_master: sqlite3.Cursor = main.conn_master.cursor()
        

        # set material table
        mat_table = self.material_table
        h_header = mat_table.horizontalHeader()
        v_header = self.material_table.verticalHeader()

        mat_table.setRowCount(14)
        self.loadMaterialTableColumns()

        cur_master.execute("SELECT type_id, comment FROM item_type order by type_id asc")
        self.type_name_to_type_id = {name: idx for (idx, name) in cur_master}
        self.type_id_to_type_name = {idx: name for (name, idx) in self.type_name_to_type_id.items()}
        self.pr_to_id = {"조각": 1, "도안": 2}    
        self.id_to_pr = {1: "조각", 2: "도안"}

        main.type_name_to_type_id = self.type_name_to_type_id
        main.type_id_to_type_name = self.type_id_to_type_name
        main.pr_to_id = self.pr_to_id
        main.id_to_pr = self.id_to_pr

        prefix = [self.type_id_to_type_name[i] for i in range(1, len(self.type_id_to_type_name)+1)]
        suffix = ["조각", "도안"]
        material_names = [f"{p} {s}" for s in suffix for p in prefix]

        mat_table.setVerticalHeaderLabels(material_names)
        mat_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        mat_table.setEditTriggers(QTableWidget.AllEditTriggers)

        h_header.setSectionResizeMode(QHeaderView.Stretch)
        h_header.setStyleSheet("font-size: 11pt;")
        h_header.setHighlightSections(False)
        v_header.setSectionResizeMode(QHeaderView.Stretch)
        v_header.setStyleSheet("font-size: 11pt;")
        v_header.setHighlightSections(False)

        # set bag_equip table
        beq_table = self.bag_equip_table
        h_header = beq_table.horizontalHeader()
        v_header = beq_table.verticalHeader()

        beq_table.setColumnCount(2)
        beq_table.setHorizontalHeaderLabels(["장비 이름", "개수"])
        beq_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        beq_table.setEditTriggers(QTableWidget.AllEditTriggers)
        beq_table.setColumnWidth(1, 100)
        beq_table.setItemDelegateForColumn(1, NumberDelegate())

        h_header.setSectionResizeMode(0, QHeaderView.Stretch)
        h_header.setSectionResizeMode(1, QHeaderView.Fixed)

        self.reloadData()

        # connect buttons
        self.save_btn.clicked.connect(self.saveData)
        self.cancel_btn.clicked.connect(self.reloadData)
        self.add_btn.clicked.connect(partial(self.addEquip, idx=None, count=None))
        self.delete_btn.clicked.connect(self.deleteEquip)

    def loadMaterialTableColumns(self):
        max_rank = self.window().resource.masterGet("MaxRank")
        self.material_table.setColumnCount(max_rank-1)
        self.material_table.setHorizontalHeaderLabels([f"{i}티어" for i in range(2, max_rank+1)])

    
    def saveData(self):
        main = self.window()
        res = main.resource
        cur_user: sqlite3.Cursor = main.conn_user.cursor()
        equip_name_to_id = res.masterGet("EquipNameToId")

        # iterate material table and update user_items
        for row_idx in range(14):
            for col_idx in range(res.masterGet("MaxRank")-1):
                item = self.material_table.item(row_idx, col_idx)
                count = 0 if item.text()=="" else int(item.text())
                prefix = self.type_id_to_type_name[row_idx % 7 + 1]
                suffix = "조각" if row_idx // 7 == 0 else "도안"
                name = f"{prefix} {suffix}({col_idx+2}티어)"
                cur_user.execute("UPDATE user_items SET count=? WHERE name=?", (count, name))
        res.delete("UserItems")
        
        # iterate bag_equip table and update user_bag_equips
        cur_user.execute("DELETE FROM user_bag_equips")
        for row_idx in range(self.bag_equip_table.rowCount()):
            item = self.bag_equip_table.item(row_idx, 1)
            count = 0 if item.text()=="" else int(item.text())
            if count == 0:
                continue
            equip_id = equip_name_to_id.get(self.bag_equip_table.cellWidget(row_idx, 0).currentText(), None)
            if equip_id is None:
                continue
            cur_user.execute("INSERT INTO user_bag_equips VALUES (?, ?)", (equip_id, count))
        res.delete("BagEquips")
        
        main.conn_user.commit()


    def reloadData(self):
        self.material_table.clearContents()
        self.loadMaterial()
        self.bag_equip_table.clearContents()
        self.bag_equip_table.setRowCount(0)
        self.loadEquip()

    
    # Add row to bag_equip_table
    def addEquip(self, idx, count):
        table = self.bag_equip_table
        row_idx = table.rowCount()
        table.insertRow(row_idx)

        box = ExtendedComboBox(ignoreWheel=True)
        box.setCompleterFont(12)
        box.addItems(self.window().resource.masterGet("EquipNameDefaultOrder"))
        if idx is None:
            box.setCurrentText("")
        else:
            box.setCurrentIndex(idx-1)
        table.setCellWidget(row_idx, 0, box)

        item = QTableWidgetItem("" if count is None else str(count))
        table.setItem(row_idx, 1, item)


    # Delete current row from bag_equip_table
    def deleteEquip(self):
        table = self.bag_equip_table
        row_idx = table.currentRow()
        table.removeRow(row_idx)
    

    def loadEquip(self):
        res = self.window().resource
        bag_equips = res.userGet("BagEquips")
        equip_default_order = res.masterGet("EquipDefaultOrder")
        equip_order_cnt_list = [(equip_default_order[equip_id], cnt) for equip_id, cnt in bag_equips.items()]
        equip_order_cnt_list.sort(key=lambda x: x[0])
        for order, cnt in equip_order_cnt_list:
            self.addEquip(order, cnt)
    
    def loadMaterial(self):
        for row_idx in range(14):
            for col_idx in range(self.window().resource.masterGet("MaxRank")-1):
                item = QTableWidgetItem("")
                self.material_table.setItem(row_idx, col_idx, item)
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
        
        user_items = self.window().resource.userGet("UserItems")

        for (name, count) in user_items.items():
            name = name.split("(")
            rank = int(name[1].rstrip("티어)"))

            name_w_o_rank = name[0].split(" ")
            prefix = " ".join(name_w_o_rank[:-1])
            suffix = name_w_o_rank[-1]

            prefix = self.type_name_to_type_id[prefix]
            suffix = self.pr_to_id[suffix]


            row_num = (prefix-1) + 7 * (suffix-1)
            col_num = rank-2
            item = self.material_table.item(row_num, col_num)
            if count != 0:
                item.setText(str(count))
            item.setFlags(item.flags() | Qt.ItemIsEnabled)