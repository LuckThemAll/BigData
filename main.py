import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from View import MainWindow
from controller import Controller

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    controller = Controller(MainWindow)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
