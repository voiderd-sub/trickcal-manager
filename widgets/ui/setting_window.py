# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_setting_window(object):
    def setupUi(self, setting_window):
        if not setting_window.objectName():
            setting_window.setObjectName(u"setting_window")
        setting_window.resize(800, 600)
        self.centralwidget = QWidget(setting_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_btn_1 = QPushButton(self.widget)
        self.menu_btn_1.setObjectName(u"menu_btn_1")
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(18)
        self.menu_btn_1.setFont(font)
        self.menu_btn_1.setCheckable(True)
        self.menu_btn_1.setChecked(True)

        self.verticalLayout.addWidget(self.menu_btn_1)

        self.verticalSpacer = QSpacerItem(20, 481, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.save_btn = QPushButton(self.widget)
        self.save_btn.setObjectName(u"save_btn")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(14)
        self.save_btn.setFont(font1)

        self.verticalLayout.addWidget(self.save_btn)

        self.exit_btn = QPushButton(self.widget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setFont(font1)

        self.verticalLayout.addWidget(self.exit_btn)


        self.horizontalLayout.addWidget(self.widget)

        self.setting_stacks = QStackedWidget(self.centralwidget)
        self.setting_stacks.setObjectName(u"setting_stacks")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setting_stacks.sizePolicy().hasHeightForWidth())
        self.setting_stacks.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(15)
        self.setting_stacks.setFont(font2)
        self.page_update = QWidget()
        self.page_update.setObjectName(u"page_update")
        self.verticalLayout_4 = QVBoxLayout(self.page_update)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.page_update)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_version = QLabel(self.page_update)
        self.label_version.setObjectName(u"label_version")
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(13)
        self.label_version.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_version)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.page_update)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.setting_update_program = QPushButton(self.page_update)
        self.setting_update_program.setObjectName(u"setting_update_program")
        self.setting_update_program.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setting_update_program.sizePolicy().hasHeightForWidth())
        self.setting_update_program.setSizePolicy(sizePolicy2)
        self.setting_update_program.setMaximumSize(QSize(20, 20))
        font4 = QFont()
        font4.setFamilies([u"ONE Mobile POP"])
        font4.setPointSize(8)
        self.setting_update_program.setFont(font4)
        self.setting_update_program.setCheckable(True)
        self.setting_update_program.setChecked(False)

        self.horizontalLayout_3.addWidget(self.setting_update_program)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_update)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_update)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamilies([u"ONE Mobile POP"])
        font5.setPointSize(12)
        self.label_4.setFont(font5)

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.setting_update_drop = QPushButton(self.page_update)
        self.setting_update_drop.setObjectName(u"setting_update_drop")
        self.setting_update_drop.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.setting_update_drop.sizePolicy().hasHeightForWidth())
        self.setting_update_drop.setSizePolicy(sizePolicy2)
        self.setting_update_drop.setMaximumSize(QSize(20, 20))
        self.setting_update_drop.setFont(font4)
        self.setting_update_drop.setCheckable(True)
        self.setting_update_drop.setChecked(False)

        self.horizontalLayout_4.addWidget(self.setting_update_drop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.groupBox = QGroupBox(self.page_update)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.update_btn_program = QPushButton(self.groupBox)
        self.update_btn_program.setObjectName(u"update_btn_program")
        self.update_btn_program.setFont(font3)

        self.horizontalLayout_6.addWidget(self.update_btn_program)

        self.update_btn_master = QPushButton(self.groupBox)
        self.update_btn_master.setObjectName(u"update_btn_master")
        self.update_btn_master.setFont(font3)

        self.horizontalLayout_6.addWidget(self.update_btn_master)

        self.update_btn_drop = QPushButton(self.groupBox)
        self.update_btn_drop.setObjectName(u"update_btn_drop")
        self.update_btn_drop.setFont(font3)

        self.horizontalLayout_6.addWidget(self.update_btn_drop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"ONE Mobile POP"])
        font6.setPointSize(11)
        self.label_5.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.setting_stacks.addWidget(self.page_update)

        self.horizontalLayout.addWidget(self.setting_stacks)

        setting_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(setting_window)

        QMetaObject.connectSlotsByName(setting_window)
    # setupUi

    def retranslateUi(self, setting_window):
        setting_window.setWindowTitle(QCoreApplication.translate("setting_window", u"MainWindow", None))
        self.menu_btn_1.setText(QCoreApplication.translate("setting_window", u"\uc5c5\ub370\uc774\ud2b8", None))
        self.save_btn.setText(QCoreApplication.translate("setting_window", u"\uc800\uc7a5", None))
        self.exit_btn.setText(QCoreApplication.translate("setting_window", u"\ub2eb\uae30", None))
        self.label.setText(QCoreApplication.translate("setting_window", u"\ud604\uc7ac \ubc84\uc804", None))
        self.label_version.setText(QCoreApplication.translate("setting_window", u"\uc784\uc2dc \ud14d\uc2a4\ud2b8", None))
        self.label_2.setText(QCoreApplication.translate("setting_window", u"24\uc2dc\uac04\ub9c8\ub2e4 \ucd5c\uc2e0 \ubc84\uc804 \uccb4\ud06c", None))
        self.setting_update_program.setText("")
        self.label_3.setText(QCoreApplication.translate("setting_window", u"24\uc2dc\uac04\ub9c8\ub2e4 \ub4dc\ub78d \ud14c\uc774\ube14 \uc5c5\ub370\uc774\ud2b8", None))
        self.label_4.setText(QCoreApplication.translate("setting_window", u"(10\ucd08 \uc815\ub3c4 \uc18c\uc694\ub429\ub2c8\ub2e4)", None))
        self.setting_update_drop.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("setting_window", u"\uc218\ub3d9 \uc5c5\ub370\uc774\ud2b8", None))
        self.update_btn_program.setText(QCoreApplication.translate("setting_window", u"\ud504\ub85c\uadf8\ub7a8 \ubc84\uc804", None))
        self.update_btn_master.setText(QCoreApplication.translate("setting_window", u"master.db", None))
        self.update_btn_drop.setText(QCoreApplication.translate("setting_window", u"\ub4dc\ub78d \ud14c\uc774\ube14", None))
        self.label_5.setText(QCoreApplication.translate("setting_window", u"\u203b master.db : \uc2e0\uaddc \uc0ac\ub3c4 / \ub7ad\ud06c \uc0dd\uae38 \ub54c \uc5c5\ub370\uc774\ud2b8\ud558\ub294 \ud30c\uc77c", None))
    # retranslateUi

