from PyQt5 import QtCore, QtGui, QtWidgets
from scorewidnow import Ui_ScoreWindow
import sys
from openWindow import Ui_OpenWindow
from PyQt5.QtWidgets import QFontDialog, QTextEdit, QFileDialog, QListWidget
from New import Ui_Form as Form
from evaluatewindow import Ui_EvaluateWindow as Box
import numpy as np
import sqlite3
mycricketapp = sqlite3.connect('match.db')
curs   =  mycricketapp.cursor()


class Ui_MainWindow(object):

    

    def __init__(self):
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Form()                           
        self.new_screen.setupUi(self.evalDialog)
        
        self.EvaluateWindow= QtWidgets.QMainWindow()
        self.eval_screen= Box()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen= Ui_OpenWindow()
        self.open_screen.setupUi(self.openDialog)

        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen= Ui_ScoreWindow()
        self.score_screen.setupUi(self.scoreDialog)
        
      
    
    def setupUi(self, MainWindow):     
        self.batsmancount=0
        self.wkeepercount=0
        self.allcount=0
        self.ballcount=0
        self.totalcount=0
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow= MainWindow
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        ##Batman COUNT
        self.Batsman = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setIndent(1)
        self.Batsman.setObjectName("Batsman")
        self.horizontalLayout.addWidget(self.Batsman)

        
        self.Batcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batcount.setFont(font)
        self.Batcount.setObjectName("Batcount")
        self.horizontalLayout.addWidget(self.Batcount)


        #WICKETKEEPER COUNT
        self.Wicketkeeepr = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeepr.setFont(font)
        self.Wicketkeeepr.setObjectName("Wicketkeeepr")
        self.horizontalLayout.addWidget(self.Wicketkeeepr)

        
        self.Wkcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wkcount.setFont(font)
        self.Wkcount.setIndent(10)
        self.Wkcount.setObjectName("Wkcount")
        self.horizontalLayout.addWidget(self.Wkcount)

        #ALLROUNDER COUNT
        self.Allrounder = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setObjectName("Allrounder")
        self.horizontalLayout.addWidget(self.Allrounder)

        
        self.Alrcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Alrcount.setFont(font)
        self.Alrcount.setIndent(10)
        self.Alrcount.setObjectName("Alrcount")
        self.horizontalLayout.addWidget(self.Alrcount)

        #BOWLER COUNT
        self.Bowlers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlers.setFont(font)
        self.Bowlers.setObjectName("Bowlers")
        self.horizontalLayout.addWidget(self.Bowlers)

        
        self.Bowlcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlcount.setFont(font)
        self.Bowlcount.setIndent(10)
        self.Bowlcount.setObjectName("Bowlcount")
        self.horizontalLayout.addWidget(self.Bowlcount)

        
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 20, -1, 20)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")



        #RADIOBUTTON BATSMAN
        self.BATSMAN = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BATSMAN.setFont(font)
        self.BATSMAN.setTabletTracking(False)
        self.BATSMAN.setAcceptDrops(False)
        self.BATSMAN.setToolTipDuration(20)
        self.BATSMAN.setStyleSheet("Batmans")
        self.BATSMAN.setObjectName("Batsman_2")
        self.horizontalLayout_3.addWidget(self.BATSMAN)

        #Wicketkeeper Button
        self.WICKETKEEPER = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.WICKETKEEPER.setFont(font)
        self.WICKETKEEPER.setObjectName("Wicketkeeper")
        self.horizontalLayout_3.addWidget(self.WICKETKEEPER)

        #Allrounder Button
        self.ALLROUNDER = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ALLROUNDER.setFont(font)
        self.ALLROUNDER.setChecked(False)
        self.ALLROUNDER.setObjectName("Allrounder_2")
        self.horizontalLayout_3.addWidget(self.ALLROUNDER)


        #Bowler Button
        self.BOWLER = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BOWLER.setFont(font)
        self.BOWLER.setObjectName("Bowlers_2")
        self.horizontalLayout_3.addWidget(self.BOWLER)


        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        
        self.Totalplayers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Totalplayers.setFont(font)
        self.Totalplayers.setIndent(30)
        self.Totalplayers.setObjectName("Totalplayers")
        self.horizontalLayout_5.addWidget(self.Totalplayers)

        
        self.playerscount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.playerscount.setFont(font)
        self.playerscount.setIndent(-10)
        self.playerscount.setObjectName("playerscount")
        self.horizontalLayout_5.addWidget(self.playerscount)


        
        self.TeamName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setIndent(100)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_5.addWidget(self.TeamName)


        
        self.name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setIndent(60)
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)


        
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(778, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)


        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #LIST WIDGET 2
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)

        #LIST WIDGET 
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")


        ##MenuBar
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #NEW
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.actionNew_Team.setShortcut("Ctrl+N")
        self.actionNew_Team.triggered.connect(self.file_new)
        #OPEN
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.actionOpen_Team.setShortcut("Ctrl+O")
        self.actionOpen_Team.triggered.connect(self.file_open)
        #SAVE
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.actionSave_Team.setShortcut("Ctrl+S")
        self.actionSave_Team.triggered.connect(self.file_save)
        #EVALUATE
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.actionEvaluate_Team.setShortcut("Ctrl+E")
        self.actionEvaluate_Team.triggered.connect(self.file_evaluate)
        #QUIT
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.menuManage_Teams.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)

        
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #BUTTON clicked
        self.BATSMAN.clicked.connect(self.load_names)
        self.WICKETKEEPER.clicked.connect(self.load_names)
        self.ALLROUNDER.clicked.connect(self.load_names)
        self.BOWLER.clicked.connect(self.load_names)

        #DOUBLE CLICK
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)

        self.items = []

        
        self.new_screen.pushButton.clicked.connect(self.namechange)
        self.open_screen.openButton.clicked.connect(self.boxclose)
        
        self.eval_screen.SelectTeam.currentTextChanged.connect(self.combo)
        self.eval_screen.Calculate.clicked.connect(self.SCORE)

##########################################################################################
                                                    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.Batsman.setText(_translate("MainWindow", "Batsman(Bat)"))
        self.Batcount.setText(_translate("MainWindow", "0"))
        
        self.Wicketkeeepr.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.Wkcount.setText(_translate("MainWindow", "0"))
        
        self.Allrounder.setText(_translate("MainWindow", "Allrounder (ALR)"))
        self.Alrcount.setText(_translate("MainWindow", "0"))
        
        self.Bowlers.setText(_translate("MainWindow", "Bowlers (Bowl)"))
        self.Bowlcount.setText(_translate("MainWindow", "0"))
        
        self.BATSMAN.setText(_translate("MainWindow", "Batsman"))
        self.WICKETKEEPER.setText(_translate("MainWindow", "WicketKeeper"))
        self.ALLROUNDER.setText(_translate("MainWindow", "AllRounder"))
        self.BOWLER.setText(_translate("MainWindow", "Bowlers"))
        
        self.Totalplayers.setText(_translate("MainWindow", "Total Players: "))
        self.playerscount.setText(_translate("MainWindow", "00"))
        self.TeamName.setText(_translate("MainWindow", "Team Name :"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "                                   Available Players                                                                                                        Selected Players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        


            

    #NEW FILE MENU
    def file_new(self):
        self.evalDialog.show()

    
    #FILE OPENING MENU
    def file_open(self):
        self.openDialog.show()
        
    
    #FILE SAVING MWNU
    def file_save(self):
        for index in range(self.listWidget.count()):
            self.items.append(str(self.listWidget.item(index).text()))
        actual_score=[]
        for player in self.items:
            curs.execute("SELECT Points from match WHERE Player='"+player+"';")
            actual_score.append(curs.fetchone())
        
        score=[]
        for i in range(len(actual_score)):
            score.append(actual_score[i][0])
        List= tuple(zip(self.items,score))
        myteam= sqlite3.connect('TEAM.db')
        curser= myteam.cursor()
        teamname= self.name.text()
        for i in range(len(List)):
            curser.execute("INSERT INTO team ('NAMES','PLAYERS','SCORES') VALUES ('%s','%s','%d')"%(teamname,List[i][0],List[i][1]))

        myteam.commit()
                  
 
    #Evaluate MENU
    def file_evaluate(self):
        self.EvaluateWindow.show()

    def combo(self):
        self.eval_screen.Selectmatch.currentTextChanged.connect(self.combo2)
        
                
    def combo2(self):
        myteam=sqlite3.connect("TEAM.db")
        cu= myteam.cursor()
        
        team = self.eval_screen.SelectTeam.currentText()
        cu.execute("SELECT PlAYERS from team WHERE NAMES='"+team+"';")
        player= cu.fetchall()
        self.eval_screen.PlayerList.clear()
        for i in range(len(player)):
            item= QtWidgets.QListWidgetItem(player[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.eval_screen.PlayerList.addItem(item)
        
        cu.execute("SELECT SCORES from team WHERE NAMES='"+team+"';")
        score=cu.fetchall()
        self.teamscore=[]
        for i in range(len(score)):
            self.teamscore.append(score[i][0])
    
        self.eval_screen.ScoreList.clear()
        for i in range(len(score)):
            items= QtWidgets.QListWidgetItem(str(score[i][0]))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            items.setFont(font)
            items.setBackground(QtGui.QColor('#fdc086'))
            self.eval_screen.ScoreList.addItem(items)

    def SCORE(self):
        self.scoreDialog.show()
        self.score_screen.Score.setText(str(sum(self.teamscore)))
        
        
        
    #QUITING METHOD    
    def quit(self):
        sys.exit()


    def namechange(self):
        self.tname= self.new_screen.lineEdit.text()
        print(self.tname)
        self.name.setText(self.tname)
        self.evalDialog.close()

    def boxclose(self):
        teamname = self.open_screen.OpenTheTeam.text()
        myteam= sqlite3.connect('TEAM.db')
        curser= myteam.cursor()
        curser.execute("SELECT PLAYERS from team WHERE NAMES= '"+teamname+"';")
        hu= curser.fetchall()
        self.listWidget.clear()
        for i in range(len(hu)):
            item= QtWidgets.QListWidgetItem(hu[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('sea green'))
            self.listWidget.addItem(item)
            
        self.openDialog.close()
        
    def load_names(self):
        
        Batsman='Batsman'
        WicketKeeper='WicketKeeper'
        Allrounder= 'Allrounder'
        Bowler= 'Bowler'
        sql    = "SELECT Player from match WHERE Type = '"+Batsman+"';"
        sql2   = "SELECT Player from match WHERE Type = '"+WicketKeeper+"';"
        sql3   = "SELECT Player from match WHERE Type ='"+Allrounder+"';"
        sql4   = "SELECT Player from match WHERE Type = '"+Bowler+"';"
        
        if self.BATSMAN.isChecked()==True:
            curs.execute(sql)
            BT= curs.fetchall()
            self.listWidget_2.clear()
            for i in range(len(BT)):
                item= QtWidgets.QListWidgetItem(BT[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget_2.addItem(item)   
            
                
        if self.WICKETKEEPER.isChecked()==True:
            curs.execute(sql2)
            WK= curs.fetchall()
            self.listWidget_2.clear()
            for i in range(len(WK)):
                item2= QtWidgets.QListWidgetItem(WK[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item2.setFont(font)
                self.listWidget_2.addItem(item2)
            
            

        if self.ALLROUNDER.isChecked()==True:
            curs.execute(sql3)
            AL= curs.fetchall()
            self.listWidget_2.clear()
            for i in range(len(AL)):
                item3= QtWidgets.QListWidgetItem(AL[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item3.setFont(font)
                self.listWidget_2.addItem(item3)
            
                
        if self.BOWLER.isChecked()==True:
            curs.execute(sql4)
            BL= curs.fetchall()
            self.listWidget_2.clear()
            for i in range(len(BL)):
                item4= QtWidgets.QListWidgetItem(BL[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item4.setFont(font)
                itemL=BL[i][0]
                self.listWidget_2.addItem(item4)
        
            


    def removelist1(self, item):
        
         if self.BATSMAN.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.batsmancount+=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Batcount.setText(str(self.batsmancount))
            self.playerscount.setText(str(self.totalcount))

         elif self.WICKETKEEPER.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.wkeepercount+=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Wkcount.setText(str(self.wkeepercount))
            self.playerscount.setText(str(self.totalcount))

         elif self.ALLROUNDER.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.allcount+=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Alrcount.setText(str(self.allcount))
            self.playerscount.setText(str(self.totalcount))

         else :
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.ballcount+=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Bowlcount.setText(str(self.ballcount))
            self.playerscount.setText(str(self.totalcount))
        

    def removelist2(self, item):
        if self.BATSMAN.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item)
            self.batsmancount-=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Batcount.setText(str(self.batsmancount))
            self.playerscount.setText(str(self.totalcount))

        elif self.WICKETKEEPER.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item)
            self.wkeepercount-=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Wkcount.setText(str(self.wkeepercount))
            self.playerscount.setText(str(self.totalcount))

        elif self.ALLROUNDER.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item)
            self.allcount-=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Alrcount.setText(str(self.allcount))
            self.playerscount.setText(str(self.totalcount))

        else:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item)
            self.ballcount-=1
            self.totalcount=self.listWidget.count()
            self.error()
            self.Bowlcount.setText(str(self.ballcount))
            self.playerscount.setText(str(self.totalcount))



    def error(self):
        error_dialog = QtWidgets.QErrorMessage()
        
        if self.batsmancount>=0 and self.batsmancount<6:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 5 batsman are allowed')
            error_dialog.exec_()

        if self.wkeepercount>=0 and self.wkeepercount<2:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 1 keeper are allowed')
            error_dialog.exec_()

        if self.allcount>=0 and self.allcount<3:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 2 allrounders are allowed')
            error_dialog.exec_()

        if self.ballcount>=0 and self.ballcount<5:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 5 bowlers are allowed')
            error_dialog.exec_()

        if self.totalcount>=0 and self.totalcount<12:
            pass
        else:
            error_dialog.showMessage('Oh no! No more than 11 Players are allowed')
            error_dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

