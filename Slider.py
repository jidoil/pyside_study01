from PySide2.QtWidgets import QMainWindow, QSlider
from PySide2.QtCore import Qt

def respond_to_slider(data):
    print("Slider moved to: ", data)

class Slider(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(0, 0, 1000, 1000)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(respond_to_slider)
        self.setCentralWidget(slider)
