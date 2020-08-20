import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from classes import Data


class RegistrationWindow(QWidget, Data):
    def __init__(self):
        QWidget.__init__(self)
        self.curdept = ""
        self.curstatus = ""

        self.initUI()

    def initUI(self):

        self.setWindowIcon(QIcon('web.png'))
        self.resize(650, 570)
        self.setWindowTitle('RegistrationWindow')

        self.firstname = QLineEdit(self)
        self.firstname.setPlaceholderText("First name")
        font = self.firstname.font()
        font.setPointSize(16)
        self.firstname.setFont(font)
        self.firstname.resize(550, 64)
        self.firstname.move(50, 50)
        self.firstname.setStyleSheet('background-color: rgb(204,255,255)')

        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Last Name")
        font = self.lastname.font()
        font.setPointSize(16)
        self.lastname.setFont(font)
        self.lastname.resize(550, 64)
        self.lastname.move(50, 120)
        self.lastname.setStyleSheet('background-color: rgb(204,255,255)')

        self.newpassword = QLineEdit(self)
        self.newpassword.setPlaceholderText("Password")
        font = self.newpassword.font()
        font.setPointSize(16)
        self.newpassword.setFont(font)
        self.newpassword.resize(550, 64)
        self.newpassword.move(50, 190)
        self.newpassword.setStyleSheet('background-color: rgb(204,255,255)')

        self.mail = QLineEdit(self)
        self.mail.setPlaceholderText("Mail address")
        font = self.mail.font()
        font.setPointSize(16)
        self.mail.setFont(font)
        self.mail.resize(550, 64)
        self.mail.move(50, 260)
        self.mail.setStyleSheet('background-color: rgb(204,255,255)')

        self.departmentlabel = QLabel(self)
        self.departmentlabel.setFont(QFont('Italic', 16))
        self.departmentlabel.setText("Department:")
        self.departmentlabel.resize(180, 64)
        self.departmentlabel.move(50, 330)

        department = QComboBox(self)
        department.addItems(['IT', 'Human resources', 'Marketing',
                                  'Finance', 'Operations management'])
        department.setFont(QFont('Italic', 16))
        department.resize(370, 64)
        department.move(230, 330)
        department.setStyleSheet('background-color: rgb(204,255,255)')

        self.curdept = 'IT'
        department.activated[str].connect(self.chooseDepartment)

        self.statuslabel = QLabel(self)
        self.statuslabel.setFont(QFont('Italic', 16))
        self.statuslabel.setText("Status:")
        self.statuslabel.resize(180, 64)
        self.statuslabel.move(50, 400)

        status = QComboBox(self)
        status.addItems(['Employee', 'Supervisor',
                              'Middle manager', 'Top manager'])
        status.setFont(QFont('Italic', 16))
        status.resize(370, 64)
        status.move(230, 400)
        status.setStyleSheet('background-color: rgb(204,255,255)')

        self.curstatus = 'Employee'
        status.activated[str].connect(self.chooseStatus)

        registrationButton = QPushButton('Sign up', self)
        registrationButton.clicked.connect(self.proceedRegistration)
        registrationButton.setFont(QFont('Italic', 16))
        registrationButton.resize(550, 64)
        registrationButton.move(50, 470)
        registrationButton.setStyleSheet('background-color: rgb(100,255,255)')

        self.warning = QLabel(self)
        self.warning.resize(550, 50)
        self.warning.move(50, 10)

    def chooseDepartment(self, text):

        self.curdept = text

    def chooseStatus(self, text):

        self.curstatus = text

    def proceedRegistration(self):

        if len(Data.users[Data.users['mail'] == self.mail.text()]) == 0:
            length = len(Data.users)
            Data.users.loc[length] = [length, self.firstname.text(), self.lastname.text(),
                                      self.newpassword.text(), self.curdept,
                                      self.curstatus, self.mail.text()]
            self.close()

        else:
            self.warning.setStyleSheet('color: red; ')
            self.warning.setText("This mail is already signed up!")
            font = QFont('Italic', 14)
            font.setBold(True)
            self.warning.setFont(font)
            self.warning.setAlignment(Qt.AlignHCenter)
