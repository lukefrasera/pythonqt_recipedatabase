import MySQLdb as mdb
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from classFile import recipe
from homePageClass import HomeWidget
from LoginClass import loginWidget
from classAddWidget import addWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()

        self.setWindowTitle("Recipe - Database")
        self.setWindowIcon(QIcon("lukeicon.png"))
        self.resize(1280,800)
        self.createStatusBar()
        self.createLoginPage()

        self.connect(self.loginWindow,SIGNAL("loginComplete()"), self.createHomePage)

    def createLoginPage(self):
        self.loginWindow = loginWidget()
        self.setCentralWidget(self.loginWindow)

    def createHomePage(self):
        self.homeWindow = HomeWidget()
        self.setCentralWidget(self.homeWindow)
        self.connect(self.homeWindow, SIGNAL("addSignal()"), self.createAddPage)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def createAddPage(self):
        self.addWindow = addWidget()
        self.addWindow.setPass(self.loginWindow.User,self.loginWindow.Pass)
        self.setCentralWidget(self.addWindow)
        self.connect(self.addWindow, SIGNAL("addComplete()"), self.createHomePage)



def main():
    app = QApplication(sys.argv)
    w = mainWindow()
    w.show()

    sys.exit(app.exec_())


if __name__ =='__main__':
    main()