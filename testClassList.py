from PyQt4.QtCore import *
from PyQt4.QtGui import *

class dList(QWidget):
	def __init__(self):
		super(dList,self).__init__()

		self.setWindowTitle("List Test")
		self.resize(1024,700)


		self.list = []
		self.layout = QVBoxLayout()
		layout2 = QVBoxLayout()
		scroll = QScrollArea()

		self.innerWidget = QWidget()
		self.innerWidget.setMinimumWidth(self.width()-45)
		self.innerWidget.setLayout(self.layout)

		addButton = QPushButton("add")
		removeButton = QPushButton("remove")

		self.layout.addWidget(QPushButton("test"))

		scroll.setWidget(self.innerWidget)
		scroll.setAlignment(Qt.AlignLeft)
		layout2.addWidget(scroll)
		layout2.addWidget(addButton)
		layout2.addWidget(removeButton)
		self.setLayout(layout2)

		addButton.clicked.connect(self.addButton)
		removeButton.clicked.connect(self.removeButton)

		

	ef resizeEvent(self,e):
		self.innerWidget.setMinimumWidth(self.width()-45)
		self.innerWidget.setMaximumWidth(self.width()-45)d

	def addButton(self):
		button = QPushButton("another button")
		self.layout.addWidget(button)
		self.list.append(button)
		self.innerWidget.setMinimumHeight(self.innerWidget.height()+35)
		self.innerWidget.setMaximumHeight(self.innerWidget.height()+35)

	def removeButton(self):
		button = self.list.pop()
		button.hide()
		self.layout.removeWidget(button)
		self.innerWidget.setMinimumHeight(self.innerWidget.height()-35)
		self.innerWidget.setMaximumHeight(self.innerWidget.height()-35)


if __name__ == '__main__':

    import sys
    
    app = QApplication(sys.argv)
    test = dList()
    test.show()

    sys.exit(app.exec_())