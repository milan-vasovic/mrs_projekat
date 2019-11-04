from PySide2.QtWidgets import QMainWindow,QDockWidget,QStatusBar, QAction, QLabel, QToolBar
from PySide2.QtCore import qApp,Slot
from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence

class StatusBar(QStatusBar):
    def __init__(self):
        QStatusBar.__init__(self)
        self.showMessage("Evryting is all good!")

    def set_status(self, message):
        self.showMessage(message)