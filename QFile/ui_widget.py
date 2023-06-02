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
        Widget.resize(603, 428)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 581, 331))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.write_button = QPushButton(self.widget)
        self.write_button.setObjectName(u"write_button")

        self.verticalLayout.addWidget(self.write_button)

        self.read_button = QPushButton(self.widget)
        self.read_button.setObjectName(u"read_button")

        self.verticalLayout.addWidget(self.read_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 330, 581, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.source_line_edit = QLineEdit(self.widget1)
        self.source_line_edit.setObjectName(u"source_line_edit")

        self.horizontalLayout_2.addWidget(self.source_line_edit)

        self.select_file_button = QPushButton(self.widget1)
        self.select_file_button.setObjectName(u"select_file_button")

        self.horizontalLayout_2.addWidget(self.select_file_button)

        self.widget2 = QWidget(Widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 380, 581, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dest_file_edit = QLineEdit(self.widget2)
        self.dest_file_edit.setObjectName(u"dest_file_edit")

        self.horizontalLayout_3.addWidget(self.dest_file_edit)

        self.copy_file_button = QPushButton(self.widget2)
        self.copy_file_button.setObjectName(u"copy_file_button")

        self.horizontalLayout_3.addWidget(self.copy_file_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.write_button.setText(QCoreApplication.translate("Widget", u"Write", None))
        self.read_button.setText(QCoreApplication.translate("Widget", u"Read", None))
        self.select_file_button.setText(QCoreApplication.translate("Widget", u"Select File", None))
        self.copy_file_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
    # retranslateUi

