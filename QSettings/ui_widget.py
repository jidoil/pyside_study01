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
        Widget.resize(689, 420)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 0, 621, 301))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_1 = QPushButton(self.widget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)

        self.button_2 = QPushButton(self.widget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy1.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_2, 0, 1, 1, 1)

        self.button_3 = QPushButton(self.widget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy1.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_3, 0, 2, 1, 1)

        self.button_4 = QPushButton(self.widget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy1.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)

        self.button_5 = QPushButton(self.widget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy1.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)

        self.button_6 = QPushButton(self.widget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy1.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)

        self.button_7 = QPushButton(self.widget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy1.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)

        self.button_8 = QPushButton(self.widget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy1.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)

        self.button_9 = QPushButton(self.widget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy1.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 310, 621, 101))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.load_colors_button = QPushButton(self.widget1)
        self.load_colors_button.setObjectName(u"load_colors_button")

        self.verticalLayout.addWidget(self.load_colors_button)

        self.save_colors_button = QPushButton(self.widget1)
        self.save_colors_button.setObjectName(u"save_colors_button")

        self.verticalLayout.addWidget(self.save_colors_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"One", None))
        self.button_2.setText(QCoreApplication.translate("Widget", u"Two", None))
        self.button_3.setText(QCoreApplication.translate("Widget", u"Three", None))
        self.button_4.setText(QCoreApplication.translate("Widget", u"Four", None))
        self.button_5.setText(QCoreApplication.translate("Widget", u"Five", None))
        self.button_6.setText(QCoreApplication.translate("Widget", u"Six", None))
        self.button_7.setText(QCoreApplication.translate("Widget", u"Seven", None))
        self.button_8.setText(QCoreApplication.translate("Widget", u"Eight", None))
        self.button_9.setText(QCoreApplication.translate("Widget", u"Nine", None))
        self.load_colors_button.setText(QCoreApplication.translate("Widget", u"Load Colors", None))
        self.save_colors_button.setText(QCoreApplication.translate("Widget", u"Save Colors", None))
    # retranslateUi

