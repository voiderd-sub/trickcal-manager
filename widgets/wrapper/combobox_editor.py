from widgets.ui.combobox_editor import Ui_combobox_editor
from PySide6.QtWidgets import QMainWindow, QItemDelegate, QLineEdit, QTableWidgetItem, QTableWidget, QHeaderView, QMessageBox
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator

import os


# Delegate for combobox_editor window
class NameDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regex = QRegularExpression("[ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9 ]+")
        validator = QRegularExpressionValidator(regex)
        editor.setValidator(validator)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        line = editor
        line.setText(str(value))

    def setModelData(self, editor, model, index):
        line = editor
        value = line.text()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)



class ComboBoxEditor(Ui_combobox_editor, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ComboBoxEditor, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setInitialState()
        assert hasattr(self, "placeholder_name"), "placeholder_name must be defined in __init__"


    def setInitialState(self):
        # set table
        delegate = NameDelegate()
        self.table.setItemDelegate(delegate)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet('font: 12pt "ONE Mobile POP";')
        
        self.add_btn.clicked.connect(self.addName)
        self.delete_btn.clicked.connect(self.deleteName)
        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.saveCurrentState)
        self.up_btn.clicked.connect(self.moveUp)
        self.down_btn.clicked.connect(self.moveDown)
        
        self.loadList()


    def showEvent(self, event):
        super().showEvent(event)
        self.loadList()
        self.updateTable()
    

    def updateTable(self):
        self.table.clearContents()
        self.table.setRowCount(len(self.name_list))
        for idx, name in enumerate(self.name_list):
            table_item = QTableWidgetItem(name)
            self.table.setItem(idx, 0, table_item)
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)

            table_item = QTableWidgetItem("")
            self.table.setItem(idx, 1, table_item)
            table_item.setFlags(table_item.flags() | Qt.ItemIsEditable)


    def saveCurrentState(self):
        raise NotImplementedError


    def addName(self):
        self.table.setRowCount(self.table.rowCount()+1)
        row_idx = self.table.rowCount()-1

        table_item = QTableWidgetItem(self.placeholder_name)
        self.table.setItem(row_idx, 0, table_item)
        table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)

        table_item = QTableWidgetItem("")
        self.table.setItem(row_idx, 1, table_item)
        table_item.setFlags(table_item.flags() | Qt.ItemIsEditable)


    def deleteName(self):
        selected_rows = sorted(set(index.row() for index in self.table.selectedIndexes()), reverse=True)
        selected_names = [self.table.item(row, 0).text() for row in selected_rows]
        if len(selected_names) == 0:
            return
    
        for row in selected_rows:
            self.table.removeRow(row)

        self.deleted_name_list.extend([name for name in selected_names
                                          if name != self.placeholder_name])


    # Initialize name_list and deleted_name_list
    def loadList(self):
        raise NotImplementedError

    
    # Move selected rows up
    def moveUp(self):
        table = self.table
        selected_rows = sorted(set(index.row() for index in table.selectedIndexes()))
        if len(selected_rows) == 0:
            return

        if selected_rows[0] == 0:
            return

        for row in selected_rows:
            table.insertRow(row-1)
            for col in range(table.columnCount()):
                table.setItem(row-1, col, table.takeItem(row+1, col))
            table.removeRow(row+1)

        table.setCurrentCell(selected_rows[0]-1, 0)
    

    # Move selected rows down
    def moveDown(self):
        table = self.table
        selected_rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        if len(selected_rows) == 0:
            return

        if selected_rows[-1] == table.rowCount()-1:
            return

        for row in selected_rows:
            table.insertRow(row+2)
            for col in range(table.columnCount()):
                table.setItem(row+2, col, table.takeItem(row, col))
            table.removeRow(row)

        table.setCurrentCell(selected_rows[-1]+1, 0)