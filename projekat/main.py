import sys
from PySide2 import QtWidgets
from core.view.main_window import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()