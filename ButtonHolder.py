from PySide2.QtWidgets import QMainWindow, QPushButton


def OnClick(data):
    print("Clicked!!", data)

class Button_Holder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("Click me")
        self.setCentralWidget(button)
        button.clicked.connect(OnClick)