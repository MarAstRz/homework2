
from PyQt5 import QtCore, QtWidgets

import mainWindowController
import loginWindowController


class ViewController(QtCore.QObject):
    def loadLoginView(self):
        self.viewlogin = loginWindowController.loginWindowController()
        self.viewlogin.loginSignal.connect(self.loadMainWinView)
        self.viewlogin.show()

    def loadMainWinView(self, userId, userName, userClass):
        self.viewMainWIn = mainWindowController.mainWindowController()
        self.viewMainWIn.show()
        self.viewMainWIn.refreshCard(userId, userName, userClass)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    view = ViewController()
    view.loadLoginView()

    sys.exit(app.exec_())

    # Form.setWindowFlags(Qt.Qt.CustomizeWindowHint)
