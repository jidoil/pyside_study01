from PySide2.QtWidgets import QWidget
from tablemodel import TableModel
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom Model")

        self.model = TableModel()
        self.tableView.setModel(self.model)
