# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equip_window_1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_equip_window_1(object):
    def setupUi(self, equip_window_1):
        if not equip_window_1.objectName():
            equip_window_1.setObjectName(u"equip_window_1")
        equip_window_1.resize(685, 512)
        self.verticalLayout = QVBoxLayout(equip_window_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hero_select = QComboBox(equip_window_1)
        self.hero_select.setObjectName(u"hero_select")

        self.verticalLayout.addWidget(self.hero_select)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.go_left_btn = QPushButton(equip_window_1)
        self.go_left_btn.setObjectName(u"go_left_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_left_btn.sizePolicy().hasHeightForWidth())
        self.go_left_btn.setSizePolicy(sizePolicy)
        self.go_left_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.go_left_btn)

        self.rank_table = QTableWidget(equip_window_1)
        if (self.rank_table.columnCount() < 6):
            self.rank_table.setColumnCount(6)
        self.rank_table.setObjectName(u"rank_table")

        self.horizontalLayout.addWidget(self.rank_table)

        self.go_right_btn = QPushButton(equip_window_1)
        self.go_right_btn.setObjectName(u"go_right_btn")
        sizePolicy.setHeightForWidth(self.go_right_btn.sizePolicy().hasHeightForWidth())
        self.go_right_btn.setSizePolicy(sizePolicy)
        self.go_right_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.go_right_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.save_all_btn = QPushButton(equip_window_1)
        self.save_all_btn.setObjectName(u"save_all_btn")

        self.gridLayout.addWidget(self.save_all_btn, 0, 0, 1, 1)

        self.save_cur_btn = QPushButton(equip_window_1)
        self.save_cur_btn.setObjectName(u"save_cur_btn")

        self.gridLayout.addWidget(self.save_cur_btn, 0, 1, 1, 1)

        self.undo_all_btn = QPushButton(equip_window_1)
        self.undo_all_btn.setObjectName(u"undo_all_btn")

        self.gridLayout.addWidget(self.undo_all_btn, 1, 0, 1, 1)

        self.undo_cur_btn = QPushButton(equip_window_1)
        self.undo_cur_btn.setObjectName(u"undo_cur_btn")

        self.gridLayout.addWidget(self.undo_cur_btn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(equip_window_1)

        QMetaObject.connectSlotsByName(equip_window_1)
    # setupUi

    def retranslateUi(self, equip_window_1):
        equip_window_1.setWindowTitle(QCoreApplication.translate("equip_window_1", u"Form", None))
        self.go_left_btn.setText(QCoreApplication.translate("equip_window_1", u"<", None))
        self.go_right_btn.setText(QCoreApplication.translate("equip_window_1", u">", None))
        self.save_all_btn.setText(QCoreApplication.translate("equip_window_1", u"\ubaa8\ub450 \uc800\uc7a5", None))
        self.save_cur_btn.setText(QCoreApplication.translate("equip_window_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \uc800\uc7a5", None))
        self.undo_all_btn.setText(QCoreApplication.translate("equip_window_1", u"\ubcc0\uacbd\uc0ac\ud56d \ubaa8\ub450 \ucde8\uc18c", None))
        self.undo_cur_btn.setText(QCoreApplication.translate("equip_window_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \ubcc0\uacbd\uc0ac\ud56d \ucde8\uc18c", None))
    # retranslateUi

