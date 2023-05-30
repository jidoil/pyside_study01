from PySide2.QtWidgets import QApplication
import sys
from ButtonHolder import Button_Holder
from RockWidget import RockWidget
from Slider import Slider

app = QApplication(sys.argv)

window = RockWidget()

window.show()

app.exec_()