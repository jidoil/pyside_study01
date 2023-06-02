from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QFontDialog

from ui_widget import Ui_Widget


class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.pushButton.clicked.connect(self.button_clicked)


    def button_clicked(self) :
        ok, font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20), self)
        if ok:
            self.font_dialog_label.setFont(font)
        else :
            print("User didn't select any valid font")