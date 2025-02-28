# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dps_hero_cell.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from widgets.wrapper.misc import ExtendedComboBox

class Ui_DpsHeroCell(object):
    def setupUi(self, DpsHeroCell):
        if not DpsHeroCell.objectName():
            DpsHeroCell.setObjectName(u"DpsHeroCell")
        DpsHeroCell.resize(278, 113)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(15)
        DpsHeroCell.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(DpsHeroCell)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(DpsHeroCell)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cell_empty = QWidget()
        self.cell_empty.setObjectName(u"cell_empty")
        self.horizontalLayout = QHBoxLayout(self.cell_empty)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hero_select = ExtendedComboBox(self.cell_empty)
        self.hero_select.setObjectName(u"hero_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hero_select.sizePolicy().hasHeightForWidth())
        self.hero_select.setSizePolicy(sizePolicy1)
        self.hero_select.setMinimumSize(QSize(0, 40))
        self.hero_select.setFont(font)

        self.horizontalLayout.addWidget(self.hero_select)

        self.add_button = QPushButton(self.cell_empty)
        self.add_button.setObjectName(u"add_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy2)
        self.add_button.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(20)
        self.add_button.setFont(font1)

        self.horizontalLayout.addWidget(self.add_button)

        self.stackedWidget.addWidget(self.cell_empty)
        self.cell_occupied = QWidget()
        self.cell_occupied.setObjectName(u"cell_occupied")
        self.verticalLayout = QVBoxLayout(self.cell_occupied)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.widget_2 = QWidget(self.cell_occupied)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.hero_name = QLabel(self.widget_2)
        self.hero_name.setObjectName(u"hero_name")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hero_name.sizePolicy().hasHeightForWidth())
        self.hero_name.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(14)
        self.hero_name.setFont(font2)
        self.hero_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hero_name.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.hero_name)

        self.horizontalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.setting_button = QPushButton(self.widget_2)
        self.setting_button.setObjectName(u"setting_button")
        sizePolicy.setHeightForWidth(self.setting_button.sizePolicy().hasHeightForWidth())
        self.setting_button.setSizePolicy(sizePolicy)
        self.setting_button.setMinimumSize(QSize(0, 0))
        self.setting_button.setMaximumSize(QSize(35, 35))
        self.setting_button.setFont(font)

        self.horizontalLayout_4.addWidget(self.setting_button)

        self.delete_button = QPushButton(self.widget_2)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QSize(0, 0))
        self.delete_button.setMaximumSize(QSize(35, 35))
        self.delete_button.setFont(font)

        self.horizontalLayout_4.addWidget(self.delete_button)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.cell_occupied)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hero_icon = QLabel(self.widget_3)
        self.hero_icon.setObjectName(u"hero_icon")
        sizePolicy2.setHeightForWidth(self.hero_icon.sizePolicy().hasHeightForWidth())
        self.hero_icon.setSizePolicy(sizePolicy2)
        self.hero_icon.setMinimumSize(QSize(75, 75))
        self.hero_icon.setMaximumSize(QSize(75, 75))
        self.hero_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.hero_icon)

        self.equip1 = QLabel(self.widget_3)
        self.equip1.setObjectName(u"equip1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.equip1.sizePolicy().hasHeightForWidth())
        self.equip1.setSizePolicy(sizePolicy5)
        self.equip1.setMinimumSize(QSize(0, 0))
        self.equip1.setMaximumSize(QSize(70, 70))
        self.equip1.setAutoFillBackground(False)
        self.equip1.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.equip1)

        self.equip2 = QLabel(self.widget_3)
        self.equip2.setObjectName(u"equip2")
        sizePolicy5.setHeightForWidth(self.equip2.sizePolicy().hasHeightForWidth())
        self.equip2.setSizePolicy(sizePolicy5)
        self.equip2.setMinimumSize(QSize(0, 0))
        self.equip2.setMaximumSize(QSize(70, 70))
        self.equip2.setAutoFillBackground(False)
        self.equip2.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.equip2)

        self.equip3 = QLabel(self.widget_3)
        self.equip3.setObjectName(u"equip3")
        sizePolicy5.setHeightForWidth(self.equip3.sizePolicy().hasHeightForWidth())
        self.equip3.setSizePolicy(sizePolicy5)
        self.equip3.setMinimumSize(QSize(0, 0))
        self.equip3.setMaximumSize(QSize(70, 70))
        self.equip3.setAutoFillBackground(False)
        self.equip3.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.equip3)


        self.verticalLayout.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.cell_occupied)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(DpsHeroCell)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DpsHeroCell)
    # setupUi

    def retranslateUi(self, DpsHeroCell):
        DpsHeroCell.setWindowTitle(QCoreApplication.translate("DpsHeroCell", u"Form", None))
        self.groupBox.setTitle("")
        self.add_button.setText(QCoreApplication.translate("DpsHeroCell", u"+", None))
        self.hero_name.setText(QCoreApplication.translate("DpsHeroCell", u"name", None))
        self.setting_button.setText(QCoreApplication.translate("DpsHeroCell", u"?", None))
        self.delete_button.setText(QCoreApplication.translate("DpsHeroCell", u"x", None))
        self.hero_icon.setText(QCoreApplication.translate("DpsHeroCell", u"icon", None))
        self.equip1.setText("")
        self.equip2.setText("")
        self.equip3.setText("")
    # retranslateUi

