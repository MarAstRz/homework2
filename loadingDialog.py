# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 165)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 290, 165))
        self.widget_2.setMinimumSize(QtCore.QSize(320, 165))
        self.widget_2.setMaximumSize(QtCore.QSize(320, 165))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.widget_2.setObjectName("widget_2")
        self.classNameLabel = QtWidgets.QLabel(self.widget_2)
        self.classNameLabel.setGeometry(QtCore.QRect(60, 70, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.classNameLabel.setFont(font)
        self.classNameLabel.setStyleSheet("color: rgb(0, 0, 0);"
                                          "")
        self.classNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classNameLabel.setObjectName("classNameLabel")
        '''self.closeButton = QtWidgets.QPushButton(self.widget_2)
        self.closeButton.setGeometry(QtCore.QRect(8, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{\n"
"color : white;\n"
"border : none;\n"
"background-color : rgb(253, 102, 102);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;}")
        self.closeButton.setObjectName("closeButton")'''

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.classNameLabel.setText(_translate("Form", "请稍候..."))
        #self.closeButton.setText(_translate("Form", "×"))

    def setLoadingDialogText(self, label):
        self.classNameLabel.setText(label)