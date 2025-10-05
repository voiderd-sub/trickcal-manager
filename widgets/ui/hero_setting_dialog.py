# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hero_setting_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_HeroSettingDialog(object):
    def setupUi(self, HeroSettingDialog):
        if not HeroSettingDialog.objectName():
            HeroSettingDialog.setObjectName(u"HeroSettingDialog")
        HeroSettingDialog.resize(480, 720)
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(12)
        HeroSettingDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(HeroSettingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hero_name_label = QLabel(HeroSettingDialog)
        self.hero_name_label.setObjectName(u"hero_name_label")
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.hero_name_label.setFont(font1)
        self.hero_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.hero_name_label)

        self.tabWidget = QTabWidget(HeroSettingDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.detailed_settings_tab = QWidget()
        self.detailed_settings_tab.setObjectName(u"detailed_settings_tab")
        self.verticalLayout_2 = QVBoxLayout(self.detailed_settings_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.character_info_group = QGroupBox(self.detailed_settings_tab)
        self.character_info_group.setObjectName(u"character_info_group")
        self.formLayout = QFormLayout(self.character_info_group)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.character_info_group)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.char_level_spinbox = QSpinBox(self.character_info_group)
        self.char_level_spinbox.setObjectName(u"char_level_spinbox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.char_level_spinbox)

        self.label_2 = QLabel(self.character_info_group)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.char_grade_spinbox = QSpinBox(self.character_info_group)
        self.char_grade_spinbox.setObjectName(u"char_grade_spinbox")
        self.char_grade_spinbox.setMinimum(1)
        self.char_grade_spinbox.setMaximum(6)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.char_grade_spinbox)


        self.verticalLayout_2.addWidget(self.character_info_group)

        self.aside_info_group = QGroupBox(self.detailed_settings_tab)
        self.aside_info_group.setObjectName(u"aside_info_group")
        self.formLayout_2 = QFormLayout(self.aside_info_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.aside_info_group)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.aside_level_spinbox = QSpinBox(self.aside_info_group)
        self.aside_level_spinbox.setObjectName(u"aside_level_spinbox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.aside_level_spinbox)

        self.label_4 = QLabel(self.aside_info_group)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.aside_grade_spinbox = QSpinBox(self.aside_info_group)
        self.aside_grade_spinbox.setObjectName(u"aside_grade_spinbox")
        self.aside_grade_spinbox.setMaximum(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.aside_grade_spinbox)


        self.verticalLayout_2.addWidget(self.aside_info_group)

        self.equipment_info_group = QGroupBox(self.detailed_settings_tab)
        self.equipment_info_group.setObjectName(u"equipment_info_group")
        self.verticalLayout_3 = QVBoxLayout(self.equipment_info_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.equipment_info_group)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.equip_rank_spinbox = QSpinBox(self.equipment_info_group)
        self.equip_rank_spinbox.setObjectName(u"equip_rank_spinbox")

        self.horizontalLayout_2.addWidget(self.equip_rank_spinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.equip1_checkbox = QCheckBox(self.equipment_info_group)
        self.equip1_checkbox.setObjectName(u"equip1_checkbox")

        self.gridLayout_3.addWidget(self.equip1_checkbox, 0, 0, 1, 1)

        self.equip1_level_spinbox = QSpinBox(self.equipment_info_group)
        self.equip1_level_spinbox.setObjectName(u"equip1_level_spinbox")

        self.gridLayout_3.addWidget(self.equip1_level_spinbox, 0, 1, 1, 1)

        self.equip2_checkbox = QCheckBox(self.equipment_info_group)
        self.equip2_checkbox.setObjectName(u"equip2_checkbox")

        self.gridLayout_3.addWidget(self.equip2_checkbox, 1, 0, 1, 1)

        self.equip2_level_spinbox = QSpinBox(self.equipment_info_group)
        self.equip2_level_spinbox.setObjectName(u"equip2_level_spinbox")

        self.gridLayout_3.addWidget(self.equip2_level_spinbox, 1, 1, 1, 1)

        self.equip3_checkbox = QCheckBox(self.equipment_info_group)
        self.equip3_checkbox.setObjectName(u"equip3_checkbox")

        self.gridLayout_3.addWidget(self.equip3_checkbox, 2, 0, 1, 1)

        self.equip3_level_spinbox = QSpinBox(self.equipment_info_group)
        self.equip3_level_spinbox.setObjectName(u"equip3_level_spinbox")

        self.gridLayout_3.addWidget(self.equip3_level_spinbox, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addWidget(self.equipment_info_group)

        self.affection_group = QGroupBox(self.detailed_settings_tab)
        self.affection_group.setObjectName(u"affection_group")
        self.formLayout_3 = QFormLayout(self.affection_group)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.affection_group)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.affection_level_spinbox = QSpinBox(self.affection_group)
        self.affection_level_spinbox.setObjectName(u"affection_level_spinbox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.affection_level_spinbox)


        self.verticalLayout_2.addWidget(self.affection_group)

        self.apostle_group = QGroupBox(self.detailed_settings_tab)
        self.apostle_group.setObjectName(u"apostle_group")
        self.horizontalLayout_3 = QHBoxLayout(self.apostle_group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apostle_none_radio = QRadioButton(self.apostle_group)
        self.apostle_none_radio.setObjectName(u"apostle_none_radio")
        self.apostle_none_radio.setChecked(True)

        self.horizontalLayout_3.addWidget(self.apostle_none_radio)

        self.apostle_gather_radio = QRadioButton(self.apostle_group)
        self.apostle_gather_radio.setObjectName(u"apostle_gather_radio")

        self.horizontalLayout_3.addWidget(self.apostle_gather_radio)

        self.apostle_shine_radio = QRadioButton(self.apostle_group)
        self.apostle_shine_radio.setObjectName(u"apostle_shine_radio")

        self.horizontalLayout_3.addWidget(self.apostle_shine_radio)


        self.verticalLayout_2.addWidget(self.apostle_group)

        self.board_stat_group = QGroupBox(self.detailed_settings_tab)
        self.board_stat_group.setObjectName(u"board_stat_group")
        self.formLayout_4 = QFormLayout(self.board_stat_group)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_7 = QLabel(self.board_stat_group)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.personal_board_label = QLabel(self.board_stat_group)
        self.personal_board_label.setObjectName(u"personal_board_label")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.personal_board_label)

        self.label_8 = QLabel(self.board_stat_group)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.global_board_label = QLabel(self.board_stat_group)
        self.global_board_label.setObjectName(u"global_board_label")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.global_board_label)


        self.verticalLayout_2.addWidget(self.board_stat_group)

        self.skill_group = QGroupBox(self.detailed_settings_tab)
        self.skill_group.setObjectName(u"skill_group")
        self.gridLayout_4 = QGridLayout(self.skill_group)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lower_skill_label = QLabel(self.skill_group)
        self.lower_skill_label.setObjectName(u"lower_skill_label")

        self.gridLayout_4.addWidget(self.lower_skill_label, 0, 0, 1, 1)

        self.lower_skill_spinbox = QSpinBox(self.skill_group)
        self.lower_skill_spinbox.setObjectName(u"lower_skill_spinbox")
        self.lower_skill_spinbox.setMinimum(1)
        self.lower_skill_spinbox.setMaximum(10)

        self.gridLayout_4.addWidget(self.lower_skill_spinbox, 0, 1, 1, 1)

        self.upper_skill_label = QLabel(self.skill_group)
        self.upper_skill_label.setObjectName(u"upper_skill_label")

        self.gridLayout_4.addWidget(self.upper_skill_label, 1, 0, 1, 1)

        self.upper_skill_spinbox = QSpinBox(self.skill_group)
        self.upper_skill_spinbox.setObjectName(u"upper_skill_spinbox")
        self.upper_skill_spinbox.setMinimum(1)
        self.upper_skill_spinbox.setMaximum(10)

        self.gridLayout_4.addWidget(self.upper_skill_spinbox, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.skill_group)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.detailed_settings_tab, "")
        self.manual_stats_tab = QWidget()
        self.manual_stats_tab.setObjectName(u"manual_stats_tab")
        self.verticalLayout_4 = QVBoxLayout(self.manual_stats_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.use_manual_stats_checkbox = QCheckBox(self.manual_stats_tab)
        self.use_manual_stats_checkbox.setObjectName(u"use_manual_stats_checkbox")

        self.verticalLayout_4.addWidget(self.use_manual_stats_checkbox)

        self.stats_group = QGroupBox(self.manual_stats_tab)
        self.stats_group.setObjectName(u"stats_group")
        self.gridLayout_2 = QGridLayout(self.stats_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.attack_label = QLabel(self.stats_group)
        self.attack_label.setObjectName(u"attack_label")

        self.gridLayout_2.addWidget(self.attack_label, 0, 0, 1, 1)

        self.attack_spinbox = QSpinBox(self.stats_group)
        self.attack_spinbox.setObjectName(u"attack_spinbox")
        self.attack_spinbox.setMaximum(999999)

        self.gridLayout_2.addWidget(self.attack_spinbox, 0, 1, 1, 1)

        self.defense_label = QLabel(self.stats_group)
        self.defense_label.setObjectName(u"defense_label")

        self.gridLayout_2.addWidget(self.defense_label, 1, 0, 1, 1)

        self.defense_spinbox = QSpinBox(self.stats_group)
        self.defense_spinbox.setObjectName(u"defense_spinbox")
        self.defense_spinbox.setMaximum(999999)

        self.gridLayout_2.addWidget(self.defense_spinbox, 1, 1, 1, 1)

        self.hp_label = QLabel(self.stats_group)
        self.hp_label.setObjectName(u"hp_label")

        self.gridLayout_2.addWidget(self.hp_label, 2, 0, 1, 1)

        self.hp_spinbox = QSpinBox(self.stats_group)
        self.hp_spinbox.setObjectName(u"hp_spinbox")
        self.hp_spinbox.setMaximum(9999999)

        self.gridLayout_2.addWidget(self.hp_spinbox, 2, 1, 1, 1)

        self.attack_speed_label = QLabel(self.stats_group)
        self.attack_speed_label.setObjectName(u"attack_speed_label")

        self.gridLayout_2.addWidget(self.attack_speed_label, 3, 0, 1, 1)

        self.attack_speed_spinbox = QSpinBox(self.stats_group)
        self.attack_speed_spinbox.setObjectName(u"attack_speed_spinbox")
        self.attack_speed_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.attack_speed_spinbox, 3, 1, 1, 1)

        self.crit_rate_label = QLabel(self.stats_group)
        self.crit_rate_label.setObjectName(u"crit_rate_label")

        self.gridLayout_2.addWidget(self.crit_rate_label, 4, 0, 1, 1)

        self.crit_rate_spinbox = QSpinBox(self.stats_group)
        self.crit_rate_spinbox.setObjectName(u"crit_rate_spinbox")
        self.crit_rate_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.crit_rate_spinbox, 4, 1, 1, 1)

        self.crit_damage_label = QLabel(self.stats_group)
        self.crit_damage_label.setObjectName(u"crit_damage_label")

        self.gridLayout_2.addWidget(self.crit_damage_label, 5, 0, 1, 1)

        self.crit_damage_spinbox = QSpinBox(self.stats_group)
        self.crit_damage_spinbox.setObjectName(u"crit_damage_spinbox")
        self.crit_damage_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.crit_damage_spinbox, 5, 1, 1, 1)

        self.sp_regen_label = QLabel(self.stats_group)
        self.sp_regen_label.setObjectName(u"sp_regen_label")

        self.gridLayout_2.addWidget(self.sp_regen_label, 6, 0, 1, 1)

        self.sp_regen_spinbox = QSpinBox(self.stats_group)
        self.sp_regen_spinbox.setObjectName(u"sp_regen_spinbox")
        self.sp_regen_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.sp_regen_spinbox, 6, 1, 1, 1)

        self.sp_onhit_label = QLabel(self.stats_group)
        self.sp_onhit_label.setObjectName(u"sp_onhit_label")

        self.gridLayout_2.addWidget(self.sp_onhit_label, 7, 0, 1, 1)

        self.sp_onhit_spinbox = QSpinBox(self.stats_group)
        self.sp_onhit_spinbox.setObjectName(u"sp_onhit_spinbox")
        self.sp_onhit_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.sp_onhit_spinbox, 7, 1, 1, 1)

        self.cooldown_reduction_label = QLabel(self.stats_group)
        self.cooldown_reduction_label.setObjectName(u"cooldown_reduction_label")

        self.gridLayout_2.addWidget(self.cooldown_reduction_label, 8, 0, 1, 1)

        self.cooldown_reduction_spinbox = QSpinBox(self.stats_group)
        self.cooldown_reduction_spinbox.setObjectName(u"cooldown_reduction_spinbox")
        self.cooldown_reduction_spinbox.setMaximum(999)

        self.gridLayout_2.addWidget(self.cooldown_reduction_spinbox, 8, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.stats_group)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.manual_stats_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_button = QPushButton(HeroSettingDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.save_button = QPushButton(HeroSettingDialog)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(HeroSettingDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HeroSettingDialog)
    # setupUi

    def retranslateUi(self, HeroSettingDialog):
        HeroSettingDialog.setWindowTitle(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130 \uc124\uc815", None))
        self.hero_name_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130\uba85", None))
        self.character_info_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130 \uc815\ubcf4", None))
        self.label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130 \ub808\ubca8:", None))
        self.label_2.setText(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130 \uc131\uae09:", None))
        self.aside_info_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uc5b4\uc0ac\uc774\ub4dc \uc815\ubcf4", None))
        self.label_3.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc5b4\uc0ac\uc774\ub4dc \ub808\ubca8:", None))
        self.label_4.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc5b4\uc0ac\uc774\ub4dc \uc131\uae09:", None))
        self.equipment_info_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uc7a5\ube44 \uc815\ubcf4", None))
        self.label_5.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc7a5\ube44 \ub7ad\ud06c:", None))
        self.equip1_checkbox.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc7a5\ube44 1", None))
        self.equip2_checkbox.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc7a5\ube44 2", None))
        self.equip3_checkbox.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc7a5\ube44 3", None))
        self.affection_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\ud638\uac10\ub3c4", None))
        self.label_6.setText(QCoreApplication.translate("HeroSettingDialog", u"\ud638\uac10\ub3c4 \ub808\ubca8:", None))
        self.apostle_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uc0ac\ub3c4 \uc2a4\ud0ef", None))
        self.apostle_none_radio.setText(QCoreApplication.translate("HeroSettingDialog", u"\ubbf8\uc801\uc6a9", None))
        self.apostle_gather_radio.setText(QCoreApplication.translate("HeroSettingDialog", u"\ubaa8\uc5ec\ub77c \uc0ac\ub3c4", None))
        self.apostle_shine_radio.setText(QCoreApplication.translate("HeroSettingDialog", u"\ube5b\ub098\ub77c \uc0ac\ub3c4", None))
        self.board_stat_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\ubcf4\ub4dc \uc2a4\ud0ef (\uc77d\uae30 \uc804\uc6a9)", None))
        self.label_7.setText(QCoreApplication.translate("HeroSettingDialog", u"\uac1c\uc778 \ubcf4\ub4dc \uc2a4\ud0ef:", None))
        self.personal_board_label.setText(QCoreApplication.translate("HeroSettingDialog", u"Placeholder", None))
        self.label_8.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc804\uccb4 \uace0\uc815 \uc2a4\ud0ef:", None))
        self.global_board_label.setText(QCoreApplication.translate("HeroSettingDialog", u"Placeholder", None))
        self.skill_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uc2a4\ud0ac \ub808\ubca8", None))
        self.lower_skill_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc800\ud559\ub144 \uc2a4\ud0ac:", None))
        self.upper_skill_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uace0\ud559\ub144 \uc2a4\ud0ac:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.detailed_settings_tab), QCoreApplication.translate("HeroSettingDialog", u"\uc0c1\uc138 \uc124\uc815", None))
        self.use_manual_stats_checkbox.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc720\uc800\uac00 \uc785\ub825\ud55c \uc2a4\ud0ef \uc0ac\uc6a9", None))
        self.stats_group.setTitle(QCoreApplication.translate("HeroSettingDialog", u"\uce90\ub9ad\ud130 \uc2a4\ud0ef", None))
        self.attack_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uacf5\uaca9\ub825:", None))
        self.defense_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\ubc29\uc5b4\ub825:", None))
        self.hp_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uccb4\ub825:", None))
        self.attack_speed_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uacf5\uaca9\uc18d\ub3c4:", None))
        self.crit_rate_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uce58\uba85\ud0c0 \ud655\ub960:", None))
        self.crit_damage_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\uce58\uba85\ud0c0 \ud53c\ud574:", None))
        self.sp_regen_label.setText(QCoreApplication.translate("HeroSettingDialog", u"SP \uc790\uc5f0\ud68c\ubcf5\ub7c9:", None))
        self.sp_onhit_label.setText(QCoreApplication.translate("HeroSettingDialog", u"SP \ud53c\uaca9\ud68c\ubcf5\ub7c9:", None))
        self.cooldown_reduction_label.setText(QCoreApplication.translate("HeroSettingDialog", u"\ucfe8\ud0c0\uc784 \uac10\uc18c:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual_stats_tab), QCoreApplication.translate("HeroSettingDialog", u"\uc2a4\ud0ef \uc9c1\uc811 \uc785\ub825", None))
        self.cancel_button.setText(QCoreApplication.translate("HeroSettingDialog", u"\ucde8\uc18c", None))
        self.save_button.setText(QCoreApplication.translate("HeroSettingDialog", u"\uc800\uc7a5", None))
    # retranslateUi

