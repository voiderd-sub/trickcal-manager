# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QStackedWidget, QWidget)

from ui.wrapper import (PageEquip1, PageHero, Sidebar)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = Sidebar(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.sidebar)

        self.stacked_window = QStackedWidget(self.centralwidget)
        self.stacked_window.setObjectName(u"stacked_window")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stacked_window.sizePolicy().hasHeightForWidth())
        self.stacked_window.setSizePolicy(sizePolicy1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.stacked_window.addWidget(self.page_home)
        self.page_hero = PageHero(self.stacked_window)
        self.page_hero.setObjectName(u"page_hero")
        self.stacked_window.addWidget(self.page_hero)
        self.page_equip_1 = PageEquip1(self.stacked_window)
        self.page_equip_1.setObjectName(u"page_equip_1")
        self.stacked_window.addWidget(self.page_equip_1)
        self.page_equip_2 = QWidget()
        self.page_equip_2.setObjectName(u"page_equip_2")
        self.stacked_window.addWidget(self.page_equip_2)
        self.page_equip_3 = QWidget()
        self.page_equip_3.setObjectName(u"page_equip_3")
        self.stacked_window.addWidget(self.page_equip_3)
        self.page_crayon_1 = QWidget()
        self.page_crayon_1.setObjectName(u"page_crayon_1")
        self.stacked_window.addWidget(self.page_crayon_1)
        self.page_crayon_2 = QWidget()
        self.page_crayon_2.setObjectName(u"page_crayon_2")
        self.stacked_window.addWidget(self.page_crayon_2)
        self.page_food_1 = QWidget()
        self.page_food_1.setObjectName(u"page_food_1")
        self.stacked_window.addWidget(self.page_food_1)
        self.page_food_2 = QWidget()
        self.page_food_2.setObjectName(u"page_food_2")
        self.stacked_window.addWidget(self.page_food_2)
        self.page_food_3 = QWidget()
        self.page_food_3.setObjectName(u"page_food_3")
        self.stacked_window.addWidget(self.page_food_3)
        self.page_lab_1 = QWidget()
        self.page_lab_1.setObjectName(u"page_lab_1")
        self.stacked_window.addWidget(self.page_lab_1)
        self.page_lab_2 = QWidget()
        self.page_lab_2.setObjectName(u"page_lab_2")
        self.stacked_window.addWidget(self.page_lab_2)
        self.page_lab_3 = QWidget()
        self.page_lab_3.setObjectName(u"page_lab_3")
        self.stacked_window.addWidget(self.page_lab_3)

        self.horizontalLayout.addWidget(self.stacked_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_window.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trickal Manager", None))
    # retranslateUi

