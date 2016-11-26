# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from appli import *


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
    global self
    global MainWindow
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(701, 478)
        MainWindow.setWindowOpacity(3.0)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(430, 110, 47, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.client = QtGui.QLineEdit(self.centralWidget)
        self.client.setGeometry(QtCore.QRect(430, 130, 113, 20))
        self.client.setObjectName(_fromUtf8("client"))
        self.label_9 = QtGui.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(430, 60, 61, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(430, 10, 47, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.port = QtGui.QLineEdit(self.centralWidget)
        self.port.setGeometry(QtCore.QRect(580, 80, 113, 20))
        self.port.setObjectName(_fromUtf8("port"))
        self.Mqtt_server = QtGui.QLineEdit(self.centralWidget)
        self.Mqtt_server.setGeometry(QtCore.QRect(430, 80, 113, 20))
        self.Mqtt_server.setObjectName(_fromUtf8("Mqtt_server"))
        self.label_11 = QtGui.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(580, 60, 47, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.password = QtGui.QLineEdit(self.centralWidget)
        self.password.setGeometry(QtCore.QRect(580, 30, 113, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.username = QtGui.QLineEdit(self.centralWidget)
        self.username.setGeometry(QtCore.QRect(430, 30, 113, 20))
        self.username.setObjectName(_fromUtf8("username"))
        self.label_12 = QtGui.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(580, 10, 47, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.linker = QtGui.QPushButton(self.centralWidget)
        self.linker.setGeometry(QtCore.QRect(580, 120, 111, 41))
        self.linker.setObjectName(_fromUtf8("linker"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MQTT", None))
        self.label_6.setText(_translate("MainWindow", "Client ID", None))
        self.client.setText(_translate("MainWindow", "60", None))
        self.label_9.setText(_translate("MainWindow", "Mqtt Server", None))
        self.label_10.setText(_translate("MainWindow", "Username", None))
        self.port.setText(_translate("MainWindow", "11523", None))
        self.Mqtt_server.setText(_translate("MainWindow", "m12.cloudmqtt.com", None))
        self.label_11.setText(_translate("MainWindow", "Port", None))
        self.password.setText(_translate("MainWindow", "MmIWxonlCM7u", None))
        self.username.setText(_translate("MainWindow", "fcfvaydb", None))
        self.label_12.setText(_translate("MainWindow", "Password", None))
        self.linker.setText(_translate("MainWindow", "Connect", None))
        self.label.setText(_translate("MainWindow", "TOPIC", None))
        self.linker.clicked.connect(self.ater)

    def ater(self):
        link2(self)




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

