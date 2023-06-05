from PySide2 import QtCore
from PySide2.QtCore import Qt, QTime, QModelIndex
from PySide2.QtGui import QFont, QBrush, QColor


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)

        self.table = [
            ["john", "doe", "55", "trainer", "married", "Gounduana", "black"],
            ["kevin", "wood", "32", "thief", "single", "Verkso", "pink"],
            ["frank", "stoney", "42", "manager", "single", "Gounduana", "red"],
            ["elice", "lynn", "22", "worker", "Married", "Verkso", "blue"],
        ]

    def setData(self, index, value, role):
        if not role == Qt.EditRole :
            return False
        self.table[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def data(self, index, role):
        # if role == Qt.DisplayRole :
        #     print("role : " + str(role))
        #     # value = " [ Row : " + str(index.row() + 1) + ", Column : " + str(index.column() + 1 )
        #     value = " "
        #     return value


        # row = index.row()
        # col = index.column()
        #
        # if role == Qt.DisplayRole:
        #     if row == 0 and col == 1:
        #         return "<-- Left"
        #     if row == 1 and col == 1:
        #         return "right -->"
        #     if row == 0 and col == 0:
        #         return QTime.currentTime().toString()
        #     value = "[ Row : " + str(index.row() + 1) + ", Column : " +str(index.column() + 1) +"]"
        #     return value
        # if role == Qt.FontRole :
        #     font = QFont()
        #     font.setBold(True)
        #     return font
        # if role == Qt.BackgroundRole :
        #     if row == 1 and col == 2:
        #         # background = QBrush(Qt.yellow)
        #         return QBrush(Qt.yellow)
        # if role == Qt.TextAlignmentRole :
        #     if row == 1 and col == 1:
        #         return Qt.AlignRight

        if role == Qt.DisplayRole or role == Qt.EditRole :
            return self.table[index.row()][index.column()]
        elif role == Qt.DecorationRole and index.column() == 6 :
            return QColor(self.table[index.row()][index.column()])

    def rowCount(self, index:QModelIndex):
        if not index.isValid() :
            return len(self.table)
        return 0

    def columnCount(self, index):
        if not index.isValid() :
            return len(self.table[0])
        return 0

    def headerData(self, section, orientation, role):
        # if role == Qt.DisplayRole :
        #     if orientation == Qt.Horizontal:
        #         if section == 0 : return "first"
        #         if section == 1 : return "second"
        #         if section == 2 : return "third"
        #         if section == 3 : return "fourth"
          if role == Qt.DisplayRole :
                if orientation == Qt.Horizontal:
                    if section == 0 : return "First Name"
                    if section == 1 : return "Last Name"
                    if section == 2 : return "Age"
                    if section == 3 : return "Profession"
                    if section == 4 : return "Martial Status"
                    if section == 5 : return "Country"
                    if section == 6 : return "Favorite color"
          return super().headerData(section, orientation, role)