from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy


class SizeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policy")

        label = QLabel("Some text: ")
        line_edit = QLineEdit()

        # Size Policy
        line_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button_1 = QPushButton("one")
        button_2 = QPushButton("two")
        button_3 = QPushButton("three")

        h_layout_2 = QHBoxLayout()

        # 1 = Fixed
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 3)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)

