# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'completeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 165)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 320, 165))
        self.widget_2.setMinimumSize(QtCore.QSize(320, 165))
        self.widget_2.setMaximumSize(QtCore.QSize(320, 165))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.widget_2.setObjectName("widget_2")
        self.toolButton = QtWidgets.QToolButton(self.widget_2)
        self.toolButton.setGeometry(QtCore.QRect(128, 38, 64, 88))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(14)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("color: rgb(0, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/complete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "上传成功"))
import wrIcon_rc
