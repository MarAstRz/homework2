from PyQt5 import QtCore, QtWidgets, Qt
import configparser
import login
import os, sys

class loginWindowController(QtWidgets.QWidget, login.Ui_Form):
    loginSignal = Qt.pyqtSignal(str, str, str)

    def __init__(self, parent=None):
        super(loginWindowController, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.load_config()
        self.loginButton.clicked.connect(self.loginButtonClicked)
        self.closeButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def loginButtonClicked(self):
        if (self.userIdEdit.text() != "" and self.userNameEdit.text() != ""):
            self.login()
            self.loginSignal.emit(self.userIdEdit.text(), self.userNameEdit.text(), "信计172")
            self.close()
    def mousePressEvent(self, event):
        #print(event.button(),Qt.Qt.LeftButton)
        if event.button() == Qt.Qt.LeftButton:
            self.m_flag = True

            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置

            event.accept()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            #print("2")

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
       # print("3")

    def load_config(self):
        config = configparser.ConfigParser()
        file = config.read(getPath('user.ini'), encoding='utf-8')
        config_dict = config.defaults()
        #print(file == [])
        if file != [] and config_dict['remember'] == 'True':
            self.user_name = config_dict['user_name']
            self.userNameEdit.setText(self.user_name)
            self.password = config_dict['password']
            self.userIdEdit.setText(self.password)
            self.saveUser.setChecked(True)
        else:
            self.saveUser.setChecked(False)

    def login(self):
        self.user_name = self.userNameEdit.text()
        self.password = self.userIdEdit.text()
        config = configparser.ConfigParser()
        if self.saveUser.isChecked():
            #print(1)
            config["DEFAULT"] = {
                "user_name": self.user_name,
                "password": self.password,
                "remember": self.saveUser.isChecked()
            }
        else:
            #print(2)
            config["DEFAULT"] = {
                "user_name": self.user_name,
                "password": "",
                "remember": self.saveUser.isChecked()
            }
        with open(getPath('user.ini'), 'w' ,encoding='utf-8')as configfile:
            config.write(configfile)

def getPath(fileName):
    path = os.path.join(os.path.dirname(sys.argv[0]), fileName)
    return path
        #print(self.user_name, self.password)