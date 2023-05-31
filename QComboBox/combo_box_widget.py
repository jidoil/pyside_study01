from PySide2.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout


class ComboBoxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo box widget demo")

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Pluto")
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Venus")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set Value")
        button_set_current.clicked.connect(self.set_current)
        button_get_value = QPushButton("Get values")
        button_get_value.clicked.connect(self.get_values)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_value)

        self.setLayout(v_layout)

    def current_value(self):
        print("Current item : ", self.combo_box.currentText(), " - current index : ", self.combo_box.currentIndex())
    def set_current(self):
        self.combo_box.setCurrentIndex(2)
    def get_values(self):
        for i in range(self.combo_box.count()):
            print("index [ ", i , "] : ", self.combo_box.itemText(i))
