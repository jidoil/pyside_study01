from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QToolBar, QAction, QStatusBar, QPushButton


class main_window(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("the Main Window app")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("&Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addMenu("Copy")
        edit_menu.addMenu("Cut")
        edit_menu.addMenu("Paste")
        edit_menu.addMenu("Undo")
        edit_menu.addMenu("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message")
        action1.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some otheraction", self)
        action2.setStatusTip("Status message")
        action2.triggered.connect(self.toolbar_button_clicked)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        
        toolbar.addWidget(QPushButton("Click Here"))

        toolbar.addSeparator()

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


        self.setStatusBar(QStatusBar(self))
    def quit_app(self):
        self.app.quit()

    def toolbar_button_clicked(self):
        self.statusBar().showMessage("toolbar -> StatusBar clicked", 3000)

    def button1_clicked(self):
        print("button1 Clicked!")