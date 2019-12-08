import os

from PyQt5 import QtCore, QtWidgets, Qt

import adminCard
import classCard1
import classCard2
import completeDialog
import loadingDialog
import networkThread
import newCard
import updateDialog as ud
import wrongDialog
from main import Ui_MainWindow
import verifyDialog
import newCourseDialog
def file_extension(path):
    return os.path.splitext(path)[1]


class mainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindowController, self).__init__(parent)
        self.setupUi(self)
        self.closeButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.settingButton.clicked.connect(self.test)
        '''thread = cardWorker(self)
        thread.start()'''
        self.cardNum = 0
        self.spacerItemCourse = 0

    def initCard(self, userId, userName, userStatus, userClass):
        if userStatus == 'admin':
            self.dThread = networkThread.adminCardWorker(self, userId, userName, userClass)
            self.dThread.start()
        else:
            self.thread = networkThread.cardWorker(self, userId, userName, userClass)
            self.thread.start()

    def addCard(self, className, courseName, deadLine, submit, int):
        card = classCard1.Ui_Form()
        widget = QtWidgets.QWidget()
        card.setupUi(widget)
        card.setTheText(courseName, deadLine, submit)
        card.submitButton.clicked.connect(lambda :self.openDialog(className, card.className.text(), card, 0))
        self.gridLayout.addWidget(card.testCard_1, int, 0)
        #spacerItem = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem, int + 1, 0)

    def addCard2(self, className, courseName, deadLine, submit, int):
        card = classCard2.Ui_Form()
        widget = QtWidgets.QWidget()
        card.setupUi(widget)
        card.setTheText(courseName, deadLine, submit)
        card.submitButton_4.clicked.connect(lambda: self.openDialog(className, card.className_4.text(), card, 0))
        self.gridLayout.addWidget(card.testCard_4, int, 0)
        #spacerItem = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem, int + 1, 0)

    def openDialog(self, className, courseName, card, index):
        gridLayout = QtWidgets.QGridLayout(self.widget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout2")
        self.widget.setVisible(True)
        self.widget.setLayout(gridLayout)
        ui = ud.Ui_Form()
        widget2 = QtWidgets.QWidget()
        ui.setupUi(widget2)
        ui.classNameLabel.setText(courseName)
        ui.closeButton.clicked.connect(self.closeDialog)
        gridLayout.addWidget(ui.widget_2)
        ui.switch(index)
        if index == 1:
            ui.adminDownloadTextSet()
            print(self.label.text())
            ui.submitButton.clicked.connect(lambda:
                                            self.download(ui.lineEdit.text(),
                                                        className,
                                                        courseName,
                                                        card))


        else:
            ui.submitButton.clicked.connect(lambda:
                                            self.submit(ui.lineEdit.text(),
                                                        self.label.text(),
                                                        courseName,
                                                        card))

    def closeDialog(self):
        self.widget.setVisible(False)
        #print(self.widget.layout().count())
        for i in range(self.widget.layout().count()):
            self.widget.layout().itemAt(i).widget().deleteLater()
        self.widget.layout().deleteLater()

    def test(self):
        self.widget.setVisible(True)


    def submit(self, path, name, className, ui):
        if path != "":
            self.setupDialog("loading", "请稍后...")
            _path = path
            _class = '信计172'
            _name = name
            _dir = '/data/fff/homework2.0/main/' + _class + '/' + className + '/'
            # _dir = '/Users/marast/Downloads/homework/main/' + _class + '/' + className + '/'
            fileName = _name
            fileExtension = file_extension(_path)
            try:
                files = {'file': open(_path, 'rb')}
                data = {'fileName': fileName, 'dir': _dir, 'fileExtension': fileExtension}
                self.thread = networkThread.uploadNetWork(self, data, files, ui)
                self.thread.start()
            except (FileNotFoundError):
                print("dir not found")

    def download(self, path, className, courseName, ui):
        if path != "":
            self.setupDialog("loading", "请稍后...")
            self.thread2 = networkThread.downloadNetwork(self, className, courseName, path, ui)
            self.thread2.start()

    def successSolt(self, b, ui):
        #print(b)
        if b == 200 :
            self.setupDialog("complete", "")
            if ui != 0:
                ui.setButton()
        else :
            self.setupDialog("error", "")

    def setupDialog(self, id, text):
        if id == "loading" :
            widget = QtWidgets.QWidget()
            loadingdialogui = loadingDialog.Ui_Form()
            loadingdialogui.setupUi(widget)
            loadingdialog = loadingdialogui.widget_2
            loadingdialogui.setLoadingDialogText(text)
            self.widget.layout().itemAt(0).widget().deleteLater()
            self.widget.layout().addWidget(loadingdialog)
        elif id == "complete" :
            widget = QtWidgets.QWidget()
            completedialogui = completeDialog.Ui_Form()
            completedialogui.setupUi(widget)
            completedialog = completedialogui.widget_2
            self.widget.layout().itemAt(0).widget().deleteLater()
            self.widget.layout().addWidget(completedialog)

        elif id == 'error' :
            widget = QtWidgets.QWidget()
            wrongdialogui = wrongDialog.Ui_Form()
            wrongdialogui.setupUi(widget)
            wrongdialog = wrongdialogui.widget_2

            self.widget.layout().itemAt(0).widget().deleteLater()
            self.widget.layout().addWidget(wrongdialog)

    def cardSlot(self, res, userId, userName, className):
        self.cardNum = len(res.json()[0])
        self.spacerItemCourse = self.cardNum + 1
        for i in range(len(res.json()[2])):
            self.addCard(className, res.json()[0][res.json()[2][i]], "null", "点击提交", i)
        for i in range(len(res.json()[1])):
            self.addCard2(className, res.json()[0][res.json()[1][i]], "null", "已提交", len(res.json()[2]) + i)
        self.label.setText(userId + ' ' + userName)
        spacerItem = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, self.spacerItemCourse, 0)

    def adminCardSlot(self, res, className):
        #print(res)
        self.gridLayout.removeItem(self.gridLayout.itemAt(0))
        self.cardNum = len(res.json()[0])
        self.spacerItemCourse = self.cardNum + 1
        #print(self.cardNum)
        for i in range(len(res.json()[0]) + 1):
            if i == len(res.json()[0]):
                self.adminAddNewCard(i, className)
            else:
                self.adminAddCard(className, res.json()[0][i], "null", i)
        spacerItem = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, self.spacerItemCourse, 0)
        self.label.setText(className + " 管理员")


    def adminAddCard(self, className, courseName, deadLine, int):

        card = adminCard.Ui_Form()
        widget = QtWidgets.QWidget()
        card.setupUi(widget)
        card.setTheText(courseName, deadLine)
        card.downloadButton.clicked.connect(lambda: self.openDialog(className, card.className.text(), card, 1))
        card.closeButton.clicked.connect(lambda: self.openVerifyDialog(className, courseName))
        self.gridLayout.addWidget(card.testCard_1, int, 0)


    def adminAddNewCard(self, int, userClass):

        card = newCard.Ui_Form()
        widget = QtWidgets.QWidget()
        card.setupUi(widget)
        card.toolButton.clicked.connect(lambda: self.openNCDialog(userClass))
        self.gridLayout.addWidget(card.widget, int, 0)




    def delDir(self, className, courseName):
        self.setupDialog("loading", "请稍后...")
        self.addThreat = networkThread.delDirNetwork(className, courseName, self)
        self.addThreat.start()

    def openVerifyDialog(self, className, courseName):
        gridLayout = QtWidgets.QGridLayout(self.widget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout2")
        self.widget.setVisible(True)
        #print(self.widget.layout().count())
        self.widget.setLayout(gridLayout)
        ui = verifyDialog.Ui_Form()
        widget2 = QtWidgets.QWidget()
        ui.setupUi(widget2)
        ui.pushButton.clicked.connect(self.closeDialog)
        gridLayout.addWidget(ui.widget_2)
        ui.submitButton.clicked.connect(lambda: self.delDir(className, courseName))

    def adminRefreshCard(self):
        for i in range(self.gridLayout.count() - 1):
            self.gridLayout.itemAt(i).widget().deleteLater()
        #print(self.gridLayout.itemAt(0))
        self.dThread.start()


    def openNCDialog(self, className):
        gridLayout = QtWidgets.QGridLayout(self.widget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout2")
        self.widget.setVisible(True)
        #print(self.widget.layout().count())
        self.widget.setLayout(gridLayout)
        ui = newCourseDialog.Ui_Form()
        widget2 = QtWidgets.QWidget()
        ui.setupUi(widget2)
        ui.pushButton.clicked.connect(self.closeDialog)
        gridLayout.addWidget(ui.widget_2)
        ui.submitButton.clicked.connect(lambda: self.createDir(className, ui.lineEdit.text()))

    def createDir(self, className, courseName):
        if courseName != '':
            self.setupDialog("loading", "请稍后...")
            self.addThreat = networkThread.addNewCardNetWork(className, courseName, self)
            self.addThreat.start()



    def mousePressEvent(self, event):
        if event.button() == Qt.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))

