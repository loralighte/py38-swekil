import swekil
import os
from PyQt5.QtCore import *

class RunCommands(QObject):
    def __init__(self, parent=None):
        super(RunCommands, self).__init__(parent)
    @pyqtSlot(str)
    def exec(self, message):
        os.system(message)

commands = RunCommands()

index = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
swekil.Window.openWindow(swekil.Window(), index, 600, 400, "My Window", [['commands', commands]])

