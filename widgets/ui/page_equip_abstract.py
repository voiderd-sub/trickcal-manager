# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_equip_abstract.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_page_equip_abstract(object):
    def setupUi(self, page_equip_abstract):
        if not page_equip_abstract.objectName():
            page_equip_abstract.setObjectName(u"page_equip_abstract")
        page_equip_abstract.resize(800, 600)
        self.verticalLayout_3 = QVBoxLayout(page_equip_abstract)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(page_equip_abstract)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.containerHp = QWidget(self.groupBox)
        self.containerHp.setObjectName(u"containerHp")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(15)
        self.containerHp.setFont(font1)
        self.containerHp.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.containerHp)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 10, 0)
        self.iconHp = QLabel(self.containerHp)
        self.iconHp.setObjectName(u"iconHp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconHp.sizePolicy().hasHeightForWidth())
        self.iconHp.setSizePolicy(sizePolicy1)
        self.iconHp.setMinimumSize(QSize(27, 27))
        self.iconHp.setMaximumSize(QSize(27, 27))
        self.iconHp.setFont(font1)
        self.iconHp.setScaledContents(True)
        self.iconHp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.iconHp)

        self.nameHp = QLabel(self.containerHp)
        self.nameHp.setObjectName(u"nameHp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nameHp.sizePolicy().hasHeightForWidth())
        self.nameHp.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(14)
        self.nameHp.setFont(font2)
        self.nameHp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.nameHp)

        self.statHp = QLabel(self.containerHp)
        self.statHp.setObjectName(u"statHp")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statHp.sizePolicy().hasHeightForWidth())
        self.statHp.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(13)
        self.statHp.setFont(font3)
        self.statHp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.statHp)

        self.rateHp = QLabel(self.containerHp)
        self.rateHp.setObjectName(u"rateHp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rateHp.sizePolicy().hasHeightForWidth())
        self.rateHp.setSizePolicy(sizePolicy4)
        self.rateHp.setMinimumSize(QSize(70, 0))
        self.rateHp.setFont(font3)
        self.rateHp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rateHp)


        self.verticalLayout_2.addWidget(self.containerHp)

        self.containerAttackPhysic = QWidget(self.groupBox)
        self.containerAttackPhysic.setObjectName(u"containerAttackPhysic")
        self.containerAttackPhysic.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.containerAttackPhysic)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 10, 0)
        self.iconAttackPhysic = QLabel(self.containerAttackPhysic)
        self.iconAttackPhysic.setObjectName(u"iconAttackPhysic")
        sizePolicy1.setHeightForWidth(self.iconAttackPhysic.sizePolicy().hasHeightForWidth())
        self.iconAttackPhysic.setSizePolicy(sizePolicy1)
        self.iconAttackPhysic.setMinimumSize(QSize(27, 27))
        self.iconAttackPhysic.setMaximumSize(QSize(27, 27))
        self.iconAttackPhysic.setFont(font1)
        self.iconAttackPhysic.setScaledContents(True)
        self.iconAttackPhysic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.iconAttackPhysic)

        self.nameAttackPhysic = QLabel(self.containerAttackPhysic)
        self.nameAttackPhysic.setObjectName(u"nameAttackPhysic")
        sizePolicy2.setHeightForWidth(self.nameAttackPhysic.sizePolicy().hasHeightForWidth())
        self.nameAttackPhysic.setSizePolicy(sizePolicy2)
        self.nameAttackPhysic.setFont(font2)
        self.nameAttackPhysic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.nameAttackPhysic)

        self.statAttackPhysic = QLabel(self.containerAttackPhysic)
        self.statAttackPhysic.setObjectName(u"statAttackPhysic")
        sizePolicy3.setHeightForWidth(self.statAttackPhysic.sizePolicy().hasHeightForWidth())
        self.statAttackPhysic.setSizePolicy(sizePolicy3)
        self.statAttackPhysic.setFont(font3)
        self.statAttackPhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.statAttackPhysic)

        self.rateAttackPhysic = QLabel(self.containerAttackPhysic)
        self.rateAttackPhysic.setObjectName(u"rateAttackPhysic")
        sizePolicy4.setHeightForWidth(self.rateAttackPhysic.sizePolicy().hasHeightForWidth())
        self.rateAttackPhysic.setSizePolicy(sizePolicy4)
        self.rateAttackPhysic.setMinimumSize(QSize(70, 0))
        self.rateAttackPhysic.setFont(font3)
        self.rateAttackPhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.rateAttackPhysic)


        self.verticalLayout_2.addWidget(self.containerAttackPhysic)

        self.containerAttackMagic = QWidget(self.groupBox)
        self.containerAttackMagic.setObjectName(u"containerAttackMagic")
        self.containerAttackMagic.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.containerAttackMagic)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 10, 0)
        self.iconAttackMagic = QLabel(self.containerAttackMagic)
        self.iconAttackMagic.setObjectName(u"iconAttackMagic")
        sizePolicy1.setHeightForWidth(self.iconAttackMagic.sizePolicy().hasHeightForWidth())
        self.iconAttackMagic.setSizePolicy(sizePolicy1)
        self.iconAttackMagic.setMinimumSize(QSize(27, 27))
        self.iconAttackMagic.setMaximumSize(QSize(27, 27))
        self.iconAttackMagic.setFont(font1)
        self.iconAttackMagic.setScaledContents(True)
        self.iconAttackMagic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.iconAttackMagic)

        self.nameAttackMagic = QLabel(self.containerAttackMagic)
        self.nameAttackMagic.setObjectName(u"nameAttackMagic")
        sizePolicy2.setHeightForWidth(self.nameAttackMagic.sizePolicy().hasHeightForWidth())
        self.nameAttackMagic.setSizePolicy(sizePolicy2)
        self.nameAttackMagic.setFont(font2)
        self.nameAttackMagic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.nameAttackMagic)

        self.statAttackMagic = QLabel(self.containerAttackMagic)
        self.statAttackMagic.setObjectName(u"statAttackMagic")
        sizePolicy3.setHeightForWidth(self.statAttackMagic.sizePolicy().hasHeightForWidth())
        self.statAttackMagic.setSizePolicy(sizePolicy3)
        self.statAttackMagic.setFont(font3)
        self.statAttackMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.statAttackMagic)

        self.rateAttackMagic = QLabel(self.containerAttackMagic)
        self.rateAttackMagic.setObjectName(u"rateAttackMagic")
        sizePolicy4.setHeightForWidth(self.rateAttackMagic.sizePolicy().hasHeightForWidth())
        self.rateAttackMagic.setSizePolicy(sizePolicy4)
        self.rateAttackMagic.setMinimumSize(QSize(70, 0))
        self.rateAttackMagic.setFont(font3)
        self.rateAttackMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.rateAttackMagic)


        self.verticalLayout_2.addWidget(self.containerAttackMagic)

        self.containerDefensePhysic = QWidget(self.groupBox)
        self.containerDefensePhysic.setObjectName(u"containerDefensePhysic")
        self.containerDefensePhysic.setFont(font1)
        self.horizontalLayout_9 = QHBoxLayout(self.containerDefensePhysic)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 10, 0)
        self.iconDefensePhysic = QLabel(self.containerDefensePhysic)
        self.iconDefensePhysic.setObjectName(u"iconDefensePhysic")
        sizePolicy1.setHeightForWidth(self.iconDefensePhysic.sizePolicy().hasHeightForWidth())
        self.iconDefensePhysic.setSizePolicy(sizePolicy1)
        self.iconDefensePhysic.setMinimumSize(QSize(27, 27))
        self.iconDefensePhysic.setMaximumSize(QSize(27, 27))
        self.iconDefensePhysic.setFont(font1)
        self.iconDefensePhysic.setScaledContents(True)
        self.iconDefensePhysic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.iconDefensePhysic)

        self.nameDefensePhysic = QLabel(self.containerDefensePhysic)
        self.nameDefensePhysic.setObjectName(u"nameDefensePhysic")
        sizePolicy2.setHeightForWidth(self.nameDefensePhysic.sizePolicy().hasHeightForWidth())
        self.nameDefensePhysic.setSizePolicy(sizePolicy2)
        self.nameDefensePhysic.setFont(font2)
        self.nameDefensePhysic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.nameDefensePhysic)

        self.statDefensePhysic = QLabel(self.containerDefensePhysic)
        self.statDefensePhysic.setObjectName(u"statDefensePhysic")
        sizePolicy3.setHeightForWidth(self.statDefensePhysic.sizePolicy().hasHeightForWidth())
        self.statDefensePhysic.setSizePolicy(sizePolicy3)
        self.statDefensePhysic.setFont(font3)
        self.statDefensePhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.statDefensePhysic)

        self.rateDefensePhysic = QLabel(self.containerDefensePhysic)
        self.rateDefensePhysic.setObjectName(u"rateDefensePhysic")
        sizePolicy4.setHeightForWidth(self.rateDefensePhysic.sizePolicy().hasHeightForWidth())
        self.rateDefensePhysic.setSizePolicy(sizePolicy4)
        self.rateDefensePhysic.setMinimumSize(QSize(70, 0))
        self.rateDefensePhysic.setFont(font3)
        self.rateDefensePhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.rateDefensePhysic)


        self.verticalLayout_2.addWidget(self.containerDefensePhysic)

        self.containerDefenseMagic = QWidget(self.groupBox)
        self.containerDefenseMagic.setObjectName(u"containerDefenseMagic")
        self.containerDefenseMagic.setFont(font1)
        self.horizontalLayout_10 = QHBoxLayout(self.containerDefenseMagic)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.iconDefenseMagic = QLabel(self.containerDefenseMagic)
        self.iconDefenseMagic.setObjectName(u"iconDefenseMagic")
        sizePolicy1.setHeightForWidth(self.iconDefenseMagic.sizePolicy().hasHeightForWidth())
        self.iconDefenseMagic.setSizePolicy(sizePolicy1)
        self.iconDefenseMagic.setMinimumSize(QSize(27, 27))
        self.iconDefenseMagic.setMaximumSize(QSize(27, 27))
        self.iconDefenseMagic.setFont(font1)
        self.iconDefenseMagic.setScaledContents(True)
        self.iconDefenseMagic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.iconDefenseMagic)

        self.nameDefenseMagic = QLabel(self.containerDefenseMagic)
        self.nameDefenseMagic.setObjectName(u"nameDefenseMagic")
        sizePolicy2.setHeightForWidth(self.nameDefenseMagic.sizePolicy().hasHeightForWidth())
        self.nameDefenseMagic.setSizePolicy(sizePolicy2)
        self.nameDefenseMagic.setFont(font2)
        self.nameDefenseMagic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.nameDefenseMagic)

        self.statDefenseMagic = QLabel(self.containerDefenseMagic)
        self.statDefenseMagic.setObjectName(u"statDefenseMagic")
        sizePolicy3.setHeightForWidth(self.statDefenseMagic.sizePolicy().hasHeightForWidth())
        self.statDefenseMagic.setSizePolicy(sizePolicy3)
        self.statDefenseMagic.setFont(font3)
        self.statDefenseMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.statDefenseMagic)

        self.rateDefenseMagic = QLabel(self.containerDefenseMagic)
        self.rateDefenseMagic.setObjectName(u"rateDefenseMagic")
        sizePolicy4.setHeightForWidth(self.rateDefenseMagic.sizePolicy().hasHeightForWidth())
        self.rateDefenseMagic.setSizePolicy(sizePolicy4)
        self.rateDefenseMagic.setMinimumSize(QSize(70, 0))
        self.rateDefenseMagic.setFont(font3)
        self.rateDefenseMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.rateDefenseMagic)


        self.verticalLayout_2.addWidget(self.containerDefenseMagic)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.containerCriticalRate = QWidget(self.groupBox)
        self.containerCriticalRate.setObjectName(u"containerCriticalRate")
        self.containerCriticalRate.setFont(font1)
        self.horizontalLayout_11 = QHBoxLayout(self.containerCriticalRate)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 0, 10, 0)
        self.iconCriticalRate = QLabel(self.containerCriticalRate)
        self.iconCriticalRate.setObjectName(u"iconCriticalRate")
        sizePolicy1.setHeightForWidth(self.iconCriticalRate.sizePolicy().hasHeightForWidth())
        self.iconCriticalRate.setSizePolicy(sizePolicy1)
        self.iconCriticalRate.setMinimumSize(QSize(27, 27))
        self.iconCriticalRate.setMaximumSize(QSize(27, 27))
        self.iconCriticalRate.setFont(font1)
        self.iconCriticalRate.setScaledContents(True)
        self.iconCriticalRate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.iconCriticalRate)

        self.nameCriticalRate = QLabel(self.containerCriticalRate)
        self.nameCriticalRate.setObjectName(u"nameCriticalRate")
        sizePolicy2.setHeightForWidth(self.nameCriticalRate.sizePolicy().hasHeightForWidth())
        self.nameCriticalRate.setSizePolicy(sizePolicy2)
        self.nameCriticalRate.setFont(font2)
        self.nameCriticalRate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.nameCriticalRate)

        self.statCriticalRate = QLabel(self.containerCriticalRate)
        self.statCriticalRate.setObjectName(u"statCriticalRate")
        sizePolicy3.setHeightForWidth(self.statCriticalRate.sizePolicy().hasHeightForWidth())
        self.statCriticalRate.setSizePolicy(sizePolicy3)
        self.statCriticalRate.setFont(font3)
        self.statCriticalRate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.statCriticalRate)

        self.rateCriticalRate = QLabel(self.containerCriticalRate)
        self.rateCriticalRate.setObjectName(u"rateCriticalRate")
        sizePolicy4.setHeightForWidth(self.rateCriticalRate.sizePolicy().hasHeightForWidth())
        self.rateCriticalRate.setSizePolicy(sizePolicy4)
        self.rateCriticalRate.setMinimumSize(QSize(70, 0))
        self.rateCriticalRate.setFont(font3)
        self.rateCriticalRate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.rateCriticalRate)


        self.verticalLayout.addWidget(self.containerCriticalRate)

        self.containerCriticalMult = QWidget(self.groupBox)
        self.containerCriticalMult.setObjectName(u"containerCriticalMult")
        self.containerCriticalMult.setFont(font1)
        self.horizontalLayout_12 = QHBoxLayout(self.containerCriticalMult)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 10, 0)
        self.iconCriticalMult = QLabel(self.containerCriticalMult)
        self.iconCriticalMult.setObjectName(u"iconCriticalMult")
        sizePolicy1.setHeightForWidth(self.iconCriticalMult.sizePolicy().hasHeightForWidth())
        self.iconCriticalMult.setSizePolicy(sizePolicy1)
        self.iconCriticalMult.setMinimumSize(QSize(27, 27))
        self.iconCriticalMult.setMaximumSize(QSize(27, 27))
        self.iconCriticalMult.setFont(font1)
        self.iconCriticalMult.setScaledContents(True)
        self.iconCriticalMult.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.iconCriticalMult)

        self.nameCriticalMult = QLabel(self.containerCriticalMult)
        self.nameCriticalMult.setObjectName(u"nameCriticalMult")
        sizePolicy2.setHeightForWidth(self.nameCriticalMult.sizePolicy().hasHeightForWidth())
        self.nameCriticalMult.setSizePolicy(sizePolicy2)
        self.nameCriticalMult.setFont(font2)
        self.nameCriticalMult.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.nameCriticalMult)

        self.statCriticalMult = QLabel(self.containerCriticalMult)
        self.statCriticalMult.setObjectName(u"statCriticalMult")
        sizePolicy3.setHeightForWidth(self.statCriticalMult.sizePolicy().hasHeightForWidth())
        self.statCriticalMult.setSizePolicy(sizePolicy3)
        self.statCriticalMult.setFont(font3)
        self.statCriticalMult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.statCriticalMult)

        self.rateCriticalMult = QLabel(self.containerCriticalMult)
        self.rateCriticalMult.setObjectName(u"rateCriticalMult")
        sizePolicy4.setHeightForWidth(self.rateCriticalMult.sizePolicy().hasHeightForWidth())
        self.rateCriticalMult.setSizePolicy(sizePolicy4)
        self.rateCriticalMult.setMinimumSize(QSize(70, 0))
        self.rateCriticalMult.setFont(font3)
        self.rateCriticalMult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.rateCriticalMult)


        self.verticalLayout.addWidget(self.containerCriticalMult)

        self.containerCriticalResist = QWidget(self.groupBox)
        self.containerCriticalResist.setObjectName(u"containerCriticalResist")
        self.containerCriticalResist.setFont(font1)
        self.horizontalLayout_13 = QHBoxLayout(self.containerCriticalResist)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 10, 0)
        self.iconCriticalResist = QLabel(self.containerCriticalResist)
        self.iconCriticalResist.setObjectName(u"iconCriticalResist")
        sizePolicy1.setHeightForWidth(self.iconCriticalResist.sizePolicy().hasHeightForWidth())
        self.iconCriticalResist.setSizePolicy(sizePolicy1)
        self.iconCriticalResist.setMinimumSize(QSize(27, 27))
        self.iconCriticalResist.setMaximumSize(QSize(27, 27))
        self.iconCriticalResist.setFont(font1)
        self.iconCriticalResist.setScaledContents(True)
        self.iconCriticalResist.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.iconCriticalResist)

        self.nameCriticalResist = QLabel(self.containerCriticalResist)
        self.nameCriticalResist.setObjectName(u"nameCriticalResist")
        sizePolicy2.setHeightForWidth(self.nameCriticalResist.sizePolicy().hasHeightForWidth())
        self.nameCriticalResist.setSizePolicy(sizePolicy2)
        self.nameCriticalResist.setFont(font2)
        self.nameCriticalResist.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.nameCriticalResist)

        self.statCriticalResist = QLabel(self.containerCriticalResist)
        self.statCriticalResist.setObjectName(u"statCriticalResist")
        sizePolicy3.setHeightForWidth(self.statCriticalResist.sizePolicy().hasHeightForWidth())
        self.statCriticalResist.setSizePolicy(sizePolicy3)
        self.statCriticalResist.setFont(font3)
        self.statCriticalResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.statCriticalResist)

        self.rateCriticalResist = QLabel(self.containerCriticalResist)
        self.rateCriticalResist.setObjectName(u"rateCriticalResist")
        sizePolicy4.setHeightForWidth(self.rateCriticalResist.sizePolicy().hasHeightForWidth())
        self.rateCriticalResist.setSizePolicy(sizePolicy4)
        self.rateCriticalResist.setMinimumSize(QSize(70, 0))
        self.rateCriticalResist.setFont(font3)
        self.rateCriticalResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.rateCriticalResist)


        self.verticalLayout.addWidget(self.containerCriticalResist)

        self.containerCriticalMultResist = QWidget(self.groupBox)
        self.containerCriticalMultResist.setObjectName(u"containerCriticalMultResist")
        self.containerCriticalMultResist.setFont(font1)
        self.horizontalLayout_14 = QHBoxLayout(self.containerCriticalMultResist)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 10, 0)
        self.iconCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.iconCriticalMultResist.setObjectName(u"iconCriticalMultResist")
        sizePolicy1.setHeightForWidth(self.iconCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.iconCriticalMultResist.setSizePolicy(sizePolicy1)
        self.iconCriticalMultResist.setMinimumSize(QSize(27, 27))
        self.iconCriticalMultResist.setMaximumSize(QSize(27, 27))
        self.iconCriticalMultResist.setFont(font1)
        self.iconCriticalMultResist.setScaledContents(True)
        self.iconCriticalMultResist.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.iconCriticalMultResist)

        self.nameCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.nameCriticalMultResist.setObjectName(u"nameCriticalMultResist")
        sizePolicy2.setHeightForWidth(self.nameCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.nameCriticalMultResist.setSizePolicy(sizePolicy2)
        self.nameCriticalMultResist.setFont(font2)
        self.nameCriticalMultResist.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.nameCriticalMultResist)

        self.statCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.statCriticalMultResist.setObjectName(u"statCriticalMultResist")
        sizePolicy3.setHeightForWidth(self.statCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.statCriticalMultResist.setSizePolicy(sizePolicy3)
        self.statCriticalMultResist.setFont(font3)
        self.statCriticalMultResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.statCriticalMultResist)

        self.rateCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.rateCriticalMultResist.setObjectName(u"rateCriticalMultResist")
        sizePolicy4.setHeightForWidth(self.rateCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.rateCriticalMultResist.setSizePolicy(sizePolicy4)
        self.rateCriticalMultResist.setMinimumSize(QSize(70, 0))
        self.rateCriticalMultResist.setFont(font3)
        self.rateCriticalMultResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.rateCriticalMultResist)


        self.verticalLayout.addWidget(self.containerCriticalMultResist)

        self.containerAll = QWidget(self.groupBox)
        self.containerAll.setObjectName(u"containerAll")
        self.containerAll.setFont(font1)
        self.horizontalLayout_16 = QHBoxLayout(self.containerAll)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 0, 0)
        self.iconAll = QLabel(self.containerAll)
        self.iconAll.setObjectName(u"iconAll")
        sizePolicy1.setHeightForWidth(self.iconAll.sizePolicy().hasHeightForWidth())
        self.iconAll.setSizePolicy(sizePolicy1)
        self.iconAll.setMinimumSize(QSize(27, 27))
        self.iconAll.setMaximumSize(QSize(27, 27))
        self.iconAll.setFont(font1)
        self.iconAll.setScaledContents(True)
        self.iconAll.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.iconAll)

        self.containerAll_2 = QWidget(self.containerAll)
        self.containerAll_2.setObjectName(u"containerAll_2")
        self.horizontalLayout_3 = QHBoxLayout(self.containerAll_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.nameAll = QLabel(self.containerAll_2)
        self.nameAll.setObjectName(u"nameAll")
        sizePolicy2.setHeightForWidth(self.nameAll.sizePolicy().hasHeightForWidth())
        self.nameAll.setSizePolicy(sizePolicy2)
        self.nameAll.setFont(font2)
        self.nameAll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.nameAll)

        self.rateAll = QLabel(self.containerAll_2)
        self.rateAll.setObjectName(u"rateAll")
        sizePolicy3.setHeightForWidth(self.rateAll.sizePolicy().hasHeightForWidth())
        self.rateAll.setSizePolicy(sizePolicy3)
        self.rateAll.setFont(font3)
        self.rateAll.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.rateAll)


        self.horizontalLayout_16.addWidget(self.containerAll_2)


        self.verticalLayout.addWidget(self.containerAll)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.widget = QWidget(page_equip_abstract)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(3)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_13 = QWidget(self.widget)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_2 = QGridLayout(self.widget_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.goal_list = QComboBox(self.widget_13)
        self.goal_list.setObjectName(u"goal_list")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.goal_list.sizePolicy().hasHeightForWidth())
        self.goal_list.setSizePolicy(sizePolicy6)
        self.goal_list.setMinimumSize(QSize(0, 25))
        self.goal_list.setFont(font2)

        self.gridLayout_2.addWidget(self.goal_list, 0, 1, 1, 1)

        self.goal_rate_label_left = QLabel(self.widget_13)
        self.goal_rate_label_left.setObjectName(u"goal_rate_label_left")
        sizePolicy4.setHeightForWidth(self.goal_rate_label_left.sizePolicy().hasHeightForWidth())
        self.goal_rate_label_left.setSizePolicy(sizePolicy4)
        self.goal_rate_label_left.setFont(font2)

        self.gridLayout_2.addWidget(self.goal_rate_label_left, 1, 0, 1, 1)

        self.goal_rate_label_right = QLabel(self.widget_13)
        self.goal_rate_label_right.setObjectName(u"goal_rate_label_right")
        sizePolicy4.setHeightForWidth(self.goal_rate_label_right.sizePolicy().hasHeightForWidth())
        self.goal_rate_label_right.setSizePolicy(sizePolicy4)
        self.goal_rate_label_right.setFont(font2)
        self.goal_rate_label_right.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.goal_rate_label_right, 1, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_13)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_equip_hide = QRadioButton(self.groupBox_2)
        self.radio_equip_hide.setObjectName(u"radio_equip_hide")
        self.radio_equip_hide.setFont(font3)
        self.radio_equip_hide.setChecked(True)

        self.gridLayout.addWidget(self.radio_equip_hide, 0, 0, 1, 1)

        self.radio_equip_show = QRadioButton(self.groupBox_2)
        self.radio_equip_show.setObjectName(u"radio_equip_show")
        self.radio_equip_show.setFont(font3)

        self.gridLayout.addWidget(self.radio_equip_show, 0, 1, 1, 1)

        self.check_show_completed = QCheckBox(self.groupBox_2)
        self.check_show_completed.setObjectName(u"check_show_completed")
        self.check_show_completed.setFont(font3)

        self.gridLayout.addWidget(self.check_show_completed, 1, 0, 1, 2)


        self.horizontalLayout_6.addWidget(self.groupBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.equip_abstract_scrolls = QScrollArea(self.widget)
        self.equip_abstract_scrolls.setObjectName(u"equip_abstract_scrolls")
        self.equip_abstract_scrolls.setFont(font3)
        self.equip_abstract_scrolls.setWidgetResizable(True)
        self.scroll_container = QWidget()
        self.scroll_container.setObjectName(u"scroll_container")
        self.scroll_container.setGeometry(QRect(0, 0, 762, 206))
        self.equip_abstract_scrolls.setWidget(self.scroll_container)

        self.verticalLayout_4.addWidget(self.equip_abstract_scrolls)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(page_equip_abstract)

        QMetaObject.connectSlotsByName(page_equip_abstract)
    # setupUi

    def retranslateUi(self, page_equip_abstract):
        page_equip_abstract.setWindowTitle(QCoreApplication.translate("page_equip_abstract", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("page_equip_abstract", u"\ub7ad\ud06c\uc791 \uc2a4\ud0ef \ucd1d\ud569", None))
        self.iconHp.setText("")
        self.nameHp.setText(QCoreApplication.translate("page_equip_abstract", u"\uccb4\ub825", None))
        self.statHp.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateHp.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconAttackPhysic.setText("")
        self.nameAttackPhysic.setText(QCoreApplication.translate("page_equip_abstract", u"\ubb3c\ub9ac \uacf5\uaca9\ub825", None))
        self.statAttackPhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateAttackPhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconAttackMagic.setText("")
        self.nameAttackMagic.setText(QCoreApplication.translate("page_equip_abstract", u"\ub9c8\ubc95 \uacf5\uaca9\ub825", None))
        self.statAttackMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateAttackMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconDefensePhysic.setText("")
        self.nameDefensePhysic.setText(QCoreApplication.translate("page_equip_abstract", u"\ubb3c\ub9ac \ubc29\uc5b4\ub825", None))
        self.statDefensePhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateDefensePhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconDefenseMagic.setText("")
        self.nameDefenseMagic.setText(QCoreApplication.translate("page_equip_abstract", u"\ub9c8\ubc95 \ubc29\uc5b4\ub825", None))
        self.statDefenseMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateDefenseMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalRate.setText("")
        self.nameCriticalRate.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85\ud0c0", None))
        self.statCriticalRate.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateCriticalRate.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalMult.setText("")
        self.nameCriticalMult.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85 \ud53c\ud574", None))
        self.statCriticalMult.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateCriticalMult.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalResist.setText("")
        self.nameCriticalResist.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85\ud0c0 \uc800\ud56d", None))
        self.statCriticalResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateCriticalResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalMultResist.setText("")
        self.nameCriticalMultResist.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85 \ud53c\ud574 \uc800\ud56d", None))
        self.statCriticalMultResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.rateCriticalMultResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconAll.setText("")
        self.nameAll.setText(QCoreApplication.translate("page_equip_abstract", u"\uc804\uccb4 \uc9c4\ud589\ub960", None))
        self.rateAll.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.label.setText(QCoreApplication.translate("page_equip_abstract", u"\uc815\ub82c \uae30\uc900", None))
        self.goal_rate_label_left.setText(QCoreApplication.translate("page_equip_abstract", u"\ubaa9\ud45c \ub2ec\uc131\ub960", None))
        self.goal_rate_label_right.setText(QCoreApplication.translate("page_equip_abstract", u"0%", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("page_equip_abstract", u"\ud45c\uc2dc\uc124\uc815", None))
        self.radio_equip_hide.setText(QCoreApplication.translate("page_equip_abstract", u"\ub7ad\ud06c\ub9cc \ud45c\uc2dc", None))
        self.radio_equip_show.setText(QCoreApplication.translate("page_equip_abstract", u"\uc7a5\ube44\uae4c\uc9c0 \ud45c\uc2dc", None))
        self.check_show_completed.setText(QCoreApplication.translate("page_equip_abstract", u"\ubaa9\ud45c \ub2ec\uc131 \uc0ac\ub3c4 \ubcf4\uc774\uae30", None))
    # retranslateUi

