import requests
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
import time

import add_new_student
import add_pannel
import add_new_teacher
import add_new_class
import enter
import enter_teacher
import enter_admin
import del_student
import del_class
import del_teacher
import connect_group_by_admin
import chat_of_admin
import chat_of_user
import show_students
import user_profile
import my_user_profile
import edit_my_user_profile
import teachers_groups

num_click = 0


class AddNewStudent(QtWidgets.QWidget, add_new_student.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name_get = name
        self.surname = surname
        self.unical_code_get = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)
        self.create_btn.clicked.connect(self.create_student)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name_get, self.surname, self.unical_code_get, self.login)
        self.start.show()

    def create_student(self):
        class_index = self.enter_index_input.text()
        name = self.enter_name_input.text()
        surname = self.enter_surname_input.text()
        middle_name = self.enter_middle_name_input.text()
        username = self.enter_login_input.text()
        password = self.enter_password_input.text()
        data = {'class_index': class_index, 'name': name, 'surname': surname, 'middle_name': middle_name, 'username': username, 'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/add_student', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Ученик добавлен')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class AdministratorPanel(QtWidgets.QWidget, add_pannel.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.name_label.setText(self.name + ' ' + self.surname)
        self.name_label.setObjectName(self.unical_code)
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)
        self.delete_class_btn.clicked.connect(self.delete_class)
        self.delete_student_btn.clicked.connect(self.delete_student)
        self.connect_chat_btn.clicked.connect(self.connect_class)
        self.add_new_class_btn.clicked.connect(self.add_new_class)
        self.add_new_student_btn.clicked.connect(self.add_new_student)
        self.add_new_teacher_btn.clicked.connect(self.add_new_teacher)

        try:
            data = requests.get('http://127.0.0.1:5000/get_all_groups').json()
        except:
            return
        print(data)
        for i in range(0, len(data['result'])):
            if data["result"][i][0][0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                add_layout = QHBoxLayout()
                a = data["result"][i][0][-1]
                lst = list(data["result"][i][0])
                lst.pop(-1)
                new = ''.join(lst)
                new_str = new + ' ' + a
                new_btn = QPushButton(f'{new_str}')
                new_btn.setMinimumHeight(50)
                new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(193, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(139, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(225, 100, 100);\n"
"border-radius: 10px;\n"
"}")
                new_btn.setObjectName(f'{data["result"][i][0]}')
                new_btn.clicked.connect(self.connect_my_groups)
                # new_btn.setMaximumSize(200, 40)
                add_layout.addWidget(new_btn)
                print(new_btn.objectName())
                self.scrollAreaLayout.addLayout(add_layout)
            else:
                add_layout = QHBoxLayout()
                new_btn = QPushButton(f'{data["result"][i][0]}')
                new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(193, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(139, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(225, 100, 100);\n"
"border-radius: 10px;\n"
"}")
                new_btn.setMinimumHeight(50)
                new_btn.setGeometry(QtCore.QRect(10, 10, 410, 60))
                new_btn.setMinimumSize(QtCore.QSize(30, 60))
                new_btn.setObjectName(f'{data["result"][i][0]}')
                new_btn.clicked.connect(self.connect_my_groups)
                # new_btn.setMaximumSize(200, 40)
                add_layout.addWidget(new_btn)
                print(new_btn.objectName())
                self.scrollAreaLayout.addLayout(add_layout)

    def connect_my_groups(self):
        sender = self.sender()
        class_name = sender.text()
        class_name = class_name.replace(' ', '')
        self.close()
        self.start = MessagesWindowConnectionAdmin(self.name, self.surname, self.unical_code, self.login, class_name)
        self.start.show()

    def exit_to_main_pannel(self):
        self.close()
        self.start = Enter()
        self.start.show()

    # def show_my_groups(self):
    #     self.close()
    #     self.start = AdminGroups(self.name, self.surname, self.unical_code, self.login)
    #     self.start.show()

    def delete_class(self):
        self.close()
        self.start = DelClass(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def delete_student(self):
        self.close()
        self.start = DelStudent(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def connect_class(self):
        self.close()
        self.start = ConnectGroupByAdmin(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def add_new_class(self):
        self.close()
        self.start = AddNewClass(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def add_new_student(self):
        self.close()
        self.start = AddNewStudent(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def add_new_teacher(self):
        self.close()
        self.start = AddNewTeacher(self.name, self.surname, self.unical_code, self.login)
        self.start.show()


class AddNewTeacher(QtWidgets.QWidget, add_new_teacher.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)
        self.create_btn.clicked.connect(self.create_teacher)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def create_teacher(self):
        name = self.enter_name_input.text()
        surname = self.enter_surname_input.text()
        middle_name = self.enter_middle_name_input.text()
        username = self.enter_login_input.text()
        password = self.enter_password_input.text()
        data = {'name': name, 'surname': surname, 'middle_name': middle_name,
                'username': username, 'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/add_teacher', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Учитель добавлен')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class AddNewClass(QtWidgets.QWidget, add_new_class.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.create_btn.clicked.connect(self.create_class)
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def create_class(self):
        letter = self.class_letter_input.text()
        index = self.unical_id_class_input.text()
        unical_code = self.unical_id_class_input.text()
        data = {'letter': letter, 'index': index, 'unical_code': unical_code}
        try:
            response = requests.post('http://127.0.0.1:5000/add_class', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Класс добавлен')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class Enter(QtWidgets.QWidget, enter.Ui_Form):
    def __init__(self):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.enter_btn.clicked.connect(self.enter)
        self.admin_btn.clicked.connect(self.go_to_admin)
        self.teacher_btn.clicked.connect(self.go_to_teacher)

    def go_to_admin(self):
        self.close()
        self.start = EnterAdmin()
        self.start.show()

    def go_to_teacher(self):
        self.close()
        self.start = EnterTeacher()
        self.start.show()

    def enter(self):
        username = self.enter_login.text()
        password = self.enter_password.text()
        data = {'username': username, 'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/enter_user', json=data)
        except:
            return
        if response.status_code == 200:
            try:
                data = requests.get('http://127.0.0.1:5000/enter_user', params={'username': username}).json()
            except:
                return
            self.close()
            self.start = MessagesWindowUsers(data['name'], data['surname'], data['unical_code'], data['login'], data['class_index'])
            self.start.show()


class EnterTeacher(QtWidgets.QWidget, enter_teacher.Ui_Form):
    def __init__(self):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.return_btn_teacher.clicked.connect(self.go_to_enter)
        self.enter_btn_teacher.clicked.connect(self.enter_teacher)

    def go_to_enter(self):
        self.close()
        self.start = Enter()
        self.start.show()

    def enter_teacher(self):
        username = self.enter_login_teacher.text()
        password = self.enter_password_teacher.text()
        data = {'username': username, 'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/enter_teacher', json=data)
        except:
            return
        if response.status_code == 200:
            try:
                data = requests.get('http://127.0.0.1:5000/enter_teacher', params={'username': username}).json()
            except:
                return
            self.close()
            self.start = TeachersGroups(data['name'], data['surname'], data['unical_code'], data['login'])
            self.start.show()



class EnterAdmin(QtWidgets.QWidget, enter_admin.Ui_Form):
    def __init__(self):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.return_btn_admin.clicked.connect(self.go_to_enter)
        self.enter_btn_admin.clicked.connect(self.enter_admin)

    def go_to_enter(self):
        self.close()
        self.start = Enter()
        self.start.show()

    def enter_admin(self):
        username = self.enter_login_admin.text()
        password = self.enter_password_admin.text()
        data = {'username': username, 'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/enter_admin', json=data)
        except:
            return
        if response.status_code == 200:
            try:
                data = requests.get('http://127.0.0.1:5000/enter_admin', params={'username': username}).json()
            except:
                return
            self.close()
            self.start = AdministratorPanel(data['name'], data['surname'], data['unical_code'], data['login'])
            self.start.show()


class DelStudent(QtWidgets.QWidget, del_student.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def delete_one_student(self):
        unical_code_student = self.unical_code_input.text()
        admin_password = self.delete_admin_password_input.text()
        data = {'unical_code_student': unical_code_student, 'admin_password': admin_password}
        try:
            response = requests.post('http://127.0.0.1:5000/delete_student', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Ученик удалён')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class DelClass(QtWidgets.QWidget, del_class.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)
        self.del_btn.clicked.connect(self.delete_one_class)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def delete_one_class(self):
        unical_code_student = self.unical_code_input.text()
        admin_password = self.delete_admin_password_input.text()
        data = {'unical_code_student': unical_code_student, 'admin_password': admin_password}
        try:
            response = requests.post('http://127.0.0.1:5000/delete_class', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Класс удалён')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class DelTeacher(QtWidgets.QWidget, del_teacher.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)

    def delete_one_teacher(self):
        unical_code_student = self.unical_code_input.text()
        admin_password = self.delete_admin_password_input.text()
        data = {'unical_code_student': unical_code_student, 'admin_password': admin_password}
        try:
            response = requests.post('http://127.0.0.1:5000/delete_teacher', json=data)
        except:
            return
        if response.status_code == 200:
            error = QtWidgets.QMessageBox()
            error.setText('Учитель удалён')
            error.setWindowTitle('Диалоговое окно')
            error.exec_()
            self.close()
        else:
            return


class ConnectGroupByAdmin(QtWidgets.QWidget, connect_group_by_admin.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_to_main_pannel)
        self.connect_btn.clicked.connect(self.connection)

    def exit_to_main_pannel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()

    def connection(self):
        other_unical_code = self.unical_code_input.text()
        password = self._admin_password_input.text()
        data = {'password': password}
        try:
            response = requests.post('http://127.0.0.1:5000/connect_group_by_admin', json=data)
        except:
            return
        if response.status_code == 200:
            try:
                data = requests.get('http://127.0.0.1:5000/connect_group_by_admin',
                                    params={'other_unical_code': other_unical_code}).json()
            except:
                return
            self.close()
            self.start = MessagesWindowConnectionAdmin(self.name, self.surname, self.unical_code, self.login, data['name_of_class'])
            self.start.show()


# class AdminGroups(QtWidgets.QWidget, admin_groups.Ui_Form):
#     def __init__(self, name, surname, unical_code, login):
#         super().__init__()
#         # Подключение настроек
#         self.setupUi(self)
#         self.name = name
#         self.surname = surname
#         self.unical_code = unical_code
#         self.login = login
#         self.exit_btn.clicked.connect(self.exit_to_main_pannel)
#         try:
#             data = requests.get('http://127.0.0.1:5000/get_all_groups').json()
#         except:
#             return
#         print(data)
#         for i in range(0, len(data['result'])):
#             add_layout = QHBoxLayout()
#             new_btn = QPushButton(f'{data["result"][i]}')
#             new_btn.setMinimumHeight(20)
#             new_btn.setObjectName(f"{data['result'][i]}")
#             # new_btn.clicked.connect(self.return_to_chat)
#             new_btn.setMaximumSize(200, 40)
#             add_layout.addWidget(new_btn)
#             print(new_btn.objectName())
#             self.scrollAreaLayout.addLayout(add_layout)
#         self.label.setText(self.name + ' ' + self.surname)
#
#     def exit_to_main_pannel(self):
#         self.close()
#         self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
#         self.start.show()


class TeachersGroups(QtWidgets.QWidget, teachers_groups.Ui_Form):
    def __init__(self, name, surname, unical_code, login):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.exit_btn.clicked.connect(self.exit_from)
        try:
            data = requests.get('http://127.0.0.1:5000/get_all_groups_teachers', params={'unical_code': unical_code}).json()
        except:
            return
        print(data)
        for i in range(0, len(data['result'])):
            if data["result"][i][0][0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                add_layout = QHBoxLayout()
                a = data["result"][i][0][-1]
                lst = list(data["result"][i][0])
                lst.pop(-1)
                new = ''.join(lst)
                new_str = new + ' ' + a
                new_btn = QPushButton(f'{new_str}')
                new_btn.setMinimumHeight(20)
                new_btn.setObjectName(f'{data["result"][i][0]}')
                new_btn.clicked.connect(self.return_to_chat)
                new_btn.setMaximumSize(200, 40)
                add_layout.addWidget(new_btn)
                print(new_btn.objectName())
                self.scrollAreaLayout.addLayout(add_layout)
            else:
                add_layout = QHBoxLayout()
                new_btn = QPushButton(f'{data["result"][i][0]}')
                new_btn.setMinimumHeight(20)
                new_btn.setObjectName(f'{data["result"][i][0]}')
                new_btn.clicked.connect(self.return_to_chat)
                new_btn.setMaximumSize(200, 40)
                add_layout.addWidget(new_btn)
                print(new_btn.objectName())
                self.scrollAreaLayout.addLayout(add_layout)

    def exit_from(self):
        self.close()
        self.start = Enter()
        self.start.show()

    def return_to_chat(self):
        sender = self.sender()
        class_name = sender.text()
        class_name = class_name.replace(' ', '')
        self.close()
        self.start = MessagesWindowConnectionTeacher(self.name, self.surname, self.unical_code, self.login, class_name)
        self.start.show()


class MessagesWindowConnectionAdmin(QtWidgets.QWidget, chat_of_admin.Ui_Form):
    def __init__(self, name, surname, unical_code, login, class_name):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.class_name = class_name
        # Подключение кнопки отправки сообщений
        self.btn_send.clicked.connect(self.send_message)
        self.menu_btn.clicked.connect(self.show_users)
        self.exit_btn.clicked.connect(self.exit_to_admin_panel)
        # Определение встроенного таймера отпрвки сообщения
        self.timer = QtCore.QTimer()
        # Подключение таймера к функции отправки сообщений
        self.timer.timeout.connect(self.load_messages)
        # Определение разницы между GET и POST запросами на сервер
        self.timer.start(1000)
        # Определение параметра сортировки сообщений по времени
        self.after = 0
        self.layoutList = []
        self.send_area.setText(' ')

        # Добавление имени, забранного с поля регистрации
        self.name_user.setText(self.name + ' ' + self.surname)
        self.name_user.setStyleSheet('color: rgb(100, 252, 200)')
        if self.class_name[0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            a = self.class_name[-1]
            lst = list(self.class_name)
            lst.pop(-1)
            new = ''.join(lst)
            new_str = new + ' ' + a
            self.name_other_user.setText(new_str)
        else:
            self.name_other_user.setText(self.class_name)
        self.load_messages()


    def show_users(self):
        # self.close()
        self.start = ShowStudents(self.name, self.surname, self.unical_code, self.class_name)
        self.start.show()

    def exit_to_admin_panel(self):
        self.close()
        self.start = AdministratorPanel(self.name, self.surname, self.unical_code, self.login)
        self.start.show()
        self.timer.stop()

    def send_message(self):
        global num_click
        if self.send_area.text() != ' ':
            num_click += 1
            name = self.name_user.text()
            text = self.send_area.text()
            print(f'unical_code - {self.unical_code}')
            data = {'name': name, 'text': text, 'unical_code': self.unical_code, 'class_index': self.class_name}
            try:
                response = requests.post('http://127.0.0.1:5000/send', json=data)
            except:
                error = QtWidgets.QMessageBox()
                error.setText('Сервер не отвечает')
                error.setWindowTitle('Ошибка')
                error.exec_()
                return
            if response.status_code != 200:
                return
        self.load_messages()

    def pretty_messages(self, message):
        add_layout = QHBoxLayout()
        add_layout.setObjectName(f'{num_click}')

        new_btn = QPushButton('X')
        new_btn.setMinimumHeight(30)
        try:
            data = requests.get('http://127.0.0.1:5000/send', params={'time': message['time'], 'class_name': self.class_name}).json()
        except:
            return
        if data['id'] is not None and data['isadmin'] == 'True':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            new_text.setStyleSheet('color: rgb(255, 215, 0)')
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        elif data['id'] is not None and data['isadmin'] == 'False':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        else:
            print(self.layoutList)

    # Подключаем функцию загрузки сообщений в поле просмотра сообщений
    def load_messages(self):
        try:
            data = requests.get('http://127.0.0.1:5000/messages', params={'after': self.after}).json()
        except:
            return

        # Вывод сообщений в поле просмотра сообщений на основе параметра json
        for message in data['messages']:
            self.pretty_messages(message)
            self.after = message['time']

    def delete_message(self):
        sender = self.sender()
        name = sender.objectName()
        widget_id = self.layoutList.index(name)
        data = {'id': int(name), 'class_name': self.class_name, 'my_unical_code': self.unical_code}
        try:
            response = requests.post('http://127.0.0.1:5000/delmessage', json=data)
        except:
            return
        if response.status_code == 200:
            print(name)
            print(widget_id)
            print(self.layoutList)

            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(0).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(1).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().deleteLater()
            self.layoutList.pop(widget_id)


class MessagesWindowConnectionTeacher(QtWidgets.QWidget, chat_of_admin.Ui_Form):
    def __init__(self, name, surname, unical_code, login, class_name):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.class_name = class_name
        # Подключение кнопки отправки сообщений
        self.btn_send.clicked.connect(self.send_message)
        self.menu_btn.clicked.connect(self.show_users)
        self.exit_btn.clicked.connect(self.exit_to_admin_panel)
        # Определение встроенного таймера отпрвки сообщения
        self.timer = QtCore.QTimer()
        # Подключение таймера к функции отправки сообщений
        self.timer.timeout.connect(self.load_messages)
        # Определение разницы между GET и POST запросами на сервер
        self.timer.start(1000)
        # Определение параметра сортировки сообщений по времени
        self.after = 0
        self.layoutList = []
        self.send_area.setText(' ')

        # Добавление имени, забранного с поля регистрации
        self.name_user.setText(self.name + ' ' + self.surname)
        self.name_user.setStyleSheet('color: rgb(124, 252, 0)')
        if self.class_name[0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            a = self.class_name[-1]
            lst = list(self.class_name)
            lst.pop(-1)
            new = ''.join(lst)
            new_str = new + ' ' + a
            self.name_other_user.setText(new_str)
        else:
            self.name_other_user.setText(self.class_name)
        self.load_messages()


    def show_users(self):
        # self.close()
        self.start = ShowStudents(self.name, self.surname, self.unical_code, self.class_name)
        self.start.show()

    def exit_to_admin_panel(self):
        self.close()
        self.start = TeachersGroups(self.name, self.surname, self.unical_code, self.login)
        self.start.show()
        self.timer.stop()

    def send_message(self):
        if self.class_name == 'School_news':
            pass
        else:
            global num_click
            if self.send_area.text() != ' ':
                num_click += 1
                name = self.name_user.text()
                text = self.send_area.text()
                print(f'unical_code - {self.unical_code}')
                data = {'name': name, 'text': text, 'unical_code': self.unical_code, 'class_index': self.class_name}
                try:
                    response = requests.post('http://127.0.0.1:5000/send', json=data)
                except:
                    error = QtWidgets.QMessageBox()
                    error.setText('Сервер не отвечает')
                    error.setWindowTitle('Ошибка')
                    error.exec_()
                    return
                if response.status_code != 200:
                    return
            self.load_messages()

    def pretty_messages(self, message):
        add_layout = QHBoxLayout()
        add_layout.setObjectName(f'{num_click}')

        new_btn = QPushButton('X')
        new_btn.setMinimumHeight(30)
        try:
            data = requests.get('http://127.0.0.1:5000/send', params={'time': message['time'], 'class_name': self.class_name}).json()
        except:
            return
        if data['id'] is not None and data['isadmin'] == 'True':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            new_text.setStyleSheet('color: rgb(255, 215, 0)')
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        elif data['id'] is not None and data['isadmin'] == 'False':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        else:
            print(self.layoutList)

    # Подключаем функцию загрузки сообщений в поле просмотра сообщений
    def load_messages(self):
        try:
            data = requests.get('http://127.0.0.1:5000/messages', params={'after': self.after}).json()
        except:
            return

        # Вывод сообщений в поле просмотра сообщений на основе параметра json
        for message in data['messages']:
            self.pretty_messages(message)
            self.after = message['time']

    def delete_message(self):
        sender = self.sender()
        name = sender.objectName()
        widget_id = self.layoutList.index(name)
        data = {'id': int(name), 'class_name': self.class_name, 'my_unical_code': self.unical_code}
        try:
            response = requests.post('http://127.0.0.1:5000/delmessage', json=data)
        except:
            return
        if response.status_code == 200:
            print(name)
            print(widget_id)
            print(self.layoutList)

            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(0).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(1).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().deleteLater()
            self.layoutList.pop(widget_id)

    def none_action(self):
        pass

class MessagesWindowUsers(QtWidgets.QWidget, chat_of_user.Ui_Form):
    def __init__(self, name, surname, unical_code, login, class_name):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.login = login
        self.class_name = class_name
        # Подключение кнопки отправки сообщений
        self.btn_send.clicked.connect(self.send_message)
        # Подключение кнопки перехода на окно редактирования кода
        self.exit_btn.clicked.connect(self.exit_to_admin_panel)
        self.menu_btn.clicked.connect(self.show_users)
        self.name_user_btn.clicked.connect(self.open_profile)
        # Определение встроенного таймера отпрвки сообщения
        self.timer = QtCore.QTimer()
        # Подключение таймера к функции отправки сообщений
        self.timer.timeout.connect(self.load_messages)
        # Определение разницы между GET и POST запросами на сервер
        self.timer.start(1000)
        # Определение параметра сортировки сообщений по времени
        self.after = 0
        self.layoutList = []
        self.send_area.setText(' ')

        # Добавление имени, забранного с поля регистрации
        print(self.name)
        print(self.surname)
        print(self.class_name)
        self.name_user_btn.setText(self.name + ' ' + self.surname)
        self.name_other_user.setText(self.class_name)

    def show_users(self):
        # self.close()
        self.start = ShowStudents(self.name, self.surname, self.unical_code, self.class_name)
        self.start.show()

    def exit_to_admin_panel(self):
        self.close()
        self.start = Enter()
        self.start.show()
        self.timer.stop()

    def send_message(self):
        global num_click
        if self.send_area.text() != ' ':
            num_click += 1
            name = self.name_user_btn.text()
            text = self.send_area.text()
            print(f'unical_code - {self.unical_code}')
            data = {'name': name, 'text': text, 'unical_code': self.unical_code, 'class_index': self.class_name.replace(' ', '')}
            try:
                response = requests.post('http://127.0.0.1:5000/send', json=data)
            except:
                error = QtWidgets.QMessageBox()
                error.setText('Сервер не отвечает')
                error.setWindowTitle('Ошибка')
                error.exec_()
                return
            if response.status_code != 200:
                return
        self.load_messages()

    def pretty_messages(self, message):
        add_layout = QHBoxLayout()
        add_layout.setObjectName(f'{num_click}')

        new_btn = QPushButton('X')
        new_btn.setMinimumHeight(30)
        try:
            data = requests.get('http://127.0.0.1:5000/send', params={'time': message['time'], 'class_name': self.class_name.replace(' ', '')}).json()
        except:
            return
        if data['id'] is not None and data['isadmin'] == 'True':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            new_text.setStyleSheet('color: rgb(255, 215, 0)')
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        elif data['id'] is not None and data['isadmin'] == 'False':
            print(data)
            new_btn.setObjectName(str(data['id']))
            new_btn.clicked.connect(self.delete_message)
            new_btn.setMaximumSize(35, 50)

            new_text = QLabel(f'''{time.strftime("%d:%m:%Y:%H:%M:%S", time.localtime(message['time']))}
            ''' + message['name'] + ': ' + message['text'])
            new_text.setMinimumHeight(50)
            add_layout.addWidget(new_text)
            add_layout.addWidget(new_btn)

            self.scrollAreaLayout.addLayout(add_layout)
            self.layoutList.append(str(data['id']))
            print(self.layoutList)

            self.send_area.setText(' ')

            print(time.strftime("%H:%M:%S", time.localtime(message['time'])))
            print(message['time'])
        else:
            print(self.layoutList)

    # Подключаем функцию загрузки сообщений в поле просмотра сообщений
    def load_messages(self):
        try:
            data = requests.get('http://127.0.0.1:5000/messages', params={'after': self.after}).json()
        except:
            return

        # Вывод сообщений в поле просмотра сообщений на основе параметра json
        for message in data['messages']:
            self.pretty_messages(message)
            self.after = message['time']

    def delete_message(self):
        sender = self.sender()
        name = sender.objectName()
        widget_id = self.layoutList.index(name)
        data = {'id': int(name), 'class_name': self.class_name.replace(' ', ''), 'my_unical_code': self.unical_code}
        try:
            response = requests.post('http://127.0.0.1:5000/delmessage', json=data)
        except:
            return
        if response.status_code == 200:
            print(name)
            print(widget_id)
            print(self.layoutList)

            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(0).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().itemAt(1).widget().deleteLater()
            self.scrollAreaLayout.itemAt(widget_id).layout().deleteLater()
            self.layoutList.pop(widget_id)
        else:
            pass

    def open_profile(self):
        response = requests.get('http://127.0.0.1:5000/get_info_about_user',
                                params={'unical_code': self.unical_code}).json()
        # self.close()
        self.start = MyUserProfile(self.name, self.surname, self.unical_code, self.class_name,
                                   response['other_class_index'], response['name'], response['surname'],
                                   response['middle_name'], self.unical_code, response['status'],
                                   response['about_user'], response['phone_number'], response['avatar_photo'])
        self.start.show()


class ShowStudents(QtWidgets.QWidget, show_students.Ui_Form):
    def __init__(self, name, surname, unical_code, class_index):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.class_index = class_index
        print(self.class_index)
        try:
            data = requests.get('http://127.0.0.1:5000/show_students', params={'class_index': self.class_index.replace(' ', '')}).json()
        except:
            return
        print(data)
        for i in range(0, len(data['result'])):
            if str(class_index[0]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                if data["result"][i][2] != self.unical_code:
                    if data["result"][i][3] == 'True':
                        add_layout = QHBoxLayout()
                        new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                        # new_btn.setStyleSheet('color: rgb(255, 215, 0)')
                        new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(193, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(139, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(225, 100, 100);\n"
"border-radius: 10px;\n"
"}")
                        new_btn.setMinimumHeight(50)
                        new_btn.setObjectName(f'{data["result"][i][2]}')
                        # new_btn.clicked.connect(self.return_to_profile)
                        # new_btn.setMaximumSize(150, 20)
                        add_layout.addWidget(new_btn)
                        print(new_btn.objectName())
                        self.scrollAreaLayout.addLayout(add_layout)
                    else:

                        add_layout = QHBoxLayout()
                        new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                        new_btn.setMinimumHeight(50)
                        new_btn.setObjectName(f'{data["result"][i][2]}')
                        new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 0, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(12, 0, 185);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 193, 255);\n"
"border-radius: 10px;\n"
"}")
                        new_btn.clicked.connect(self.return_to_profile)
                        # new_btn.setMaximumSize(150, 20)
                        add_layout.addWidget(new_btn)
                        print(new_btn.objectName())
                        self.scrollAreaLayout.addLayout(add_layout)
            else:
                if data["result"][i][2] != self.unical_code:
                    if data["result"][i][3] == 'True':
                        add_layout = QHBoxLayout()
                        new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                        # new_btn.setStyleSheet('color: rgb(255, 215, 0)')
                        new_btn.setMinimumHeight(50)
                        new_btn.setObjectName(f'{data["result"][i][2]}')
                        new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(193, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(139, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(225, 100, 100);\n"
"border-radius: 10px;\n"
"}")
                        # new_btn.clicked.connect(self.return_to_profile)
                        # new_btn.setMaximumSize(150, 20)
                        add_layout.addWidget(new_btn)
                        print(new_btn.objectName())
                        self.scrollAreaLayout.addLayout(add_layout)
                    else:
                        if len(data["result"][i][2]) < 15:
                            add_layout = QHBoxLayout()
                            new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                            new_btn.setMinimumHeight(50)
                            new_btn.setObjectName(f'{data["result"][i][2]}')
                            new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 0, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(12, 0, 185);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 193, 255);\n"
"border-radius: 10px;\n"
"}")
                            # new_btn.clicked.connect(self.return_to_profile)
                            # new_btn.setMaximumSize(150, 20)
                            add_layout.addWidget(new_btn)
                            print(new_btn.objectName())
                            self.scrollAreaLayout.addLayout(add_layout)
                        else:
                            add_layout = QHBoxLayout()
                            new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                            new_btn.setMinimumHeight(50)
                            new_btn.setObjectName(f'{data["result"][i][2]}')
                            new_btn.setStyleSheet("QPushButton:hover{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 0, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(12, 0, 185);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 193, 255);\n"
"border-radius: 10px;\n"
"}")
                            new_btn.clicked.connect(self.return_to_profile)
                            # new_btn.setMaximumSize(150, 20)
                            add_layout.addWidget(new_btn)
                            print(new_btn.objectName())
                            self.scrollAreaLayout.addLayout(add_layout)

    def return_to_profile(self):
        sender = self.sender()
        response = requests.get('http://127.0.0.1:5000/get_info_about_user', params={'unical_code': sender.objectName()}).json()
        self.close()
        self.start = UserProfile(self.name, self.surname, self.unical_code, self.class_index, response['other_class_index'], response['name'], response['surname'],
                                 response['middle_name'], sender.objectName(), response['status'], response['about_user'], response['phone_number'], response['avatar_photo'])
        self.start.show()


class ShowTeachers(QtWidgets.QWidget, show_students.Ui_Form):
    def __init__(self, name, surname, unical_code, class_index):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.class_index = class_index
        print(self.class_index)
        try:
            data = requests.get('http://127.0.0.1:5000/show_students', params={'class_index': self.class_index.replace(' ', '')}).json()
        except:
            return
        print(data)
        for i in range(0, len(data['result'])):
            if data["result"][i][2] != self.unical_code:
                if data["result"][i][3] == 'True':
                    add_layout = QHBoxLayout()
                    new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                    new_btn.setStyleSheet('color: rgb(255, 215, 0)')
                    new_btn.setMinimumHeight(20)
                    new_btn.setObjectName(f'{data["result"][i][2]}')
                    # new_btn.clicked.connect(self.return_to_profile)
                    new_btn.setMaximumSize(150, 20)
                    add_layout.addWidget(new_btn)
                    print(new_btn.objectName())
                    self.scrollAreaLayout.addLayout(add_layout)
                else:
                    add_layout = QHBoxLayout()
                    new_btn = QPushButton(f'{data["result"][i][0]} {data["result"][i][1]}')
                    new_btn.setMinimumHeight(20)
                    new_btn.setObjectName(f'{data["result"][i][2]}')
                    # new_btn.clicked.connect(self.return_to_profile)
                    new_btn.setMaximumSize(150, 20)
                    add_layout.addWidget(new_btn)
                    print(new_btn.objectName())
                    self.scrollAreaLayout.addLayout(add_layout)

    # def return_to_profile(self):
    #     sender = self.sender()
    #     response = requests.get('http://127.0.0.1:5000/get_info_about_user', params={'unical_code': sender.objectName()}).json()
    #     self.close()
    #     self.start = UserProfile(self.name, self.surname, self.unical_code, self.class_index, response['other_class_index'], response['name'], response['surname'],
    #                              response['middle_name'], sender.objectName(), response['status'], response['about_user'], response['phone_number'], response['avatar_photo'])
    #     self.start.show()


class UserProfile(QtWidgets.QWidget, user_profile.Ui_Form):
    def __init__(self, name, surname, unical_code, class_name, other_class_index, other_name, other_surname, other_midle_name, other_unical_code, other_status, other_info_about_user,
                 other_phone_number, other_avatar_photo):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.class_name = class_name
        self.other_class_index = other_class_index
        self.other_name = other_name
        self.other_surname = other_surname
        self.other_middle_name = other_midle_name
        self.other_unical_code = other_unical_code
        self.other_status = other_status
        self.other_info_about_user = other_info_about_user
        self.other_phone_number = other_phone_number
        self.other_avatar_photo = other_avatar_photo

        # self.name_label.setText(self.other_name)
        # self.surname_label.setText(self.other_surname)
        # self.middle_name_label.setText(self.other_middle_name)
        self.name_surname_middle_name.setText(self.other_surname + ' ' + self.other_name + ' ' + self.other_middle_name)
        self.status_label.setText(self.other_status)
        self.about_user_label.setText(other_info_about_user)
        self.phone_number_label.setText(self.other_phone_number)
        self.class_label.setText(self.other_class_index)

        self.exit_btn.clicked.connect(self.exit_from)
        # self.write_to_user_btn.clicked.connect(self.write_to_user)

    def exit_from(self):
        self.close()

    def write_to_user(self):
        pass


class MyUserProfile(QtWidgets.QWidget, my_user_profile.Ui_Form):
    def __init__(self, name, surname, unical_code, class_name, other_class_index, other_name, other_surname, other_midle_name, other_unical_code, other_status, other_info_about_user,
                 other_phone_number, other_avatar_photo):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.class_name = class_name
        self.other_class_index = other_class_index
        self.other_name = other_name
        self.other_surname = other_surname
        self.other_middle_name = other_midle_name
        self.other_unical_code = other_unical_code
        self.other_status = other_status
        self.other_info_about_user = other_info_about_user
        self.other_phone_number = other_phone_number
        self.other_avatar_photo = other_avatar_photo

        # self.name_label.setText(self.other_name)
        # self.surname_label.setText(self.other_surname)
        # self.middle_name_label.setText(self.other_middle_name)
        self.name_surname_middle_name.setText(self.other_surname + ' ' + self.other_name + ' ' + self.other_middle_name)
        self.status_label.setText(self.other_status)
        self.about_user_label.setText(other_info_about_user)
        self.phone_number_label.setText(self.other_phone_number)
        self.class_label.setText(self.other_class_index)

        self.exit_btn.clicked.connect(self.exit_from)
        self.change_profile_btn.clicked.connect(self.change_info_in_profile)

    def exit_from(self):
        self.close()

    def change_info_in_profile(self):
        self.close()
        self.start = EditProfile(self.name, self.surname, self.unical_code, self.class_name,
                                 self.other_class_index, self.other_name, self.other_surname,
                                 self.other_middle_name, self.other_unical_code, self.other_status,
                                 self.other_info_about_user, self.other_phone_number, self.other_avatar_photo)
        self.start.show()


class EditProfile(QtWidgets.QWidget, edit_my_user_profile.Ui_Form):
    def __init__(self, name, surname, unical_code, class_name, other_class_index, other_name, other_surname, other_midle_name, other_unical_code, other_status, other_info_about_user,
                 other_phone_number, other_avatar_photo):
        super().__init__()
        # Подключение настроек
        self.setupUi(self)
        self.name = name
        self.surname = surname
        self.unical_code = unical_code
        self.class_name = class_name
        self.other_class_index = other_class_index
        self.other_name = other_name
        self.other_surname = other_surname
        self.other_middle_name = other_midle_name
        self.other_unical_code = other_unical_code
        self.other_status = other_status
        self.other_info_about_user = other_info_about_user
        self.other_phone_number = other_phone_number
        self.other_avatar_photo = other_avatar_photo

        # self.name_label.setText(self.other_name)
        # self.surname_label.setText(self.other_surname)
        # self.middle_name_label.setText(self.other_middle_name)
        self.name_surname_middle_name.setText(self.other_surname + ' ' + self.other_name + ' ' + self.other_middle_name)
        self.change_status_input.setText(self.other_status)
        self.change_info_about_user_input.setText(other_info_about_user)
        self.change_phone_number_input.setText(self.other_phone_number)
        self.class_label.setText(self.other_class_index)

        self.exit_btn.clicked.connect(self.exit_from)
        self.change_profile_btn.clicked.connect(self.save_changes_profile)

    def exit_from(self):
        self.close()

    def save_changes_profile(self):
        status = self.change_status_input.text()
        info_about = self.change_info_about_user_input.toPlainText()
        phone_number = self.change_phone_number_input.text()
        data = {'unical_code': self.unical_code,'status': status, 'info_about': info_about, 'phone_number': phone_number}
        try:
            response = requests.post('http://127.0.0.1:5000/update_profile_user', json=data)
        except:
            return
        if response.status_code == 200:
            self.close()



dialog = QtWidgets.QApplication([])
d = Enter()
d.show()
dialog.exec_()
