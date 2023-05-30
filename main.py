from PySide2.QtWidgets import QApplication
import sys
from ButtonHolder import Button_Holder

app = QApplication(sys.argv)

window = Button_Holder()
window.show()

app.exec_()