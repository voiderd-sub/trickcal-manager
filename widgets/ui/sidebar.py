# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(280, 700)
        self.verticalLayout_5 = QVBoxLayout(sidebar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(13, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.sidebar_name_label = QLabel(sidebar)
        self.sidebar_name_label.setObjectName(u"sidebar_name_label")

        self.horizontalLayout.addWidget(self.sidebar_name_label)

        self.horizontalSpacer = QSpacerItem(13, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.home_btn = QPushButton(sidebar)
        self.main_menu_group = QButtonGroup(sidebar)
        self.main_menu_group.setObjectName(u"main_menu_group")
        self.main_menu_group.addButton(self.home_btn)
        self.home_btn.setObjectName(u"home_btn")
        icon = QIcon()
        icon.addFile(u"icon/sidebar/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(25, 25))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.home_btn)

        self.hero_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.hero_btn)
        self.hero_btn.setObjectName(u"hero_btn")
        icon1 = QIcon()
        icon1.addFile(u"icon/sidebar/hero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hero_btn.setIcon(icon1)
        self.hero_btn.setIconSize(QSize(25, 25))
        self.hero_btn.setCheckable(True)
        self.hero_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.hero_btn)

        self.equip_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.equip_btn)
        self.equip_btn.setObjectName(u"equip_btn")
        icon2 = QIcon()
        icon2.addFile(u"icon/sidebar/equip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.equip_btn.setIcon(icon2)
        self.equip_btn.setIconSize(QSize(25, 25))
        self.equip_btn.setCheckable(True)
        self.equip_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.equip_btn)

        self.equip_sub = QWidget(sidebar)
        self.equip_sub.setObjectName(u"equip_sub")
        self.verticalLayout = QVBoxLayout(self.equip_sub)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.equip_sub_btn_1 = QPushButton(self.equip_sub)
        self.equip_group = QButtonGroup(sidebar)
        self.equip_group.setObjectName(u"equip_group")
        self.equip_group.addButton(self.equip_sub_btn_1)
        self.equip_sub_btn_1.setObjectName(u"equip_sub_btn_1")
        self.equip_sub_btn_1.setIconSize(QSize(25, 25))
        self.equip_sub_btn_1.setCheckable(True)
        self.equip_sub_btn_1.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_sub_btn_1)

        self.equip_sub_btn_2 = QPushButton(self.equip_sub)
        self.equip_group.addButton(self.equip_sub_btn_2)
        self.equip_sub_btn_2.setObjectName(u"equip_sub_btn_2")
        self.equip_sub_btn_2.setIconSize(QSize(25, 25))
        self.equip_sub_btn_2.setCheckable(True)
        self.equip_sub_btn_2.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_sub_btn_2)

        self.equip_sub_btn_3 = QPushButton(self.equip_sub)
        self.equip_group.addButton(self.equip_sub_btn_3)
        self.equip_sub_btn_3.setObjectName(u"equip_sub_btn_3")
        self.equip_sub_btn_3.setIconSize(QSize(25, 25))
        self.equip_sub_btn_3.setCheckable(True)
        self.equip_sub_btn_3.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_sub_btn_3)


        self.verticalLayout_5.addWidget(self.equip_sub)

        self.crayon_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.crayon_btn)
        self.crayon_btn.setObjectName(u"crayon_btn")
        icon3 = QIcon()
        icon3.addFile(u"icon/sidebar/crayon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crayon_btn.setIcon(icon3)
        self.crayon_btn.setIconSize(QSize(25, 25))
        self.crayon_btn.setCheckable(True)
        self.crayon_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.crayon_btn)

        self.crayon_sub = QWidget(sidebar)
        self.crayon_sub.setObjectName(u"crayon_sub")
        self.verticalLayout_2 = QVBoxLayout(self.crayon_sub)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.crayon_sub_btn_1 = QPushButton(self.crayon_sub)
        self.crayon_group = QButtonGroup(sidebar)
        self.crayon_group.setObjectName(u"crayon_group")
        self.crayon_group.addButton(self.crayon_sub_btn_1)
        self.crayon_sub_btn_1.setObjectName(u"crayon_sub_btn_1")
        self.crayon_sub_btn_1.setIconSize(QSize(25, 25))
        self.crayon_sub_btn_1.setCheckable(True)
        self.crayon_sub_btn_1.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.crayon_sub_btn_1)

        self.crayon_sub_btn_2 = QPushButton(self.crayon_sub)
        self.crayon_group.addButton(self.crayon_sub_btn_2)
        self.crayon_sub_btn_2.setObjectName(u"crayon_sub_btn_2")
        self.crayon_sub_btn_2.setIconSize(QSize(25, 25))
        self.crayon_sub_btn_2.setCheckable(True)
        self.crayon_sub_btn_2.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.crayon_sub_btn_2)


        self.verticalLayout_5.addWidget(self.crayon_sub)

        self.food_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.food_btn)
        self.food_btn.setObjectName(u"food_btn")
        icon4 = QIcon()
        icon4.addFile(u"icon/sidebar/food.png", QSize(), QIcon.Normal, QIcon.Off)
        self.food_btn.setIcon(icon4)
        self.food_btn.setIconSize(QSize(25, 25))
        self.food_btn.setCheckable(True)
        self.food_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.food_btn)

        self.food_sub = QWidget(sidebar)
        self.food_sub.setObjectName(u"food_sub")
        self.verticalLayout_4 = QVBoxLayout(self.food_sub)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.food_sub_btn_1 = QPushButton(self.food_sub)
        self.food_group = QButtonGroup(sidebar)
        self.food_group.setObjectName(u"food_group")
        self.food_group.addButton(self.food_sub_btn_1)
        self.food_sub_btn_1.setObjectName(u"food_sub_btn_1")
        self.food_sub_btn_1.setIconSize(QSize(25, 25))
        self.food_sub_btn_1.setCheckable(True)
        self.food_sub_btn_1.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.food_sub_btn_1)

        self.food_sub_btn_2 = QPushButton(self.food_sub)
        self.food_group.addButton(self.food_sub_btn_2)
        self.food_sub_btn_2.setObjectName(u"food_sub_btn_2")
        self.food_sub_btn_2.setIconSize(QSize(25, 25))
        self.food_sub_btn_2.setCheckable(True)
        self.food_sub_btn_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.food_sub_btn_2)

        self.food_sub_btn_3 = QPushButton(self.food_sub)
        self.food_group.addButton(self.food_sub_btn_3)
        self.food_sub_btn_3.setObjectName(u"food_sub_btn_3")
        self.food_sub_btn_3.setIconSize(QSize(25, 25))
        self.food_sub_btn_3.setCheckable(True)
        self.food_sub_btn_3.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.food_sub_btn_3)


        self.verticalLayout_5.addWidget(self.food_sub)

        self.lab_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.lab_btn)
        self.lab_btn.setObjectName(u"lab_btn")
        icon5 = QIcon()
        icon5.addFile(u"icon/sidebar/lab.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lab_btn.setIcon(icon5)
        self.lab_btn.setIconSize(QSize(25, 25))
        self.lab_btn.setCheckable(True)
        self.lab_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.lab_btn)

        self.lab_sub = QWidget(sidebar)
        self.lab_sub.setObjectName(u"lab_sub")
        self.verticalLayout_3 = QVBoxLayout(self.lab_sub)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lab_sub_btn_1 = QPushButton(self.lab_sub)
        self.lab_group = QButtonGroup(sidebar)
        self.lab_group.setObjectName(u"lab_group")
        self.lab_group.addButton(self.lab_sub_btn_1)
        self.lab_sub_btn_1.setObjectName(u"lab_sub_btn_1")
        self.lab_sub_btn_1.setIconSize(QSize(25, 25))
        self.lab_sub_btn_1.setCheckable(True)
        self.lab_sub_btn_1.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.lab_sub_btn_1)

        self.lab_sub_btn_2 = QPushButton(self.lab_sub)
        self.lab_group.addButton(self.lab_sub_btn_2)
        self.lab_sub_btn_2.setObjectName(u"lab_sub_btn_2")
        self.lab_sub_btn_2.setIconSize(QSize(25, 25))
        self.lab_sub_btn_2.setCheckable(True)
        self.lab_sub_btn_2.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.lab_sub_btn_2)

        self.lab_sub_btn_3 = QPushButton(self.lab_sub)
        self.lab_group.addButton(self.lab_sub_btn_3)
        self.lab_sub_btn_3.setObjectName(u"lab_sub_btn_3")
        self.lab_sub_btn_3.setIconSize(QSize(25, 25))
        self.lab_sub_btn_3.setCheckable(True)
        self.lab_sub_btn_3.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.lab_sub_btn_3)


        self.verticalLayout_5.addWidget(self.lab_sub)

        self.verticalSpacer = QSpacerItem(20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.account_group = QGroupBox(sidebar)
        self.account_group.setObjectName(u"account_group")
        self.horizontalLayout_2 = QHBoxLayout(self.account_group)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.account_list = QComboBox(self.account_group)
        self.account_list.setObjectName(u"account_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_list.sizePolicy().hasHeightForWidth())
        self.account_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.account_list)

        self.account_setting_btn = QPushButton(self.account_group)
        self.account_setting_btn.setObjectName(u"account_setting_btn")

        self.horizontalLayout_2.addWidget(self.account_setting_btn)


        self.verticalLayout_5.addWidget(self.account_group)

        self.setting_btn = QPushButton(sidebar)
        self.setting_btn.setObjectName(u"setting_btn")
        icon6 = QIcon()
        icon6.addFile(u"icon/sidebar/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon6)
        self.setting_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.setting_btn)


        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.sidebar_name_label.setText(QCoreApplication.translate("sidebar", u"Trickcal Manager", None))
        self.home_btn.setText(QCoreApplication.translate("sidebar", u"\ub0b4\uc2e4 \uc694\uc57d", None))
        self.hero_btn.setText(QCoreApplication.translate("sidebar", u"\uc0ac\ub3c4", None))
        self.equip_btn.setText(QCoreApplication.translate("sidebar", u"\ub7ad\ud06c\uc791", None))
        self.equip_sub_btn_1.setText(QCoreApplication.translate("sidebar", u"\ub7ad\ud06c\uc791 \ud604\ud669 \ubc0f \ubaa9\ud45c \uc124\uc815", None))
        self.equip_sub_btn_2.setText(QCoreApplication.translate("sidebar", u"\ubcf4\uc720 \uc7a5\ube44 \uc7ac\ub8cc", None))
        self.equip_sub_btn_3.setText(QCoreApplication.translate("sidebar", u"\ud30c\ubc0d \ub3d9\uc120 \uacc4\uc0b0", None))
        self.crayon_btn.setText(QCoreApplication.translate("sidebar", u"\ubcf4\ub4dc", None))
        self.crayon_sub_btn_1.setText(QCoreApplication.translate("sidebar", u"\ubcf4\ub4dc\uc791 \ud604\ud669", None))
        self.crayon_sub_btn_2.setText(QCoreApplication.translate("sidebar", u"\ud669\ud06c\uce78 \ucc0d\ub294 \ube44\uc6a9 \uacc4\uc0b0", None))
        self.food_btn.setText(QCoreApplication.translate("sidebar", u"\ud638\uac10\ub3c4", None))
        self.food_sub_btn_1.setText(QCoreApplication.translate("sidebar", u"\uce5c\ubc00 \ub808\ubca8 \ud604\ud669 \ubc0f \ubaa9\ud45c \uc124\uc815", None))
        self.food_sub_btn_2.setText(QCoreApplication.translate("sidebar", u"\ubcf4\uc720 \uc74c\uc2dd \ubc0f \uc7ac\ub8cc", None))
        self.food_sub_btn_3.setText(QCoreApplication.translate("sidebar", u"\ud30c\ubc0d \ub3d9\uc120 \ubc0f \uc74c\uc2dd \uc81c\uc791 \uacc4\uc0b0", None))
        self.lab_btn.setText(QCoreApplication.translate("sidebar", u"\uc5f0\uad6c", None))
        self.lab_sub_btn_1.setText(QCoreApplication.translate("sidebar", u"\uc5f0\uad6c \ud604\ud669 \ubc0f \ubaa9\ud45c \uc124\uc815", None))
        self.lab_sub_btn_2.setText(QCoreApplication.translate("sidebar", u"\ubcf4\uc720 \uc5f0\uad6c \uc7ac\ub8cc", None))
        self.lab_sub_btn_3.setText(QCoreApplication.translate("sidebar", u"\ud30c\ubc0d \ub3d9\uc120 \uacc4\uc0b0", None))
        self.account_group.setTitle(QCoreApplication.translate("sidebar", u"\uacc4\uc815", None))
        self.account_setting_btn.setText(QCoreApplication.translate("sidebar", u"\uacc4\uc815 \uad00\ub9ac", None))
        self.setting_btn.setText(QCoreApplication.translate("sidebar", u"\uc124\uc815", None))
    # retranslateUi

