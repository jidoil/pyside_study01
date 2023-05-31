from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout


class LabelAndLine(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("test")

        label = QLabel("Full Name:")
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.return_pressed)
        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print("text changed to ", self.line_edit.text())


    # def selection_changed(self):
    #     print("selection changed: " , self.line_edit.selectedText())
    #
    # def text_edited(self, new_text):
    #     print("Text edited. new TExt: ", new_text)
    #
    # def cursor_position_changed(self, old, new):
    #     print("cursor old posoitno", old, " -new position", new)
    #
    # def editing_finished(self):
    #     print("editing finished. ")
    #
    def return_pressed(self):
        print("return pressed")