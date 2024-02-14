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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from widgets.wrapper.misc import ExtendedComboBox

class Ui_page_crayon_1(object):
    def setupUi(self, page_crayon_1):
        if not page_crayon_1.objectName():
            page_crayon_1.setObjectName(u"page_crayon_1")
        page_crayon_1.resize(800, 633)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.go_left_btn.sizePolicy().hasHeightForWidth())
        self.go_left_btn.setSizePolicy(sizePolicy2)
        self.go_left_btn.setMaximumSize(QSize(30, 16777215))
        self.go_left_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.go_left_btn)

        self.board_table = QTableWidget(page_crayon_1)
        self.board_table.setObjectName(u"board_table")
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(10)
        self.board_table.setFont(font3)
        self.board_table.setColumnCount(0)

        self.horizontalLayout.addWidget(self.board_table)

        self.go_right_btn = QPushButton(page_crayon_1)
        self.go_right_btn.setObjectName(u"go_right_btn")
        sizePolicy2.setHeightForWidth(self.go_right_btn.sizePolicy().hasHeightForWidth())
        self.go_right_btn.setSizePolicy(sizePolicy2)
        self.go_right_btn.setMaximumSize(QSize(30, 16777215))
        self.go_right_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.go_right_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_setAll = QGroupBox(page_crayon_1)
        self.groupBox_setAll.setObjectName(u"groupBox_setAll")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_setAll.sizePolicy().hasHeightForWidth())
        self.groupBox_setAll.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"ONE Mobile POP"])
        font4.setPointSize(14)
        self.groupBox_setAll.setFont(font4)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_setAll)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = QCheckBox(self.groupBox_setAll)
        self.checkBox_2.setObjectName(u"checkBox_2")
        font5 = QFont()
        font5.setFamilies([u"ONE Mobile POP"])
        font5.setPointSize(13)
        self.checkBox_2.setFont(font5)

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.groupBox_setAll)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font5)

        self.verticalLayout_3.addWidget(self.checkBox)


        self.gridLayout_3.addWidget(self.groupBox_setAll, 0, 0, 1, 1)

        self.groupBox_setAll_3 = QGroupBox(page_crayon_1)
        self.groupBox_setAll_3.setObjectName(u"groupBox_setAll_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_setAll_3.sizePolicy().hasHeightForWidth())
        self.groupBox_setAll_3.setSizePolicy(sizePolicy4)
        self.groupBox_setAll_3.setFont(font4)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_setAll_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.groupBox_setAll_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.select_normal_1_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_1_btn.setObjectName(u"select_normal_1_btn")
        self.select_normal_1_btn.setEnabled(True)
        font6 = QFont()
        font6.setFamilies([u"ONE Mobile POP"])
        font6.setPointSize(12)
        font6.setStrikeOut(False)
        self.select_normal_1_btn.setFont(font6)

        self.horizontalLayout_6.addWidget(self.select_normal_1_btn)

        self.select_normal_2_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_2_btn.setObjectName(u"select_normal_2_btn")
        self.select_normal_2_btn.setEnabled(True)
        self.select_normal_2_btn.setFont(font6)

        self.horizontalLayout_6.addWidget(self.select_normal_2_btn)

        self.select_normal_3_btn = QPushButton(self.groupBox_setAll_3)
        self.select_normal_3_btn.setObjectName(u"select_normal_3_btn")
        self.select_normal_3_btn.setEnabled(True)
        self.select_normal_3_btn.setFont(font6)

        self.horizontalLayout_6.addWidget(self.select_normal_3_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_setAll_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.select_all_1_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_1_btn.setObjectName(u"select_all_1_btn")
        self.select_all_1_btn.setEnabled(True)
        self.select_all_1_btn.setFont(font6)

        self.horizontalLayout_4.addWidget(self.select_all_1_btn)

        self.select_all_2_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_2_btn.setObjectName(u"select_all_2_btn")
        self.select_all_2_btn.setEnabled(True)
        self.select_all_2_btn.setFont(font6)

        self.horizontalLayout_4.addWidget(self.select_all_2_btn)

        self.select_all_3_btn = QPushButton(self.groupBox_setAll_3)
        self.select_all_3_btn.setObjectName(u"select_all_3_btn")
        self.select_all_3_btn.setEnabled(True)
        self.select_all_3_btn.setFont(font6)

        self.horizontalLayout_4.addWidget(self.select_all_3_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addWidget(self.groupBox_setAll_3, 0, 1, 1, 1)

        self.groupBox_setAll_2 = QGroupBox(page_crayon_1)
        self.groupBox_setAll_2.setObjectName(u"groupBox_setAll_2")
        sizePolicy3.setHeightForWidth(self.groupBox_setAll_2.sizePolicy().hasHeightForWidth())
        self.groupBox_setAll_2.setSizePolicy(sizePolicy3)
        self.groupBox_setAll_2.setFont(font4)
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


        self.gridLayout_3.addWidget(self.groupBox_setAll_2, 1, 0, 1, 1)

        self.groupBox_save_undo = QGroupBox(page_crayon_1)
        self.groupBox_save_undo.setObjectName(u"groupBox_save_undo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_save_undo.sizePolicy().hasHeightForWidth())
        self.groupBox_save_undo.setSizePolicy(sizePolicy5)
        self.groupBox_save_undo.setFont(font4)
        self.gridLayout = QGridLayout(self.groupBox_save_undo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.save_all_btn = QPushButton(self.groupBox_save_undo)
        self.save_all_btn.setObjectName(u"save_all_btn")
        self.save_all_btn.setEnabled(True)
        self.save_all_btn.setFont(font6)

        self.gridLayout.addWidget(self.save_all_btn, 0, 0, 1, 1)

        self.undo_cur_btn = QPushButton(self.groupBox_save_undo)
        self.undo_cur_btn.setObjectName(u"undo_cur_btn")
        self.undo_cur_btn.setFont(font2)

        self.gridLayout.addWidget(self.undo_cur_btn, 1, 1, 1, 1)

        self.save_cur_btn = QPushButton(self.groupBox_save_undo)
        self.save_cur_btn.setObjectName(u"save_cur_btn")
        self.save_cur_btn.setFont(font2)

        self.gridLayout.addWidget(self.save_cur_btn, 0, 1, 1, 1)

        self.undo_all_btn = QPushButton(self.groupBox_save_undo)
        self.undo_all_btn.setObjectName(u"undo_all_btn")
        self.undo_all_btn.setFont(font2)

        self.gridLayout.addWidget(self.undo_all_btn, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_save_undo, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.retranslateUi(page_crayon_1)

        QMetaObject.connectSlotsByName(page_crayon_1)
    # setupUi

    def retranslateUi(self, page_crayon_1):
        page_crayon_1.setWindowTitle(QCoreApplication.translate("page_crayon_1", u"Form", None))
        self.filter_btn.setText(QCoreApplication.translate("page_crayon_1", u" \uc0ac\ub3c4 \ubaa9\ub85d \ud544\ud130 ", None))
        self.go_left_btn.setText(QCoreApplication.translate("page_crayon_1", u"<", None))
        self.go_right_btn.setText(QCoreApplication.translate("page_crayon_1", u">", None))
        self.groupBox_setAll.setTitle(QCoreApplication.translate("page_crayon_1", u"\ud45c\uc2dc \uc124\uc815", None))
        self.checkBox_2.setText(QCoreApplication.translate("page_crayon_1", u"\uc2a4\ud0ef \uc124\uba85 \uc790\uc138\ud788 \ud45c\uc2dc", None))
        self.checkBox.setText(QCoreApplication.translate("page_crayon_1", u"\uc77c\ubc18\uce78 \uc2a4\ud0ef \uc885\ub958 \ud45c\uc2dc", None))
        self.groupBox_setAll_3.setTitle(QCoreApplication.translate("page_crayon_1", u"\uac04\ud3b8 \uc120\ud0dd", None))
        self.label.setText(QCoreApplication.translate("page_crayon_1", u"\uc77c\ubc18\uce78 \uc77c\uad04\uc120\ud0dd", None))
        self.select_normal_1_btn.setText(QCoreApplication.translate("page_crayon_1", u"1\uad00", None))
        self.select_normal_2_btn.setText(QCoreApplication.translate("page_crayon_1", u"2\uad00", None))
        self.select_normal_3_btn.setText(QCoreApplication.translate("page_crayon_1", u"3\uad00", None))
        self.label_2.setText(QCoreApplication.translate("page_crayon_1", u"\uc804\uccb4\uce78 \uc77c\uad04\uc120\ud0dd", None))
        self.select_all_1_btn.setText(QCoreApplication.translate("page_crayon_1", u"1\uad00", None))
        self.select_all_2_btn.setText(QCoreApplication.translate("page_crayon_1", u"2\uad00", None))
        self.select_all_3_btn.setText(QCoreApplication.translate("page_crayon_1", u"3\uad00", None))
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
        self.groupBox_save_undo.setTitle(QCoreApplication.translate("page_crayon_1", u"\uc800\uc7a5 / \ucde8\uc18c", None))
        self.save_all_btn.setText(QCoreApplication.translate("page_crayon_1", u"\ubaa8\ub450 \uc800\uc7a5", None))
        self.undo_cur_btn.setText(QCoreApplication.translate("page_crayon_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \ubcc0\uacbd\uc0ac\ud56d \ucde8\uc18c", None))
        self.save_cur_btn.setText(QCoreApplication.translate("page_crayon_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \uc800\uc7a5", None))
        self.undo_all_btn.setText(QCoreApplication.translate("page_crayon_1", u"\ubcc0\uacbd\uc0ac\ud56d \ubaa8\ub450 \ucde8\uc18c", None))
    # retranslateUi

