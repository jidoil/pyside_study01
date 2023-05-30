from PySide2.QtWidgets import QApplication
import sys
from ButtonHolder import Button_Holder
from Slider import Slider

app = QApplication(sys.argv)

window = Slider()

window.show()

app.exec_()