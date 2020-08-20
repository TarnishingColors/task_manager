import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class byPriorityWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        self.resize(650, 550)
        self.setWindowTitle('byPriorityWindow')
        self.setWindowIcon(QIcon('web.png'))
