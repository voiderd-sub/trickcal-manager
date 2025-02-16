# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_equip_3.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_page_equip_3(object):
    def setupUi(self, page_equip_3):
        if not page_equip_3.objectName():
            page_equip_3.setObjectName(u"page_equip_3")
        page_equip_3.resize(800, 600)
        self.verticalLayout_9 = QVBoxLayout(page_equip_3)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(page_equip_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.container = QWidget(page_equip_3)
        self.container.setObjectName(u"container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.container)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.goal_list = QComboBox(self.container)
        self.goal_list.setObjectName(u"goal_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.goal_list.sizePolicy().hasHeightForWidth())
        self.goal_list.setSizePolicy(sizePolicy2)
        self.goal_list.setFont(font1)

        self.horizontalLayout.addWidget(self.goal_list)


        self.verticalLayout_9.addWidget(self.container)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.container_3 = QWidget(page_equip_3)
        self.container_3.setObjectName(u"container_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.container_3.sizePolicy().hasHeightForWidth())
        self.container_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_9 = QHBoxLayout(self.container_3)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.groupBox = QGroupBox(self.container_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.container_7 = QWidget(self.groupBox)
        self.container_7.setObjectName(u"container_7")
        sizePolicy1.setHeightForWidth(self.container_7.sizePolicy().hasHeightForWidth())
        self.container_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.container_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.container_7)
        self.label_15.setObjectName(u"label_15")
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(13)
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_15)

        self.label_3 = QLabel(self.container_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.container_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.container_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_6.addWidget(self.container_7)

        self.container_18 = QWidget(self.groupBox)
        self.container_18.setObjectName(u"container_18")
        sizePolicy1.setHeightForWidth(self.container_18.sizePolicy().hasHeightForWidth())
        self.container_18.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.container_18)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.container_19 = QWidget(self.container_18)
        self.container_19.setObjectName(u"container_19")
        self.horizontalLayout_14 = QHBoxLayout(self.container_19)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.daily_candy_yes = QRadioButton(self.container_19)
        self.daily_candy_yes.setObjectName(u"daily_candy_yes")
        self.daily_candy_yes.setFont(font2)
        self.daily_candy_yes.setChecked(True)

        self.horizontalLayout_14.addWidget(self.daily_candy_yes)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.daily_candy_no = QRadioButton(self.container_19)
        self.daily_candy_no.setObjectName(u"daily_candy_no")
        self.daily_candy_no.setFont(font2)

        self.horizontalLayout_14.addWidget(self.daily_candy_no)


        self.verticalLayout_4.addWidget(self.container_19)

        self.container_11 = QWidget(self.container_18)
        self.container_11.setObjectName(u"container_11")
        self.horizontalLayout_2 = QHBoxLayout(self.container_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hallow_13_yes = QRadioButton(self.container_11)
        self.hallow_13_yes.setObjectName(u"hallow_13_yes")
        self.hallow_13_yes.setFont(font2)
        self.hallow_13_yes.setChecked(True)

        self.horizontalLayout_2.addWidget(self.hallow_13_yes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.hallow_13_no = QRadioButton(self.container_11)
        self.hallow_13_no.setObjectName(u"hallow_13_no")
        self.hallow_13_no.setFont(font2)

        self.horizontalLayout_2.addWidget(self.hallow_13_no)


        self.verticalLayout_4.addWidget(self.container_11)

        self.container_13 = QWidget(self.container_18)
        self.container_13.setObjectName(u"container_13")
        self.gridLayout = QGridLayout(self.container_13)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.research_level = QLineEdit(self.container_13)
        self.research_level.setObjectName(u"research_level")
        self.research_level.setFont(font2)

        self.gridLayout.addWidget(self.research_level, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.container_13)

        self.container_12 = QWidget(self.container_18)
        self.container_12.setObjectName(u"container_12")
        self.gridLayout_2 = QGridLayout(self.container_12)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.candy_buying = QLineEdit(self.container_12)
        self.candy_buying.setObjectName(u"candy_buying")
        self.candy_buying.setFont(font2)

        self.gridLayout_2.addWidget(self.candy_buying, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.container_12)


        self.horizontalLayout_6.addWidget(self.container_18)


        self.horizontalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.container_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.container_4 = QWidget(self.groupBox_2)
        self.container_4.setObjectName(u"container_4")
        sizePolicy1.setHeightForWidth(self.container_4.sizePolicy().hasHeightForWidth())
        self.container_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.container_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.container_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_6 = QLabel(self.container_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.container_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.container_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_12.addWidget(self.container_4)

        self.container_5 = QWidget(self.groupBox_2)
        self.container_5.setObjectName(u"container_5")
        sizePolicy1.setHeightForWidth(self.container_5.sizePolicy().hasHeightForWidth())
        self.container_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.container_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.container_16 = QWidget(self.container_5)
        self.container_16.setObjectName(u"container_16")
        self.horizontalLayout_4 = QHBoxLayout(self.container_16)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.use_standard_yes = QRadioButton(self.container_16)
        self.use_standard_yes.setObjectName(u"use_standard_yes")
        self.use_standard_yes.setFont(font2)
        self.use_standard_yes.setChecked(True)

        self.horizontalLayout_4.addWidget(self.use_standard_yes)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.use_standard_no = QRadioButton(self.container_16)
        self.use_standard_no.setObjectName(u"use_standard_no")
        self.use_standard_no.setFont(font2)

        self.horizontalLayout_4.addWidget(self.use_standard_no)


        self.verticalLayout_6.addWidget(self.container_16)

        self.container_17 = QWidget(self.container_5)
        self.container_17.setObjectName(u"container_17")
        self.horizontalLayout_5 = QHBoxLayout(self.container_17)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.daily_elleaf_yes = QRadioButton(self.container_17)
        self.daily_elleaf_yes.setObjectName(u"daily_elleaf_yes")
        self.daily_elleaf_yes.setFont(font2)
        self.daily_elleaf_yes.setChecked(True)

        self.horizontalLayout_5.addWidget(self.daily_elleaf_yes)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.daily_elleaf_no = QRadioButton(self.container_17)
        self.daily_elleaf_no.setObjectName(u"daily_elleaf_no")
        self.daily_elleaf_no.setFont(font2)

        self.horizontalLayout_5.addWidget(self.daily_elleaf_no)


        self.verticalLayout_6.addWidget(self.container_17)

        self.container_14 = QWidget(self.container_5)
        self.container_14.setObjectName(u"container_14")
        self.gridLayout_6 = QGridLayout(self.container_14)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lecture_level = QLineEdit(self.container_14)
        self.lecture_level.setObjectName(u"lecture_level")
        self.lecture_level.setFont(font2)

        self.gridLayout_6.addWidget(self.lecture_level, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.container_14)

        self.container_15 = QWidget(self.container_5)
        self.container_15.setObjectName(u"container_15")
        self.gridLayout_5 = QGridLayout(self.container_15)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cur_standard = QLineEdit(self.container_15)
        self.cur_standard.setObjectName(u"cur_standard")
        self.cur_standard.setFont(font2)

        self.gridLayout_5.addWidget(self.cur_standard, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.container_15)


        self.horizontalLayout_12.addWidget(self.container_5)


        self.horizontalLayout_9.addWidget(self.groupBox_2)


        self.verticalLayout_9.addWidget(self.container_3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.groupBox_4 = QGroupBox(page_equip_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy4)
        self.groupBox_4.setFont(font1)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.container_6 = QWidget(self.groupBox_4)
        self.container_6.setObjectName(u"container_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.container_6.sizePolicy().hasHeightForWidth())
        self.container_6.setSizePolicy(sizePolicy5)
        self.verticalLayout = QVBoxLayout(self.container_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.container_6)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.container_6)
        self.label_14.setObjectName(u"label_14")
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)


        self.horizontalLayout_7.addWidget(self.container_6)

        self.container_8 = QWidget(self.groupBox_4)
        self.container_8.setObjectName(u"container_8")
        sizePolicy5.setHeightForWidth(self.container_8.sizePolicy().hasHeightForWidth())
        self.container_8.setSizePolicy(sizePolicy5)
        self.verticalLayout_2 = QVBoxLayout(self.container_8)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container_9 = QWidget(self.container_8)
        self.container_9.setObjectName(u"container_9")
        sizePolicy5.setHeightForWidth(self.container_9.sizePolicy().hasHeightForWidth())
        self.container_9.setSizePolicy(sizePolicy5)
        self.horizontalLayout_13 = QHBoxLayout(self.container_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.auto_update_yes = QRadioButton(self.container_9)
        self.auto_update_yes.setObjectName(u"auto_update_yes")
        self.auto_update_yes.setFont(font2)
        self.auto_update_yes.setChecked(True)

        self.horizontalLayout_13.addWidget(self.auto_update_yes)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.auto_update_no = QRadioButton(self.container_9)
        self.auto_update_no.setObjectName(u"auto_update_no")
        self.auto_update_no.setFont(font2)

        self.horizontalLayout_13.addWidget(self.auto_update_no)


        self.verticalLayout_2.addWidget(self.container_9)

        self.widget = QWidget(self.container_8)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.update_btn = QPushButton(self.widget)
        self.update_btn.setObjectName(u"update_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy6)
        self.update_btn.setMinimumSize(QSize(120, 0))
        self.update_btn.setFont(font2)

        self.gridLayout_3.addWidget(self.update_btn, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout_7.addWidget(self.container_8)

        self.container_20 = QWidget(self.groupBox_4)
        self.container_20.setObjectName(u"container_20")
        sizePolicy5.setHeightForWidth(self.container_20.sizePolicy().hasHeightForWidth())
        self.container_20.setSizePolicy(sizePolicy5)
        self.verticalLayout_7 = QVBoxLayout(self.container_20)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.container_20)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.container_20)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_17)


        self.horizontalLayout_7.addWidget(self.container_20)

        self.container_21 = QWidget(self.groupBox_4)
        self.container_21.setObjectName(u"container_21")
        sizePolicy5.setHeightForWidth(self.container_21.sizePolicy().hasHeightForWidth())
        self.container_21.setSizePolicy(sizePolicy5)
        self.verticalLayout_8 = QVBoxLayout(self.container_21)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.container_21)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.container_10 = QWidget(self.widget_2)
        self.container_10.setObjectName(u"container_10")
        sizePolicy5.setHeightForWidth(self.container_10.sizePolicy().hasHeightForWidth())
        self.container_10.setSizePolicy(sizePolicy5)
        self.horizontalLayout_8 = QHBoxLayout(self.container_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.round_yes = QRadioButton(self.container_10)
        self.round_yes.setObjectName(u"round_yes")
        self.round_yes.setFont(font2)
        self.round_yes.setChecked(True)

        self.horizontalLayout_8.addWidget(self.round_yes)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.round_no = QRadioButton(self.container_10)
        self.round_no.setObjectName(u"round_no")
        self.round_no.setFont(font2)

        self.horizontalLayout_8.addWidget(self.round_no)


        self.gridLayout_4.addWidget(self.container_10, 0, 0, 1, 1)

        self.container_22 = QWidget(self.widget_2)
        self.container_22.setObjectName(u"container_22")
        sizePolicy5.setHeightForWidth(self.container_22.sizePolicy().hasHeightForWidth())
        self.container_22.setSizePolicy(sizePolicy5)
        self.horizontalLayout_10 = QHBoxLayout(self.container_22)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.use_equip_yes = QRadioButton(self.container_22)
        self.use_equip_yes.setObjectName(u"use_equip_yes")
        self.use_equip_yes.setFont(font2)
        self.use_equip_yes.setChecked(True)

        self.horizontalLayout_10.addWidget(self.use_equip_yes)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.use_equip_no = QRadioButton(self.container_22)
        self.use_equip_no.setObjectName(u"use_equip_no")
        self.use_equip_no.setFont(font2)

        self.horizontalLayout_10.addWidget(self.use_equip_no)


        self.gridLayout_4.addWidget(self.container_22, 1, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_2)


        self.horizontalLayout_7.addWidget(self.container_21)


        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.calc_btn = QPushButton(page_equip_3)
        self.calc_btn.setObjectName(u"calc_btn")
        sizePolicy6.setHeightForWidth(self.calc_btn.sizePolicy().hasHeightForWidth())
        self.calc_btn.setSizePolicy(sizePolicy6)
        self.calc_btn.setMinimumSize(QSize(150, 0))
        self.calc_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.calc_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)


        self.retranslateUi(page_equip_3)

        QMetaObject.connectSlotsByName(page_equip_3)
    # setupUi

    def retranslateUi(self, page_equip_3):
        page_equip_3.setWindowTitle(QCoreApplication.translate("page_equip_3", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_equip_3", u"\uacc4\uc0b0 \uc124\uc815", None))
        self.label_10.setText(QCoreApplication.translate("page_equip_3", u"\uacc4\uc0b0 \ubaa9\ud45c ", None))
        self.groupBox.setTitle(QCoreApplication.translate("page_equip_3", u"\uc655\uc0ac\ud0d5", None))
        self.label_15.setText(QCoreApplication.translate("page_equip_3", u"\ub370\uc77c\ub9ac \uc655\uc0ac\ud0d5 \uad6c\ub9e4\ud588\uc5b4\uc694?", None))
        self.label_3.setText(QCoreApplication.translate("page_equip_3", u"\uc131\ubb3c \ub808\ubca8 13 \uc774\uc0c1\uc778\uac00\uc694?", None))
        self.label_4.setText(QCoreApplication.translate("page_equip_3", u"\uacf5\ubb3c 10% \uc99d\uac00 \uc5f0\uad6c\ub294 \uba87 \uac1c?", None))
        self.label_5.setText(QCoreApplication.translate("page_equip_3", u"\ub9e4\uc77c \uc655\uc0ac\ud0d5 \uba87 \ubc88 \ucda9\uc804\ud558\ub098\uc694?", None))
        self.daily_candy_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.daily_candy_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.hallow_13_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.hallow_13_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.research_level.setPlaceholderText(QCoreApplication.translate("page_equip_3", u"0 ~ 10", None))
        self.candy_buying.setPlaceholderText(QCoreApplication.translate("page_equip_3", u"0 ~ 10", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("page_equip_3", u"\uc815\uc11d", None))
        self.label_9.setText(QCoreApplication.translate("page_equip_3", u"\uc815\uc11d \uc0ac\uc6a9\ud560\uae4c\uc694?", None))
        self.label_6.setText(QCoreApplication.translate("page_equip_3", u"\uc6d4\uc815\uc561 \uad6c\ub9e4\ud588\uc5b4\uc694?", None))
        self.label_7.setText(QCoreApplication.translate("page_equip_3", u"\ub2e8\uc18d\ubc18 \uba87 \uac15\uae4c\uc9c0 \uae7c\uc5b4\uc694?", None))
        self.label_8.setText(QCoreApplication.translate("page_equip_3", u"\ubcf4\uc720 \uc815\uc11d\uc740 \uba87 \uac1c?", None))
        self.use_standard_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.use_standard_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.daily_elleaf_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.daily_elleaf_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.lecture_level.setPlaceholderText(QCoreApplication.translate("page_equip_3", u"0 ~ 30", None))
        self.cur_standard.setPlaceholderText(QCoreApplication.translate("page_equip_3", u"0 ~ 999,999", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("page_equip_3", u"\uae30\ud0c0", None))
        self.label_13.setText(QCoreApplication.translate("page_equip_3", u"\ucd5c\uc2e0 \ub4dc\ub78d\ub960 \ub370\uc774\ud130\ub97c\n"
"\ub9e4\ubc88 \ubc1b\uc544\uc62c\uae4c\uc694?", None))
        self.label_14.setText(QCoreApplication.translate("page_equip_3", u"\ub4dc\ub78d\ub960 \uc218\ub3d9 \uc5c5\ub370\uc774\ud2b8", None))
        self.auto_update_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.auto_update_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.update_btn.setText(QCoreApplication.translate("page_equip_3", u"\uc5c5\ub370\uc774\ud2b8", None))
        self.label_16.setText(QCoreApplication.translate("page_equip_3", u"\ub4dc\ub78d\ub960 5% \ub2e8\uc704\ub85c \ubc18\uc62c\ub9bc\n"
"(\ucf1c\ub294 \uac78 \uad8c\uc7a5)", None))
        self.label_17.setText(QCoreApplication.translate("page_equip_3", u"\ubcf4\uc720 \uc644\uc81c\ud15c \uc0ac\uc6a9\ud560\uae4c\uc694?", None))
        self.round_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.round_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.use_equip_yes.setText(QCoreApplication.translate("page_equip_3", u"\uc751", None))
        self.use_equip_no.setText(QCoreApplication.translate("page_equip_3", u"\uc544\ub2c8", None))
        self.calc_btn.setText(QCoreApplication.translate("page_equip_3", u"\uacc4\uc0b0\ud558\uae30!", None))
    # retranslateUi

