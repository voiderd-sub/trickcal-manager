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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

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
        font.setPointSize(20)
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
        self.horizontalLayout = QHBoxLayout(self.containerHp)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.iconHp = QLabel(self.containerHp)
        self.iconHp.setObjectName(u"iconHp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconHp.sizePolicy().hasHeightForWidth())
        self.iconHp.setSizePolicy(sizePolicy1)
        self.iconHp.setMinimumSize(QSize(40, 40))
        self.iconHp.setMaximumSize(QSize(40, 40))
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
        self.nameHp.setFont(font1)
        self.nameHp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.nameHp)

        self.statHp = QLabel(self.containerHp)
        self.statHp.setObjectName(u"statHp")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statHp.sizePolicy().hasHeightForWidth())
        self.statHp.setSizePolicy(sizePolicy3)
        self.statHp.setFont(font1)
        self.statHp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.statHp)


        self.verticalLayout_2.addWidget(self.containerHp)

        self.containerAttackPhysic = QWidget(self.groupBox)
        self.containerAttackPhysic.setObjectName(u"containerAttackPhysic")
        self.containerAttackPhysic.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.containerAttackPhysic)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.iconAttackPhysic = QLabel(self.containerAttackPhysic)
        self.iconAttackPhysic.setObjectName(u"iconAttackPhysic")
        sizePolicy1.setHeightForWidth(self.iconAttackPhysic.sizePolicy().hasHeightForWidth())
        self.iconAttackPhysic.setSizePolicy(sizePolicy1)
        self.iconAttackPhysic.setMinimumSize(QSize(40, 40))
        self.iconAttackPhysic.setMaximumSize(QSize(40, 40))
        self.iconAttackPhysic.setFont(font1)
        self.iconAttackPhysic.setScaledContents(True)
        self.iconAttackPhysic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.iconAttackPhysic)

        self.nameAttackPhysic = QLabel(self.containerAttackPhysic)
        self.nameAttackPhysic.setObjectName(u"nameAttackPhysic")
        sizePolicy2.setHeightForWidth(self.nameAttackPhysic.sizePolicy().hasHeightForWidth())
        self.nameAttackPhysic.setSizePolicy(sizePolicy2)
        self.nameAttackPhysic.setFont(font1)
        self.nameAttackPhysic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.nameAttackPhysic)

        self.statAttackPhysic = QLabel(self.containerAttackPhysic)
        self.statAttackPhysic.setObjectName(u"statAttackPhysic")
        sizePolicy3.setHeightForWidth(self.statAttackPhysic.sizePolicy().hasHeightForWidth())
        self.statAttackPhysic.setSizePolicy(sizePolicy3)
        self.statAttackPhysic.setFont(font1)
        self.statAttackPhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.statAttackPhysic)


        self.verticalLayout_2.addWidget(self.containerAttackPhysic)

        self.containerAttackMagic = QWidget(self.groupBox)
        self.containerAttackMagic.setObjectName(u"containerAttackMagic")
        self.containerAttackMagic.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.containerAttackMagic)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.iconAttackMagic = QLabel(self.containerAttackMagic)
        self.iconAttackMagic.setObjectName(u"iconAttackMagic")
        sizePolicy1.setHeightForWidth(self.iconAttackMagic.sizePolicy().hasHeightForWidth())
        self.iconAttackMagic.setSizePolicy(sizePolicy1)
        self.iconAttackMagic.setMinimumSize(QSize(40, 40))
        self.iconAttackMagic.setMaximumSize(QSize(40, 40))
        self.iconAttackMagic.setFont(font1)
        self.iconAttackMagic.setScaledContents(True)
        self.iconAttackMagic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.iconAttackMagic)

        self.nameAttackMagic = QLabel(self.containerAttackMagic)
        self.nameAttackMagic.setObjectName(u"nameAttackMagic")
        sizePolicy2.setHeightForWidth(self.nameAttackMagic.sizePolicy().hasHeightForWidth())
        self.nameAttackMagic.setSizePolicy(sizePolicy2)
        self.nameAttackMagic.setFont(font1)
        self.nameAttackMagic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.nameAttackMagic)

        self.statAttackMagic = QLabel(self.containerAttackMagic)
        self.statAttackMagic.setObjectName(u"statAttackMagic")
        sizePolicy3.setHeightForWidth(self.statAttackMagic.sizePolicy().hasHeightForWidth())
        self.statAttackMagic.setSizePolicy(sizePolicy3)
        self.statAttackMagic.setFont(font1)
        self.statAttackMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.statAttackMagic)


        self.verticalLayout_2.addWidget(self.containerAttackMagic)

        self.containerDefensePhysic = QWidget(self.groupBox)
        self.containerDefensePhysic.setObjectName(u"containerDefensePhysic")
        self.containerDefensePhysic.setFont(font1)
        self.horizontalLayout_9 = QHBoxLayout(self.containerDefensePhysic)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.iconDefensePhysic = QLabel(self.containerDefensePhysic)
        self.iconDefensePhysic.setObjectName(u"iconDefensePhysic")
        sizePolicy1.setHeightForWidth(self.iconDefensePhysic.sizePolicy().hasHeightForWidth())
        self.iconDefensePhysic.setSizePolicy(sizePolicy1)
        self.iconDefensePhysic.setMinimumSize(QSize(40, 40))
        self.iconDefensePhysic.setMaximumSize(QSize(40, 40))
        self.iconDefensePhysic.setFont(font1)
        self.iconDefensePhysic.setScaledContents(True)
        self.iconDefensePhysic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.iconDefensePhysic)

        self.nameDefensePhysic = QLabel(self.containerDefensePhysic)
        self.nameDefensePhysic.setObjectName(u"nameDefensePhysic")
        sizePolicy2.setHeightForWidth(self.nameDefensePhysic.sizePolicy().hasHeightForWidth())
        self.nameDefensePhysic.setSizePolicy(sizePolicy2)
        self.nameDefensePhysic.setFont(font1)
        self.nameDefensePhysic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.nameDefensePhysic)

        self.statDefensePhysic = QLabel(self.containerDefensePhysic)
        self.statDefensePhysic.setObjectName(u"statDefensePhysic")
        sizePolicy3.setHeightForWidth(self.statDefensePhysic.sizePolicy().hasHeightForWidth())
        self.statDefensePhysic.setSizePolicy(sizePolicy3)
        self.statDefensePhysic.setFont(font1)
        self.statDefensePhysic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.statDefensePhysic)


        self.verticalLayout_2.addWidget(self.containerDefensePhysic)

        self.containerDefenseMagic = QWidget(self.groupBox)
        self.containerDefenseMagic.setObjectName(u"containerDefenseMagic")
        self.containerDefenseMagic.setFont(font1)
        self.horizontalLayout_10 = QHBoxLayout(self.containerDefenseMagic)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.iconDefenseMagic = QLabel(self.containerDefenseMagic)
        self.iconDefenseMagic.setObjectName(u"iconDefenseMagic")
        sizePolicy1.setHeightForWidth(self.iconDefenseMagic.sizePolicy().hasHeightForWidth())
        self.iconDefenseMagic.setSizePolicy(sizePolicy1)
        self.iconDefenseMagic.setMinimumSize(QSize(40, 40))
        self.iconDefenseMagic.setMaximumSize(QSize(40, 40))
        self.iconDefenseMagic.setFont(font1)
        self.iconDefenseMagic.setScaledContents(True)
        self.iconDefenseMagic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.iconDefenseMagic)

        self.nameDefenseMagic = QLabel(self.containerDefenseMagic)
        self.nameDefenseMagic.setObjectName(u"nameDefenseMagic")
        sizePolicy2.setHeightForWidth(self.nameDefenseMagic.sizePolicy().hasHeightForWidth())
        self.nameDefenseMagic.setSizePolicy(sizePolicy2)
        self.nameDefenseMagic.setFont(font1)
        self.nameDefenseMagic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.nameDefenseMagic)

        self.statDefenseMagic = QLabel(self.containerDefenseMagic)
        self.statDefenseMagic.setObjectName(u"statDefenseMagic")
        sizePolicy3.setHeightForWidth(self.statDefenseMagic.sizePolicy().hasHeightForWidth())
        self.statDefenseMagic.setSizePolicy(sizePolicy3)
        self.statDefenseMagic.setFont(font1)
        self.statDefenseMagic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.statDefenseMagic)


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
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.iconCriticalRate = QLabel(self.containerCriticalRate)
        self.iconCriticalRate.setObjectName(u"iconCriticalRate")
        sizePolicy1.setHeightForWidth(self.iconCriticalRate.sizePolicy().hasHeightForWidth())
        self.iconCriticalRate.setSizePolicy(sizePolicy1)
        self.iconCriticalRate.setMinimumSize(QSize(40, 40))
        self.iconCriticalRate.setMaximumSize(QSize(40, 40))
        self.iconCriticalRate.setFont(font1)
        self.iconCriticalRate.setScaledContents(True)
        self.iconCriticalRate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.iconCriticalRate)

        self.nameCriticalRate = QLabel(self.containerCriticalRate)
        self.nameCriticalRate.setObjectName(u"nameCriticalRate")
        sizePolicy2.setHeightForWidth(self.nameCriticalRate.sizePolicy().hasHeightForWidth())
        self.nameCriticalRate.setSizePolicy(sizePolicy2)
        self.nameCriticalRate.setFont(font1)
        self.nameCriticalRate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.nameCriticalRate)

        self.statCriticalRate = QLabel(self.containerCriticalRate)
        self.statCriticalRate.setObjectName(u"statCriticalRate")
        sizePolicy3.setHeightForWidth(self.statCriticalRate.sizePolicy().hasHeightForWidth())
        self.statCriticalRate.setSizePolicy(sizePolicy3)
        self.statCriticalRate.setFont(font1)
        self.statCriticalRate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.statCriticalRate)


        self.verticalLayout.addWidget(self.containerCriticalRate)

        self.containerCriticalMult = QWidget(self.groupBox)
        self.containerCriticalMult.setObjectName(u"containerCriticalMult")
        self.containerCriticalMult.setFont(font1)
        self.horizontalLayout_12 = QHBoxLayout(self.containerCriticalMult)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.iconCriticalMult = QLabel(self.containerCriticalMult)
        self.iconCriticalMult.setObjectName(u"iconCriticalMult")
        sizePolicy1.setHeightForWidth(self.iconCriticalMult.sizePolicy().hasHeightForWidth())
        self.iconCriticalMult.setSizePolicy(sizePolicy1)
        self.iconCriticalMult.setMinimumSize(QSize(40, 40))
        self.iconCriticalMult.setMaximumSize(QSize(40, 40))
        self.iconCriticalMult.setFont(font1)
        self.iconCriticalMult.setScaledContents(True)
        self.iconCriticalMult.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.iconCriticalMult)

        self.nameCriticalMult = QLabel(self.containerCriticalMult)
        self.nameCriticalMult.setObjectName(u"nameCriticalMult")
        sizePolicy2.setHeightForWidth(self.nameCriticalMult.sizePolicy().hasHeightForWidth())
        self.nameCriticalMult.setSizePolicy(sizePolicy2)
        self.nameCriticalMult.setFont(font1)
        self.nameCriticalMult.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.nameCriticalMult)

        self.statCriticalMult = QLabel(self.containerCriticalMult)
        self.statCriticalMult.setObjectName(u"statCriticalMult")
        sizePolicy3.setHeightForWidth(self.statCriticalMult.sizePolicy().hasHeightForWidth())
        self.statCriticalMult.setSizePolicy(sizePolicy3)
        self.statCriticalMult.setFont(font1)
        self.statCriticalMult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.statCriticalMult)


        self.verticalLayout.addWidget(self.containerCriticalMult)

        self.containerCriticalResist = QWidget(self.groupBox)
        self.containerCriticalResist.setObjectName(u"containerCriticalResist")
        self.containerCriticalResist.setFont(font1)
        self.horizontalLayout_13 = QHBoxLayout(self.containerCriticalResist)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.iconCriticalResist = QLabel(self.containerCriticalResist)
        self.iconCriticalResist.setObjectName(u"iconCriticalResist")
        sizePolicy1.setHeightForWidth(self.iconCriticalResist.sizePolicy().hasHeightForWidth())
        self.iconCriticalResist.setSizePolicy(sizePolicy1)
        self.iconCriticalResist.setMinimumSize(QSize(40, 40))
        self.iconCriticalResist.setMaximumSize(QSize(40, 40))
        self.iconCriticalResist.setFont(font1)
        self.iconCriticalResist.setScaledContents(True)
        self.iconCriticalResist.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.iconCriticalResist)

        self.nameCriticalResist = QLabel(self.containerCriticalResist)
        self.nameCriticalResist.setObjectName(u"nameCriticalResist")
        sizePolicy2.setHeightForWidth(self.nameCriticalResist.sizePolicy().hasHeightForWidth())
        self.nameCriticalResist.setSizePolicy(sizePolicy2)
        self.nameCriticalResist.setFont(font1)
        self.nameCriticalResist.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.nameCriticalResist)

        self.statCriticalResist = QLabel(self.containerCriticalResist)
        self.statCriticalResist.setObjectName(u"statCriticalResist")
        sizePolicy3.setHeightForWidth(self.statCriticalResist.sizePolicy().hasHeightForWidth())
        self.statCriticalResist.setSizePolicy(sizePolicy3)
        self.statCriticalResist.setFont(font1)
        self.statCriticalResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.statCriticalResist)


        self.verticalLayout.addWidget(self.containerCriticalResist)

        self.containerCriticalMultResist = QWidget(self.groupBox)
        self.containerCriticalMultResist.setObjectName(u"containerCriticalMultResist")
        self.containerCriticalMultResist.setFont(font1)
        self.horizontalLayout_14 = QHBoxLayout(self.containerCriticalMultResist)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.iconCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.iconCriticalMultResist.setObjectName(u"iconCriticalMultResist")
        sizePolicy1.setHeightForWidth(self.iconCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.iconCriticalMultResist.setSizePolicy(sizePolicy1)
        self.iconCriticalMultResist.setMinimumSize(QSize(40, 40))
        self.iconCriticalMultResist.setMaximumSize(QSize(40, 40))
        self.iconCriticalMultResist.setFont(font1)
        self.iconCriticalMultResist.setScaledContents(True)
        self.iconCriticalMultResist.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.iconCriticalMultResist)

        self.nameCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.nameCriticalMultResist.setObjectName(u"nameCriticalMultResist")
        sizePolicy2.setHeightForWidth(self.nameCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.nameCriticalMultResist.setSizePolicy(sizePolicy2)
        self.nameCriticalMultResist.setFont(font1)
        self.nameCriticalMultResist.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.nameCriticalMultResist)

        self.statCriticalMultResist = QLabel(self.containerCriticalMultResist)
        self.statCriticalMultResist.setObjectName(u"statCriticalMultResist")
        sizePolicy3.setHeightForWidth(self.statCriticalMultResist.sizePolicy().hasHeightForWidth())
        self.statCriticalMultResist.setSizePolicy(sizePolicy3)
        self.statCriticalMultResist.setFont(font1)
        self.statCriticalMultResist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.statCriticalMultResist)


        self.verticalLayout.addWidget(self.containerCriticalMultResist)

        self.containerAll = QWidget(self.groupBox)
        self.containerAll.setObjectName(u"containerAll")
        self.containerAll.setFont(font1)
        self.horizontalLayout_16 = QHBoxLayout(self.containerAll)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.iconAll = QLabel(self.containerAll)
        self.iconAll.setObjectName(u"iconAll")
        sizePolicy1.setHeightForWidth(self.iconAll.sizePolicy().hasHeightForWidth())
        self.iconAll.setSizePolicy(sizePolicy1)
        self.iconAll.setMinimumSize(QSize(40, 40))
        self.iconAll.setMaximumSize(QSize(40, 40))
        self.iconAll.setFont(font1)
        self.iconAll.setScaledContents(True)
        self.iconAll.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.iconAll)

        self.nameAll = QLabel(self.containerAll)
        self.nameAll.setObjectName(u"nameAll")
        sizePolicy2.setHeightForWidth(self.nameAll.sizePolicy().hasHeightForWidth())
        self.nameAll.setSizePolicy(sizePolicy2)
        self.nameAll.setFont(font1)
        self.nameAll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.nameAll)

        self.statAll = QLabel(self.containerAll)
        self.statAll.setObjectName(u"statAll")
        sizePolicy3.setHeightForWidth(self.statAll.sizePolicy().hasHeightForWidth())
        self.statAll.setSizePolicy(sizePolicy3)
        self.statAll.setFont(font1)
        self.statAll.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.statAll)


        self.verticalLayout.addWidget(self.containerAll)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.widget = QWidget(page_equip_abstract)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget_13 = QWidget(self.widget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(30, 30, 461, 40))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label)

        self.comboBox = QComboBox(self.widget_13)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_15.addWidget(self.comboBox)


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
        self.iconAttackPhysic.setText("")
        self.nameAttackPhysic.setText(QCoreApplication.translate("page_equip_abstract", u"\ubb3c\ub9ac \uacf5\uaca9\ub825", None))
        self.statAttackPhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconAttackMagic.setText("")
        self.nameAttackMagic.setText(QCoreApplication.translate("page_equip_abstract", u"\ub9c8\ubc95 \uacf5\uaca9\ub825", None))
        self.statAttackMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconDefensePhysic.setText("")
        self.nameDefensePhysic.setText(QCoreApplication.translate("page_equip_abstract", u"\ubb3c\ub9ac \ubc29\uc5b4\ub825", None))
        self.statDefensePhysic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconDefenseMagic.setText("")
        self.nameDefenseMagic.setText(QCoreApplication.translate("page_equip_abstract", u"\ub9c8\ubc95 \ubc29\uc5b4\ub825", None))
        self.statDefenseMagic.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalRate.setText("")
        self.nameCriticalRate.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85\ud0c0", None))
        self.statCriticalRate.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalMult.setText("")
        self.nameCriticalMult.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85 \ud53c\ud574", None))
        self.statCriticalMult.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalResist.setText("")
        self.nameCriticalResist.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85\ud0c0 \uc800\ud56d", None))
        self.statCriticalResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconCriticalMultResist.setText("")
        self.nameCriticalMultResist.setText(QCoreApplication.translate("page_equip_abstract", u"\uce58\uba85 \ud53c\ud574 \uc800\ud56d", None))
        self.statCriticalMultResist.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.iconAll.setText("")
        self.nameAll.setText(QCoreApplication.translate("page_equip_abstract", u"\uc804\uccb4 \uc9c4\ud589\ub960", None))
        self.statAll.setText(QCoreApplication.translate("page_equip_abstract", u"0", None))
        self.label.setText(QCoreApplication.translate("page_equip_abstract", u"\ubcf4\uae30 \uc124\uc815", None))
    # retranslateUi

