from PySide2.QtCore import QByteArray, QUrl, QJsonDocument, QJsonArray
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide2.QtWidgets import QWidget
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget) :
    def __init__(self):
        super().__init__()

        self.net_reply = None
        self.setupUi(self)
        self.setWindowTitle("JSON API Demo")

        self.net_manager = QNetworkAccessManager(self)
        self.m_data_buffer = QByteArray()
        self.request = QNetworkRequest()
        self.request.setUrl(QUrl("https://jsonplaceholder.typicode.com/posts"))

        self.fetch_button.clicked.connect(self.fetch_button_clicked)

    def fetch_button_clicked(self):
        self.net_reply = self.net_manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_read_to_read)
        self.net_reply.finished.connect(self.data_read_finished)
    def data_read_to_read(self):
        print("Some Data Available")
        self.m_data_buffer.append(self.net_reply.readAll())

    def data_read_finished(self):
        print("Data read finished")
        if self.net_reply.error():
            print("Error")
        else:
            doc = QJsonDocument.fromJson(self.m_data_buffer)
            array = QJsonArray(doc.array())
            for i in range(array.count()):
                object = array.at(i).toObject()
                text = "[" + str(i) + "] :" + str(object["title"])
                self.listWidget.addItem(text)

