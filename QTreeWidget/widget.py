from PySide2.QtWidgets import QWidget, QTreeWidgetItem

from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tree Widget Demo")

        self.treeWidget.setColumnCount(2)

        #set hearder
        self.treeWidget.setHeaderLabels(["ID", "Name"])

        # ADD data
        treeItem1 = QTreeWidgetItem(self.treeWidget)
        treeItem1.setText(0, "11")
        treeItem1.setText(1, "Show")

        treeItem2 = QTreeWidgetItem(self.treeWidget)
        treeItem2.setText(0, "22")
        treeItem2.setText(1, "David")

        treeItem3 = QTreeWidgetItem(self.treeWidget)
        treeItem3.setText(0, "33")
        treeItem3.setText(1, "Steve")

        treeItem2.addChild(treeItem3)

        self.list_item_button.clicked.connect(self.list_items)

    def list_items(self):
        top_level_item_count = self.treeWidget.topLevelItemCount()
        for i in range(top_level_item_count):
            item = self.treeWidget.topLevelItem(i)
            if item :
                from PySide2.QtCore import Qt
                print("ID : ", item.data(0, Qt.DisplayRole), " | Name : ", item.data(1, Qt.DisplayRole))
                child_count = item.childCount()
                if child_count :
                    for c in range(child_count):
                        child = item.child(child_count)
                        print("---ID : ", child.data(0, Qt.DisplayRole), " | Name : ", child.data(1, Qt.DisplayRole))
