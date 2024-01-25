# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_AccountSettings(object):
    def setupUi(self, AccountSettings):
        if not AccountSettings.objectName():
            AccountSettings.setObjectName(u"AccountSettings")
        AccountSettings.resize(490, 400)
        self.centralwidget = QWidget(AccountSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.account_list = QListWidget(self.centralwidget)
        self.account_list.setObjectName(u"account_list")

        self.verticalLayout.addWidget(self.account_list)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.account_name_line = QLineEdit(self.centralwidget)
        self.account_name_line.setObjectName(u"account_name_line")

        self.horizontalLayout_2.addWidget(self.account_name_line)

        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout_2.addWidget(self.add_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.verticalLayout.addWidget(self.delete_btn)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        AccountSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountSettings)

        QMetaObject.connectSlotsByName(AccountSettings)
    # setupUi

    def retranslateUi(self, AccountSettings):
        AccountSettings.setWindowTitle(QCoreApplication.translate("AccountSettings", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("AccountSettings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\uacc4\uc815 \ucd94\uac00</span> : '\uacc4\uc815 \uc774\ub984 \uc785\ub825' \ub780\uc5d0 \uc774\ub984 \uc785\ub825 \ud6c4 \ucd94\uac00 \ubc84\ud2bc \ud074\ub9ad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\uacc4\uc815 \uc774\ub984 \ubcc0"
                        "\uacbd</span> : \ub9ac\uc2a4\ud2b8\uc5d0\uc11c \ub354\ube14 \ud074\ub9ad \ud6c4 \uc218\uc815</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\uacc4\uc815 \uc0ad\uc81c</span> : \ub9ac\uc2a4\ud2b8\uc5d0\uc11c \uc0ad\uc81c\ud560 \uacc4\uc815\uc758 \uccb4\ud06c\ubc15\uc2a4 \uc120\ud0dd \ud6c4 \uc0ad\uc81c \ubc84\ud2bc \ud074\ub9ad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc800\uc7a5 \ubc84\ud2bc\uc744 \ub20c\ub7ec\uc57c\ub9cc \ubc18\uc601\ub429\ub2c8\ub2e4.</p></body></html>", None))
        self.account_name_line.setText("")
        self.account_name_line.setPlaceholderText(QCoreApplication.translate("AccountSettings", u"\uacc4\uc815 \uc774\ub984 \uc785\ub825 (\ud55c\uae00, \uc601\uc5b4, \uc22b\uc790, \ub744\uc5b4\uc4f0\uae30\ub9cc \uc785\ub825 \uac00\ub2a5)", None))
        self.add_btn.setText(QCoreApplication.translate("AccountSettings", u"\uacc4\uc815 \ucd94\uac00", None))
        self.delete_btn.setText(QCoreApplication.translate("AccountSettings", u"\uc120\ud0dd\ud55c \uacc4\uc815 \uc0ad\uc81c", None))
        self.save_btn.setText(QCoreApplication.translate("AccountSettings", u"\uc800\uc7a5", None))
        self.cancel_btn.setText(QCoreApplication.translate("AccountSettings", u"\ucde8\uc18c", None))
    # retranslateUi

