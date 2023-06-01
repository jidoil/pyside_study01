# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infodialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName(u"InfoDialog")
        InfoDialog.resize(400, 148)
        self.widget = QWidget(InfoDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 361, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.position_line_edit = QLineEdit(self.widget)
        self.position_line_edit.setObjectName(u"position_line_edit")

        self.horizontalLayout.addWidget(self.position_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.favorite_os_combo_box = QComboBox(self.widget)
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.setObjectName(u"favorite_os_combo_box")

        self.horizontalLayout_2.addWidget(self.favorite_os_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ok_button = QPushButton(self.widget)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(InfoDialog)

        QMetaObject.connectSlotsByName(InfoDialog)
    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QCoreApplication.translate("InfoDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InfoDialog", u"Position", None))
        self.label_2.setText(QCoreApplication.translate("InfoDialog", u"Favorite", None))
        self.favorite_os_combo_box.setItemText(0, QCoreApplication.translate("InfoDialog", u"Windows", None))
        self.favorite_os_combo_box.setItemText(1, QCoreApplication.translate("InfoDialog", u"Linux", None))
        self.favorite_os_combo_box.setItemText(2, QCoreApplication.translate("InfoDialog", u"Mac", None))

        self.ok_button.setText(QCoreApplication.translate("InfoDialog", u"Ok", None))
        self.cancel_button.setText(QCoreApplication.translate("InfoDialog", u"Cancel", None))
    # retranslateUi

