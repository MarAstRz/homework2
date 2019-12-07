from PyQt5 import QtCore, QtWidgets

import loginWindowController
import mainWindowController


class ViewController(QtCore.QObject):
    def loadLoginView(self):
        self.viewlogin = loginWindowController.loginWindowController()
        self.viewlogin.loginSignal.connect(self.loadMainWinView)
        self.viewlogin.show()

    def loadMainWinView(self, userId, userName, userStatus, userClass):
        print(userStatus)
        self.viewMainWIn = mainWindowController.mainWindowController()
        self.viewMainWIn.show()
        self.viewMainWIn.refreshCard(userId, userName, userStatus, userClass)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = ViewController()
    view.loadLoginView()
    print("name:" + __name__)
    sys.exit(app.exec_())

