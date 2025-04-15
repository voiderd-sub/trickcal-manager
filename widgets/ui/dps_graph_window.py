# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dps_graph_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from widgets.wrapper.misc import ExtendedComboBox

class Ui_DpsGraphWindow(object):
    def setupUi(self, DpsGraphWindow):
        if not DpsGraphWindow.objectName():
            DpsGraphWindow.setObjectName(u"DpsGraphWindow")
        DpsGraphWindow.resize(999, 730)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(15)
        DpsGraphWindow.setFont(font)
        self.centralwidget = QWidget(DpsGraphWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(17)
        self.tabWidget.setFont(font1)
        self.summary = QWidget()
        self.summary.setObjectName(u"summary")
        self.horizontalLayout = QHBoxLayout(self.summary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.summary_canvas_container = QWidget(self.summary)
        self.summary_canvas_container.setObjectName(u"summary_canvas_container")
        self.verticalLayout_3 = QVBoxLayout(self.summary_canvas_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout.addWidget(self.summary_canvas_container)

        self.summary_option_container = QWidget(self.summary)
        self.summary_option_container.setObjectName(u"summary_option_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_option_container.sizePolicy().hasHeightForWidth())
        self.summary_option_container.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(14)
        self.summary_option_container.setFont(font2)
        self.verticalLayout_4 = QVBoxLayout(self.summary_option_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.summary_option_container)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_damage = QRadioButton(self.widget)
        self.radio_damage.setObjectName(u"radio_damage")
        self.radio_damage.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_damage)

        self.radio_contribution = QRadioButton(self.widget)
        self.radio_contribution.setObjectName(u"radio_contribution")

        self.horizontalLayout_2.addWidget(self.radio_contribution)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"ONE Mobile POP"])
        font3.setPointSize(13)
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"ONE Mobile POP"])
        font4.setPointSize(12)
        self.label.setFont(font4)
        self.label.setLineWidth(1)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setLineWidth(1)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.groupBox_2 = QGroupBox(self.summary_option_container)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_container_mean = QWidget(self.groupBox_2)
        self.label_container_mean.setObjectName(u"label_container_mean")
        self.horizontalLayout_9 = QHBoxLayout(self.label_container_mean)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.mean_is = QLabel(self.label_container_mean)
        self.mean_is.setObjectName(u"mean_is")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mean_is.sizePolicy().hasHeightForWidth())
        self.mean_is.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.mean_is)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.mean_val = QLabel(self.label_container_mean)
        self.mean_val.setObjectName(u"mean_val")
        self.mean_val.setFont(font3)
        self.mean_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.mean_val)


        self.verticalLayout_5.addWidget(self.label_container_mean)

        self.label_container_p90 = QWidget(self.groupBox_2)
        self.label_container_p90.setObjectName(u"label_container_p90")
        self.horizontalLayout_7 = QHBoxLayout(self.label_container_p90)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.p90_is = QLabel(self.label_container_p90)
        self.p90_is.setObjectName(u"p90_is")
        sizePolicy2.setHeightForWidth(self.p90_is.sizePolicy().hasHeightForWidth())
        self.p90_is.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.p90_is)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.p90_val = QLabel(self.label_container_p90)
        self.p90_val.setObjectName(u"p90_val")
        self.p90_val.setFont(font3)
        self.p90_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.p90_val)


        self.verticalLayout_5.addWidget(self.label_container_p90)

        self.label_container_p10 = QWidget(self.groupBox_2)
        self.label_container_p10.setObjectName(u"label_container_p10")
        self.horizontalLayout_8 = QHBoxLayout(self.label_container_p10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.p10_is = QLabel(self.label_container_p10)
        self.p10_is.setObjectName(u"p10_is")
        sizePolicy2.setHeightForWidth(self.p10_is.sizePolicy().hasHeightForWidth())
        self.p10_is.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.p10_is)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.p10_val = QLabel(self.label_container_p10)
        self.p10_val.setObjectName(u"p10_val")
        self.p10_val.setFont(font3)
        self.p10_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.p10_val)


        self.verticalLayout_5.addWidget(self.label_container_p10)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 449, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.summary_option_container)

        self.tabWidget.addTab(self.summary, "")
        self.hero_analysis = QWidget()
        self.hero_analysis.setObjectName(u"hero_analysis")
        self.horizontalLayout_6 = QHBoxLayout(self.hero_analysis)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.analysis_canvas_container = QWidget(self.hero_analysis)
        self.analysis_canvas_container.setObjectName(u"analysis_canvas_container")
        self.verticalLayout_11 = QVBoxLayout(self.analysis_canvas_container)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.horizontalLayout_6.addWidget(self.analysis_canvas_container)

        self.analysis_option_container = QWidget(self.hero_analysis)
        self.analysis_option_container.setObjectName(u"analysis_option_container")
        sizePolicy.setHeightForWidth(self.analysis_option_container.sizePolicy().hasHeightForWidth())
        self.analysis_option_container.setSizePolicy(sizePolicy)
        self.analysis_option_container.setFont(font2)
        self.verticalLayout_9 = QVBoxLayout(self.analysis_option_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.hero_name_combobox = ExtendedComboBox(self.analysis_option_container)
        self.hero_name_combobox.setObjectName(u"hero_name_combobox")
        self.hero_name_combobox.setFont(font)

        self.verticalLayout_9.addWidget(self.hero_name_combobox)

        self.verticalSpacer_16 = QSpacerItem(20, 449, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_16)


        self.horizontalLayout_6.addWidget(self.analysis_option_container)

        self.tabWidget.addTab(self.hero_analysis, "")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.horizontalLayout_3 = QHBoxLayout(self.tables)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.tables)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tables, "")
        self.builds = QWidget()
        self.builds.setObjectName(u"builds")
        self.tabWidget.addTab(self.builds, "")

        self.verticalLayout.addWidget(self.tabWidget)

        DpsGraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DpsGraphWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DpsGraphWindow)
    # setupUi

    def retranslateUi(self, DpsGraphWindow):
        DpsGraphWindow.setWindowTitle(QCoreApplication.translate("DpsGraphWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("DpsGraphWindow", u"\ud45c\uc2dc\ud560 \uac12", None))
        self.radio_damage.setText(QCoreApplication.translate("DpsGraphWindow", u"\ub51c\ub7c9", None))
        self.radio_contribution.setText(QCoreApplication.translate("DpsGraphWindow", u"\uae30\uc5ec\ub3c4", None))
        self.label_3.setText(QCoreApplication.translate("DpsGraphWindow", u"\u203b\uae30\uc5ec\ub3c4\ub780?", None))
        self.label.setText(QCoreApplication.translate("DpsGraphWindow", u"\ud574\ub2f9 \uc0ac\ub3c4\ub97c \ub371\uc5d0\uc11c \ube7c\uba74, \uc804\uccb4 \ub51c\ub7c9\uc774 \uba87%\ub098 \ub0b4\ub824\uac00\ub294\uc9c0 \ubcf4\uc5ec\uc8fc\ub294 \uc218\uce58", None))
        self.label_4.setText(QCoreApplication.translate("DpsGraphWindow", u"\uae30\uc5ec\ub3c4\uac00 \ub192\uc744\uc218\ub85d \uc911\uc694\ud55c \uc0ac\ub3c4!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DpsGraphWindow", u"\ucd1d \ub300\ubbf8\uc9c0", None))
        self.mean_is.setText(QCoreApplication.translate("DpsGraphWindow", u"\ud3c9\uade0", None))
        self.mean_val.setText(QCoreApplication.translate("DpsGraphWindow", u"100", None))
        self.p90_is.setText(QCoreApplication.translate("DpsGraphWindow", u"\uc0c1\uc704 10%", None))
        self.p90_val.setText(QCoreApplication.translate("DpsGraphWindow", u"100", None))
        self.p10_is.setText(QCoreApplication.translate("DpsGraphWindow", u"\ud558\uc704 10%", None))
        self.p10_val.setText(QCoreApplication.translate("DpsGraphWindow", u"100", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary), QCoreApplication.translate("DpsGraphWindow", u"\uc804\uccb4 \uc694\uc57d", None))
        self.hero_name_combobox.setPlaceholderText(QCoreApplication.translate("DpsGraphWindow", u"\uc0ac\ub3c4 \uc120\ud0dd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hero_analysis), QCoreApplication.translate("DpsGraphWindow", u"\uc0ac\ub3c4\ubcc4 \ubd84\uc11d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("DpsGraphWindow", u"\ud45c\ub85c \ubcf4\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.builds), QCoreApplication.translate("DpsGraphWindow", u"\ube4c\ub4dc \ube44\uad50", None))
    # retranslateUi

