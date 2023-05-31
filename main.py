from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import sys
from LabelAndLineEdit.LabelAndLine import LabelAndLine
from ListWidget import ListWidget
from Main.MainWindow import MainWindow
from PushBox.PushBox import PushButton
from QCheckBoxAndRadioButton.CheckBoxWidget import CheckBoxWidget
from QComboBox.combo_box_widget import ComboBoxWidget
from QGridLayout.grid_layout import GridWidget
from QLabelAndImages.label_and_images import LabelAndImages
from QMessageBox.Message import MessageBox
from QTabWidget.TabWidget import TabWidget
from QTextEdit.text_edit_widget import Text_Edit
from SizePolicy.size_widget import SizeWidget


# window = MainWindow(app)
# window = MessageBox()
# window = PushButton()
# window = LabelAndLine()
# window = Text_Edit()
# window = LabelAndImages()
# window = SizeWidget()
# window = GridWidget()
# window = CheckBoxWidget()
# window = ListWidget()
# window = TabWidget()
# window = ComboBoxWidget()


loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load("QUiLoader/widget.ui", None) #Load the ui - happens at run time!

def do_something() :
    print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

#Changing the properties in the form
window.setWindowTitle("User data")

#Accessing widgets in the form
window.submit_button.clicked.connect(do_something)
window.show()
app.exec_()