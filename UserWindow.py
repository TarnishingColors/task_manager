from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CreateProjectWindow import CreateProjectWindow
from ControlProjectsWindow import ControlProjectsWindow
from byProjectWindow import byProjectWindow
from byPriorityWindow import byPriorityWindow
from byDateWindow import byDateWindow
from KanbanWindow import KanbanBoard
from classes import Data
import os
import plotly.figure_factory as ff


class UserWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):

        self.resize(700, 500)
        self.setWindowTitle('UserWindow')
        self.setWindowIcon(QIcon('web.png'))

        self.optionlabel = QLabel(self)
        self.optionlabel.setText("Choose an option from below")
        self.optionlabel.setAlignment(Qt.AlignHCenter)
        self.optionlabel.setFont(QFont('Italic', 20))
        self.optionlabel.resize(600, 64)
        self.optionlabel.move(50, 50)

        createProjectButton = QPushButton("Create project", self)
        createProjectButton.setFont(QFont('Italic', 16))
        createProjectButton.clicked.connect(self.createProject)
        createProjectButton.resize(300, 64)
        createProjectButton.move(375, 150)
        createProjectButton.setStyleSheet('background-color: rgb(100,255,255)')

        controlProjectButton = QPushButton("Control projects", self)
        controlProjectButton.setFont(QFont('Italic', 16))
        controlProjectButton.clicked.connect(self.controlProjects)
        controlProjectButton.resize(300, 64)
        controlProjectButton.move(375, 250)
        controlProjectButton.setStyleSheet('background-color: rgb(100,255,255)')

        ganttButton = QPushButton("Show Gantt Chart", self)
        ganttButton.setFont(QFont('Italic', 16))
        ganttButton.clicked.connect(self.showGanttChart)
        ganttButton.resize(300, 64)
        ganttButton.move(375, 350)
        ganttButton.setStyleSheet('background-color: rgb(100,255,255)')

        self.button = QToolButton(self)
        self.button.resize(200, 64)
        self.button.setText("Nibba")
        self.button.setPopupMode(QToolButton.MenuButtonPopup)
        self.button.setMenu(QMenu(self.button))
        self.button.move(50, 150)
        self.textBox = QTextBrowser(self)
        action = QWidgetAction(self.button)
        action.setDefaultWidget(self.textBox)
        self.button.menu().addAction(action)

        self.taskslabel = QLabel("Show tasks:", self)
        self.taskslabel.setFont(QFont('Italic', 16))
        self.taskslabel.resize(300, 64)
        self.taskslabel.setStyleSheet('background-color: rgb(100, 255, 255)')
        self.taskslabel.move(50, 150)
        self.taskslabel.setAlignment(Qt.AlignCenter)

        taskSort = QComboBox(self)
        taskSort.addItems(['by project', 'by priority',
                              'by date', 'kanban-board'])
        taskSort.setFont(QFont('Italic', 16))
        taskSort.setStyleSheet('background-color: rgb(100, 255, 255)')
        taskSort.resize(300, 64)
        taskSort.move(50, 214)

        taskSort.activated[str].connect(self.sortingProjects)

    def sortingProjects(self, text):

        if text == 'by project':
            self.byProjectWindow = byProjectWindow()
            self.byProjectWindow.show()

        elif text == 'by priority':
            self.byPriorityWindow = byPriorityWindow()
            self.byPriorityWindow.show()

        elif text == 'by date':
            self.byDateWindow = byDateWindow()
            self.byDateWindow.show()

        else:
            self.kanban = KanbanBoard()
            self.kanban.show()

    def createProject(self):

        self.createProjectW = CreateProjectWindow()
        self.createProjectW.show()

    def controlProjects(self):

        self.controlProjectsW = ControlProjectsWindow()
        self.controlProjectsW.show()

    def showGanttChart(self):

        curTasks = Data.tasks[Data.tasks['department'] == Data.cur_user_dept]
        df = []
        for index, task in curTasks.iterrows():
            df.append(dict(Task=task['name'], Start=task['start_date'], Finish=task['deadline']))

        fig = ff.create_gantt(df)
        fig.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                    "Are you sure you want to quit?",
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            os.remove('users.csv')
            os.remove('projects.csv')
            os.remove('tasks.csv')
            Data.projects.to_csv('projects.csv', index=False, header=False)
            Data.tasks.to_csv('tasks.csv', index=False, header=False)
            Data.users.to_csv('users.csv', index=False, header=False)
            Data.comments.to_csv('comments.csv', index=False, header=False)
            event.accept()
        else:
            event.ignore()
