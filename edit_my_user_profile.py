# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentprofedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 625)
        Form.setMinimumSize(QtCore.QSize(420, 625))
        Form.setMaximumSize(QtCore.QSize(420, 625))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-510, -1030, 1241, 1801))
        self.label.setStyleSheet("background-image: url(:/newPrefix/123456tyhgb);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.name_surname_middle_name = QtWidgets.QLabel(Form)
        self.name_surname_middle_name.setGeometry(QtCore.QRect(10, 30, 401, 81))
        self.name_surname_middle_name.setStyleSheet("font: 75 16pt \"Arial\";")
        self.name_surname_middle_name.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 131, 81))
        self.label_3.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 131, 81))
        self.label_4.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 321, 81))
        self.label_5.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 191, 81))
        self.label_6.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 401, 511))
        self.label_7.setStyleSheet("background-color: rgb(247, 227, 203);\n"
"border-radius:10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.change_status_input = QtWidgets.QLineEdit(Form)
        self.change_status_input.setGeometry(QtCore.QRect(120, 195, 271, 31))
        self.change_status_input.setStyleSheet("font: 14pt \"Arial\";")
        self.change_status_input.setObjectName("change_status_input")
        self.change_info_about_user_input = QtWidgets.QTextEdit(Form)
        self.change_info_about_user_input.setGeometry(QtCore.QRect(20, 310, 351, 171))
        self.change_info_about_user_input.setStyleSheet("font: 14pt \"Arial\";")
        self.change_info_about_user_input.setObjectName("change_info_about_user_input")
        self.change_phone_number_input = QtWidgets.QLineEdit(Form)
        self.change_phone_number_input.setGeometry(QtCore.QRect(210, 505, 181, 35))
        self.change_phone_number_input.setMinimumSize(QtCore.QSize(0, 35))
        self.change_phone_number_input.setStyleSheet("font: 14pt \"Arial\";")
        self.change_phone_number_input.setObjectName("change_phone_number_input")
        self.change_profile_btn = QtWidgets.QPushButton(Form)
        self.change_profile_btn.setGeometry(QtCore.QRect(230, 550, 161, 51))
        self.change_profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.change_profile_btn.setMouseTracking(False)
        self.change_profile_btn.setStyleSheet("QPushButton:hover{\n"
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
        self.change_profile_btn.setObjectName("change_profile_btn")
        self.class_lable = QtWidgets.QLabel(Form)
        self.class_lable.setGeometry(QtCore.QRect(110, 125, 291, 31))
        self.class_lable.setStyleSheet("font: 75 14pt \"Arial\";")
        self.class_lable.setText("")
        self.class_lable.setObjectName("class_lable")
        self.label.raise_()
        self.label_7.raise_()
        self.name_surname_middle_name.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.change_status_input.raise_()
        self.change_info_about_user_input.raise_()
        self.change_phone_number_input.raise_()
        self.change_profile_btn.raise_()
        self.class_lable.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_surname_middle_name.setText(_translate("Form", "Артём Пустынный Сергеевич"))
        self.label_3.setText(_translate("Form", "Статус:"))
        self.label_4.setText(_translate("Form", "Класс:"))
        self.label_5.setText(_translate("Form", "Иформация о пользователе:"))
        self.label_6.setText(_translate("Form", "Номер телефона:"))
        self.change_profile_btn.setText(_translate("Form", "Сохранить"))
import new_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
