# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 541)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 541))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 410))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 410))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(0, 20, 300, 31))
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color:balck;")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 300, 325))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 325))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 280, 300))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.textEdit.setFont(font)
        self.textEdit.setEnabled(False)
        self.textEdit.setStyleSheet("color:black;")
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.closeButton = QtWidgets.QPushButton(self.widget_2)
        self.closeButton.setGeometry(QtCore.QRect(8, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{\n"
"color : white;\n"
"border : none;\n"
"background-color : rgb(253, 102, 102);\n"
"border-radius:7px;}\n"
"QPushButton:hover{\n"
"color: black;}")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请稍后..."))
        self.closeButton.setText(_translate("Form", "×"))
