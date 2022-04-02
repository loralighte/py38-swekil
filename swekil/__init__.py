import sys
from PyQt5 import QtCore
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

class Window(QWebView):
    def __init__(self):
        super().__init__()
        
    def openWindow(self, index, window_width, window_height, window_title, modules):
        frame = self.page().mainFrame()

        self.setWindowTitle(window_title)
        self.load(QtCore.QUrl.fromLocalFile(index))
        self.setFixedSize(window_width, window_height)

        if modules:
            for module in modules:
                frame.addToJavaScriptWindowObject(module[0], module[1])

        self.show()
        sys.exit(app.exec_())
        