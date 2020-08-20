from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from classes import Data
from datetime import datetime
from functools import partial


class byDateWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        self.resize(1550, 650)
        self.setWindowTitle('byDateWindow')
        self.setWindowIcon(QIcon('web.png'))

        grid = QGridLayout()
        commentSection = QGroupBox()

        self.tableWidget = QTableWidget()
        curTasks = Data.tasks[Data.tasks['department'] == Data.cur_user_dept]
        curTasks = curTasks.sort_values(by='deadline')

        self.tableWidget.setRowCount(curTasks.shape[0])
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Due to"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Status"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Edit"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Comments"))
        i = 0
        for index, row in curTasks.iterrows():
            dead = list(map(int, row['deadline'].split('-')))
            curdead = datetime(dead[0], dead[1], dead[2]).date()
            delta = curdead - Data.current_date
            print(Data.current_date, curdead, delta.days)
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
            curLabel.setFont(QFont('Italic', 10))

            curDeadline = QLabel(dead[8:10] + '.' + dead[5:7] + '.' + dead[2:4])
            curDeadline.setFont(QFont('Italic', 10))
            curDeadline.setAlignment(Qt.AlignCenter)

            curStatus = QLabel(str(row['status']))
            curStatus.setAlignment(Qt.AlignCenter)
            curStatus.setFont(QFont('Italic', 10))

            editButton = QPushButton("Edit")
            editButton.setFont(QFont('Italic', 10))

            commentButton = QPushButton("View")
            commentButton.setFont(QFont('Italic', 10))

            self.tableWidget.setCellWidget(i, 0, curLabel)
            self.tableWidget.setCellWidget(i, 1, curDeadline)
            self.tableWidget.setCellWidget(i, 2, curStatus)
            self.tableWidget.setCellWidget(i, 3, editButton)
            self.tableWidget.setCellWidget(i, 4, commentButton)

            for j in range(3):
                try:
                    self.tableWidget.cellWidget(i, j) \
                        .setStyleSheet('background-color: rgb({0},{1},{2})'.format(red, green, blue))
                except Exception as e:
                    print(e)

            i += 1

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        scroll = QScrollArea()
        scroll.setWidget(self.tableWidget)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(600)
        scroll.setFixedWidth(800)
        boxlayout = QVBoxLayout(self)
        boxlayout.addWidget(scroll)

    def viewComments(self, name):
        pass
