# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(416, 626)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-230, -30, 741, 761))
        self.label.setStyleSheet("background-image: url(:/newPrefix/123456tyhgb);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(9, 16, 400, 590))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 588))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 351, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton:hover{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Группа 10А"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
