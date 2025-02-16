# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crayon_scrollarea.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QScrollArea, QSizePolicy,
    QWidget)

class Ui_crayon_scrollarea(object):
    def setupUi(self, crayon_scrollarea):
        if not crayon_scrollarea.objectName():
            crayon_scrollarea.setObjectName(u"crayon_scrollarea")
        crayon_scrollarea.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(crayon_scrollarea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(crayon_scrollarea)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 280))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(crayon_scrollarea)

        QMetaObject.connectSlotsByName(crayon_scrollarea)
    # setupUi

    def retranslateUi(self, crayon_scrollarea):
        crayon_scrollarea.setWindowTitle(QCoreApplication.translate("crayon_scrollarea", u"Form", None))
    # retranslateUi

