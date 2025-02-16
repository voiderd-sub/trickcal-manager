# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equip_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 500)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_1 = QTextEdit(self.tab_1)
        self.text_1.setObjectName(u"text_1")
        self.text_1.setReadOnly(True)

        self.gridLayout.addWidget(self.text_1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_3 = QTextEdit(self.tab_3)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.text_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.text_2 = QTextEdit(self.tab_2)
        self.text_2.setObjectName(u"text_2")
        self.text_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.text_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.text_4 = QTextEdit(self.tab_4)
        self.text_4.setObjectName(u"text_4")
        self.text_4.setReadOnly(True)

        self.gridLayout_4.addWidget(self.text_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ok_btn = QPushButton(Dialog)
        self.ok_btn.setObjectName(u"ok_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.ok_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.ok_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Dialog", u"\uc694\uc57d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\uc7ac\ub8cc\ubcc4 \uc218\uae09\ucc98", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\uc9c0\uc5ed \ubcc4 \uba74\uc81c \ud69f\uc218", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"\uc815\uc11d \uc0ac\uc6a9\ucc98", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"\ud655\uc778\ud588\uc5b4\uc694", None))
    # retranslateUi

