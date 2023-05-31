from PySide2.QtWidgets import QMessageBox, QWidget, QPushButton, QVBoxLayout


class MessageBox(QWidget):
    def __init__(self):
        super().__init__()

        # widget
        self.setWindowTitle("Widget")

        # button
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        self.setLayout(layout)

        # function
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("setWindowTitle: title")
        message.setText("setText: Somthime")
        message.setInformativeText("setInformativeText")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        ret = message.exec_()
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("not Ok")
