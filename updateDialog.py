from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 540)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 541))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(320, 165))
        self.widget_2.setMaximumSize(QtCore.QSize(320, 165))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(45, 60, 145, 24))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 179);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setDisabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(205, 60, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 178);")
        self.pushButton.clicked.connect(lambda : self.chooseFile())
        self.pushButton.setObjectName("pushButton")
        self.submitButton = QtWidgets.QPushButton(self.widget_2)
        self.submitButton.setGeometry(QtCore.QRect(112, 108, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: rgb(0, 204, 0);"
                                        "color:white;")
        self.submitButton.setObjectName("submitButton")
        self.closeButton = QtWidgets.QPushButton( self.widget_2)
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
        self.closeButton.setObjectName("closeButton")
        self.classNameLabel = QtWidgets.QLabel(self.widget_2)
        self.classNameLabel.setGeometry(QtCore.QRect(60, 8, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.classNameLabel.setFont(font)
        self.classNameLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.classNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classNameLabel.setObjectName("classNameLabel")
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "选择文件"))
        self.submitButton.setText(_translate("Form", "提交"))
        self.closeButton.setText(_translate("Form", "×"))
        self.classNameLabel.setText(_translate("Form", "NULL"))

    def chooseFile(self):
        fileNameChoose, fileType = QtWidgets.QFileDialog.getOpenFileName()  # 设置文件扩展名过滤,用双分号间隔

        self.lineEdit.setText(fileNameChoose)




