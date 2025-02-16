# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crayon_stat_container.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CrayonStatContainer(object):
    def setupUi(self, CrayonStatContainer):
        if not CrayonStatContainer.objectName():
            CrayonStatContainer.setObjectName(u"CrayonStatContainer")
        CrayonStatContainer.resize(343, 135)
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(14)
        CrayonStatContainer.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(CrayonStatContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon = QLabel(CrayonStatContainer)
        self.icon.setObjectName(u"icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font1.setPointSize(15)
        self.icon.setFont(font1)
        self.icon.setScaledContents(True)
        self.icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.icon)

        self.name = QLabel(CrayonStatContainer)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(120, 0))
        font2 = QFont()
        font2.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font2.setPointSize(17)
        self.name.setFont(font2)
        self.name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.name)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stat_purple = QLabel(CrayonStatContainer)
        self.stat_purple.setObjectName(u"stat_purple")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stat_purple.sizePolicy().hasHeightForWidth())
        self.stat_purple.setSizePolicy(sizePolicy2)
        self.stat_purple.setFont(font1)
        self.stat_purple.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stat_purple)

        self.stat_gold = QLabel(CrayonStatContainer)
        self.stat_gold.setObjectName(u"stat_gold")
        sizePolicy2.setHeightForWidth(self.stat_gold.sizePolicy().hasHeightForWidth())
        self.stat_gold.setSizePolicy(sizePolicy2)
        self.stat_gold.setFont(font1)
        self.stat_gold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stat_gold)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.num_purple = QLabel(CrayonStatContainer)
        self.num_purple.setObjectName(u"num_purple")
        sizePolicy.setHeightForWidth(self.num_purple.sizePolicy().hasHeightForWidth())
        self.num_purple.setSizePolicy(sizePolicy)
        self.num_purple.setMinimumSize(QSize(120, 0))
        self.num_purple.setFont(font1)
        self.num_purple.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.num_purple)

        self.num_gold = QLabel(CrayonStatContainer)
        self.num_gold.setObjectName(u"num_gold")
        sizePolicy.setHeightForWidth(self.num_gold.sizePolicy().hasHeightForWidth())
        self.num_gold.setSizePolicy(sizePolicy)
        self.num_gold.setMinimumSize(QSize(120, 0))
        self.num_gold.setFont(font1)
        self.num_gold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.num_gold)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(CrayonStatContainer)

        QMetaObject.connectSlotsByName(CrayonStatContainer)
    # setupUi

    def retranslateUi(self, CrayonStatContainer):
        CrayonStatContainer.setWindowTitle(QCoreApplication.translate("CrayonStatContainer", u"Form", None))
        self.icon.setText("")
        self.name.setText(QCoreApplication.translate("CrayonStatContainer", u"\uccb4\ub825", None))
        self.stat_purple.setText(QCoreApplication.translate("CrayonStatContainer", u"0", None))
        self.stat_gold.setText(QCoreApplication.translate("CrayonStatContainer", u"0", None))
        self.num_purple.setText(QCoreApplication.translate("CrayonStatContainer", u"0", None))
        self.num_gold.setText(QCoreApplication.translate("CrayonStatContainer", u"0", None))
    # retranslateUi

