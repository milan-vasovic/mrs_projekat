from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Slot, qApp
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QAction, QToolBar, QLabel
from PySide2.QtCore import Qt
from .dock_widget import *
from PySide2 import QtGui
from core.view.tool_bar import *

class MainWindow(QtWidgets.QMainWindow):
    """
    Klasa koja predstavlja glavni prozor.
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setWindowTitle("Rukovalac dokumentima")
        self.setWindowIcon(QtGui.QIcon("resources/icons/icons8-edit-file-64.png"))
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.help_menu = QtWidgets.QMenu("Help")

        self.menu_actions = {
            "new": QtWidgets.QAction("New", self.file_menu),
            "new window": QtWidgets.QAction("New Window", self.file_menu),
            "open": QtWidgets.QAction("Open...", self.file_menu),
            "save": QtWidgets.QAction("Save", self.file_menu),
            "save as": QtWidgets.QAction("Save As...", self.file_menu),
            "exit": QtWidgets.QAction("Exit", self.file_menu),
            "about": QtWidgets.QAction("About", self.help_menu)
        }

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        # ToolBar
        toolbar = ToolBar()
        self.addToolBar(toolbar)

        # CentralWidget
        central = QLabel("CentralWidget")
        self.setCentralWidget(central)

        # DockWidget
        dock = DockWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        
        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Everything is good")

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.9, geometry.height() * 0.9)

        def _populate_menus(self):
            """
            Privatna metoda koja smesta menije u meni bar.
            """
            self.file_menu.addAction(self.menu_actions["new"])
            self.file_menu.addAction(self.menu_actions["new window"])
            self.file_menu.addAction(self.menu_actions["open"])
            self.file_menu.addAction(self.menu_actions["save"])
            self.file_menu.addAction(self.menu_actions["save as"])
            self.file_menu.addSeparator()
            self.file_menu.addAction(exit_action)
            self.menu.addMenu(self.file_menu)
            self.help_menu.addAction(self.menu_actions["about"])
            self.menu.addMenu(self.help_menu)

        def about_action(self):
            """
            Metoda koja prikazuje informacioni dijalog korisniku o aplikaciji.
            """
            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "About Rukovalac dokumentima", "Autori:\n     Milan Vasovic\n     Dominik Vrabcenik\nMentor:\n     Aleksandra Mitrović\nPredmetni profesor:\n      Branko Perišić")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        def _bind_actions(self):
            """
            Privatna metoda koja uvezuje reagovanje na dogadjaje.
            """
            self.menu_actions["about"].triggered.connect(about_action)

        _populate_menus(self)
        _bind_actions(self)

