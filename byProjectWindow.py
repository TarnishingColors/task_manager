from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from classes import Data
from datetime import datetime
from functools import partial
from ProjectInfoWindow import ProjectInfo


class byProjectWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        self.resize(650, 650)
        self.setWindowTitle('byProjectWindow')
        self.setWindowIcon(QIcon('web.png'))

        curProjects = Data.projects[Data.projects['author_id'] == Data.cur_user_id]
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(curProjects.shape[0])
        self.tableWidget.setColumnCount(3)

        for index, row in curProjects.iterrows():
            curLabel = QLabel(row['name'])
            curLabel.setAlignment(Qt.AlignCenter)
            curLabel.setFont(QFont('Italic', 15))
            curLabel.resize(300, 64)

            curPriority = QLabel(str(row['priority level']))
            curPriority.setAlignment(Qt.AlignCenter)
            curPriority.setFont(QFont('Italic', 15))
            curPriority.resize(300, 64)

            curButton = QPushButton("info")
            curButton.setFont(QFont('Italic', 15))
            curButton.setStyleSheet('background-color: rgb(204,255,255)')
            curButton.clicked.connect(partial(self.projectInfo, int(row['pid'])))
            curButton.resize(200, 64)

            self.tableWidget.setCellWidget(index, 0, curLabel)
            print(2)
            self.tableWidget.setCellWidget(index, 1, curPriority)
            self.tableWidget.setCellWidget(index, 2, curButton)

        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Priority"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem(""))
        scroll = QScrollArea()
        scroll.setWidget(self.tableWidget)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        boxlayout = QVBoxLayout(self)
        boxlayout.addWidget(scroll)

    def projectInfo(self, id):
        self.project = ProjectInfo(id)
        self.project.show()

        self.close()
