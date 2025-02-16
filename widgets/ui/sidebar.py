# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
import widgets.icon_resource_rc

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(280, 736)
        self.verticalLayout_5 = QVBoxLayout(sidebar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(13, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.sidebar_name_label = QLabel(sidebar)
        self.sidebar_name_label.setObjectName(u"sidebar_name_label")
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(18)
        self.sidebar_name_label.setFont(font)

        self.horizontalLayout.addWidget(self.sidebar_name_label)

        self.horizontalSpacer = QSpacerItem(13, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.home_btn = QPushButton(sidebar)
        self.main_menu_group = QButtonGroup(sidebar)
        self.main_menu_group.setObjectName(u"main_menu_group")
        self.main_menu_group.addButton(self.home_btn)
        self.home_btn.setObjectName(u"home_btn")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.home_btn.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icon/icon/sidebar/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(25, 25))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.home_btn)

        self.hero_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.hero_btn)
        self.hero_btn.setObjectName(u"hero_btn")
        self.hero_btn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/sidebar/hero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hero_btn.setIcon(icon1)
        self.hero_btn.setIconSize(QSize(25, 25))
        self.hero_btn.setCheckable(True)
        self.hero_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.hero_btn)

        self.equip_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.equip_btn)
        self.equip_btn.setObjectName(u"equip_btn")
        self.equip_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/sidebar/equip.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.equip_btn.setIcon(icon2)
        self.equip_btn.setIconSize(QSize(25, 25))
        self.equip_btn.setCheckable(True)
        self.equip_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.equip_btn)

        self.equip_sub = QWidget(sidebar)
        self.equip_sub.setObjectName(u"equip_sub")
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        self.equip_sub.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.equip_sub)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.equip_abstract_btn = QPushButton(self.equip_sub)
        self.equip_group = QButtonGroup(sidebar)
        self.equip_group.setObjectName(u"equip_group")
        self.equip_group.addButton(self.equip_abstract_btn)
        self.equip_abstract_btn.setObjectName(u"equip_abstract_btn")
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(12)
        self.equip_abstract_btn.setFont(font3)
        self.equip_abstract_btn.setIconSize(QSize(25, 25))
        self.equip_abstract_btn.setCheckable(True)
        self.equip_abstract_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_abstract_btn)

        self.equip_1_btn = QPushButton(self.equip_sub)
        self.equip_group.addButton(self.equip_1_btn)
        self.equip_1_btn.setObjectName(u"equip_1_btn")
        self.equip_1_btn.setFont(font3)
        self.equip_1_btn.setIconSize(QSize(25, 25))
        self.equip_1_btn.setCheckable(True)
        self.equip_1_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_1_btn)

        self.equip_2_btn = QPushButton(self.equip_sub)
        self.equip_group.addButton(self.equip_2_btn)
        self.equip_2_btn.setObjectName(u"equip_2_btn")
        self.equip_2_btn.setFont(font3)
        self.equip_2_btn.setIconSize(QSize(25, 25))
        self.equip_2_btn.setCheckable(True)
        self.equip_2_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_2_btn)

        self.equip_3_btn = QPushButton(self.equip_sub)
        self.equip_group.addButton(self.equip_3_btn)
        self.equip_3_btn.setObjectName(u"equip_3_btn")
        self.equip_3_btn.setFont(font3)
        self.equip_3_btn.setIconSize(QSize(25, 25))
        self.equip_3_btn.setCheckable(True)
        self.equip_3_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.equip_3_btn)


        self.verticalLayout_5.addWidget(self.equip_sub)

        self.crayon_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.crayon_btn)
        self.crayon_btn.setObjectName(u"crayon_btn")
        self.crayon_btn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/sidebar/crayon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.crayon_btn.setIcon(icon3)
        self.crayon_btn.setIconSize(QSize(25, 25))
        self.crayon_btn.setCheckable(True)
        self.crayon_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.crayon_btn)

        self.crayon_sub = QWidget(sidebar)
        self.crayon_sub.setObjectName(u"crayon_sub")
        self.crayon_sub.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.crayon_sub)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.crayon_abstract_btn = QPushButton(self.crayon_sub)
        self.crayon_group = QButtonGroup(sidebar)
        self.crayon_group.setObjectName(u"crayon_group")
        self.crayon_group.addButton(self.crayon_abstract_btn)
        self.crayon_abstract_btn.setObjectName(u"crayon_abstract_btn")
        self.crayon_abstract_btn.setFont(font3)
        self.crayon_abstract_btn.setIconSize(QSize(25, 25))
        self.crayon_abstract_btn.setCheckable(True)
        self.crayon_abstract_btn.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.crayon_abstract_btn)

        self.crayon_1_btn = QPushButton(self.crayon_sub)
        self.crayon_group.addButton(self.crayon_1_btn)
        self.crayon_1_btn.setObjectName(u"crayon_1_btn")
        self.crayon_1_btn.setFont(font3)
        self.crayon_1_btn.setIconSize(QSize(25, 25))
        self.crayon_1_btn.setCheckable(True)
        self.crayon_1_btn.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.crayon_1_btn)

        self.crayon_2_btn = QPushButton(self.crayon_sub)
        self.crayon_group.addButton(self.crayon_2_btn)
        self.crayon_2_btn.setObjectName(u"crayon_2_btn")
        self.crayon_2_btn.setFont(font3)
        self.crayon_2_btn.setIconSize(QSize(25, 25))
        self.crayon_2_btn.setCheckable(True)
        self.crayon_2_btn.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.crayon_2_btn)


        self.verticalLayout_5.addWidget(self.crayon_sub)

        self.dps_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.dps_btn)
        self.dps_btn.setObjectName(u"dps_btn")
        self.dps_btn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/sidebar/dps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dps_btn.setIcon(icon4)
        self.dps_btn.setIconSize(QSize(25, 25))
        self.dps_btn.setCheckable(True)
        self.dps_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.dps_btn)

        self.dps_sub = QWidget(sidebar)
        self.dps_sub.setObjectName(u"dps_sub")
        self.dps_sub.setFont(font2)
        self.verticalLayout_4 = QVBoxLayout(self.dps_sub)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.dps_1_btn = QPushButton(self.dps_sub)
        self.dps_group = QButtonGroup(sidebar)
        self.dps_group.setObjectName(u"dps_group")
        self.dps_group.addButton(self.dps_1_btn)
        self.dps_1_btn.setObjectName(u"dps_1_btn")
        self.dps_1_btn.setFont(font3)
        self.dps_1_btn.setIconSize(QSize(25, 25))
        self.dps_1_btn.setCheckable(True)
        self.dps_1_btn.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.dps_1_btn)

        self.dps_2_btn = QPushButton(self.dps_sub)
        self.dps_group.addButton(self.dps_2_btn)
        self.dps_2_btn.setObjectName(u"dps_2_btn")
        self.dps_2_btn.setFont(font3)
        self.dps_2_btn.setIconSize(QSize(25, 25))
        self.dps_2_btn.setCheckable(True)
        self.dps_2_btn.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.dps_2_btn)


        self.verticalLayout_5.addWidget(self.dps_sub)

        self.cash_btn = QPushButton(sidebar)
        self.main_menu_group.addButton(self.cash_btn)
        self.cash_btn.setObjectName(u"cash_btn")
        self.cash_btn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/sidebar/cash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cash_btn.setIcon(icon5)
        self.cash_btn.setIconSize(QSize(25, 25))
        self.cash_btn.setCheckable(True)
        self.cash_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.cash_btn)

        self.cash_sub = QWidget(sidebar)
        self.cash_sub.setObjectName(u"cash_sub")
        self.cash_sub.setFont(font2)
        self.verticalLayout_3 = QVBoxLayout(self.cash_sub)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cash_1_btn = QPushButton(self.cash_sub)
        self.cash_group = QButtonGroup(sidebar)
        self.cash_group.setObjectName(u"cash_group")
        self.cash_group.addButton(self.cash_1_btn)
        self.cash_1_btn.setObjectName(u"cash_1_btn")
        self.cash_1_btn.setFont(font3)
        self.cash_1_btn.setIconSize(QSize(25, 25))
        self.cash_1_btn.setCheckable(True)
        self.cash_1_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.cash_1_btn)

        self.cash_2_btn = QPushButton(self.cash_sub)
        self.cash_group.addButton(self.cash_2_btn)
        self.cash_2_btn.setObjectName(u"cash_2_btn")
        self.cash_2_btn.setFont(font3)
        self.cash_2_btn.setIconSize(QSize(25, 25))
        self.cash_2_btn.setCheckable(True)
        self.cash_2_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.cash_2_btn)

        self.cash_3_btn = QPushButton(self.cash_sub)
        self.cash_group.addButton(self.cash_3_btn)
        self.cash_3_btn.setObjectName(u"cash_3_btn")
        self.cash_3_btn.setFont(font3)
        self.cash_3_btn.setIconSize(QSize(25, 25))
        self.cash_3_btn.setCheckable(True)
        self.cash_3_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.cash_3_btn)


        self.verticalLayout_5.addWidget(self.cash_sub)

        self.verticalSpacer = QSpacerItem(20, 177, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.account_group = QGroupBox(sidebar)
        self.account_group.setObjectName(u"account_group")
        self.account_group.setFont(font3)
        self.horizontalLayout_2 = QHBoxLayout(self.account_group)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.account_list = QComboBox(self.account_group)
        self.account_list.setObjectName(u"account_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_list.sizePolicy().hasHeightForWidth())
        self.account_list.setSizePolicy(sizePolicy)
        self.account_list.setFont(font3)

        self.horizontalLayout_2.addWidget(self.account_list)

        self.account_setting_btn = QPushButton(self.account_group)
        self.account_setting_btn.setObjectName(u"account_setting_btn")
        self.account_setting_btn.setFont(font3)

        self.horizontalLayout_2.addWidget(self.account_setting_btn)


        self.verticalLayout_5.addWidget(self.account_group)

        self.setting_btn = QPushButton(sidebar)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"icon/sidebar/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_btn.setIcon(icon6)
        self.setting_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.setting_btn)


        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.sidebar_name_label.setText(QCoreApplication.translate("sidebar", u"Trickcal Manager", None))
        self.home_btn.setText(QCoreApplication.translate("sidebar", u"\ub0b4\uc2e4 \uc694\uc57d (\uc900\ube44\uc911)", None))
        self.hero_btn.setText(QCoreApplication.translate("sidebar", u"\uc0ac\ub3c4", None))
        self.equip_btn.setText(QCoreApplication.translate("sidebar", u"\ub7ad\ud06c\uc791", None))
        self.equip_abstract_btn.setText(QCoreApplication.translate("sidebar", u"\ub7ad\ud06c\uc791 \ud604\ud669 \ud55c \ub208\uc5d0 \ubcf4\uae30", None))
        self.equip_1_btn.setText(QCoreApplication.translate("sidebar", u"\ucc29\uc6a9 \uc7a5\ube44 \ubc0f \ubaa9\ud45c \uc124\uc815", None))
        self.equip_2_btn.setText(QCoreApplication.translate("sidebar", u"\ubcf4\uc720 \uc7a5\ube44 \uc7ac\ub8cc", None))
        self.equip_3_btn.setText(QCoreApplication.translate("sidebar", u"\ud30c\ubc0d \ub3d9\uc120 \uacc4\uc0b0", None))
        self.crayon_btn.setText(QCoreApplication.translate("sidebar", u"\ubcf4\ub4dc", None))
        self.crayon_abstract_btn.setText(QCoreApplication.translate("sidebar", u"\uc804\uccb4 \ubcf4\ub4dc \ud604\ud669", None))
        self.crayon_1_btn.setText(QCoreApplication.translate("sidebar", u"\ubcf4\ub4dc\uc791 \ud604\ud669 \uae30\ub85d", None))
        self.crayon_2_btn.setText(QCoreApplication.translate("sidebar", u"\ucd5c\uc18c \ube44\uc6a9 \ubcf4\ub4dc\ud310", None))
        self.dps_btn.setText(QCoreApplication.translate("sidebar", u"DPS \uacc4\uc0b0\uae30", None))
        self.dps_1_btn.setText(QCoreApplication.translate("sidebar", u"\ub371 \ubc0f \uacc4\uc0b0 \uc124\uc815 (\uce74\ub4dc\ub819 \uae30\ub85d\ub3c4 \uc5ec\uae30\uc11c)", None))
        self.dps_2_btn.setText(QCoreApplication.translate("sidebar", u"\uc2e4\uc81c \uacc4\uc0b0\ud558\uae30? (\uba54\ub274 \ub098\ub220\uc57c\ud568?)", None))
        self.cash_btn.setText(QCoreApplication.translate("sidebar", u"\uacfc\uae08 \ud6a8\uc728 \uacc4\uc0b0\uae30", None))
        self.cash_1_btn.setText(QCoreApplication.translate("sidebar", u"\uae30\ubcf8 \uc124\uc815", None))
        self.cash_2_btn.setText(QCoreApplication.translate("sidebar", u"\uacc4\uc0b0\ud558\uae30", None))
        self.cash_3_btn.setText(QCoreApplication.translate("sidebar", u"\uc774 \ubc84\ud2bc \uc0ad\uc81c\ud560\uae4c?", None))
        self.account_group.setTitle(QCoreApplication.translate("sidebar", u"\uacc4\uc815", None))
        self.account_setting_btn.setText(QCoreApplication.translate("sidebar", u"\uacc4\uc815 \uad00\ub9ac", None))
        self.setting_btn.setText(QCoreApplication.translate("sidebar", u"\uc124\uc815", None))
    # retranslateUi

