from PySide2.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout


class GridWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        button_0 = QPushButton("Zero")
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")
        button_8 = QPushButton("Eight")
        button_9 = QPushButton("Nine")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0, 0)
        grid_layout.addWidget(button_2, 0, 1, 1, 2)
        grid_layout.addWidget(button_3, 1, 0, 2, 1)
        grid_layout.addWidget(button_4, 1, 1)
        grid_layout.addWidget(button_5, 1, 2)
        grid_layout.addWidget(button_6, 2, 1)
        grid_layout.addWidget(button_7, 2, 2)
        grid_layout.addWidget(button_8, 3, 3)
        grid_layout.addWidget(button_9, 4, 4)

        self.setLayout(grid_layout)
