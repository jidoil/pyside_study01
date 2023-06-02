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
        Widget.resize(510, 401)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(390, 10, 111, 381))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_dir_button = QPushButton(self.widget)
        self.choose_dir_button.setObjectName(u"choose_dir_button")

        self.verticalLayout.addWidget(self.choose_dir_button)

        self.create_dir_button = QPushButton(self.widget)
        self.create_dir_button.setObjectName(u"create_dir_button")

        self.verticalLayout.addWidget(self.create_dir_button)

        self.dir_exists_button = QPushButton(self.widget)
        self.dir_exists_button.setObjectName(u"dir_exists_button")

        self.verticalLayout.addWidget(self.dir_exists_button)

        self.dir_or_file_button = QPushButton(self.widget)
        self.dir_or_file_button.setObjectName(u"dir_or_file_button")

        self.verticalLayout.addWidget(self.dir_or_file_button)

        self.folder_content_button = QPushButton(self.widget)
        self.folder_content_button.setObjectName(u"folder_content_button")

        self.verticalLayout.addWidget(self.folder_content_button)

        self.verticalSpacer = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 371, 381))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.listWidget = QListWidget(self.widget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.choose_dir_button.setText(QCoreApplication.translate("Widget", u"Choose Dir", None))
        self.create_dir_button.setText(QCoreApplication.translate("Widget", u"Create Dir", None))
        self.dir_exists_button.setText(QCoreApplication.translate("Widget", u"Dir Exist?", None))
        self.dir_or_file_button.setText(QCoreApplication.translate("Widget", u"Dir or File", None))
        self.folder_content_button.setText(QCoreApplication.translate("Widget", u"Folder Content", None))
    # retranslateUi

