from PySide2.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout


class Text_Edit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Edit")

        self.text_edit = QTextEdit()

        current_text_button = QPushButton("Current Text")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("paste")
        paste_button.clicked.connect(self.paste)

        undo_button = QPushButton("undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("set html")
        set_html_button.clicked.connect(self.set_html)

        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(set_plain_text_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)
        self.setLayout(v_layout)


    def current_text_button_clicked(self):
        print("asdf")

    def paste(self):
        self.text_edit.paste()

    def set_plain_text(self):
        self.text_edit.setPlainText("Sed ut perspiciaste adf wef sdfadf")

    def set_html(self):
        self.text_edit.setHtml("<h1>kigal</h1><p>adsfasdf a</p>")