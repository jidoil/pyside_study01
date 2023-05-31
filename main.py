from PySide2.QtWidgets import QApplication
import sys

from Main.MainWindow import MainWindow
from QMessage.Message import MessageBox

app = QApplication(sys.argv)
window = MainWindow(app)
# window = MessageBox()
window.show()
app.exec_()
