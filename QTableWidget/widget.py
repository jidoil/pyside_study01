from PySide2.QtWidgets import QWidget, QTableWidgetItem

from ui_widget import Ui_Widget
class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTable Demo")

        self.list_items_button.clicked.connect(self.list_items_button_clicked)
        self.set_item_button.clicked.connect(self.set_item_button_clicked)



    def list_items_button_clicked(self):
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        for r in range(rows):
            for c in range(columns):
                item = self.tableWidget.item(r, c)
                if(item):
                    from PySide2.QtCore import Qt
                    data = item.data(Qt.DisplayRole)
                    print(data)
                else:
                    print("No data")


    def set_item_button_clicked(self):
        #
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.insertColumn(self.tableWidget.columnCount())

        item = QTableWidgetItem("Hello")
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, self.tableWidget.rowCount()-1, item)
