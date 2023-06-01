import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

from widget import Widget

app = QtWidgets.QApplication(sys.argv)
window = Widget()
app.exec_()
window.show()








# a = [1, 3, 5, 4, 2]
# x = [1, 3, 5, 4, 2]
# a.reverse()
# for i in range(len(a)):
#     print(a[i])
# c = x[::-1]
# print(c)
# b = ['python', 'is', 'so', 'interesting']
# res = ' '.join(b)
# print(res)