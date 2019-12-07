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
        print(self.downloadPath + '/' + name)
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

