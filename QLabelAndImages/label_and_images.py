from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout


class LabelAndImages(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("/home/rapa/PycharmProjects/PySide2_Practice/QLabelAndImages/Images/minions.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)
