# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, func):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 1060)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 1191, 491))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushSearch.setGeometry(QtCore.QRect(1000, 500, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushSearch.setFont(font)
        self.pushSearch.setObjectName("pushSearch")
        self.pushExit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit_2.setGeometry(QtCore.QRect(1000, 620, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushExit_2.setFont(font)
        self.pushExit_2.setObjectName("pushExit_2")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 490, 701, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.tab_project = QtWidgets.QWidget()
        self.tab_project.setObjectName("tab_project")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_project)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 0, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 0, 2, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 4, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setTristate(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 1, 2, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy)
        self.checkBox_16.setTristate(False)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 1, 0, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab_project)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 1, 1, 1, 1)
        self.tab.addTab(self.tab_project, "")
        self.tab_topic = QtWidgets.QWidget()
        self.tab_topic.setObjectName("tab_topic")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_8.setGeometry(QtCore.QRect(577, 30, 88, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_9.setGeometry(QtCore.QRect(435, 30, 135, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_10.setGeometry(QtCore.QRect(97, 30, 111, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_11.setGeometry(QtCore.QRect(310, 30, 118, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy)
        self.checkBox_11.setTristate(False)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_12.setGeometry(QtCore.QRect(215, 30, 88, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_topic)
        self.checkBox_2.setGeometry(QtCore.QRect(2, 30, 88, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setObjectName("checkBox_2")
        self.tab.addTab(self.tab_topic, "")
        self.tab_work = QtWidgets.QWidget()
        self.tab_work.setObjectName("tab_work")
        self.checkBox_14 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_14.setGeometry(QtCore.QRect(215, 30, 81, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_17 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_17.setGeometry(QtCore.QRect(435, 30, 135, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_18.setGeometry(QtCore.QRect(520, 30, 103, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_18.sizePolicy().hasHeightForWidth())
        self.checkBox_18.setSizePolicy(sizePolicy)
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_19.setGeometry(QtCore.QRect(130, 30, 76, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy)
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_20.setGeometry(QtCore.QRect(2, 30, 122, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_20.sizePolicy().hasHeightForWidth())
        self.checkBox_20.setSizePolicy(sizePolicy)
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.tab_work)
        self.checkBox_21.setGeometry(QtCore.QRect(310, 30, 118, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy)
        self.checkBox_21.setTristate(False)
        self.checkBox_21.setObjectName("checkBox_21")
        self.tab.addTab(self.tab_work, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1198, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcut("")
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushSearch.setText(_translate("MainWindow", "Search"))
        self.pushExit_2.setText(_translate("MainWindow", "Exit"))
        self.checkBox_7.setText(_translate("MainWindow", "Manual"))
        self.checkBox_5.setText(_translate("MainWindow", "BackEnd"))
        self.checkBox_6.setText(_translate("MainWindow", "Code"))
        self.checkBox.setText(_translate("MainWindow", "Automate"))
        self.checkBox_3.setText(_translate("MainWindow", "FrameWork"))
        self.checkBox_4.setText(_translate("MainWindow", "FrontEnd"))
        self.checkBox_15.setText(_translate("MainWindow", "Python"))
        self.checkBox_16.setText(_translate("MainWindow", "DataBase"))
        self.checkBox_13.setText(_translate("MainWindow", "Java"))
        self.tab.setTabText(self.tab.indexOf(self.tab_project),
                            _translate("MainWindow", "Project"))
        self.checkBox_8.setText(_translate("MainWindow", "Inferred"))
        self.checkBox_9.setText(_translate("MainWindow", "Undemarcated"))
        self.checkBox_10.setText(_translate("MainWindow", "Enviroment"))
        self.checkBox_11.setText(_translate("MainWindow", "Demarcated"))
        self.checkBox_12.setText(_translate("MainWindow", "Parking"))
        self.checkBox_2.setText(_translate("MainWindow", "Project"))
        self.tab.setTabText(self.tab.indexOf(self.tab_topic),
                            _translate("MainWindow", "Topic"))
        self.checkBox_14.setText(_translate("MainWindow", "Meeting"))
        self.checkBox_17.setText(_translate("MainWindow", "Review"))
        self.checkBox_18.setText(_translate("MainWindow", "Ready4Qa"))
        self.checkBox_19.setText(_translate("MainWindow", "Defect"))
        self.checkBox_20.setText(_translate("MainWindow", "Requirement"))
        self.checkBox_21.setText(_translate("MainWindow", "Regression"))
        self.tab.setTabText(self.tab.indexOf(self.tab_work),
                            _translate("MainWindow", "Work"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+X"))

        self.pushExit_2.clicked.connect(
            func.close_application)


if __name__ == "__main__":
    import sys
    from functions import Functions
    func = Functions()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, func)
    MainWindow.show()
    sys.exit(app.exec_())
