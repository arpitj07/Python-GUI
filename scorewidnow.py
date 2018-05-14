
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScoreWindow(object):
    def setupUi(self, ScoreWindow):
        ScoreWindow.setObjectName("ScoreWindow")
        ScoreWindow.resize(471, 386)
        self.centralwidget = QtWidgets.QWidget(ScoreWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Score = QtWidgets.QLineEdit(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(180, 180, 113, 22))
        self.Score.setObjectName("Score")
        self.teamscore = QtWidgets.QLabel(self.centralwidget)
        self.teamscore.setGeometry(QtCore.QRect(180, 130, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamscore.setFont(font)
        self.teamscore.setObjectName("teamscore")
        ScoreWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ScoreWindow)
        self.statusbar.setObjectName("statusbar")
        ScoreWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScoreWindow)
        QtCore.QMetaObject.connectSlotsByName(ScoreWindow)

    def retranslateUi(self, ScoreWindow):
        _translate = QtCore.QCoreApplication.translate
        ScoreWindow.setWindowTitle(_translate("ScoreWindow", "MainWindow"))
        self.teamscore.setText(_translate("ScoreWindow", "Your Team Score :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreWindow = QtWidgets.QMainWindow()
    ui = Ui_ScoreWindow()
    ui.setupUi(ScoreWindow)
    ScoreWindow.show()
    sys.exit(app.exec_())

