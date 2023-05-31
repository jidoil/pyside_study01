from PySide2.QtWidgets import QApplication
import sys

from LabelAndLineEdit.LabelAndLine import LabelAndLine
from Main.MainWindow import MainWindow
from PushBox.PushBox import PushButton
from QMessage.Message import MessageBox

app = QApplication(sys.argv)
# window = MainWindow(app)
# window = MessageBox()
# window = PushButton()
window = LabelAndLine()

window.show()
app.exec_()
