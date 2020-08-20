import sys
from PyQt5.QtWidgets import *
from EnterWindow import EnterWindow
from classes import User, Project, Task


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = EnterWindow()
    sys.exit(app.exec_())
