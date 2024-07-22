# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_goal_with_stat.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SetGoalWithStat(object):
    def setupUi(self, SetGoalWithStat):
        if not SetGoalWithStat.objectName():
            SetGoalWithStat.setObjectName(u"SetGoalWithStat")
        SetGoalWithStat.resize(500, 320)
        self.centralwidget = QWidget(SetGoalWithStat)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(15)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Hp = QPushButton(self.centralwidget)
        self.Hp.setObjectName(u"Hp")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hp.sizePolicy().hasHeightForWidth())
        self.Hp.setSizePolicy(sizePolicy)
        self.Hp.setMinimumSize(QSize(170, 0))
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(13)
        self.Hp.setFont(font1)
        self.Hp.setIconSize(QSize(22, 22))
        self.Hp.setCheckable(True)

        self.gridLayout.addWidget(self.Hp, 0, 0, 1, 1)

        self.AttackPhysic = QPushButton(self.centralwidget)
        self.AttackPhysic.setObjectName(u"AttackPhysic")
        sizePolicy.setHeightForWidth(self.AttackPhysic.sizePolicy().hasHeightForWidth())
        self.AttackPhysic.setSizePolicy(sizePolicy)
        self.AttackPhysic.setMinimumSize(QSize(170, 0))
        self.AttackPhysic.setFont(font1)
        self.AttackPhysic.setIconSize(QSize(22, 22))
        self.AttackPhysic.setCheckable(True)

        self.gridLayout.addWidget(self.AttackPhysic, 1, 0, 1, 1)

        self.CriticalRate = QPushButton(self.centralwidget)
        self.CriticalRate.setObjectName(u"CriticalRate")
        sizePolicy.setHeightForWidth(self.CriticalRate.sizePolicy().hasHeightForWidth())
        self.CriticalRate.setSizePolicy(sizePolicy)
        self.CriticalRate.setMinimumSize(QSize(170, 0))
        self.CriticalRate.setFont(font1)
        self.CriticalRate.setIconSize(QSize(22, 22))
        self.CriticalRate.setCheckable(True)

        self.gridLayout.addWidget(self.CriticalRate, 1, 1, 1, 1)

        self.AttackMagic = QPushButton(self.centralwidget)
        self.AttackMagic.setObjectName(u"AttackMagic")
        sizePolicy.setHeightForWidth(self.AttackMagic.sizePolicy().hasHeightForWidth())
        self.AttackMagic.setSizePolicy(sizePolicy)
        self.AttackMagic.setMinimumSize(QSize(170, 0))
        self.AttackMagic.setFont(font1)
        self.AttackMagic.setIconSize(QSize(22, 22))
        self.AttackMagic.setCheckable(True)

        self.gridLayout.addWidget(self.AttackMagic, 2, 0, 1, 1)

        self.CriticalMult = QPushButton(self.centralwidget)
        self.CriticalMult.setObjectName(u"CriticalMult")
        sizePolicy.setHeightForWidth(self.CriticalMult.sizePolicy().hasHeightForWidth())
        self.CriticalMult.setSizePolicy(sizePolicy)
        self.CriticalMult.setMinimumSize(QSize(170, 0))
        self.CriticalMult.setFont(font1)
        self.CriticalMult.setIconSize(QSize(22, 22))
        self.CriticalMult.setCheckable(True)

        self.gridLayout.addWidget(self.CriticalMult, 2, 1, 1, 1)

        self.DefensePhysic = QPushButton(self.centralwidget)
        self.DefensePhysic.setObjectName(u"DefensePhysic")
        sizePolicy.setHeightForWidth(self.DefensePhysic.sizePolicy().hasHeightForWidth())
        self.DefensePhysic.setSizePolicy(sizePolicy)
        self.DefensePhysic.setMinimumSize(QSize(170, 0))
        self.DefensePhysic.setFont(font1)
        self.DefensePhysic.setIconSize(QSize(22, 22))
        self.DefensePhysic.setCheckable(True)

        self.gridLayout.addWidget(self.DefensePhysic, 3, 0, 1, 1)

        self.CriticalResist = QPushButton(self.centralwidget)
        self.CriticalResist.setObjectName(u"CriticalResist")
        sizePolicy.setHeightForWidth(self.CriticalResist.sizePolicy().hasHeightForWidth())
        self.CriticalResist.setSizePolicy(sizePolicy)
        self.CriticalResist.setMinimumSize(QSize(170, 0))
        self.CriticalResist.setFont(font1)
        self.CriticalResist.setIconSize(QSize(22, 22))
        self.CriticalResist.setCheckable(True)

        self.gridLayout.addWidget(self.CriticalResist, 3, 1, 1, 1)

        self.DefenseMagic = QPushButton(self.centralwidget)
        self.DefenseMagic.setObjectName(u"DefenseMagic")
        sizePolicy.setHeightForWidth(self.DefenseMagic.sizePolicy().hasHeightForWidth())
        self.DefenseMagic.setSizePolicy(sizePolicy)
        self.DefenseMagic.setMinimumSize(QSize(170, 0))
        self.DefenseMagic.setFont(font1)
        self.DefenseMagic.setIconSize(QSize(22, 22))
        self.DefenseMagic.setCheckable(True)

        self.gridLayout.addWidget(self.DefenseMagic, 4, 0, 1, 1)

        self.CriticalMultResist = QPushButton(self.centralwidget)
        self.CriticalMultResist.setObjectName(u"CriticalMultResist")
        sizePolicy.setHeightForWidth(self.CriticalMultResist.sizePolicy().hasHeightForWidth())
        self.CriticalMultResist.setSizePolicy(sizePolicy)
        self.CriticalMultResist.setMinimumSize(QSize(170, 0))
        self.CriticalMultResist.setFont(font1)
        self.CriticalMultResist.setIconSize(QSize(22, 22))
        self.CriticalMultResist.setCheckable(True)

        self.gridLayout.addWidget(self.CriticalMultResist, 4, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.over_max_rank_box = QCheckBox(self.centralwidget)
        self.over_max_rank_box.setObjectName(u"over_max_rank_box")
        font2 = QFont()
        font2.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font2.setPointSize(13)
        self.over_max_rank_box.setFont(font2)

        self.horizontalLayout.addWidget(self.over_max_rank_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SetGoalWithStat.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetGoalWithStat)

        QMetaObject.connectSlotsByName(SetGoalWithStat)
    # setupUi

    def retranslateUi(self, SetGoalWithStat):
        SetGoalWithStat.setWindowTitle(QCoreApplication.translate("SetGoalWithStat", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("SetGoalWithStat", u"\ub7ad\ud06c\uc791\uc73c\ub85c \uc62c\ub9ac\uace0 \uc2f6\uc740 \uc2a4\ud0ef\uc744 \uc804\ubd80 \uccb4\ud06c\ud574\uc8fc\uc138\uc694", None))
        self.Hp.setText(QCoreApplication.translate("SetGoalWithStat", u"\uccb4\ub825", None))
        self.AttackPhysic.setText(QCoreApplication.translate("SetGoalWithStat", u"\ubb3c\ub9ac \uacf5\uaca9\ub825", None))
        self.CriticalRate.setText(QCoreApplication.translate("SetGoalWithStat", u"\uce58\uba85\ud0c0", None))
        self.AttackMagic.setText(QCoreApplication.translate("SetGoalWithStat", u"\ub9c8\ubc95 \uacf5\uaca9\ub825", None))
        self.CriticalMult.setText(QCoreApplication.translate("SetGoalWithStat", u"\uce58\uba85 \ud53c\ud574", None))
        self.DefensePhysic.setText(QCoreApplication.translate("SetGoalWithStat", u"\ubb3c\ub9ac \ubc29\uc5b4\ub825", None))
        self.CriticalResist.setText(QCoreApplication.translate("SetGoalWithStat", u"\uce58\uba85\ud0c0 \uc800\ud56d", None))
        self.DefenseMagic.setText(QCoreApplication.translate("SetGoalWithStat", u"\ub9c8\ubc95 \ubc29\uc5b4\ub825", None))
        self.CriticalMultResist.setText(QCoreApplication.translate("SetGoalWithStat", u"\uce58\uba85 \ud53c\ud574 \uc800\ud56d", None))
        self.over_max_rank_box.setText(QCoreApplication.translate("SetGoalWithStat", u"\ub2e4\uc74c \ub7ad\ud06c \ud655\uc7a5 \ub300\ube44\ud558\uae30", None))
        self.save_btn.setText(QCoreApplication.translate("SetGoalWithStat", u"\ud655\uc778", None))
        self.cancel_btn.setText(QCoreApplication.translate("SetGoalWithStat", u"\ucde8\uc18c", None))
    # retranslateUi

