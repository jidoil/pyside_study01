from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QMenuBar, QToolBar, QAction, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("The Main Window App")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.clicked_quit_action)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        #toolbar
        toolbar = QToolBar("Main Tool Bar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)
        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message for action 1")
        action1.triggered.connect(self.clicked_quit_action)
        toolbar.addAction(action1)

        action2 = QAction("Second Actino", self)
        action2.setStatusTip("Show STatus!")
        action2.triggered.connect(self.toolbar_clicked)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        self.setStatusBar(QStatusBar(self))


    def clicked_quit_action(self):
        print("Quit Clicked")
        self.app.quit()

    def toolbar_clicked(self):
        self.statusBar().showMessage("status!", 3000)