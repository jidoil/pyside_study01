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
        Widget.resize(400, 114)
        self.provide_info_button = QPushButton(Widget)
        self.provide_info_button.setObjectName(u"provide_info_button")
        self.provide_info_button.setGeometry(QRect(30, 10, 341, 27))
        self.info_label = QLabel(Widget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(30, 60, 341, 41))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.provide_info_button.setText(QCoreApplication.translate("Widget", u"Provide Info", None))
        self.info_label.setText(QCoreApplication.translate("Widget", u"some text", None))
    # retranslateUi

