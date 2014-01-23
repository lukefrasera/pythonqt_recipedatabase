from PyQt4.QtGui import *
import MySQLdb as mdb
from PyQt4.QtCore import *

class loginWidget(QWidget):
	def __init__(self):
		super(loginWidget,self).__init__()
		self.connected = False
		self.createLoginPage()	
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.verticalLogin)
		self.setLayout(mainLayout)

	def createLoginPage(self):
		self.verticalLogin  = QGroupBox("Login")
		layout = QFormLayout()

		self.UsernameLabel = QLabel("Username")
		self.Username = QLineEdit()

		self.passwordLabel = QLabel("Password")
		self.password = QLineEdit()
		self.password.setEchoMode(2)

		self.LoginButton = QPushButton("Login")
		self.LoginButton.clicked.connect(self.login)
		self.incorrect = QLabel("incorrect Username/Password")
		self.incorrect.hide()

		layout.addRow(self.UsernameLabel,self.Username)
		layout.addRow(self.passwordLabel,self.password)
		layout.addRow(self.LoginButton)
		layout.addRow(self.incorrect)
		self.verticalLogin.setLayout(layout)


	def login(self):
		self.User = str(self.Username.text())
		self.Pass = str(self.password.text())
		try:
			self.con = mdb.connect(host = '127.0.0.1', user = self.User, passwd = self.Pass, db = 'world')
			self.connected = True
			self.con.close()
			self.incorrect.hide()
			self.emit(SIGNAL("loginComplete()"))
		except:
			self.incorrect.show()