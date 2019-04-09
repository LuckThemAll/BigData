import sys
from PyQt5 import QtWidgets
from view import MainWindow
from controller import Controller

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    controller = Controller(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
