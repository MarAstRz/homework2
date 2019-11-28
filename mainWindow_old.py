# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from classCard import Ui_Form


class Ui_MainWindow(object):
    workIconBlue = QtGui.QIcon()
    workIconGray = QtGui.QIcon()
    messageIconBlue = QtGui.QIcon()
    messageIconGray = QtGui.QIcon()
    infoIconBlue = QtGui.QIcon()
    infoIconGray = QtGui.QIcon()



    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 399)
        MainWindow.setMinimumSize(QtCore.QSize(640, 340))
        MainWindow.setMaximumSize(QtCore.QSize(640, 500))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "outline:none;\n"
                                 "color:white;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.topTitleBar = QtWidgets.QWidget(self.centralwidget)
        self.topTitleBar.setGeometry(QtCore.QRect(0, 0, 640, 56))
        self.topTitleBar.setStyleSheet("\n"
                                       "border:none;\n"
                                       "\n"
                                       "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.697, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(204, 204, 204, 255));\n"
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

        self.closeButton.clicked.connect(QtCore.QCoreApplication.instance().quit)


        self.minimumButton = QtWidgets.QPushButton(self.topTitleBar)
        self.minimumButton.setGeometry(QtCore.QRect(30, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.minimumButton.setFont(font)
        self.minimumButton.setStyleSheet("QPushButton{\n"
                                         "color : white;\n"
                                         "border : none;\n"
                                         "background-color : rgb(254, 204, 102);\n"
                                         "border-radius:7px;}\n"
                                         "QPushButton:hover{\n"
                                         "color: black;}")
        self.minimumButton.setObjectName("minimumButton")
        self.maximumButton = QtWidgets.QPushButton(self.topTitleBar)
        self.maximumButton.setGeometry(QtCore.QRect(52, 8, 14, 14))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(9)
        self.maximumButton.setFont(font)
        self.maximumButton.setStyleSheet("QPushButton{\n"
                                         "color : white;\n"
                                         "border : none;\n"
                                         "background-color : rgb(103, 194, 83);\n"
                                         "border-radius:7px;}\n"
                                         "QPushButton:hover{\n"
                                         "color: black;}")
        self.maximumButton.setObjectName("maximumButton")
        self.userLogoButton = QtWidgets.QPushButton(self.topTitleBar)
        self.userLogoButton.setGeometry(QtCore.QRect(554, 12, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.userLogoButton.setFont(font)
        self.userLogoButton.setStyleSheet("border-radius:16px;\n"
                                          "background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(15, 128, 255), stop:1 rgb(0, 0, 255));\n"
                                          "")
        self.userLogoButton.setObjectName("userLogoButton")
        self.settingButton = QtWidgets.QPushButton(self.topTitleBar)
        self.settingButton.setGeometry(QtCore.QRect(596, 12, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(23)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet("border-radius:16px;\n"
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
        self.workButton = QtWidgets.QPushButton(self.topTitleBar)
        self.workButton.setGeometry(QtCore.QRect(252, 12, 32, 32))
        self.workButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.workButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.workButton.setText("")
        icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap(":/icon/order_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/order_blue.png"))
        self.workButton.setIcon(icon1)
        self.workButton.setIconSize(QtCore.QSize(32, 32))
        self.workButton.setCheckable(False)
        self.workButton.setChecked(False)
        self.workButton.setAutoDefault(False)
        self.workButton.setDefault(False)
        self.workButton.setObjectName("workButton")








        self.messageButton = QtWidgets.QPushButton(self.topTitleBar)
        self.messageButton.setGeometry(QtCore.QRect(304, 12, 32, 32))
        self.messageButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.messageButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/user_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.messageButton.setIcon(icon2)
        self.messageButton.setIconSize(QtCore.QSize(32, 32))
        self.messageButton.setCheckable(False)
        self.messageButton.setObjectName("messageButton")
        self.infoButton = QtWidgets.QPushButton(self.topTitleBar)
        self.infoButton.setGeometry(QtCore.QRect(356, 12, 32, 32))
        self.infoButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.infoButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/setting_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon3)
        self.infoButton.setIconSize(QtCore.QSize(32, 32))
        self.infoButton.setCheckable(False)
        self.infoButton.setObjectName("infoButton")
        self.thirdW = QtWidgets.QWidget(self.centralwidget)
        self.thirdW.setGeometry(QtCore.QRect(0, 56, 640, 270))
        self.thirdW.setObjectName("thirdW")
        self.label_6 = QtWidgets.QLabel(self.thirdW)
        self.label_6.setGeometry(QtCore.QRect(280, 120, 58, 16))
        self.label_6.setStyleSheet("color:black;")
        self.label_6.setObjectName("label_6")
        self.firstW = QtWidgets.QWidget(self.centralwidget)
        self.firstW.setEnabled(True)
        self.firstW.setGeometry(QtCore.QRect(0, 56, 640, 330))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.firstW.setFont(font)
        self.firstW.setObjectName("firstW")
        self.cardArea = QtWidgets.QScrollArea(self.firstW)


        self.cardArea.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal"
                                                        "{"
                                                        "height:8px;"
                                                        "background:rgba(0,0,0,0%);"
                                                        "margin:0px,0px,0px,0px;"
                                                        "padding-left:9px;"
                                                        "padding-right:9px;"
                                                        "}"
                                                        "QScrollBar::handle:horizontal"
                                                        "{"
                                                        "height:8px;"
                                                        "background:rgba(0,0,0,25%);"
                                                        " border-radius:4px;"
                                                        "min-width:20;"
                                                        "}"
                                                        "QScrollBar::handle:horizontal:hover"
                                                        "{"
                                                        "height:8px;"
                                                        "background:rgba(0,0,0,50%);"
                                                        " border-radius:4px;"
                                                        "min-width:20;"
                                                        "}"
                                                        "QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal"
                                                        "{"
                                                        "width:0px;"
                                                        
                                                        "}"
                                                          "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal"
                                                          "{"
                                                          "background:rgba(0,0,0,10%);"
                                                          "border-radius:4px;"
                                                          "}"


                                                    )
        self.cardArea.verticalScrollBar().setStyleSheet(

                                                   "QScrollBar::sub-line:vertical"
                                                   "{"
                                                   "height:9px;width:8px;"
                                                   "border-image:url(:/images/a/1.png);"
                                                   "subcontrol-position:top;"
                                                   "}"
                                                   "QScrollBar::add-line:vertical:hover"
                                                   "{"
                                                   "height:9px;width:8px;"
                                                   "border-image:url(:/images/a/4.png);"
                                                   "subcontrol-position:bottom;"
                                                   "}"
                                                   "QScrollBar::sub-line:vertical:hover"
                                                   "{"
                                                   "height:9px;width:8px;"
                                                   "border-image:url(:/images/a/2.png);"
                                                   "subcontrol-position:top;"
                                                   "}"
                                                   )

        self.cardArea.setGeometry(QtCore.QRect(0, 0, 640, 240))
        self.cardArea.setStyleSheet("border:none;")
        self.cardArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cardArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.cardArea.setWidgetResizable(True)
        self.cardArea.setObjectName("cardArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 640, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(658, 220))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.testCard_1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.testCard_1.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.testCard_1.setMinimumSize(QtCore.QSize(200, 200))
        self.testCard_1.setMaximumSize(QtCore.QSize(200, 200))
        self.testCard_1.setStyleSheet("background-color: rgb(15, 128, 255);\n"
                                      "\n"
                                      "border-radius: 10px;")
        self.testCard_1.setObjectName("testCard_1")
        self.submitButton = QtWidgets.QPushButton(self.testCard_1)
        self.submitButton.setGeometry(QtCore.QRect(52, 140, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.submitButton.setObjectName("submitButton")
        self.cardInfo_1 = QtWidgets.QWidget(self.testCard_1)
        self.cardInfo_1.setGeometry(QtCore.QRect(0, 10, 200, 120))
        self.cardInfo_1.setStyleSheet("color:white;")
        self.cardInfo_1.setObjectName("cardInfo_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cardInfo_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ClassName = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.ClassName.setFont(font)
        self.ClassName.setAutoFillBackground(False)
        self.ClassName.setAlignment(QtCore.Qt.AlignCenter)
        self.ClassName.setWordWrap(False)
        self.ClassName.setObjectName("ClassName")
        self.verticalLayout.addWidget(self.ClassName)
        self.className = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.className.setFont(font)
        self.className.setAlignment(QtCore.Qt.AlignCenter)
        self.className.setObjectName("className")
        self.verticalLayout.addWidget(self.className)
        self.DeadLine = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.DeadLine.setFont(font)
        self.DeadLine.setAlignment(QtCore.Qt.AlignCenter)
        self.DeadLine.setObjectName("DeadLine")
        self.verticalLayout.addWidget(self.DeadLine)
        self.deadLine = QtWidgets.QLabel(self.cardInfo_1)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.deadLine.setFont(font)
        self.deadLine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deadLine.setTextFormat(QtCore.Qt.AutoText)
        self.deadLine.setAlignment(QtCore.Qt.AlignCenter)
        self.deadLine.setObjectName("deadLine")
        self.verticalLayout.addWidget(self.deadLine)


        self.testCard_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.testCard_2.setGeometry(QtCore.QRect(220, 10, 200, 200))
        self.testCard_2.setMinimumSize(QtCore.QSize(200, 200))
        self.testCard_2.setMaximumSize(QtCore.QSize(200, 200))
        self.testCard_2.setStyleSheet("background-color: rgb(64, 128, 2);\n"
                                      "border-radius: 10px;")
        self.testCard_2.setObjectName("testCard_2")
        self.submitButton_2 = QtWidgets.QPushButton(self.testCard_2)
        self.submitButton_2.setEnabled(False)
        self.submitButton_2.setGeometry(QtCore.QRect(52, 140, 96, 32))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.submitButton_2.setFont(font)
        self.submitButton_2.setAcceptDrops(False)
        self.submitButton_2.setStyleSheet("QPushButton{\n"
                                          "background-color: rgb(179, 179, 179);}\n"
                                          "QPushButton:enabled{\n"
                                          "background-color: rgb(0, 204, 0);}")
        self.submitButton_2.setAutoDefault(False)
        self.submitButton_2.setDefault(False)
        self.submitButton_2.setFlat(False)
        self.submitButton_2.setObjectName("submitButton_2")
        self.cardInfo_2 = QtWidgets.QWidget(self.testCard_2)
        self.cardInfo_2.setGeometry(QtCore.QRect(0, 10, 200, 120))
        self.cardInfo_2.setStyleSheet("color:white;")
        self.cardInfo_2.setObjectName("cardInfo_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cardInfo_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ClassName_2 = QtWidgets.QLabel(self.cardInfo_2)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.ClassName_2.setFont(font)
        self.ClassName_2.setAutoFillBackground(False)
        self.ClassName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ClassName_2.setWordWrap(False)
        self.ClassName_2.setObjectName("ClassName_2")
        self.verticalLayout_2.addWidget(self.ClassName_2)
        self.className_2 = QtWidgets.QLabel(self.cardInfo_2)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.className_2.setFont(font)
        self.className_2.setAlignment(QtCore.Qt.AlignCenter)
        self.className_2.setObjectName("className_2")
        self.verticalLayout_2.addWidget(self.className_2)
        self.DeadLine_2 = QtWidgets.QLabel(self.cardInfo_2)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(18)
        self.DeadLine_2.setFont(font)
        self.DeadLine_2.setAlignment(QtCore.Qt.AlignCenter)
        self.DeadLine_2.setObjectName("DeadLine_2")
        self.verticalLayout_2.addWidget(self.DeadLine_2)
        self.deadLine_2 = QtWidgets.QLabel(self.cardInfo_2)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.deadLine_2.setFont(font)
        self.deadLine_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deadLine_2.setTextFormat(QtCore.Qt.AutoText)
        self.deadLine_2.setAlignment(QtCore.Qt.AlignCenter)
        self.deadLine_2.setObjectName("deadLine_2")
        self.verticalLayout_2.addWidget(self.deadLine_2)
        self.cardArea.setWidget(self.scrollAreaWidgetContents)
        self.secondW = QtWidgets.QWidget(self.centralwidget)
        self.secondW.setGeometry(QtCore.QRect(0, 56, 640, 300))
        self.secondW.setStyleSheet("color : black;")
        self.secondW.setObjectName("secondW")
        self.userLogoButton_2 = QtWidgets.QPushButton(self.secondW)
        self.userLogoButton_2.setGeometry(QtCore.QRect(50, 20, 96, 96))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(39)
        self.userLogoButton_2.setFont(font)
        self.userLogoButton_2.setStyleSheet("border-radius:48px;\n"
                                            "background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(15, 128, 255), stop:1 rgb(0, 0, 255));\n"
                                            "color:white;\n"
                                            "")
        self.userLogoButton_2.setObjectName("userLogoButton_2")
        self.pushButton = QtWidgets.QPushButton(self.secondW)
        self.pushButton.setGeometry(QtCore.QRect(59, 126, 78, 13))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(11)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:none;\n"
                                      "background-color: rgb(179, 179, 179);\n"
                                      "border-radius:6px;\n"
                                      "color:rgb(76, 76, 76)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.secondW)
        self.pushButton_2.setGeometry(QtCore.QRect(75, 150, 46, 13))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:none;\n"
                                        "background-color: rgb(179, 179, 179);\n"
                                        "border-radius:6px;\n"
                                        "color:rgb(76, 76, 76)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.userInfoDetail = QtWidgets.QWidget(self.secondW)
        self.userInfoDetail.setGeometry(QtCore.QRect(146, 20, 491, 251))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        self.userInfoDetail.setFont(font)
        self.userInfoDetail.setObjectName("userInfoDetail")
        self.label = QtWidgets.QLabel(self.userInfoDetail)
        self.label.setGeometry(QtCore.QRect(20, 0, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.userInfoDetail)
        self.widget.setGeometry(QtCore.QRect(92, 40, 254, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.topTitleBar.raise_()
        self.thirdW.raise_()
        self.secondW.raise_()
        self.firstW.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.messageButton.clicked.connect(self.secondW.raise_)
        self.infoButton.clicked.connect(self.thirdW.raise_)
        self.workButton.clicked.connect(self.firstW.raise_)

        self.workIconBlue.addPixmap(QtGui.QPixmap(":/icon/order_blue.png"))
        self.workIconGray.addPixmap(QtGui.QPixmap(":/icon/order_g.png"))
        self.messageIconBlue.addPixmap(QtGui.QPixmap(":/icon/user_blue.png"))
        self.messageIconGray.addPixmap(QtGui.QPixmap(":/icon/user_g.png"))
        self.infoIconBlue.addPixmap(QtGui.QPixmap(":/icon/setting_blue.png"))
        self.infoIconGray.addPixmap(QtGui.QPixmap(":/icon/setting_g.png"))



        self.workButton.clicked.connect(self.workButtonOnClick)
        self.messageButton.clicked.connect(self.messageButtonOnClick)
        self.infoButton.clicked.connect(self.infoButtonOnClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeButton.setText(_translate("MainWindow", "×"))
        self.minimumButton.setText(_translate("MainWindow", "-"))
        self.maximumButton.setText(_translate("MainWindow", "+"))
        self.userLogoButton.setText(_translate("MainWindow", "哲"))
        self.label_6.setText(_translate("MainWindow", "界面3"))
        self.submitButton.setText(_translate("MainWindow", "点击提交"))
        self.ClassName.setText(_translate("MainWindow", "课程名称"))
        self.className.setText(_translate("MainWindow", "C语言程序设计实验"))
        self.DeadLine.setText(_translate("MainWindow", "截止日期"))
        self.deadLine.setText(_translate("MainWindow", "2019年12月10日"))
        self.submitButton_2.setText(_translate("MainWindow", "已提交"))
        self.ClassName_2.setText(_translate("MainWindow", "课程名称"))
        self.className_2.setText(_translate("MainWindow", "Python程序设计实验"))
        self.DeadLine_2.setText(_translate("MainWindow", "截止日期"))
        self.deadLine_2.setText(_translate("MainWindow", "2019年11月10日"))
        self.userLogoButton_2.setText(_translate("MainWindow", "哲"))
        self.pushButton.setText(_translate("MainWindow", "更改头像背景"))
        self.pushButton_2.setText(_translate("MainWindow", "修改密码"))
        self.label.setText(_translate("MainWindow", "我的信息:"))
        self.label_2.setText(_translate("MainWindow", "范润哲"))
        self.label_4.setText(_translate("MainWindow", "170267"))
        self.label_3.setText(_translate("MainWindow", "信息与计算科学172"))


    def workButtonOnClick(self):
        #self.workButton.setChecked(True);

        self.workButton.setIcon(self.workIconBlue)
        self.infoButton.setIcon(self.infoIconGray)
        self.messageButton.setIcon(self.messageIconGray)

    def messageButtonOnClick(self):
        self.messageButton.setIcon(self.messageIconBlue)
        self.workButton.setIcon(self.workIconGray)
        self.infoButton.setIcon(self.infoIconGray)

    def infoButtonOnClick(self):
        self.infoButton.setIcon(self.infoIconBlue)
        self.messageButton.setIcon(self.messageIconGray)
        self.workButton.setIcon(self.workIconGray)
import mainWindowIcon_rc
