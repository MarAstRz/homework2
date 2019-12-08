import os

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


def file_extension(path):
    return os.path.splitext(path)[1]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 540)
        MainWindow.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "outline:none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
                                         "background-color: rgba(255, 255, 255, 0);\n"
                                         "border:none;")
        self.centralwidget.setObjectName("centralwidget")
        self.window = QtWidgets.QWidget(self.centralwidget)
        self.window.setGeometry(QtCore.QRect(0, 0, 350, 515))
        self.window.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.window.setObjectName("window")
        self.topTitleBar = QtWidgets.QWidget(self.window)
        self.topTitleBar.setGeometry(QtCore.QRect(0, 0, 350, 56))
        self.topTitleBar.setStyleSheet("border-bottom-left-radius:0px;\n"
                                       "border-bottom-right-radius:0px;\n"
                                       "border:none;\n"
                                       "\n"
                                       "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.697, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(204, 204, 204, 255));\n"
                                       "\n"
                                       "\n"
                                       "")
        self.topTitleBar.setObjectName("topTitleBar")
        self.closeButton = QtWidgets.QPushButton(self.topTitleBar)
        self.closeButton.setGeometry(QtCore.QRect(8, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{\n"
                                       "color : white;\n"
                                       "border : none;\n"
                                       "background-color : rgb(253, 102, 102);\n"
                                       "border-radius:7px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "color: black;}")
        self.closeButton.setObjectName("closeButton")
        self.settingButton = QtWidgets.QPushButton(self.topTitleBar)
        self.settingButton.setGeometry(QtCore.QRect(306, 12, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(23)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet("\n"
                                         "background-color: rgba(255, 255, 255, 0);\n"
                                         "color : black;\n"
                                         "\n"
                                         "")
        self.settingButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/filter_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon)
        self.settingButton.setIconSize(QtCore.QSize(24, 24))
        self.settingButton.setObjectName("settingButton")
        self.label = QtWidgets.QLabel(self.topTitleBar)
        self.label.setGeometry(QtCore.QRect(110, 18, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(128, 128, 128);\n"
                                 "background-color: rgba(255, 255, 255, 0);\n"
                                 "\n"
                                 "\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.window)
        self.scrollArea.setGeometry(QtCore.QRect(0, 56, 351, 464))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-top-left-radius:0px;\n"
                                      "border-top-right-radius0px;")

        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical"
                                                          "{"
                                                          "width:10px;"
                                                          "background:rgba(0,0,0,0%);"
                                                          "margin:0px,0px,0px,0px;"
                                                          "padding-top:8px;"
                                                          "padding-bottom:8px;"
                                                          "padding-right:4px;"
                                                          "}"
                                                          "QScrollBar::handle:vertical"
                                                          "{"
                                                          "width:6px;"
                                                          "background:rgba(0,0,0,25%);"
                                                          "border-radius:3px;"
                                                          "min-height:20;"
                                                          "}"
                                                          "QScrollBar::handle:vertical:hover"
                                                          "{"
                                                          "height:6px;"
                                                          "background:rgba(0,0,0,50%);"
                                                          "border-radius:3px;"
                                                          "min-height:20;"
                                                          "}"
                                                          "QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical"
                                                          "{"
                                                          "height:0px;"
                                                          "}"
                                                          "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
                                                          "{"
                                                          "background:rgba(0,0,0,10%);"
                                                          "border-radius:3px;"
                                                          "}"
                                                          )

        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 351, 461))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color:gray;")
        MainWindow.setStatusBar(self.statusbar)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(0, 0, 350, 540))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.widget.setObjectName("widget")
        self.widget.setVisible(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeButton.setText(_translate("MainWindow", "×"))
        self.label.setText(_translate("MainWindow", "加载中..."))
        self.statusbar.showMessage("v2.0.0")


