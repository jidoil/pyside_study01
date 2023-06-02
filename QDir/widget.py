from PySide2.QtCore import QDir, QFileInfo
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDir Demo")

        self.choose_dir_button.clicked.connect(self.choose_dir_button_clicked)
        self.create_dir_button.clicked.connect(self.create_dir_button_clicked)
        self.dir_exists_button.clicked.connect(self.dir_exists_button_clicked)
        self.dir_or_file_button.clicked.connect(self.dir_or_file_button_clicked)
        self.folder_content_button.clicked.connect(self.folder_content_button_clicked)

    def dir_or_file_button_clicked(self):
        current_item = self.listWidget.currentItem()
        if current_item is None:
            return
        file_info = QFileInfo(current_item.text())
        if file_info.isDir() :
            QMessageBox.information(self, "Message", "This is a dir")
        elif file_info.isFile() :
            QMessageBox.information(self, "Message", "This is a file")
        else :
            QMessageBox.information(self, "Message", "Something else")
    def folder_content_button_clicked(self):
        self.listWidget.clear()
        dir_path = self.lineEdit.text()
        if not dir_path :
            return
        dir = QDir(dir_path)
        file_list  = dir.entryInfoList()
        for i in range(len(file_list)) :
            file_ionfo = file_list[i]
            self.listWidget.addItem(file_ionfo.absoluteFilePath())


    def choose_dir_button_clicked(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Choose Folder")
        if not dir_name :
            return
        print("file : ", dir_name)
        self.lineEdit.setText(dir_name)

    def create_dir_button_clicked(self):
        dir_path = self.lineEdit.text()

        if not dir_path :
            return

        dir = QDir(dir_path)
        if not dir.exists() :
            if dir.mkpath(dir_path) :
                QMessageBox.information(self, "Message", "Directory created")
        else :
            QMessageBox.information(self, "Message", "Dir already Exists!")

    def dir_exists_button_clicked(self):
        dir_path = self.lineEdit.text()
        if not dir_path :
            return
        dir = QDir(dir_path)
        if dir.exists() :
            QMessageBox.information(self, "Message", "dir exists")
        else :
            QMessageBox.information(self, "MEssage", "Directory not exists.")