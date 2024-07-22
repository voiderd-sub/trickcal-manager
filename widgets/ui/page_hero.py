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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hero_table_container.sizePolicy().hasHeightForWidth())
        self.hero_table_container.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hero_table.sizePolicy().hasHeightForWidth())
        self.hero_table.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font1.setPointSize(15)
        self.hero_table.setFont(font1)
        self.hero_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.hero_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hero_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.hero_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.hero_table.verticalHeader().setDefaultSectionSize(100)

        self.verticalLayout_2.addWidget(self.hero_table)

        self.update_btn = QPushButton(self.hero_table_container)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(0, 40))
        self.update_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.update_btn)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.hero_table_container)

        self.button_area = QWidget(page_hero)
        self.button_area.setObjectName(u"button_area")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_area.sizePolicy().hasHeightForWidth())
        self.button_area.setSizePolicy(sizePolicy2)
        self.button_area.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.button_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.order_box = QComboBox(self.button_area)
        self.order_box.addItem("")
        self.order_box.addItem("")
        self.order_box.setObjectName(u"order_box")
        self.order_box.setMinimumSize(QSize(0, 40))
        self.order_box.setFont(font1)

        self.verticalLayout_4.addWidget(self.order_box)

        self.verticalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.groupBox = QGroupBox(self.button_area)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.star_1_btn = QPushButton(self.groupBox)
        self.star_1_btn.setObjectName(u"star_1_btn")
        self.star_1_btn.setMinimumSize(QSize(0, 40))
        self.star_1_btn.setFont(font1)

        self.verticalLayout.addWidget(self.star_1_btn)

        self.star_2_btn = QPushButton(self.groupBox)
        self.star_2_btn.setObjectName(u"star_2_btn")
        self.star_2_btn.setMinimumSize(QSize(0, 40))
        self.star_2_btn.setFont(font1)

        self.verticalLayout.addWidget(self.star_2_btn)

        self.all_check_btn = QPushButton(self.groupBox)
        self.all_check_btn.setObjectName(u"all_check_btn")
        self.all_check_btn.setMinimumSize(QSize(0, 40))
        self.all_check_btn.setFont(font1)

        self.verticalLayout.addWidget(self.all_check_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.all_uncheck_btn = QPushButton(self.groupBox)
        self.all_uncheck_btn.setObjectName(u"all_uncheck_btn")
        self.all_uncheck_btn.setMinimumSize(QSize(0, 40))
        self.all_uncheck_btn.setFont(font1)

        self.verticalLayout.addWidget(self.all_uncheck_btn)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 339, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.button_area)


        self.retranslateUi(page_hero)

        self.order_box.setCurrentIndex(0)


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
        self.order_box.setItemText(0, QCoreApplication.translate("page_hero", u"\uae30\ubcf8 \uc815\ub82c", None))
        self.order_box.setItemText(1, QCoreApplication.translate("page_hero", u"\uac00\ub098\ub2e4 \uc21c", None))

        self.order_box.setPlaceholderText("")
        self.groupBox.setTitle(QCoreApplication.translate("page_hero", u"\uc77c\uad04 \uc120\ud0dd", None))
        self.star_1_btn.setText(QCoreApplication.translate("page_hero", u"1\uc131 \uc804\ubd80 \ubcf4\uc720 \uc911", None))
        self.star_2_btn.setText(QCoreApplication.translate("page_hero", u"2\uc131 \uc804\ubd80 \ubcf4\uc720 \uc911", None))
        self.all_check_btn.setText(QCoreApplication.translate("page_hero", u"\uc804 \uc0ac\ub3c4 \ubcf4\uc720 \uc911", None))
        self.all_uncheck_btn.setText(QCoreApplication.translate("page_hero", u"\uc804\ubd80 \ubbf8\ubcf4\uc720", None))
    # retranslateUi

