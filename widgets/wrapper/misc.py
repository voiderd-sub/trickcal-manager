from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import QCompleter, QComboBox, QProxyStyle, QStyledItemDelegate, QTableWidget, QItemDelegate, QLineEdit
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator


# Combobox with search-filtering
class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None, ignoreWheel=False):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

        # set the font for the completer popup
        self.completer.popup().setFont(QFont("ONE Mobile POP", 15))

        # ignore wheel event
        if ignoreWheel:
            self.wheelEvent = lambda event: event.ignore()


    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)


    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


    # ignore pressing enter key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            event.ignore()
            return
        super(ExtendedComboBox, self).keyPressEvent(event)
    

    def setCompleterFont(self, font_size):
        self.completer.popup().setFont(QFont("ONE Mobile POP", font_size))


# Proxy style for wrapping text in QPushButton
class wrapStyle(QProxyStyle):
    def __init__(self):
        super().__init__()

    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole):
        flags |= Qt.TextWordWrap
        super().drawItemText(painter, rect, flags, pal, enabled, text, textRole)


# Delegate for combobox_editor window
class NumberDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regex = QRegularExpression("[0-9]*")
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


class MaterialTableDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(MaterialTableDelegate, self).initStyleOption(option, index)

        if not index.model().flags(index) & Qt.ItemIsEnabled:
            option.backgroundBrush = QColor(200, 200, 200)  # Set the background color for disabled items

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regex = QRegularExpression("[0-9]*")
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


class MaterialTableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(MaterialTableWidget, self).__init__(*args, **kwargs)

        # Set the item delegate to the customized delegate
        self.setItemDelegate(MaterialTableDelegate())