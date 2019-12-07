# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminCard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 140)
        Form.setMinimumSize(QtCore.QSize(300, 140))
        Form.setMaximumSize(QtCore.QSize(300, 140))
        self.testCard_1 = QtWidgets.QWidget(Form)
        self.testCard_1.setGeometry(QtCore.QRect(0, 0, 300, 140))
        self.testCard_1.setMinimumSize(QtCore.QSize(300, 140))
        self.testCard_1.setMaximumSize(QtCore.QSize(300, 140))
        self.testCard_1.setStyleSheet("/*background-color: rgb(15, 128, 255);\n"
"*/\n"
"border-radius: 10px;\n"
"background-color: rgb(15, 128, 255);\n"
"\n"
"")
        self.testCard_1.setObjectName("testCard_1")
        self.downloadButton = QtWidgets.QPushButton(self.testCard_1)
        self.downloadButton.setGeometry(QtCore.QRect(190, 88, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.downloadButton.setObjectName("downloadButton")
        self.cardInfo_1 = QtWidgets.QWidget(self.testCard_1)
        self.cardInfo_1.setGeometry(QtCore.QRect(0, 10, 181, 120))
        self.cardInfo_1.setStyleSheet("color:white;\n"
"background-color: rgb(15, 128, 255);\n"
"")
        self.cardInfo_1.setObjectName("cardInfo_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cardInfo_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ClassName = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.ClassName.setFont(font)
        self.ClassName.setAutoFillBackground(False)
        self.ClassName.setAlignment(QtCore.Qt.AlignCenter)
        self.ClassName.setWordWrap(False)
        self.ClassName.setObjectName("ClassName")
        self.verticalLayout.addWidget(self.ClassName)
        self.className = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.className.setFont(font)
        self.className.setAlignment(QtCore.Qt.AlignCenter)
        self.className.setObjectName("className")
        self.verticalLayout.addWidget(self.className)
        self.DeadLine = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.DeadLine.setFont(font)
        self.DeadLine.setAlignment(QtCore.Qt.AlignCenter)
        self.DeadLine.setObjectName("DeadLine")
        self.verticalLayout.addWidget(self.DeadLine)
        self.deadLine = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.deadLine.setFont(font)
        self.deadLine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deadLine.setTextFormat(QtCore.Qt.AutoText)
        self.deadLine.setAlignment(QtCore.Qt.AlignCenter)
        self.deadLine.setObjectName("deadLine")
        self.verticalLayout.addWidget(self.deadLine)
        self.infoButton = QtWidgets.QPushButton(self.testCard_1)
        self.infoButton.setGeometry(QtCore.QRect(190, 20, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.infoButton.setFont(font)
        self.infoButton.setStyleSheet("background-color: rgb(15, 128, 255);\n"
"\n"
"border:1px solid rgb(0, 204, 0);;")
        self.infoButton.setObjectName("infoButton")
        self.closeButton = QtWidgets.QPushButton(self.testCard_1)
        self.closeButton.setGeometry(QtCore.QRect(8, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{\n"
"color: rgb(15, 128, 255);\n"
"background-color: rgb(15, 128, 255);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border : none;\n"
"background-color : rgb(253, 102, 102);\n"
"border-radius:7px;\n"
"color: white;\n"
"}")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.downloadButton.setText(_translate("Form", "打包下载"))
        self.ClassName.setText(_translate("Form", "课程名称"))
        self.className.setText(_translate("Form", "NULL"))
        self.DeadLine.setText(_translate("Form", "截止日期"))
        self.deadLine.setText(_translate("Form", "NULL"))
        self.infoButton.setText(_translate("Form", "查看内容"))
        self.closeButton.setText(_translate("Form", "×"))

    def setTheText(self, className, deadLine):
        self.deadLine.setText(deadLine)
        self.className.setText(className)

    def setButton(self):
        self.downloadButton.setText("已下载")
