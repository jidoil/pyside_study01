from PySide2.QtGui import QPalette, QFont
from PySide2.QtWidgets import QWidget, QColorDialog, QFontDialog

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("QFonDialog Demo")

        # 컬러가 나타나기 위한 셋업
        self.label.setAutoFillBackground(True)

        # 시그널, 슬롯 설정
        self.text_color_button.clicked.connect(self.text_color_button_clicked)
        self.background_color_button.clicked.connect(self.background_color_button_clicked)
        self.font_button.clicked.connect(self.set_font)

    def text_color_button_clicked(self):
        palette = self.label.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color, self, "Choose")

        if chosenColor.isValid():
            palette.setColor(QPalette.WindowText, chosenColor)
            self.label.setPalette(palette)
        else:
            print("User chose a bad text color")

    def background_color_button_clicked(self):
        palette = self.label.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color, self, "Choose Background color")

        if chosenColor.isValid():
            palette.setColor(QPalette.Window, chosenColor)
            self.label.setPalette(palette)
        else:
            print("User chose a bad background color")

    def set_font(self):
        ok, font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20), self)
        if ok :
            self.label.setFont(font)
        else :
            print("User didnt select any valid font")

