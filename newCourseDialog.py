# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newCourseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 541)
        Form.setMinimumSize(QtCore.QSize(351, 541))
        Form.setMaximumSize(QtCore.QSize(351, 541))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 541))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(290, 135))
        self.widget_2.setMaximumSize(QtCore.QSize(290, 135))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 100, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 178);")
        self.pushButton.setObjectName("pushButton")
        self.submitButton = QtWidgets.QPushButton(self.widget_2)
        self.submitButton.setGeometry(QtCore.QRect(130, 100, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: rgb(0, 204, 0);\n"
"color:white;")
        self.submitButton.setObjectName("submitButton")
        self.classNameLabel = QtWidgets.QLabel(self.widget_2)
        self.classNameLabel.setGeometry(QtCore.QRect(45, 8, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.classNameLabel.setFont(font)
        self.classNameLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.classNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classNameLabel.setObjectName("classNameLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 210, 31))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 179);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "取消"))
        self.submitButton.setText(_translate("Form", "确认"))
        self.classNameLabel.setText(_translate("Form", "输入作业名称"))
