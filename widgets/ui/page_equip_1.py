# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_equip_1.ui'
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

from widgets.wrapper.extended_combobox import ExtendedComboBox

class Ui_page_equip_1(object):
    def setupUi(self, page_equip_1):
        if not page_equip_1.objectName():
            page_equip_1.setObjectName(u"page_equip_1")
        page_equip_1.resize(800, 633)
        self.verticalLayout_5 = QVBoxLayout(page_equip_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.hero_select = ExtendedComboBox(page_equip_1)
        self.hero_select.setObjectName(u"hero_select")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hero_select.sizePolicy().hasHeightForWidth())
        self.hero_select.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.hero_select)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.go_left_btn = QPushButton(page_equip_1)
        self.go_left_btn.setObjectName(u"go_left_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.go_left_btn.sizePolicy().hasHeightForWidth())
        self.go_left_btn.setSizePolicy(sizePolicy1)
        self.go_left_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.go_left_btn)

        self.rank_table = QTableWidget(page_equip_1)
        self.rank_table.setObjectName(u"rank_table")
        self.rank_table.setColumnCount(0)

        self.horizontalLayout.addWidget(self.rank_table)

        self.go_right_btn = QPushButton(page_equip_1)
        self.go_right_btn.setObjectName(u"go_right_btn")
        sizePolicy1.setHeightForWidth(self.go_right_btn.sizePolicy().hasHeightForWidth())
        self.go_right_btn.setSizePolicy(sizePolicy1)
        self.go_right_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.go_right_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(page_equip_1)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.combo_cur_rank = QComboBox(self.widget)
        self.combo_cur_rank.setObjectName(u"combo_cur_rank")

        self.gridLayout_4.addWidget(self.combo_cur_rank, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.combo_goal_rank = QComboBox(self.widget)
        self.combo_goal_rank.setObjectName(u"combo_goal_rank")

        self.gridLayout_4.addWidget(self.combo_goal_rank, 1, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)

        self.horizontalSpacer = QSpacerItem(99, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.check_complete = QCheckBox(self.widget)
        self.check_complete.setObjectName(u"check_complete")

        self.horizontalLayout_4.addWidget(self.check_complete)


        self.horizontalLayout_5.addWidget(self.widget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_setAll = QGroupBox(page_equip_1)
        self.groupBox_setAll.setObjectName(u"groupBox_setAll")
        self.gridLayout = QGridLayout(self.groupBox_setAll)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_target = QGroupBox(self.groupBox_setAll)
        self.groupBox_target.setObjectName(u"groupBox_target")
        self.verticalLayout = QVBoxLayout(self.groupBox_target)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_cur = QRadioButton(self.groupBox_target)
        self.radio_cur.setObjectName(u"radio_cur")

        self.verticalLayout.addWidget(self.radio_cur)

        self.radio_all = QRadioButton(self.groupBox_target)
        self.radio_all.setObjectName(u"radio_all")

        self.verticalLayout.addWidget(self.radio_all)


        self.gridLayout.addWidget(self.groupBox_target, 0, 0, 2, 1)

        self.set_goal_w_stat_btn = QPushButton(self.groupBox_setAll)
        self.set_goal_w_stat_btn.setObjectName(u"set_goal_w_stat_btn")

        self.gridLayout.addWidget(self.set_goal_w_stat_btn, 2, 0, 1, 2)

        self.set_uncheck_btn = QPushButton(self.groupBox_setAll)
        self.set_uncheck_btn.setObjectName(u"set_uncheck_btn")

        self.gridLayout.addWidget(self.set_uncheck_btn, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_set_goal = QComboBox(self.groupBox_setAll)
        self.combo_set_goal.setObjectName(u"combo_set_goal")

        self.horizontalLayout_2.addWidget(self.combo_set_goal)

        self.label_2 = QLabel(self.groupBox_setAll)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.set_check_btn = QPushButton(self.groupBox_setAll)
        self.set_check_btn.setObjectName(u"set_check_btn")

        self.horizontalLayout_2.addWidget(self.set_check_btn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_setAll)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_mode = QGroupBox(page_equip_1)
        self.groupBox_mode.setObjectName(u"groupBox_mode")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_mode)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_cur_mode = QRadioButton(self.groupBox_mode)
        self.radio_cur_mode.setObjectName(u"radio_cur_mode")

        self.verticalLayout_2.addWidget(self.radio_cur_mode)

        self.radio_goal_mode = QRadioButton(self.groupBox_mode)
        self.radio_goal_mode.setObjectName(u"radio_goal_mode")

        self.verticalLayout_2.addWidget(self.radio_goal_mode)


        self.horizontalLayout_3.addWidget(self.groupBox_mode)

        self.groupBox_ease = QGroupBox(page_equip_1)
        self.groupBox_ease.setObjectName(u"groupBox_ease")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_ease)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.filter_btn = QPushButton(self.groupBox_ease)
        self.filter_btn.setObjectName(u"filter_btn")

        self.verticalLayout_3.addWidget(self.filter_btn)

        self.check_ease = QCheckBox(self.groupBox_ease)
        self.check_ease.setObjectName(u"check_ease")

        self.verticalLayout_3.addWidget(self.check_ease)


        self.horizontalLayout_3.addWidget(self.groupBox_ease)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.save_all_btn = QPushButton(page_equip_1)
        self.save_all_btn.setObjectName(u"save_all_btn")

        self.gridLayout_2.addWidget(self.save_all_btn, 0, 0, 1, 1)

        self.save_cur_btn = QPushButton(page_equip_1)
        self.save_cur_btn.setObjectName(u"save_cur_btn")

        self.gridLayout_2.addWidget(self.save_cur_btn, 0, 1, 1, 1)

        self.undo_all_btn = QPushButton(page_equip_1)
        self.undo_all_btn.setObjectName(u"undo_all_btn")

        self.gridLayout_2.addWidget(self.undo_all_btn, 1, 0, 1, 1)

        self.undo_cur_btn = QPushButton(page_equip_1)
        self.undo_cur_btn.setObjectName(u"undo_cur_btn")

        self.gridLayout_2.addWidget(self.undo_cur_btn, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.retranslateUi(page_equip_1)

        QMetaObject.connectSlotsByName(page_equip_1)
    # setupUi

    def retranslateUi(self, page_equip_1):
        page_equip_1.setWindowTitle(QCoreApplication.translate("page_equip_1", u"Form", None))
        self.go_left_btn.setText(QCoreApplication.translate("page_equip_1", u"<", None))
        self.go_right_btn.setText(QCoreApplication.translate("page_equip_1", u">", None))
        self.label.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ub7ad\ud06c :", None))
        self.label_4.setText(QCoreApplication.translate("page_equip_1", u"\ubaa9\ud45c \ub7ad\ud06c :", None))
        self.check_complete.setText(QCoreApplication.translate("page_equip_1", u"\uc721\uc131 \uc644\ub8cc!", None))
        self.groupBox_setAll.setTitle(QCoreApplication.translate("page_equip_1", u"\uc77c\uad04 \uc124\uc815\ud558\uae30", None))
        self.groupBox_target.setTitle(QCoreApplication.translate("page_equip_1", u"\uc801\uc6a9 \ub300\uc0c1", None))
        self.radio_cur.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \uc0ac\ub3c4", None))
        self.radio_all.setText(QCoreApplication.translate("page_equip_1", u"\uc804\uccb4 \uc0ac\ub3c4", None))
        self.set_goal_w_stat_btn.setText(QCoreApplication.translate("page_equip_1", u"\uc2a4\ud0ef \ubcc4 \ub7ad\ud06c\uc791 \ubaa9\ud45c \uc77c\uad04 \uc124\uc815", None))
        self.set_uncheck_btn.setText(QCoreApplication.translate("page_equip_1", u"\uc804\ubd80 \uccb4\ud06c \ud574\uc81c", None))
        self.label_2.setText(QCoreApplication.translate("page_equip_1", u"\ub7ad\ud06c\uae4c\uc9c0", None))
        self.set_check_btn.setText(QCoreApplication.translate("page_equip_1", u"\uccb4\ud06c", None))
        self.groupBox_mode.setTitle(QCoreApplication.translate("page_equip_1", u"\ubaa8\ub4dc", None))
        self.radio_cur_mode.setText(QCoreApplication.translate("page_equip_1", u"\ucc29\uc6a9 \uc7a5\ube44 \uae30\ub85d", None))
        self.radio_goal_mode.setText(QCoreApplication.translate("page_equip_1", u"\ubaa9\ud45c \uc124\uc815", None))
        self.groupBox_ease.setTitle(QCoreApplication.translate("page_equip_1", u"\ud3b8\uc758\uc131", None))
        self.filter_btn.setText(QCoreApplication.translate("page_equip_1", u"\uc0ac\ub3c4 \ubaa9\ub85d \ud544\ud130", None))
        self.check_ease.setText(QCoreApplication.translate("page_equip_1", u"7\ub7ad \ud480\ud15c\uc740 \uc790\ub3d9\uc73c\ub85c \uc721\uc131 \uc644\ub8cc \ud45c\uc2dc", None))
        self.save_all_btn.setText(QCoreApplication.translate("page_equip_1", u"\ubaa8\ub450 \uc800\uc7a5", None))
        self.save_cur_btn.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \uc800\uc7a5", None))
        self.undo_all_btn.setText(QCoreApplication.translate("page_equip_1", u"\ubcc0\uacbd\uc0ac\ud56d \ubaa8\ub450 \ucde8\uc18c", None))
        self.undo_cur_btn.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \ubcc0\uacbd\uc0ac\ud56d \ucde8\uc18c", None))
    # retranslateUi

