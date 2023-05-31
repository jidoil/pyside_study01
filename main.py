from PySide2.QtWidgets import QApplication
import sys

from LabelAndLineEdit.LabelAndLine import LabelAndLine
from Main.MainWindow import MainWindow
from PushBox.PushBox import PushButton
from QLabelAndImages.label_and_images import LabelAndImages
from QMessageBox.Message import MessageBox
from QTextEdit.text_edit_widget import Text_Edit
from SizePolicy.size_widget import SizeWidget

app = QApplication(sys.argv)
# window = MainWindow(app)
# window = MessageBox()
# window = PushButton()
# window = LabelAndLine()
# window = Text_Edit()
# window = LabelAndImages()
window = SizeWidget()
window.show()
sys.exit(app.exec_())
