from PySide2.QtWidgets import QWidget, QTabWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout


class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget Demo")

        tab_widget = QTabWidget(self)

        # info
        widget_form = QWidget()
        label_full_name = QLabel("Full name : ")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        # buttons
        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        button_layout= QVBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        button_layout.addWidget(button_3)
        widget_buttons.setLayout(button_layout)

        tab_widget.addTab(widget_form, "Info")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def button_1_clicked(self):
        print("Button clicked")