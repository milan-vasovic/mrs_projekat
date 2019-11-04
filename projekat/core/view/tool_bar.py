from PySide2.QtWidgets import  QLabel, QToolBar, QAction
from PySide2.QtCore import Qt
from PySide2 import QtGui

class ToolBar(QToolBar):
    def __init__(self):
        QToolBar.__init__(self)
        
        exitAction = QAction(QtGui.QIcon("resources/icons/exit.png"),"exit", self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.triggered.connect(self.exit_action)

        self.addAction(exitAction)

        newAction = QAction(QtGui.QIcon("resources/icons/icons8-add-file-100.png"),"new", self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.new_file)         
        
        self.addAction(newAction)

        saveAction = QAction(QtGui.QIcon("resources/icons/icons8-save-100.png"),"save", self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save_file)

        self.addAction(saveAction)

    def exit_action(self):
        quit()

    def new_file(self):
        pass

    def save_file(self):
        pass