# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combobox_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_combobox_editor(object):
    def setupUi(self, combobox_editor):
        if not combobox_editor.objectName():
            combobox_editor.setObjectName(u"combobox_editor")
        combobox_editor.resize(600, 400)
        self.centralwidget = QWidget(combobox_editor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(14)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        font1 = QFont()
        font1.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font1.setPointSize(13)
        self.table.setFont(font1)

        self.verticalLayout.addWidget(self.table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(37, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.up_btn = QPushButton(self.centralwidget)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.up_btn)

        self.down_btn = QPushButton(self.centralwidget)
        self.down_btn.setObjectName(u"down_btn")
        self.down_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.down_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 23, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.add_btn)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_5 = QSpacerItem(37, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        combobox_editor.setCentralWidget(self.centralwidget)

        self.retranslateUi(combobox_editor)

        QMetaObject.connectSlotsByName(combobox_editor)
    # setupUi

    def retranslateUi(self, combobox_editor):
        combobox_editor.setWindowTitle(QCoreApplication.translate("combobox_editor", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("combobox_editor", u"\uc774\ub984\uc73c\ub85c \ud55c\uae00, \uc601\uc5b4, \ub744\uc5b4\uc4f0\uae30, \uc22b\uc790\ub9cc \uc785\ub825 \uac00\ub2a5\n"
" \uc911\ubcf5\ub41c \uc774\ub984 \uc0ac\uc6a9 \uc2dc \uc800\uc7a5 \ubd88\uac00", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("combobox_editor", u"\ud604\uc7ac \uc774\ub984", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("combobox_editor", u"\ubcc0\uacbd \ud6c4 \uc774\ub984", None));
        self.up_btn.setText(QCoreApplication.translate("combobox_editor", u"\u25b2", None))
        self.down_btn.setText(QCoreApplication.translate("combobox_editor", u"\u25bc", None))
        self.add_btn.setText(QCoreApplication.translate("combobox_editor", u"\ucd94\uac00", None))
        self.delete_btn.setText(QCoreApplication.translate("combobox_editor", u"\uc0ad\uc81c", None))
        self.save_btn.setText(QCoreApplication.translate("combobox_editor", u"\uc800\uc7a5", None))
        self.cancel_btn.setText(QCoreApplication.translate("combobox_editor", u"\ucde8\uc18c", None))
    # retranslateUi

