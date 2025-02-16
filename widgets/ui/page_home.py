# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_home.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_page_home(object):
    def setupUi(self, page_home):
        if not page_home.objectName():
            page_home.setObjectName(u"page_home")
        page_home.resize(800, 600)
        self.gridLayout = QGridLayout(page_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(page_home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(page_home)

        QMetaObject.connectSlotsByName(page_home)
    # setupUi

    def retranslateUi(self, page_home):
        page_home.setWindowTitle(QCoreApplication.translate("page_home", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_home", u"\uc900\ube44 \uc911...", None))
    # retranslateUi

