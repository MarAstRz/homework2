import time

import requests
from PyQt5 import Qt

import mainWindowController


class uploadNetWork(Qt.QThread):
    netResult = Qt.pyqtSignal(object, int, object)
    cDialog = Qt.pyqtSignal(object)

    def __init__(self, object, data, files, ui):
        super(uploadNetWork, self).__init__()
        self.ui = ui
        self.data = data
        self.files = files
        self.object = object
        self.netResult.connect(mainWindowController.mainWindowController.successSolt)
        self.cDialog.connect(mainWindowController.mainWindowController.closeDialog)

    def run(self):
        r = requests.post('http://www.marast.cn:4000/uploadFile', data=self.data, files=self.files)
        self.netResult.emit(self.object, r.status_code, self.ui)
        time.sleep(2)
        self.cDialog.emit(self.object)


class cardWorker(Qt.QThread):

    netResult = Qt.pyqtSignal(object, requests.Response, str, str, str)

    def __init__(self, ui, userId, userName, userClass):
        super(cardWorker, self).__init__()
        self.userId = userId
        self.userName = userName
        self.userClass = userClass
        self.ui = ui
        self.netResult.connect(mainWindowController.mainWindowController.cardSlot)

    def run(self):
        data = {'userId': self.userId, 'userClass': self.userClass}
        b = requests.get('http://www.marast.cn:4000/getCardList', timeout=20, data=data)

        self.netResult.emit(self.ui, b, self.userId, self.userName, self.userClass)
        '''for i in range(len(b.json())):
            ui.addCard(b.json()[i], "null", "提交", i)'''

class downloadNetwork(Qt.QThread):

    downloadResult = Qt.pyqtSignal(object, int, object)
    cDialog = Qt.pyqtSignal(object)

    def __init__(self, object, className, courseName, downloadPath, ui):
        super(downloadNetwork, self).__init__()
        self.courseName = courseName
        self.className = className
        self.downloadPath = downloadPath
        self.object = object
        self.ui = ui
        self.downloadResult.connect(mainWindowController.mainWindowController.successSolt)
        self.cDialog.connect(mainWindowController.mainWindowController.closeDialog)


    def run(self):
        name = self.courseName + '.zip'
        dir = '/data/fff/homework2.0/'
        #dir = '/Users/marast/Downloads/homework2.0/'
        path = 'main/' + self.className + '/' + self.courseName

        #print(path)
        data = {'name': name, 'dir': dir, 'path': path}
        url = 'http://www.marast.cn:4000/mkzip'
        #url = '127.0.0.1:4000/mkzip'
        r = requests.get(url, data=data)
        #print(self.downloadPath + '/' + name)
        with open(self.downloadPath + '/' + name, "wb") as code:
            code.write(r.content)
        #print(r)
        self.downloadResult.emit(self.object, r.status_code, self.ui)
        time.sleep(2)
        self.cDialog.emit(self.object)

class adminCardWorker(Qt.QThread):
    netResult = Qt.pyqtSignal(object, requests.Response, str)

    def __init__(self, ui, userId, userName, userClass):
        super(adminCardWorker, self).__init__()
        self.userId = userId
        self.userName = userName
        self.userClass = userClass
        self.ui = ui
        self.netResult.connect(mainWindowController.mainWindowController.adminCardSlot)

    def run(self):
        data = {'userId': self.userId, 'userClass': self.userClass}
        b = requests.get('http://www.marast.cn:4000/getCardList', timeout=20, data=data)
        #print("111" + self.userName)
        self.netResult.emit(self.ui, b, self.userClass)


class loginNetwork(Qt.QThread):
    def __init__(self, userId, object):
        super(loginNetwork, self).__init__()
        self.userId = userId
        self.object = object

    def run(self):
        data = {'userId': self.userId}
        b = requests.get('http://www.marast.cn:4000/login', timeout=20, data = data)
        #print(b.json()[0]["id"])
        self.object.loginSignal.emit(self.object, self.object.userIdEdit.text(), self.object.userNameEdit.text(), b.json()[0]["status"], b.json()[0]["class"])
        #self.object.close()

class addNewCardNetWork(Qt.QThread):
    netResult = Qt.pyqtSignal(object, int, int)
    refreshCard = Qt.pyqtSignal(object)
    cDialog = Qt.pyqtSignal(object)
    def __init__(self, userClass, userCourse, object):
        super(addNewCardNetWork, self).__init__()
        self.userClass = userClass
        self.object = object
        self.userCourse = userCourse
        self.netResult.connect(mainWindowController.mainWindowController.successSolt)
        self.refreshCard.connect(mainWindowController.mainWindowController.adminRefreshCard)
        self.cDialog.connect(mainWindowController.mainWindowController.closeDialog)


    def run(self):
        data = {'userClass': self.userClass, 'userCourse': self.userCourse}
        b = requests.get('http://www.marast.cn:4000/mkdir', timeout=20, data=data)
        self.netResult.emit(self.object, b.status_code, 0)
        if b.status_code == 200:
            self.refreshCard.emit(self.object)
        time.sleep(2)
        self.cDialog.emit(self.object)

class delDirNetwork(Qt.QThread):
    netResult = Qt.pyqtSignal(object, int, int)
    refreshCard = Qt.pyqtSignal(object)
    cDialog = Qt.pyqtSignal(object)
    def __init__(self, userClass, userCourse, object):
        super(delDirNetwork, self).__init__()
        self.userClass = userClass
        self.userCourse = userCourse
        self.object = object
        self.netResult.connect(mainWindowController.mainWindowController.successSolt)
        self.refreshCard.connect(mainWindowController.mainWindowController.adminRefreshCard)
        self.cDialog.connect(mainWindowController.mainWindowController.closeDialog)

    def run(self):
        data = {'userClass': self.userClass, 'userCourse': self.userCourse}
        b = requests.get('http://www.marast.cn:4000/rmdir', timeout=20, data=data)
        self.netResult.emit(self.object, b.status_code, 0)
        if b.status_code == 200:
            self.refreshCard.emit(self.object)
        time.sleep(2)
        self.cDialog.emit(self.object)

class getDetailNetwork(Qt.QThread):
    netResult = Qt.pyqtSignal(object, object, requests.Response, str)
    def __init__(self, className, courseName, ui, object):
        super(getDetailNetwork, self).__init__()
        self.className = className
        self.courseName = courseName
        self.ui = ui
        self.object = object
        self.netResult.connect(mainWindowController.mainWindowController.refreshDetailWidget)

    def run(self):
        path = self.className + '/' + self.courseName
        data = {'dir': path}
        #print(data)

        r = requests.get('http://www.marast.cn:4000/getlist', data=data)
        #print(r.json())
        self.netResult.emit(self.object, self.ui, r, self.courseName)
        #self.ui.textEdit.setText(r.json()[0])
        #self.ui.label.setText(self.courseName)
        #print(r)


