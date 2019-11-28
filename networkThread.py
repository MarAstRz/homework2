import time

from PyQt5 import Qt
import requests

import mainWindowController


class uploadNetWork(Qt.QThread):
    netResult = Qt.pyqtSignal(object, str, object)
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
        self.netResult.emit(self.object, r.text, self.ui)
        time.sleep(2)
        self.cDialog.emit(self.object)


class cardWorker(Qt.QThread):

    netResult = Qt.pyqtSignal(object, requests.Response, str, str)

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

        self.netResult.emit(self.ui, b, self.userId, self.userName)
        '''for i in range(len(b.json())):
            ui.addCard(b.json()[i], "null", "提交", i)'''