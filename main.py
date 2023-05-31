from PySide2.QtWidgets import QApplication
import sys

from LabelAndLineEdit.LabelAndLine import LabelAndLine
from Main.MainWindow import MainWindow
from PushBox.PushBox import PushButton
from QMessageBox.Message import MessageBox
from QTextEdit.text_edit_widget import Text_Edit

app = QApplication(sys.argv)
# window = MainWindow(app)
# window = MessageBox()
# window = PushButton()
# window = LabelAndLine()

window = Text_Edit()
window.show()
app.exec_()
