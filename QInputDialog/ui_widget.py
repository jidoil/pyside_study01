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
        Widget.resize(400, 300)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 50, 301, 51))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 210, 161, 91))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.value_label = QLabel(Widget)
        self.value_label.setObjectName(u"value_label")
        self.value_label.setGeometry(QRect(210, 210, 191, 91))
        font1 = QFont()
        font1.setPointSize(25)
        self.value_label.setFont(font1)
        self.value_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Click", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Value:", None))
        self.value_label.setText(QCoreApplication.translate("Widget", u"Value", None))
    # retranslateUi

