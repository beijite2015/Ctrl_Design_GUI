# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Apr 22 15:16:57 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 533)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.vlLeftHand = QtGui.QVBoxLayout()
        self.vlLeftHand.setObjectName(_fromUtf8("vlLeftHand"))
        self.hlLHTop = QtGui.QHBoxLayout()
        self.hlLHTop.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.hlLHTop.setObjectName(_fromUtf8("hlLHTop"))
        self.bLoadSettings = QtGui.QPushButton(self.centralwidget)
        self.bLoadSettings.setObjectName(_fromUtf8("bLoadSettings"))
        self.hlLHTop.addWidget(self.bLoadSettings)
        self.bSaveSettings = QtGui.QPushButton(self.centralwidget)
        self.bSaveSettings.setObjectName(_fromUtf8("bSaveSettings"))
        self.hlLHTop.addWidget(self.bSaveSettings)
        self.bApplySettings = QtGui.QPushButton(self.centralwidget)
        self.bApplySettings.setObjectName(_fromUtf8("bApplySettings"))
        self.hlLHTop.addWidget(self.bApplySettings)
        self.vlLeftHand.addLayout(self.hlLHTop)
        self.hlLH2nd = QtGui.QHBoxLayout()
        self.hlLH2nd.setObjectName(_fromUtf8("hlLH2nd"))
        self.bPort = QtGui.QPushButton(self.centralwidget)
        self.bPort.setObjectName(_fromUtf8("bPort"))
        self.hlLH2nd.addWidget(self.bPort)
        self.cPort = QtGui.QComboBox(self.centralwidget)
        self.cPort.setObjectName(_fromUtf8("cPort"))
        self.hlLH2nd.addWidget(self.cPort)
        self.bConnect = QtGui.QPushButton(self.centralwidget)
        self.bConnect.setObjectName(_fromUtf8("bConnect"))
        self.hlLH2nd.addWidget(self.bConnect)
        self.vlLeftHand.addLayout(self.hlLH2nd)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vlLeftHand.addWidget(self.line)
        self.saActions = QtGui.QScrollArea(self.centralwidget)
        self.saActions.setFrameShape(QtGui.QFrame.NoFrame)
        self.saActions.setWidgetResizable(True)
        self.saActions.setObjectName(_fromUtf8("saActions"))
        self.saActionsContents = QtGui.QWidget()
        self.saActionsContents.setGeometry(QtCore.QRect(0, 0, 241, 368))
        self.saActionsContents.setObjectName(_fromUtf8("saActionsContents"))
        self.saActionsLayout = QtGui.QGridLayout(self.saActionsContents)
        self.saActionsLayout.setObjectName(_fromUtf8("saActionsLayout"))
        self.bbbAction = QtGui.QPushButton(self.saActionsContents)
        self.bbbAction.setObjectName(_fromUtf8("bbbAction"))
        self.saActionsLayout.addWidget(self.bbbAction, 0, 0, 1, 1)
        self.saActions.setWidget(self.saActionsContents)
        self.vlLeftHand.addWidget(self.saActions)
        self.hlLHBottom = QtGui.QHBoxLayout()
        self.hlLHBottom.setObjectName(_fromUtf8("hlLHBottom"))
        self.tCommand = QOneLineTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tCommand.sizePolicy().hasHeightForWidth())
        self.tCommand.setSizePolicy(sizePolicy)
        self.tCommand.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tCommand.setObjectName(_fromUtf8("tCommand"))
        self.hlLHBottom.addWidget(self.tCommand)
        self.bSend = QtGui.QPushButton(self.centralwidget)
        self.bSend.setMaximumSize(QtCore.QSize(35, 16777215))
        self.bSend.setObjectName(_fromUtf8("bSend"))
        self.hlLHBottom.addWidget(self.bSend)
        self.hlLHBottom.setStretch(0, 5)
        self.hlLHBottom.setStretch(1, 1)
        self.vlLeftHand.addLayout(self.hlLHBottom)
        self.horizontalLayout.addLayout(self.vlLeftHand)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.saTab1 = QtGui.QScrollArea(self.tab)
        self.saTab1.setFrameShape(QtGui.QFrame.NoFrame)
        self.saTab1.setWidgetResizable(True)
        self.saTab1.setObjectName(_fromUtf8("saTab1"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 430))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.bProp1Set = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.bProp1Set.setMaximumSize(QtCore.QSize(30, 16777215))
        self.bProp1Set.setObjectName(_fromUtf8("bProp1Set"))
        self.gridLayout_3.addWidget(self.bProp1Set, 0, 3, 1, 1)
        self.bProp1Get = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.bProp1Get.setMaximumSize(QtCore.QSize(30, 16777215))
        self.bProp1Get.setObjectName(_fromUtf8("bProp1Get"))
        self.gridLayout_3.addWidget(self.bProp1Get, 0, 2, 1, 1)
        self.tProp1 = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tProp1.sizePolicy().hasHeightForWidth())
        self.tProp1.setSizePolicy(sizePolicy)
        self.tProp1.setMinimumSize(QtCore.QSize(0, 5))
        self.tProp1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tProp1.setBaseSize(QtCore.QSize(0, 0))
        self.tProp1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tProp1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tProp1.setTabChangesFocus(True)
        self.tProp1.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.tProp1.setObjectName(_fromUtf8("tProp1"))
        self.gridLayout_3.addWidget(self.tProp1, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.lProp1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lProp1.setObjectName(_fromUtf8("lProp1"))
        self.gridLayout_3.addWidget(self.lProp1, 0, 0, 1, 1)
        self.saTab1.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.saTab1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(200, 130, 120, 80))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 118, 78))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.pushButton_11 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Settings = QtGui.QAction(MainWindow)
        self.actionSave_Settings.setObjectName(_fromUtf8("actionSave_Settings"))
        self.actionLoad_Settings = QtGui.QAction(MainWindow)
        self.actionLoad_Settings.setObjectName(_fromUtf8("actionLoad_Settings"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionLoad_Settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bLoadSettings.setText(_translate("MainWindow", "Load Settings", None))
        self.bSaveSettings.setText(_translate("MainWindow", "Save Settings", None))
        self.bApplySettings.setText(_translate("MainWindow", "Apply Settings", None))
        self.bPort.setText(_translate("MainWindow", "Port", None))
        self.bConnect.setText(_translate("MainWindow", "Connect", None))
        self.bbbAction.setText(_translate("MainWindow", "Action", None))
        self.bSend.setText(_translate("MainWindow", "Send", None))
        self.bProp1Set.setText(_translate("MainWindow", "Set", None))
        self.bProp1Get.setText(_translate("MainWindow", "Get", None))
        self.lProp1.setText(_translate("MainWindow", "Prop1:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TabA", None))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "TabB", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings", None))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

from qonelinetextedit import QOneLineTextEdit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

