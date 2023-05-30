from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)

    def button1_clicked(self, data):
        print("button 1 clicked : ", data)

    def button2_clicked(self, data):
        print("button 2 clicked:", data)