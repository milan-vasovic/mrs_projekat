from PySide2.QtCore import Qt, QDir
from PySide2.QtWidgets import QTreeView,QFileSystemModel,QDockWidget  

class DockWidget(QDockWidget):
    def __init__(self):
        QDockWidget.__init__(self, "File Menager")
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())

        tree = QTreeView()
        tree.setModel(model)
        self.setWidget(tree)