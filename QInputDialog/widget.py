from PySide2.QtWidgets import QWidget, QInputDialog

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QInputDial Demo")

        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # text, ok = QInputDialog.getText(self, "getText", "Enter your name : ")
        # if ok and not text == "" :
        #     self.value_label.setText(text)
        # value, ok = QInputDialog.getDouble(self, "Get Double", "Select a value", 100, 50, 200)
        # if ok :
        #     self.value_label.setText(f'{value}')
        items = ["Spring", "Summer", "Fall", "Winter"]
        item, ok = QInputDialog.getItem(self, "QInputDialog.getItem()", "Season:", items)
        if (ok):
            self.value_label.setText(item)