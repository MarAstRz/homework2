# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newCard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 120)
        Form.setMinimumSize(QtCore.QSize(300, 120))
        Form.setMaximumSize(QtCore.QSize(300, 120))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 300, 120))
        self.widget.setMinimumSize(QtCore.QSize(300, 120))
        self.widget.setMaximumSize(QtCore.QSize(300, 120))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border:2px dashed black;")
        self.widget.setObjectName("widget")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(100, 15, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(14)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("border:none;\n"
"color:black;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "新建课程"))
