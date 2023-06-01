from PySide2.QtWidgets import QWidget, QFileDialog

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")

        self.file_button.clicked.connect(self.button_clicked)

    def button_clicked(self):

        # dir = QFileDialog.getExistingDirectory(self, "Open directory",
        #                                        "/home",
        #                                        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        # print("Chosen dir : ", dir)

        # file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
        #                                           "/home",
        #                                           "Images (*.png *.xpm *.jpg);;All files(*.*)"
        # print("Your chosen file is : ", file_name )
        #                                           )

        # file_name,_ = QFileDialog.getOpenFileNames(
        #     self, "Open File", "/home", "Images (*.png *.xpm *.jpg);; All files(*.*)"
        # )
        # for f in file_name:
        #     print(f)

        file_name,_ = QFileDialog.getSaveFileName(self, "Save File",
                                                  "/home/jana/untilted.png",
                                                  "Images( *.png *.xpm *.jpg);; All files(*.*)"
                                                  )

        print(file_name)