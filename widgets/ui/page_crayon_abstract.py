# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_crayon_abstract.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from widgets.wrapper.misc import CrayonStatContainer

class Ui_page_crayon_abstract(object):
    def setupUi(self, page_crayon_abstract):
        if not page_crayon_abstract.objectName():
            page_crayon_abstract.setObjectName(u"page_crayon_abstract")
        page_crayon_abstract.resize(800, 600)
        self.verticalLayout = QVBoxLayout(page_crayon_abstract)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(page_crayon_abstract)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.containerHp = CrayonStatContainer(self.groupBox)
        self.containerHp.setObjectName(u"containerHp")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.containerHp.setFont(font1)
        self.containerHp.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.containerHp)

        self.containerAttackPhysic = CrayonStatContainer(self.groupBox)
        self.containerAttackPhysic.setObjectName(u"containerAttackPhysic")
        self.containerAttackPhysic.setFont(font1)
        self.containerAttackPhysic.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.containerAttackPhysic)

        self.containerAttackMagic = CrayonStatContainer(self.groupBox)
        self.containerAttackMagic.setObjectName(u"containerAttackMagic")
        self.containerAttackMagic.setFont(font1)
        self.containerAttackMagic.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.containerAttackMagic)

        self.containerDefensePhysic = CrayonStatContainer(self.groupBox)
        self.containerDefensePhysic.setObjectName(u"containerDefensePhysic")
        self.containerDefensePhysic.setFont(font1)
        self.containerDefensePhysic.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.containerDefensePhysic)

        self.containerDefenseMagic = CrayonStatContainer(self.groupBox)
        self.containerDefenseMagic.setObjectName(u"containerDefenseMagic")
        self.containerDefenseMagic.setFont(font1)
        self.containerDefenseMagic.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.containerDefenseMagic)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.containerEmpty = QWidget(self.groupBox)
        self.containerEmpty.setObjectName(u"containerEmpty")
        self.containerEmpty.setFont(font1)
        self.containerEmpty.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.containerEmpty)

        self.containerCriticalRate = CrayonStatContainer(self.groupBox)
        self.containerCriticalRate.setObjectName(u"containerCriticalRate")
        self.containerCriticalRate.setFont(font1)
        self.containerCriticalRate.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.containerCriticalRate)

        self.containerCriticalResist = CrayonStatContainer(self.groupBox)
        self.containerCriticalResist.setObjectName(u"containerCriticalResist")
        self.containerCriticalResist.setFont(font1)
        self.containerCriticalResist.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.containerCriticalResist)

        self.containerCriticalMult = CrayonStatContainer(self.groupBox)
        self.containerCriticalMult.setObjectName(u"containerCriticalMult")
        self.containerCriticalMult.setFont(font1)
        self.containerCriticalMult.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.containerCriticalMult)

        self.containerCriticalMultResist = CrayonStatContainer(self.groupBox)
        self.containerCriticalMultResist.setObjectName(u"containerCriticalMultResist")
        self.containerCriticalMultResist.setFont(font1)
        self.containerCriticalMultResist.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.containerCriticalMultResist)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.currency_widget = QGroupBox(page_crayon_abstract)
        self.currency_widget.setObjectName(u"currency_widget")
        self.currency_widget.setMinimumSize(QSize(0, 200))
        self.currency_widget.setMaximumSize(QSize(16777215, 200))
        self.currency_widget.setFont(font)
        self.horizontalLayout_8 = QHBoxLayout(self.currency_widget)
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 10, 20, 10)
        self.widget = QWidget(self.currency_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.IconGold = QLabel(self.widget)
        self.IconGold.setObjectName(u"IconGold")
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(14)
        self.IconGold.setFont(font2)

        self.horizontalLayout_2.addWidget(self.IconGold)

        self.ValueGold = QLabel(self.widget)
        self.ValueGold.setObjectName(u"ValueGold")
        self.ValueGold.setFont(font2)
        self.ValueGold.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.ValueGold)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.LabelCell1 = QLabel(self.widget)
        self.LabelCell1.setObjectName(u"LabelCell1")
        self.LabelCell1.setFont(font2)
        self.LabelCell1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.LabelCell1)

        self.ValueCellGold = QLabel(self.widget)
        self.ValueCellGold.setObjectName(u"ValueCellGold")
        self.ValueCellGold.setFont(font2)
        self.ValueCellGold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.ValueCellGold)

        self.LabelCell2 = QLabel(self.widget)
        self.LabelCell2.setObjectName(u"LabelCell2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LabelCell2.sizePolicy().hasHeightForWidth())
        self.LabelCell2.setSizePolicy(sizePolicy2)
        self.LabelCell2.setFont(font2)
        self.LabelCell2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.LabelCell2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LabelGateway1 = QLabel(self.widget)
        self.LabelGateway1.setObjectName(u"LabelGateway1")
        self.LabelGateway1.setFont(font2)
        self.LabelGateway1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.LabelGateway1)

        self.ValueGatewayGold = QLabel(self.widget)
        self.ValueGatewayGold.setObjectName(u"ValueGatewayGold")
        self.ValueGatewayGold.setFont(font2)
        self.ValueGatewayGold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.ValueGatewayGold)

        self.LabelGateway2 = QLabel(self.widget)
        self.LabelGateway2.setObjectName(u"LabelGateway2")
        sizePolicy2.setHeightForWidth(self.LabelGateway2.sizePolicy().hasHeightForWidth())
        self.LabelGateway2.setSizePolicy(sizePolicy2)
        self.LabelGateway2.setFont(font2)
        self.LabelGateway2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.LabelGateway2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addWidget(self.widget)

        self.widget_2 = QWidget(self.currency_widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CurrencyLayout_2 = QHBoxLayout()
        self.CurrencyLayout_2.setSpacing(10)
        self.CurrencyLayout_2.setObjectName(u"CurrencyLayout_2")
        self.IconCrayon1 = QLabel(self.widget_2)
        self.IconCrayon1.setObjectName(u"IconCrayon1")
        self.IconCrayon1.setFont(font2)

        self.CurrencyLayout_2.addWidget(self.IconCrayon1)

        self.ValueCrayon1 = QLabel(self.widget_2)
        self.ValueCrayon1.setObjectName(u"ValueCrayon1")
        self.ValueCrayon1.setFont(font2)
        self.ValueCrayon1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_2.addWidget(self.ValueCrayon1)


        self.gridLayout_2.addLayout(self.CurrencyLayout_2, 0, 0, 1, 1)

        self.CurrencyLayout_4 = QHBoxLayout()
        self.CurrencyLayout_4.setSpacing(10)
        self.CurrencyLayout_4.setObjectName(u"CurrencyLayout_4")
        self.IconCrayon3 = QLabel(self.widget_2)
        self.IconCrayon3.setObjectName(u"IconCrayon3")
        self.IconCrayon3.setFont(font2)

        self.CurrencyLayout_4.addWidget(self.IconCrayon3)

        self.ValueCrayon3 = QLabel(self.widget_2)
        self.ValueCrayon3.setObjectName(u"ValueCrayon3")
        self.ValueCrayon3.setFont(font2)
        self.ValueCrayon3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_4.addWidget(self.ValueCrayon3)


        self.gridLayout_2.addLayout(self.CurrencyLayout_4, 0, 1, 1, 1)

        self.CurrencyLayout_3 = QHBoxLayout()
        self.CurrencyLayout_3.setSpacing(10)
        self.CurrencyLayout_3.setObjectName(u"CurrencyLayout_3")
        self.IconCrayon2 = QLabel(self.widget_2)
        self.IconCrayon2.setObjectName(u"IconCrayon2")
        self.IconCrayon2.setFont(font2)

        self.CurrencyLayout_3.addWidget(self.IconCrayon2)

        self.ValueCrayon2 = QLabel(self.widget_2)
        self.ValueCrayon2.setObjectName(u"ValueCrayon2")
        self.ValueCrayon2.setFont(font2)
        self.ValueCrayon2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_3.addWidget(self.ValueCrayon2)


        self.gridLayout_2.addLayout(self.CurrencyLayout_3, 1, 0, 1, 1)

        self.CurrencyLayout_5 = QHBoxLayout()
        self.CurrencyLayout_5.setSpacing(10)
        self.CurrencyLayout_5.setObjectName(u"CurrencyLayout_5")
        self.IconCrayon4 = QLabel(self.widget_2)
        self.IconCrayon4.setObjectName(u"IconCrayon4")
        self.IconCrayon4.setFont(font2)

        self.CurrencyLayout_5.addWidget(self.IconCrayon4)

        self.ValueCrayon4 = QLabel(self.widget_2)
        self.ValueCrayon4.setObjectName(u"ValueCrayon4")
        self.ValueCrayon4.setFont(font2)
        self.ValueCrayon4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.CurrencyLayout_5.addWidget(self.ValueCrayon4)


        self.gridLayout_2.addLayout(self.CurrencyLayout_5, 1, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.currency_widget)


        self.retranslateUi(page_crayon_abstract)

        QMetaObject.connectSlotsByName(page_crayon_abstract)
    # setupUi

    def retranslateUi(self, page_crayon_abstract):
        page_crayon_abstract.setWindowTitle(QCoreApplication.translate("page_crayon_abstract", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("page_crayon_abstract", u"\uc804\uccb4 \ubcf4\ub4dc \uc2a4\ud0ef \ucd1d\ud569", None))
        self.currency_widget.setTitle(QCoreApplication.translate("page_crayon_abstract", u"\uc18c\ubaa8\ud55c \uc7ac\ud654", None))
        self.IconGold.setText(QCoreApplication.translate("page_crayon_abstract", u"\uace8\ub4dc", None))
        self.ValueGold.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.LabelCell1.setText(QCoreApplication.translate("page_crayon_abstract", u"\ubcf4\ub4dc\uce78", None))
        self.ValueCellGold.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.LabelCell2.setText(QCoreApplication.translate("page_crayon_abstract", u"\uace8\ub4dc \uc18c\ubaa8", None))
        self.LabelGateway1.setText(QCoreApplication.translate("page_crayon_abstract", u"\uad00\ubb38", None))
        self.ValueGatewayGold.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.LabelGateway2.setText(QCoreApplication.translate("page_crayon_abstract", u"\uace8\ub4dc \uc18c\ubaa8", None))
        self.IconCrayon1.setText(QCoreApplication.translate("page_crayon_abstract", u"\ud770\ud06c", None))
        self.ValueCrayon1.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.IconCrayon3.setText(QCoreApplication.translate("page_crayon_abstract", u"\ubcf4\ud06c", None))
        self.ValueCrayon3.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.IconCrayon2.setText(QCoreApplication.translate("page_crayon_abstract", u"\ud30c\ud06c", None))
        self.ValueCrayon2.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
        self.IconCrayon4.setText(QCoreApplication.translate("page_crayon_abstract", u"\ud669\ud06c", None))
        self.ValueCrayon4.setText(QCoreApplication.translate("page_crayon_abstract", u"0", None))
    # retranslateUi

