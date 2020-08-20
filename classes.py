import pandas as pd
from datetime import datetime


class User:

    def __init__(self, uid, firstname, lastname, password, department, status, mail):
        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.department = department
        self.status = status
        self.mail = mail


class Project:

    def __init__(self, pid, name, author_id, description):
        self.pid = pid
        self.name = name
        self.author_id
        self.description = description


class Task:

    def __init__(self, name, project_id, department, author_id,
                 description, status, start_date, deadline):

        self.name = name
        self.project_id = project_id
        self.department = department
        self.author_id = author_id
        self.description = description
        self.status = status
        self.start_date = start_date
        self.deadline = deadline

    def changeDeadline(self, new_deadline):

        self.deadline = new_deadline


class Data:
    current_date = datetime.now().date()
    users_columns = ['uid', 'firstname', 'lastname', 'password',
                     'department', 'status', 'mail']
    projects_columns = ['pid', 'name', 'author_id',
                        'description', 'department', 'priority level']
    tasks_columns = ['name', 'project_id', 'department', 'author_id',
                     'description', 'status', 'start_date', 'deadline']
    comments_columns = ['task_id', 'text', 'author_name']

    users = pd.read_csv('users.csv', names=users_columns)
    projects = pd.read_csv('projects.csv', names=projects_columns)
    tasks = pd.read_csv('tasks.csv', names=tasks_columns)
    comments = pd.read_csv('comments.csv', names=comments_columns)
    cur_user_id = -1
    cur_user_dept = ""


