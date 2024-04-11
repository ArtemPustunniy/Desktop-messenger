# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtech.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 590)
        Form.setMinimumSize(QtCore.QSize(480, 435))
        Form.setMaximumSize(QtCore.QSize(480, 2134567))
        Form.setStyleSheet("font: 87 22pt \"Arial Black\";")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-400, -570, 1411, 1401))
        self.label.setStyleSheet("background-image: url(:/newPrefix/123456tyhgb);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setGeometry(QtCore.QRect(320, 510, 151, 61))
        self.create_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.create_btn.setMouseTracking(False)
        self.create_btn.setStyleSheet("QPushButton:hover{\n"
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
        self.create_btn.setObjectName("create_btn")
        self.enter_name_input = QtWidgets.QLineEdit(Form)
        self.enter_name_input.setGeometry(QtCore.QRect(130, 120, 301, 31))
        self.enter_name_input.setStyleSheet("font: 14pt \"Arial\";")
        self.enter_name_input.setText("")
        self.enter_name_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_name_input.setObjectName("enter_name_input")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 121, 51))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 451, 401))
        self.label_5.setStyleSheet("background-color: rgb(247, 227, 203);\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.main_label = QtWidgets.QLabel(Form)
        self.main_label.setGeometry(QtCore.QRect(100, 20, 411, 51))
        self.main_label.setObjectName("main_label")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 121, 51))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 121, 51))
        self.label_7.setStyleSheet("font: 14pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.enter_surname_input = QtWidgets.QLineEdit(Form)
        self.enter_surname_input.setGeometry(QtCore.QRect(130, 190, 301, 31))
        self.enter_surname_input.setStyleSheet("font: 14pt \"Arial\";")
        self.enter_surname_input.setObjectName("enter_surname_input")
        self.enter_middle_name_input = QtWidgets.QLineEdit(Form)
        self.enter_middle_name_input.setGeometry(QtCore.QRect(130, 260, 301, 31))
        self.enter_middle_name_input.setStyleSheet("font: 14pt \"Arial\";")
        self.enter_middle_name_input.setText("")
        self.enter_middle_name_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_middle_name_input.setObjectName("enter_middle_name_input")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 390, 121, 51))
        self.label_8.setStyleSheet("font: 14pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 121, 51))
        self.label_9.setStyleSheet("font: 14pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.enter_password_input = QtWidgets.QLineEdit(Form)
        self.enter_password_input.setGeometry(QtCore.QRect(130, 400, 301, 31))
        self.enter_password_input.setStyleSheet("font: 14pt \"Arial\";")
        self.enter_password_input.setText("")
        self.enter_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_password_input.setObjectName("enter_password_input")
        self.enter_login_input = QtWidgets.QLineEdit(Form)
        self.enter_login_input.setGeometry(QtCore.QRect(130, 330, 301, 31))
        self.enter_login_input.setStyleSheet("font: 14pt \"Arial\";")
        self.enter_login_input.setObjectName("enter_login_input")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(10, 510, 151, 61))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.exit_btn.setMouseTracking(False)
        self.exit_btn.setStyleSheet("QPushButton:hover{\n"
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
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/left-arrow (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(50, 40))
        self.exit_btn.setObjectName("exit_btn")
        self.label.raise_()
        self.create_btn.raise_()
        self.label_5.raise_()
        self.main_label.raise_()
        self.enter_name_input.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.enter_surname_input.raise_()
        self.enter_middle_name_input.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.enter_password_input.raise_()
        self.enter_login_input.raise_()
        self.exit_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.create_btn.setText(_translate("Form", "Добавить"))
        self.label_4.setText(_translate("Form", "Имя:"))
        self.main_label.setText(_translate("Form", "Новый учитель"))
        self.label_6.setText(_translate("Form", "Фамилия:"))
        self.label_7.setText(_translate("Form", "Отчество:"))
        self.label_8.setText(_translate("Form", "Пароль:"))
        self.label_9.setText(_translate("Form", "Логин:"))
import new_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())