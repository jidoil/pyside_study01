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
        self.list_items_button = QPushButton(Widget)
        self.list_items_button.setObjectName(u"list_items_button")
        self.list_items_button.setGeometry(QRect(0, 240, 401, 27))
        self.set_item_button = QPushButton(Widget)
        self.set_item_button.setObjectName(u"set_item_button")
        self.set_item_button.setGeometry(QRect(0, 270, 401, 27))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 401, 231))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.list_items_button.setText(QCoreApplication.translate("Widget", u"List items", None))
        self.set_item_button.setText(QCoreApplication.translate("Widget", u"Set item", None))
    # retranslateUi

