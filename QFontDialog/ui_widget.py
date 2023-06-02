# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 144)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 30, 311, 27))
        self.font_dialog_label = QLabel(Widget)
        self.font_dialog_label.setObjectName(u"font_dialog_label")
        self.font_dialog_label.setGeometry(QRect(50, 80, 311, 41))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Click", None))
        self.font_dialog_label.setText(QCoreApplication.translate("Widget", u"The sky is blue", None))
    # retranslateUi

