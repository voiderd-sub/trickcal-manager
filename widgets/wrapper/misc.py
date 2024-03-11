from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import (QWidget, QCompleter, QComboBox, QProxyStyle,QStyledItemDelegate,
                               QTableWidget, QItemDelegate, QLineEdit, QLayout, QStyle,
                               QSizePolicy, QPushButton)
from PySide6.QtGui import QFont, QColor, QRegularExpressionValidator, QPixmap
from PySide6.QtCore import QRegularExpression, Qt, QRect, QPoint, QSize

from widgets.ui.crayon_stat_container import Ui_CrayonStatContainer


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


class BoardTableDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(BoardTableDelegate, self).initStyleOption(option, index)

        if not index.model().flags(index) & Qt.ItemIsEnabled:
            option.backgroundBrush = QColor(227, 227, 227)  # Set the background color for disabled items


class BoardTableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(BoardTableWidget, self).__init__(*args, **kwargs)

        # Set the item delegate to the customized delegate
        self.setItemDelegate(BoardTableDelegate())


# FlowLayout for wrapping widgets
class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self._items:
            size = size.expandedTo(item.sizeHint())
        left, top, right, bottom = self.getContentsMargins()
        size += QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QRect(QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()

class CrayonStatContainer(Ui_CrayonStatContainer, QWidget):
    def __init__(self, parent=None):
        super(CrayonStatContainer, self).__init__(parent)
        self.setupUi(self)
    
    def setTexts(self, values):
        for attr_name, value in values.items():
            getattr(self, attr_name).setText(str(value))
    
    def setIcon(self, stat_name):
        self.icon.setPixmap(QPixmap(f"icon/status/Icon_{stat_name}.png"))


class QCheckButton(QPushButton):
    def __init__(self, parent=None):
        super(QCheckButton, self).__init__(parent)
        self.setCheckable(True)
        self.clicked.connect(self.setBtnText)
        self.setBtnText()

    def setBtnText(self):
        if self.isChecked():
            self.setText("✔️")
        else:
            self.setText("")