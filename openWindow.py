

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenWindow(object):
    def setupUi(self, OpenWindow):
        OpenWindow.setObjectName("OpenWindow")
        OpenWindow.resize(535, 389)
        self.centralwidget = QtWidgets.QWidget(OpenWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.OpenTeam = QtWidgets.QLabel(self.centralwidget)
        self.OpenTeam.setGeometry(QtCore.QRect(150, 120, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OpenTeam.setFont(font)
        self.OpenTeam.setObjectName("OpenTeam")

        
        self.OpenTheTeam = QtWidgets.QLineEdit(self.centralwidget)
        self.OpenTheTeam.setGeometry(QtCore.QRect(180, 160, 151, 22))
        self.OpenTheTeam.setObjectName("OpenTheTeam")
        
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(210, 210, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        
        OpenWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OpenWindow)
        self.statusbar.setObjectName("statusbar")
        OpenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OpenWindow)
        QtCore.QMetaObject.connectSlotsByName(OpenWindow)

    def retranslateUi(self, OpenWindow):
        _translate = QtCore.QCoreApplication.translate
        OpenWindow.setWindowTitle(_translate("OpenWindow", "MainWindow"))
        self.OpenTeam.setText(_translate("OpenWindow", "Enter Team Name to Open"))
        self.openButton.setText(_translate("OpenWindow", "OK"))



