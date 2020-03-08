from PyQt5 import QtCore, QtWidgets

import loginWindowController
import mainWindowController


class ViewController(QtCore.QObject):
    def loadLoginView(self):
        self.viewlogin = loginWindowController.loginWindowController()
        self.viewlogin.loginSignal.connect(self.loadMainWinView)
        self.viewlogin.show()

    def loadMainWinView(self, logniView, userId, userName, userStatus, userClass):
        logniView.close()
        self.viewMainWIn = mainWindowController.mainWindowController()
        self.viewMainWIn.show()
        self.viewMainWIn.initCard(userId, userName, userStatus, userClass)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = ViewController()
    view.loadLoginView()
    sys.exit(app.exec_())

