from PySide2.QtWidgets import QApplication
import sys

from main_widget import main_window
from theMessagBox import Widget

app = QApplication(sys.argv)

# window = RockWidget()
# window = main_window(app)
window = Widget()
window.show()

app.exec_()