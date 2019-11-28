from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 325)
        #Form.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(250, 325))
        Form.setMaximumSize(QtCore.QSize(250, 325))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(20)
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        Form.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"outline:none;")
        self.passwordWidget = QtWidgets.QWidget(Form)
        self.passwordWidget.setGeometry(QtCore.QRect(15, 215, 220, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordWidget.sizePolicy().hasHeightForWidth())
        self.passwordWidget.setSizePolicy(sizePolicy)
        self.passwordWidget.setMinimumSize(QtCore.QSize(220, 30))
        self.passwordWidget.setStyleSheet("border : 1px solid rgb(137, 136, 138);\n"
"border-style : none none solid none;\n"
"")
        self.passwordWidget.setObjectName("passwordWidget")
        self.loginButton = QtWidgets.QPushButton(self.passwordWidget)
        self.loginButton.setGeometry(QtCore.QRect(195, 3, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"color: black;\n"
"border-style:none;\n"
"border:1px solid black; \n"
"border-radius:10px;}\n"
"QPushButton:hover{\n"
"background-color : black; \n"
"color : white;} \n"
"QPushButton:pressed{\n"
"background-color : white; \n"
"color : black;}\n"
"")
        icon = QtGui.QIcon.fromTheme("login")
        self.loginButton.setIcon(icon)
        self.loginButton.setObjectName("loginButton")
        self.userNameEdit = QtWidgets.QLineEdit(self.passwordWidget)
        self.userNameEdit.setGeometry(QtCore.QRect(0, 0, 190, 28))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.userNameEdit.setFont(font)
        self.userNameEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userNameEdit.setStyleSheet("border : none;\n"
"color : black;")
        self.userNameEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userNameEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.userNameEdit.setClearButtonEnabled(False)
        self.userNameEdit.setObjectName("userNameEdit")
        self.usernameWidget = QtWidgets.QWidget(Form)
        self.usernameWidget.setGeometry(QtCore.QRect(15, 175, 220, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameWidget.sizePolicy().hasHeightForWidth())
        self.usernameWidget.setSizePolicy(sizePolicy)
        self.usernameWidget.setMinimumSize(QtCore.QSize(220, 30))
        self.usernameWidget.setStyleSheet("border : 1px solid rgb(137, 136, 138);\n"
"border-style : none none solid none;")
        self.usernameWidget.setObjectName("usernameWidget")
        self.userIdEdit = QtWidgets.QLineEdit(self.usernameWidget)
        self.userIdEdit.setGeometry(QtCore.QRect(0, 0, 220, 28))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.userIdEdit.setFont(font)
        self.userIdEdit.setTabletTracking(False)
        self.userIdEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userIdEdit.setAutoFillBackground(False)
        self.userIdEdit.setStyleSheet("border : none;\n"
"color : black;\n"
"padding: -1;\n"
"")
        self.userIdEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.userIdEdit.setClearButtonEnabled(False)
        self.userIdEdit.setObjectName("userIdEdit")
        self.closeButton = QtWidgets.QPushButton(Form)
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
        self.checkboxWidget = QtWidgets.QWidget(Form)
        self.checkboxWidget.setGeometry(QtCore.QRect(30, 265, 190, 40))
        self.checkboxWidget.setObjectName("checkboxWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.checkboxWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveUser = QtWidgets.QCheckBox(self.checkboxWidget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(11)
        self.saveUser.setFont(font)
        self.saveUser.setMouseTracking(True)
        self.saveUser.setFocusPolicy(QtCore.Qt.TabFocus)
        self.saveUser.setStyleSheet("color : balck;")
        self.saveUser.setObjectName("saveUser")
        self.horizontalLayout.addWidget(self.saveUser)
        self.autoLogin = QtWidgets.QCheckBox(self.checkboxWidget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(11)
        self.autoLogin.setFont(font)
        self.autoLogin.setFocusPolicy(QtCore.Qt.TabFocus)
        self.autoLogin.setStyleSheet("color : balck;")
        self.autoLogin.setObjectName("autoLogin")
        self.horizontalLayout.addWidget(self.autoLogin)
        self.signinButton = QtWidgets.QPushButton(Form)
        self.signinButton.setGeometry(QtCore.QRect(221, 5, 25, 20))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(11)
        self.signinButton.setFont(font)
        self.signinButton.setStyleSheet("QPushButton{\n"
"color : black;\n"
"border: none;}\n"
"QPushButton:hover{\n"
"color : rgb(15, 128, 255);}")
        self.signinButton.setObjectName("signinButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(64, 60, 122, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.closeButton.raise_()
        self.usernameWidget.raise_()
        self.checkboxWidget.raise_()
        self.passwordWidget.raise_()
        self.signinButton.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginButton.setText(_translate("Form", "➝"))
        self.userNameEdit.setPlaceholderText(_translate("Form", "姓名"))
        self.userIdEdit.setPlaceholderText(_translate("Form", "学号"))
        self.closeButton.setText(_translate("Form", "×"))
        self.saveUser.setText(_translate("Form", "保存用户"))
        self.autoLogin.setText(_translate("Form", "自动登陆"))
        self.signinButton.setText(_translate("Form", "注册"))
        self.label.setText(_translate("Form", "用户验证"))
import icon_rc
