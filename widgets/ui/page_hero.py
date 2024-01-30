# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_hero.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGridLayout,
    QHBoxLayout, QHeaderView, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_page_hero(object):
    def setupUi(self, page_hero):
        if not page_hero.objectName():
            page_hero.setObjectName(u"page_hero")
        page_hero.resize(500, 500)
        self.horizontalLayout = QHBoxLayout(page_hero)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hero_table_container = QWidget(page_hero)
        self.hero_table_container.setObjectName(u"hero_table_container")
        self.hero_table_container.setMinimumSize(QSize(300, 0))
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(12)
        self.hero_table_container.setFont(font)
        self.gridLayout = QGridLayout(self.hero_table_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hero_table = QTableWidget(self.hero_table_container)
        if (self.hero_table.columnCount() < 3):
            self.hero_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.hero_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hero_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hero_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.hero_table.setObjectName(u"hero_table")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hero_table.sizePolicy().hasHeightForWidth())
        self.hero_table.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font1.setPointSize(14)
        self.hero_table.setFont(font1)
        self.hero_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.hero_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hero_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.hero_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.hero_table.verticalHeader().setDefaultSectionSize(100)

        self.verticalLayout_2.addWidget(self.hero_table)

        self.update_btn = QPushButton(self.hero_table_container)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setFont(font)

        self.verticalLayout_2.addWidget(self.update_btn)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.hero_table_container)

        self.button_area = QWidget(page_hero)
        self.button_area.setObjectName(u"button_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_area.sizePolicy().hasHeightForWidth())
        self.button_area.setSizePolicy(sizePolicy1)
        self.button_area.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.button_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.star_1_btn = QPushButton(self.button_area)
        self.star_1_btn.setObjectName(u"star_1_btn")
        self.star_1_btn.setFont(font)

        self.verticalLayout.addWidget(self.star_1_btn)

        self.star_2_btn = QPushButton(self.button_area)
        self.star_2_btn.setObjectName(u"star_2_btn")
        self.star_2_btn.setFont(font)

        self.verticalLayout.addWidget(self.star_2_btn)

        self.all_check_btn = QPushButton(self.button_area)
        self.all_check_btn.setObjectName(u"all_check_btn")
        self.all_check_btn.setFont(font)

        self.verticalLayout.addWidget(self.all_check_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.all_uncheck_btn = QPushButton(self.button_area)
        self.all_uncheck_btn.setObjectName(u"all_uncheck_btn")
        self.all_uncheck_btn.setFont(font)

        self.verticalLayout.addWidget(self.all_uncheck_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 339, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save_btn = QPushButton(self.button_area)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font)

        self.verticalLayout_3.addWidget(self.save_btn)

        self.undo_btn = QPushButton(self.button_area)
        self.undo_btn.setObjectName(u"undo_btn")
        self.undo_btn.setFont(font)

        self.verticalLayout_3.addWidget(self.undo_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.button_area)


        self.retranslateUi(page_hero)

        QMetaObject.connectSlotsByName(page_hero)
    # setupUi

    def retranslateUi(self, page_hero):
        page_hero.setWindowTitle(QCoreApplication.translate("page_hero", u"Form", None))
        ___qtablewidgetitem = self.hero_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("page_hero", u"\uc774\ubbf8\uc9c0", None));
        ___qtablewidgetitem1 = self.hero_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("page_hero", u"\uc774\ub984", None));
        ___qtablewidgetitem2 = self.hero_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("page_hero", u"\ud604\uc7ac \ub4f1\uae09", None));
        self.update_btn.setText(QCoreApplication.translate("page_hero", u"\uc0ac\ub3c4 \ub370\uc774\ud130 \uc5c5\ub370\uc774\ud2b8", None))
        self.star_1_btn.setText(QCoreApplication.translate("page_hero", u"1\uc131 \uc804\ubd80 \ubcf4\uc720 \uc911", None))
        self.star_2_btn.setText(QCoreApplication.translate("page_hero", u"2\uc131 \uc804\ubd80 \ubcf4\uc720 \uc911", None))
        self.all_check_btn.setText(QCoreApplication.translate("page_hero", u"\uc804 \uc0ac\ub3c4 \ubcf4\uc720 \uc911", None))
        self.all_uncheck_btn.setText(QCoreApplication.translate("page_hero", u"\uc804\ubd80 \ubbf8\ubcf4\uc720", None))
        self.save_btn.setText(QCoreApplication.translate("page_hero", u"\uc800\uc7a5", None))
        self.undo_btn.setText(QCoreApplication.translate("page_hero", u"\ubcc0\uacbd\uc0ac\ud56d \ucde8\uc18c", None))
    # retranslateUi

