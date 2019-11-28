from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 140)

        self.testCard_1 = QtWidgets.QWidget(Form)
        self.testCard_1.setGeometry(QtCore.QRect(0, 0, 300, 140))
        self.testCard_1.setMinimumSize(QtCore.QSize(300, 140))
        self.testCard_1.setMaximumSize(QtCore.QSize(300, 140))
        self.testCard_1.setStyleSheet("background-color: rgb(15, 128, 255);\n"
"border-radius: 10px;")
        self.testCard_1.setObjectName("testCard_1")
        self.submitButton = QtWidgets.QPushButton(self.testCard_1)
        self.submitButton.setGeometry(QtCore.QRect(190, 54, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.submitButton.setObjectName("submitButton")
        self.cardInfo_1 = QtWidgets.QWidget(self.testCard_1)
        self.cardInfo_1.setGeometry(QtCore.QRect(0, 10, 181, 120))
        self.cardInfo_1.setStyleSheet("color:white;")
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
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.submitButton.setText(_translate("Form", "NULL"))
        self.ClassName.setText(_translate("Form", "课程名称"))
        self.className.setText(_translate("Form", "NULL"))
        self.DeadLine.setText(_translate("Form", "截止日期"))
        self.deadLine.setText(_translate("Form", "NULL"))

    def setTheText(self, className, deadLine, submit):
        self.deadLine.setText(deadLine)
        self.className.setText(className)
        self.submitButton.setText(submit)

    def setButton(self):
        self.submitButton.setStyleSheet("background-color: gray;")
        self.submitButton.setText("已提交")
        self.testCard_1.setStyleSheet("background-color: rgb(64, 128, 2);\n"
"border-radius: 10px;")
        self.cardInfo_1.setStyleSheet("background-color: rgb(64, 128, 2);\n"
"border-radius: 10px;\n"
                                      "color:white;")

