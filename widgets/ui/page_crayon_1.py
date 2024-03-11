# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_crayon_1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidgetItem,
    QVBoxLayout, QWidget)

from widgets.wrapper.misc import (BoardTableWidget, ExtendedComboBox)

class Ui_page_crayon_1(object):
    def setupUi(self, page_crayon_1):
        if not page_crayon_1.objectName():
            page_crayon_1.setObjectName(u"page_crayon_1")
        page_crayon_1.resize(868, 765)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_crayon_1.sizePolicy().hasHeightForWidth())
        page_crayon_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(11)
        page_crayon_1.setFont(font)
        self.verticalLayout = QVBoxLayout(page_crayon_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.hero_select = ExtendedComboBox(page_crayon_1)
        self.hero_select.setObjectName(u"hero_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hero_select.sizePolicy().hasHeightForWidth())
        self.hero_select.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.hero_select.setFont(font1)

        self.horizontalLayout_3.addWidget(self.hero_select)

        self.filter_btn = QPushButton(page_crayon_1)
        self.filter_btn.setObjectName(u"filter_btn")
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(12)
        self.filter_btn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.filter_btn)

        self.horizontalSpacer_6 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.go_left_btn = QPushButton(page_crayon_1)
        self.go_left_btn.setObjectName(u"go_left_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.go_left_btn.sizePolicy().hasHeightForWidth())
        self.go_left_btn.setSizePolicy(sizePolicy2)
        self.go_left_btn.setMinimumSize(QSize(0, 370))
        self.go_left_btn.setMaximumSize(QSize(30, 16777215))
        self.go_left_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.go_left_btn)

        self.board_table = BoardTableWidget(page_crayon_1)
        self.board_table.setObjectName(u"board_table")
        sizePolicy1.setHeightForWidth(self.board_table.sizePolicy().hasHeightForWidth())
        self.board_table.setSizePolicy(sizePolicy1)
        self.board_table.setMinimumSize(QSize(0, 370))
        self.board_table.setMaximumSize(QSize(16777215, 350))
        self.board_table.setFont(font2)
        self.board_table.setColumnCount(0)

        self.horizontalLayout.addWidget(self.board_table)

        self.go_right_btn = QPushButton(page_crayon_1)
        self.go_right_btn.setObjectName(u"go_right_btn")
        sizePolicy2.setHeightForWidth(self.go_right_btn.sizePolicy().hasHeightForWidth())
        self.go_right_btn.setSizePolicy(sizePolicy2)
        self.go_right_btn.setMinimumSize(QSize(0, 370))
        self.go_right_btn.setMaximumSize(QSize(30, 16777215))
        self.go_right_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.go_right_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.currency_widget = QGroupBox(page_crayon_1)
        self.currency_widget.setObjectName(u"currency_widget")
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(14)
        self.currency_widget.setFont(font3)
        self.horizontalLayout_8 = QHBoxLayout(self.currency_widget)
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 10, 20, 10)
        self.widget = QWidget(self.currency_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.IconGold = QLabel(self.widget)
        self.IconGold.setObjectName(u"IconGold")
        self.IconGold.setFont(font3)

        self.horizontalLayout_2.addWidget(self.IconGold)

        self.ValueGold = QLabel(self.widget)
        self.ValueGold.setObjectName(u"ValueGold")
        self.ValueGold.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.ValueGold)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LabelEraser1 = QLabel(self.widget)
        self.LabelEraser1.setObjectName(u"LabelEraser1")
        self.LabelEraser1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.LabelEraser1)

        self.ValueEraserGold = QLabel(self.widget)
        self.ValueEraserGold.setObjectName(u"ValueEraserGold")
        self.ValueEraserGold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.ValueEraserGold)

        self.LabelEraser2 = QLabel(self.widget)
        self.LabelEraser2.setObjectName(u"LabelEraser2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LabelEraser2.sizePolicy().hasHeightForWidth())
        self.LabelEraser2.setSizePolicy(sizePolicy4)
        self.LabelEraser2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.LabelEraser2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addWidget(self.widget)

        self.widget_2 = QWidget(self.currency_widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CurrencyLayout_2 = QHBoxLayout()
        self.CurrencyLayout_2.setSpacing(10)
        self.CurrencyLayout_2.setObjectName(u"CurrencyLayout_2")
        self.IconCrayon1 = QLabel(self.widget_2)
        self.IconCrayon1.setObjectName(u"IconCrayon1")

        self.CurrencyLayout_2.addWidget(self.IconCrayon1)

        self.ValueCrayon1 = QLabel(self.widget_2)
        self.ValueCrayon1.setObjectName(u"ValueCrayon1")
        self.ValueCrayon1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_2.addWidget(self.ValueCrayon1)


        self.gridLayout_2.addLayout(self.CurrencyLayout_2, 0, 0, 1, 1)

        self.CurrencyLayout_4 = QHBoxLayout()
        self.CurrencyLayout_4.setSpacing(10)
        self.CurrencyLayout_4.setObjectName(u"CurrencyLayout_4")
        self.IconCrayon3 = QLabel(self.widget_2)
        self.IconCrayon3.setObjectName(u"IconCrayon3")

        self.CurrencyLayout_4.addWidget(self.IconCrayon3)

        self.ValueCrayon3 = QLabel(self.widget_2)
        self.ValueCrayon3.setObjectName(u"ValueCrayon3")
        self.ValueCrayon3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_4.addWidget(self.ValueCrayon3)


        self.gridLayout_2.addLayout(self.CurrencyLayout_4, 0, 1, 1, 1)

        self.CurrencyLayout_3 = QHBoxLayout()
        self.CurrencyLayout_3.setSpacing(10)
        self.CurrencyLayout_3.setObjectName(u"CurrencyLayout_3")
        self.IconCrayon2 = QLabel(self.widget_2)
        self.IconCrayon2.setObjectName(u"IconCrayon2")

        self.CurrencyLayout_3.addWidget(self.IconCrayon2)

        self.ValueCrayon2 = QLabel(self.widget_2)
        self.ValueCrayon2.setObjectName(u"ValueCrayon2")
        self.ValueCrayon2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_3.addWidget(self.ValueCrayon2)


        self.gridLayout_2.addLayout(self.CurrencyLayout_3, 1, 0, 1, 1)

        self.CurrencyLayout_5 = QHBoxLayout()
        self.CurrencyLayout_5.setSpacing(10)
        self.CurrencyLayout_5.setObjectName(u"CurrencyLayout_5")
        self.IconCrayon4 = QLabel(self.widget_2)
        self.IconCrayon4.setObjectName(u"IconCrayon4")

        self.CurrencyLayout_5.addWidget(self.IconCrayon4)

        self.ValueCrayon4 = QLabel(self.widget_2)
        self.ValueCrayon4.setObjectName(u"ValueCrayon4")
        self.ValueCrayon4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_5.addWidget(self.ValueCrayon4)


        self.gridLayout_2.addLayout(self.CurrencyLayout_5, 1, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.currency_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_setAll_2 = QGroupBox(page_crayon_1)
        self.groupBox_setAll_2.setObjectName(u"groupBox_setAll_2")
        sizePolicy3.setHeightForWidth(self.groupBox_setAll_2.sizePolicy().hasHeightForWidth())
        self.groupBox_setAll_2.setSizePolicy(sizePolicy3)
        self.groupBox_setAll_2.setFont(font3)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_setAll_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.autoselect_off = QRadioButton(self.groupBox_setAll_2)
        self.autoselect_off.setObjectName(u"autoselect_off")
        self.autoselect_off.setFont(font2)
        self.autoselect_off.setChecked(True)

        self.verticalLayout_4.addWidget(self.autoselect_off)

        self.autoselect_length = QRadioButton(self.groupBox_setAll_2)
        self.autoselect_length.setObjectName(u"autoselect_length")
        self.autoselect_length.setFont(font2)

        self.verticalLayout_4.addWidget(self.autoselect_length)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.autoselect_cost = QRadioButton(self.groupBox_setAll_2)
        self.autoselect_cost.setObjectName(u"autoselect_cost")
        self.autoselect_cost.setFont(font2)

        self.horizontalLayout_5.addWidget(self.autoselect_cost)

        self.cost_1st = QComboBox(self.groupBox_setAll_2)
        self.cost_1st.addItem("")
        self.cost_1st.addItem("")
        self.cost_1st.addItem("")
        self.cost_1st.addItem("")
        self.cost_1st.setObjectName(u"cost_1st")
        self.cost_1st.setFont(font2)

        self.horizontalLayout_5.addWidget(self.cost_1st)

        self.cost_2nd = QComboBox(self.groupBox_setAll_2)
        self.cost_2nd.addItem("")
        self.cost_2nd.setObjectName(u"cost_2nd")
        self.cost_2nd.setFont(font2)

        self.horizontalLayout_5.addWidget(self.cost_2nd)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_9.addWidget(self.groupBox_setAll_2)

        self.groupBox_setAll_3 = QGroupBox(page_crayon_1)
        self.groupBox_setAll_3.setObjectName(u"groupBox_setAll_3")
        sizePolicy5.setHeightForWidth(self.groupBox_setAll_3.sizePolicy().hasHeightForWidth())
        self.groupBox_setAll_3.setSizePolicy(sizePolicy5)
        self.groupBox_setAll_3.setFont(font3)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_setAll_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.groupBox_setAll_3)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"ONE Mobile POP"])
        font4.setPointSize(13)
        self.label.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.select_normal_1_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_1_btn.setObjectName(u"select_normal_1_btn")
        self.select_normal_1_btn.setEnabled(True)
        font5 = QFont()
        font5.setFamilies([u"ONE Mobile POP"])
        font5.setPointSize(12)
        font5.setStrikeOut(False)
        self.select_normal_1_btn.setFont(font5)

        self.horizontalLayout_6.addWidget(self.select_normal_1_btn)

        self.select_normal_2_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_2_btn.setObjectName(u"select_normal_2_btn")
        self.select_normal_2_btn.setEnabled(True)
        self.select_normal_2_btn.setFont(font5)

        self.horizontalLayout_6.addWidget(self.select_normal_2_btn)

        self.select_normal_3_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_3_btn.setObjectName(u"select_normal_3_btn")
        self.select_normal_3_btn.setEnabled(True)
        self.select_normal_3_btn.setFont(font5)

        self.horizontalLayout_6.addWidget(self.select_normal_3_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_setAll_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.select_all_1_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_1_btn.setObjectName(u"select_all_1_btn")
        self.select_all_1_btn.setEnabled(True)
        self.select_all_1_btn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.select_all_1_btn)

        self.select_all_2_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_2_btn.setObjectName(u"select_all_2_btn")
        self.select_all_2_btn.setEnabled(True)
        self.select_all_2_btn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.select_all_2_btn)

        self.select_all_3_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_3_btn.setObjectName(u"select_all_3_btn")
        self.select_all_3_btn.setEnabled(True)
        self.select_all_3_btn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.select_all_3_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_9.addWidget(self.groupBox_setAll_3)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(page_crayon_1)

        QMetaObject.connectSlotsByName(page_crayon_1)
    # setupUi

    def retranslateUi(self, page_crayon_1):
        page_crayon_1.setWindowTitle(QCoreApplication.translate("page_crayon_1", u"Form", None))
        self.filter_btn.setText(QCoreApplication.translate("page_crayon_1", u" \uc0ac\ub3c4 \ubaa9\ub85d \ud544\ud130 ", None))
        self.go_left_btn.setText(QCoreApplication.translate("page_crayon_1", u"<", None))
        self.go_right_btn.setText(QCoreApplication.translate("page_crayon_1", u">", None))
        self.currency_widget.setTitle(QCoreApplication.translate("page_crayon_1", u"\uc18c\ubaa8\ud55c \uc7ac\ud654", None))
        self.IconGold.setText(QCoreApplication.translate("page_crayon_1", u"\uace8\ub4dc", None))
        self.ValueGold.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.LabelEraser1.setText(QCoreApplication.translate("page_crayon_1", u"\uc9c0\uc6b0\uac1c \uc0ac\uc6a9 \uc2dc", None))
        self.ValueEraserGold.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.LabelEraser2.setText(QCoreApplication.translate("page_crayon_1", u"\uace8\ub4dc \uc18c\ubaa8", None))
        self.IconCrayon1.setText(QCoreApplication.translate("page_crayon_1", u"\ud770\ud06c", None))
        self.ValueCrayon1.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.IconCrayon3.setText(QCoreApplication.translate("page_crayon_1", u"\ubcf4\ud06c", None))
        self.ValueCrayon3.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.IconCrayon2.setText(QCoreApplication.translate("page_crayon_1", u"\ud30c\ud06c", None))
        self.ValueCrayon2.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.IconCrayon4.setText(QCoreApplication.translate("page_crayon_1", u"\ud669\ud06c", None))
        self.ValueCrayon4.setText(QCoreApplication.translate("page_crayon_1", u"0", None))
        self.groupBox_setAll_2.setTitle(QCoreApplication.translate("page_crayon_1", u"\uc790\ub3d9 \uc120\ud0dd \uc124\uc815", None))
        self.autoselect_off.setText(QCoreApplication.translate("page_crayon_1", u"\ub044\uae30", None))
        self.autoselect_length.setText(QCoreApplication.translate("page_crayon_1", u"\ucd5c\ub2e8\uacbd\ub85c", None))
        self.autoselect_cost.setText(QCoreApplication.translate("page_crayon_1", u"\ucd5c\uc18c\ube44\uc6a9", None))
        self.cost_1st.setItemText(0, QCoreApplication.translate("page_crayon_1", u"1\uc21c\uc704", None))
        self.cost_1st.setItemText(1, QCoreApplication.translate("page_crayon_1", u"\ud669\ud06c", None))
        self.cost_1st.setItemText(2, QCoreApplication.translate("page_crayon_1", u"\ubcf4\ud06c", None))
        self.cost_1st.setItemText(3, QCoreApplication.translate("page_crayon_1", u"\uace8\ub4dc", None))

        self.cost_1st.setPlaceholderText("")
        self.cost_2nd.setItemText(0, QCoreApplication.translate("page_crayon_1", u"2\uc21c\uc704", None))

        self.cost_2nd.setPlaceholderText("")
        self.groupBox_setAll_3.setTitle(QCoreApplication.translate("page_crayon_1", u"\uac04\ud3b8 \uc120\ud0dd", None))
        self.label.setText(QCoreApplication.translate("page_crayon_1", u"\uc77c\ubc18\uce78 \uc77c\uad04\uc120\ud0dd", None))
        self.select_normal_1_btn.setText(QCoreApplication.translate("page_crayon_1", u"1\uad00", None))
        self.select_normal_2_btn.setText(QCoreApplication.translate("page_crayon_1", u"2\uad00", None))
        self.select_normal_3_btn.setText(QCoreApplication.translate("page_crayon_1", u"3\uad00", None))
        self.label_2.setText(QCoreApplication.translate("page_crayon_1", u"\uc804\uccb4\uce78 \uc77c\uad04\uc120\ud0dd", None))
        self.select_all_1_btn.setText(QCoreApplication.translate("page_crayon_1", u"1\uad00", None))
        self.select_all_2_btn.setText(QCoreApplication.translate("page_crayon_1", u"2\uad00", None))
        self.select_all_3_btn.setText(QCoreApplication.translate("page_crayon_1", u"3\uad00", None))
    # retranslateUi

