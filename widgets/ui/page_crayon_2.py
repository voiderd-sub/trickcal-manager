# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_crayon_2.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from widgets.wrapper.misc import QCheckButton

class Ui_page_crayon_2(object):
    def setupUi(self, page_crayon_2):
        if not page_crayon_2.objectName():
            page_crayon_2.setObjectName(u"page_crayon_2")
        page_crayon_2.resize(781, 584)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(17)
        page_crayon_2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(page_crayon_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.groupBox = QGroupBox(page_crayon_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkbutton = QCheckButton(self.groupBox)
        self.checkbutton.setObjectName(u"checkbutton")
        self.checkbutton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbutton.sizePolicy().hasHeightForWidth())
        self.checkbutton.setSizePolicy(sizePolicy)
        self.checkbutton.setMinimumSize(QSize(25, 25))
        self.checkbutton.setMaximumSize(QSize(25, 25))
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(8)
        self.checkbutton.setFont(font1)
        self.checkbutton.setCheckable(True)
        self.checkbutton.setChecked(False)

        self.horizontalLayout.addWidget(self.checkbutton)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(15)
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ownedHeroCheckButton = QCheckButton(self.groupBox)
        self.ownedHeroCheckButton.setObjectName(u"ownedHeroCheckButton")
        self.ownedHeroCheckButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ownedHeroCheckButton.sizePolicy().hasHeightForWidth())
        self.ownedHeroCheckButton.setSizePolicy(sizePolicy)
        self.ownedHeroCheckButton.setMinimumSize(QSize(25, 25))
        self.ownedHeroCheckButton.setMaximumSize(QSize(25, 25))
        self.ownedHeroCheckButton.setFont(font1)
        self.ownedHeroCheckButton.setCheckable(True)
        self.ownedHeroCheckButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.ownedHeroCheckButton)

        self.ownedHeroLabel = QLabel(self.groupBox)
        self.ownedHeroLabel.setObjectName(u"ownedHeroLabel")
        self.ownedHeroLabel.setFont(font2)

        self.horizontalLayout_3.addWidget(self.ownedHeroLabel)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.tabWidget = QTabWidget(page_crayon_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tab_gold = QWidget()
        self.tab_gold.setObjectName(u"tab_gold")
        self.tabWidget.addTab(self.tab_gold, "")
        self.tab_purple = QWidget()
        self.tab_purple.setObjectName(u"tab_purple")
        self.tabWidget.addTab(self.tab_purple, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(page_crayon_2)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(page_crayon_2)
    # setupUi

    def retranslateUi(self, page_crayon_2):
        page_crayon_2.setWindowTitle(QCoreApplication.translate("page_crayon_2", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("page_crayon_2", u"\ubcf4\uae30 \uc124\uc815", None))
        self.checkbutton.setText("")
        self.label_2.setText(QCoreApplication.translate("page_crayon_2", u"\uc774\ubbf8 \uce60\ud55c \uce78\ub3c4 \ud45c\uc2dc", None))
        self.ownedHeroCheckButton.setText("")
        self.ownedHeroLabel.setText(QCoreApplication.translate("page_crayon_2", u"\ubcf4\uc720 \uc0ac\ub3c4\ub9cc \ud45c\uc2dc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gold), QCoreApplication.translate("page_crayon_2", u"\ud669\ud06c\uce78", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_purple), QCoreApplication.translate("page_crayon_2", u"\ubcf4\ud06c\uce78", None))
    # retranslateUi

