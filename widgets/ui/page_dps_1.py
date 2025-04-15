# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_dps_1.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

from widgets.wrapper.dps_hero_cell import DpsHeroCell

class Ui_page_dps_1(object):
    def setupUi(self, page_dps_1):
        if not page_dps_1.objectName():
            page_dps_1.setObjectName(u"page_dps_1")
        page_dps_1.resize(800, 600)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(15)
        page_dps_1.setFont(font)
        self.verticalLayout = QVBoxLayout(page_dps_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setting_area = QTabWidget(page_dps_1)
        self.setting_area.setObjectName(u"setting_area")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_area.sizePolicy().hasHeightForWidth())
        self.setting_area.setSizePolicy(sizePolicy)
        self.setting_area.setMinimumSize(QSize(0, 0))
        self.setting_area.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(18)
        self.setting_area.setFont(font1)
        self.deck = QWidget()
        self.deck.setObjectName(u"deck")
        self.gridLayout = QGridLayout(self.deck)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.HeroCellBack1 = DpsHeroCell(self.deck)
        self.HeroCellBack1.setObjectName(u"HeroCellBack1")

        self.gridLayout.addWidget(self.HeroCellBack1, 0, 0, 1, 1)

        self.HeroCellMid1 = DpsHeroCell(self.deck)
        self.HeroCellMid1.setObjectName(u"HeroCellMid1")

        self.gridLayout.addWidget(self.HeroCellMid1, 0, 1, 1, 1)

        self.HeroCellFront1 = DpsHeroCell(self.deck)
        self.HeroCellFront1.setObjectName(u"HeroCellFront1")

        self.gridLayout.addWidget(self.HeroCellFront1, 0, 2, 1, 1)

        self.HeroCellBack2 = DpsHeroCell(self.deck)
        self.HeroCellBack2.setObjectName(u"HeroCellBack2")

        self.gridLayout.addWidget(self.HeroCellBack2, 1, 0, 1, 1)

        self.HeroCellMid2 = DpsHeroCell(self.deck)
        self.HeroCellMid2.setObjectName(u"HeroCellMid2")

        self.gridLayout.addWidget(self.HeroCellMid2, 1, 1, 1, 1)

        self.HeroCellFront2 = DpsHeroCell(self.deck)
        self.HeroCellFront2.setObjectName(u"HeroCellFront2")

        self.gridLayout.addWidget(self.HeroCellFront2, 1, 2, 1, 1)

        self.HeroCellBack3 = DpsHeroCell(self.deck)
        self.HeroCellBack3.setObjectName(u"HeroCellBack3")

        self.gridLayout.addWidget(self.HeroCellBack3, 2, 0, 1, 1)

        self.HeroCellMid3 = DpsHeroCell(self.deck)
        self.HeroCellMid3.setObjectName(u"HeroCellMid3")

        self.gridLayout.addWidget(self.HeroCellMid3, 2, 1, 1, 1)

        self.HeroCellFront3 = DpsHeroCell(self.deck)
        self.HeroCellFront3.setObjectName(u"HeroCellFront3")

        self.gridLayout.addWidget(self.HeroCellFront3, 2, 2, 1, 1)

        self.setting_area.addTab(self.deck, "")
        self.card_level = QWidget()
        self.card_level.setObjectName(u"card_level")
        self.setting_area.addTab(self.card_level, "")
        self.spell_buying = QWidget()
        self.spell_buying.setObjectName(u"spell_buying")
        self.setting_area.addTab(self.spell_buying, "")
        self.calc_setting = QWidget()
        self.calc_setting.setObjectName(u"calc_setting")
        self.setting_area.addTab(self.calc_setting, "")

        self.verticalLayout.addWidget(self.setting_area)

        self.deck_area = QWidget(page_dps_1)
        self.deck_area.setObjectName(u"deck_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deck_area.sizePolicy().hasHeightForWidth())
        self.deck_area.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.deck_area)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.presetGroup = QGroupBox(self.deck_area)
        self.presetGroup.setObjectName(u"presetGroup")
        self.verticalLayout_2 = QVBoxLayout(self.presetGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.preset_save_btn = QPushButton(self.presetGroup)
        self.preset_save_btn.setObjectName(u"preset_save_btn")

        self.verticalLayout_2.addWidget(self.preset_save_btn)

        self.preset_load_btn = QPushButton(self.presetGroup)
        self.preset_load_btn.setObjectName(u"preset_load_btn")

        self.verticalLayout_2.addWidget(self.preset_load_btn)


        self.verticalLayout_3.addWidget(self.presetGroup)

        self.verticalSpacer = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.calculate_btn = QPushButton(self.deck_area)
        self.calculate_btn.setObjectName(u"calculate_btn")

        self.verticalLayout_3.addWidget(self.calculate_btn)


        self.verticalLayout.addWidget(self.deck_area)


        self.retranslateUi(page_dps_1)

        self.setting_area.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_dps_1)
    # setupUi

    def retranslateUi(self, page_dps_1):
        page_dps_1.setWindowTitle(QCoreApplication.translate("page_dps_1", u"Form", None))
        self.setting_area.setTabText(self.setting_area.indexOf(self.deck), QCoreApplication.translate("page_dps_1", u"\ub371", None))
        self.setting_area.setTabText(self.setting_area.indexOf(self.card_level), QCoreApplication.translate("page_dps_1", u"\uce74\ub4dc \ub808\ubca8", None))
        self.setting_area.setTabText(self.setting_area.indexOf(self.spell_buying), QCoreApplication.translate("page_dps_1", u"\uc2a4\ud3a0 \uad6c\ub9e4", None))
        self.setting_area.setTabText(self.setting_area.indexOf(self.calc_setting), QCoreApplication.translate("page_dps_1", u"\uacc4\uc0b0 \uc124\uc815", None))
        self.presetGroup.setTitle(QCoreApplication.translate("page_dps_1", u"\ud504\ub9ac\uc14b", None))
        self.preset_save_btn.setText(QCoreApplication.translate("page_dps_1", u"\uc800\uc7a5\ud558\uae30", None))
        self.preset_load_btn.setText(QCoreApplication.translate("page_dps_1", u"\ubd88\ub7ec\uc624\uae30", None))
        self.calculate_btn.setText(QCoreApplication.translate("page_dps_1", u"\uacc4\uc0b0\ud558\uae30!", None))
    # retranslateUi

