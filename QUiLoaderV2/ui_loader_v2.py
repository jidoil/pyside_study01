from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()


class UserInterface(QtCore.QObject):  # An object wrapping around our ui
    def __init__(self):
        super().__init__()

        ui_file = QFile("widget.ui")
        if ui_file:
            print("load ui success")
            ui_file.open(QFile.ReadOnly)
            self.ui = loader.load(ui_file)
            self.ui.setWindowTitle("User Data")
            self.ui.submit_button.clicked.connect(self.do_something)
            ui_file.close()
        else:
            print("failed ui")

    def show(self):
        self.ui.show()

    def do_something(self):
        print(self.ui.full_name_line_edit.text(), " is a ", self.ui.occupation_line_edit.text())
