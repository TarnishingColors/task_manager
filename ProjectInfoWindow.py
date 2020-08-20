import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from classes import Data
from CreateTaskWindow import CreateTask
from datetime import datetime
from functools import partial


class ProjectInfo(QWidget):
    def __init__(self, pid):
        QWidget.__init__(self)
        self.pid = pid

        self.initUI()

    def initUI(self):
        self.resize(1050, 750)
        self.setWindowTitle('MyProject')
        self.setWindowIcon(QIcon('web.png'))

        newTaskButton = QPushButton('Create task', self)
        newTaskButton.clicked.connect(partial(self.taskStuff, self.pid))
        newTaskButton.setFont(QFont('Italic', 16))
        newTaskButton.resize(200, 64)
        newTaskButton.move(840, 5)
        newTaskButton.setStyleSheet('background-color: rgb(100,255,255)')

        self.tableWidget = QTableWidget()

        curTasks = Data.tasks[Data.tasks['project_id'] == self.pid]
        curTasks = curTasks.sort_values(by='deadline')

        self.tableWidget.setRowCount(curTasks.shape[0])
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Due to"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Status"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Edit"))
        i = 0

        for index, row in curTasks.iterrows():
            dead = list(map(int, row['deadline'].split('-')))
            curdead = datetime(dead[0], dead[1], dead[2]).date()
            delta = curdead - Data.current_date
            if delta.days < 0:
                red = 255
                green = 51
                blue = 51
            elif delta.days < 7:
                red = 255
                green = 153
                blue = 51
            else:
                red = 153
                green = 255
                blue = 51

            dead = str(curdead)

            curLabel = QLabel(str(row['name']))
            curLabel.setFont(QFont('Italic', 12))

            curDeadline = QLabel(dead[8:10] + '.' + dead[5:7] + '.' + dead[2:4])
            curDeadline.setFont(QFont('Italic', 12))
            curDeadline.setAlignment(Qt.AlignCenter)

            curStatus = QLabel(str(row['status']))
            curStatus.setAlignment(Qt.AlignCenter)
            curStatus.setFont(QFont('Italic', 12))

            editButton = QPushButton("Change")
            editButton.setFont(QFont('Italic', 12))

            self.tableWidget.setCellWidget(i, 0, curLabel)
            self.tableWidget.setCellWidget(i, 1, curDeadline)
            self.tableWidget.setCellWidget(i, 2, curStatus)
            self.tableWidget.setCellWidget(i, 3, editButton)
            print(4)

            for j in range(3):
                try:
                   self.tableWidget.cellWidget(i, j)\
                       .setStyleSheet('background-color: rgb({0},{1},{2})'.format(red, green, blue))
                except Exception as e:
                    print(e)

            i += 1

        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.setColumnWidth(0, 330)
        self.tableWidget.setColumnWidth(1, 230)
        self.tableWidget.setColumnWidth(2, 230)
        self.tableWidget.setColumnWidth(3, 180)

        scroll = QScrollArea()
        scroll.setWidget(self.tableWidget)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(600)
        boxlayout = QVBoxLayout(self)
        boxlayout.addWidget(scroll)

    def taskStuff(self, pid):
        self.CreateTask = CreateTask(pid)
        self.CreateTask.show()

        self.close()
