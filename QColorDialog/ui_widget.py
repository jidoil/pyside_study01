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
        Widget.resize(232, 300)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 230, 201, 31))
        self.background_color_button = QPushButton(Widget)
        self.background_color_button.setObjectName(u"background_color_button")
        self.background_color_button.setGeometry(QRect(30, 40, 171, 27))
        self.text_color_button = QPushButton(Widget)
        self.text_color_button.setObjectName(u"text_color_button")
        self.text_color_button.setGeometry(QRect(30, 90, 171, 27))
        self.font_button = QPushButton(Widget)
        self.font_button.setObjectName(u"font_button")
        self.font_button.setGeometry(QRect(30, 150, 171, 27))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Color Palette", None))
        self.background_color_button.setText(QCoreApplication.translate("Widget", u"Set Background Color", None))
        self.text_color_button.setText(QCoreApplication.translate("Widget", u"Set Text Color", None))
        self.font_button.setText(QCoreApplication.translate("Widget", u"Set Font", None))
    # retranslateUi

