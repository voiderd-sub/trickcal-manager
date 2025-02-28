# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QStackedWidget, QWidget)

from widgets.wrapper.page_crayon_1 import PageCrayon1
from widgets.wrapper.page_crayon_2 import PageCrayon2
from widgets.wrapper.page_crayon_abstract import PageCrayonAbstract
from widgets.wrapper.page_dps_1 import PageDps1
from widgets.wrapper.page_equip_1 import PageEquip1
from widgets.wrapper.page_equip_2 import PageEquip2
from widgets.wrapper.page_equip_3 import PageEquip3
from widgets.wrapper.page_equip_abstract import PageEquipAbstract
from widgets.wrapper.page_hero import PageHero
from widgets.wrapper.page_home import PageHome
from widgets.wrapper.sidebar import Sidebar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = Sidebar(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.sidebar)

        self.stacked_window = QStackedWidget(self.centralwidget)
        self.stacked_window.setObjectName(u"stacked_window")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stacked_window.sizePolicy().hasHeightForWidth())
        self.stacked_window.setSizePolicy(sizePolicy1)
        self.page_home = PageHome(self.stacked_window)
        self.page_home.setObjectName(u"page_home")
        self.stacked_window.addWidget(self.page_home)
        self.page_hero = PageHero(self.stacked_window)
        self.page_hero.setObjectName(u"page_hero")
        self.stacked_window.addWidget(self.page_hero)
        self.page_equip_abstract = PageEquipAbstract(self.stacked_window)
        self.page_equip_abstract.setObjectName(u"page_equip_abstract")
        self.stacked_window.addWidget(self.page_equip_abstract)
        self.page_equip_1 = PageEquip1(self.stacked_window)
        self.page_equip_1.setObjectName(u"page_equip_1")
        self.stacked_window.addWidget(self.page_equip_1)
        self.page_equip_2 = PageEquip2(self.stacked_window)
        self.page_equip_2.setObjectName(u"page_equip_2")
        self.stacked_window.addWidget(self.page_equip_2)
        self.page_equip_3 = PageEquip3(self.stacked_window)
        self.page_equip_3.setObjectName(u"page_equip_3")
        self.stacked_window.addWidget(self.page_equip_3)
        self.page_crayon_abstract = PageCrayonAbstract(self.stacked_window)
        self.page_crayon_abstract.setObjectName(u"page_crayon_abstract")
        self.stacked_window.addWidget(self.page_crayon_abstract)
        self.page_crayon_1 = PageCrayon1(self.stacked_window)
        self.page_crayon_1.setObjectName(u"page_crayon_1")
        self.stacked_window.addWidget(self.page_crayon_1)
        self.page_crayon_2 = PageCrayon2(self.stacked_window)
        self.page_crayon_2.setObjectName(u"page_crayon_2")
        self.stacked_window.addWidget(self.page_crayon_2)
        self.page_dps_1 = PageDps1(self.stacked_window)
        self.page_dps_1.setObjectName(u"page_dps_1")
        self.stacked_window.addWidget(self.page_dps_1)
        self.page_dps_2 = QWidget()
        self.page_dps_2.setObjectName(u"page_dps_2")
        self.stacked_window.addWidget(self.page_dps_2)
        self.page_cash_1 = QWidget()
        self.page_cash_1.setObjectName(u"page_cash_1")
        self.stacked_window.addWidget(self.page_cash_1)
        self.page_cash_2 = QWidget()
        self.page_cash_2.setObjectName(u"page_cash_2")
        self.stacked_window.addWidget(self.page_cash_2)
        self.page_cash_3 = QWidget()
        self.page_cash_3.setObjectName(u"page_cash_3")
        self.stacked_window.addWidget(self.page_cash_3)

        self.horizontalLayout.addWidget(self.stacked_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trickal Manager", None))
    # retranslateUi

