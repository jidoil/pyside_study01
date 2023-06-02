from PySide2 import QtWidgets
import sys

from widget import Widget

app = QtWidgets.QApplication()
window = Widget()
window.show()

sys.exit(app.exec_())