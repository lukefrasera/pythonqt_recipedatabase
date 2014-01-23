from PyQt4.QtGui import *
from PyQt4.QtCore import *
from classIngredient import Ingredient

class DList(QWidget):
	def __init__(self):
		super(DList,self).__init__()
		
		self.setWindowTitle("instructions")
		
		self.ingrList = []
		self.instrList = []
		self.commList = []
		self.keyList = []
		self.refList = []
		
		layout = QVBoxLayout()
		scroll = QScrollArea()
		self.scrollLayout = QVBoxLayout()
		self.innerWidget = QWidget()
		
		#  resize the inner widget set layout
		self.innerWidget.setMinimumWidth(self.width()-45)
		self.innerWidget.setLayout(self.scrollLayout)
		
		#  add widgets to central layout
		self.createIngredientsBox()
		self.createInstructBox()
		self.createCommentsBox()
		self.createKeywords()
		self.createReference()
		
		self.scrollLayout.addWidget(self.ingrBox)
		self.scrollLayout.addWidget(self.instructBox)
		self.scrollLayout.addWidget(self.commentBox)
		self.scrollLayout.addWidget(self.keywordsBox)
		self.scrollLayout.addWidget(self.referenceBox)
		
		#  add scroll box
		scroll.setWidget(self.innerWidget)
		layout.addWidget(scroll)
		
		#  add save/commit button
		self.commitButton = QPushButton("Commit/Save")
		layout.addWidget(self.commitButton)
		self.setMinimumWidth(self.innerWidget.width()+55)
		
		self.setLayout(layout)
		
	def createIngredientsBox(self):
		self.ingrBox = QGroupBox("Ingredients")
		self.ingrLayout = QVBoxLayout()
		self.ingrLayout.setSpacing(0)	
		addDelete = QWidget()
		addDelLay = QHBoxLayout()
		addDelLay.setMargin(0)
		addIngrButton = QPushButton("Add Ingredient")
		delIngrButton = QPushButton("Delete Ingredient")
		addDelLay.addWidget(addIngrButton)
		addDelLay.addWidget(delIngrButton)
		addDelete.setLayout(addDelLay)

		self.ingrLayout.addWidget(addDelete)
		self.ingrBox.setLayout(self.ingrLayout)
		
		addIngrButton.clicked.connect(self.addIngr)
		delIngrButton.clicked.connect(self.delIngr)
		
	def createInstructBox(self):
		self.instructBox = QGroupBox("Instructions")
		self.instructLayout = QVBoxLayout()
		
		addDelete = QWidget()
		addDelLay = QHBoxLayout()
		addDelLay.setMargin(0)
		addInstructButton = QPushButton("Add Instruction")
		delInstructButton = QPushButton("Delete Instruction")
		addDelLay.addWidget(addInstructButton)
		addDelLay.addWidget(delInstructButton)

		addDelete.setLayout(addDelLay)

		self.instructLayout.addWidget(addDelete)
		self.instructBox.setLayout(self.instructLayout)

		
		addInstructButton.clicked.connect(self.addInstruct)
		delInstructButton.clicked.connect(self.delInstruct)

	def createCommentsBox(self):
		self.commentBox = QGroupBox("Comments")
		self.commentLayout = QVBoxLayout()

		addDelete = QWidget()
		addDelLay = QHBoxLayout()
		addDelLay.setMargin(0)
		addInstructButton = QPushButton("Add Comment")
		delInstructButton = QPushButton("Delete Comment")
		addDelLay.addWidget(addInstructButton)
		addDelLay.addWidget(delInstructButton)

		addDelete.setLayout(addDelLay)

		self.commentLayout.addWidget(addDelete)
		self.commentBox.setLayout(self.commentLayout)

		addInstructButton.clicked.connect(self.addComment)
		delInstructButton.clicked.connect(self.delComment)

	def createKeywords(self):
		self.keywordsBox = QGroupBox("Keywords")
		self.keywordLayout = QVBoxLayout()

		addDelete = QWidget()
		addDelLay = QHBoxLayout()
		addDelLay.setMargin(0)
		addInstructButton = QPushButton("Add Keyword")
		delInstructButton = QPushButton("Delete Keyword")
		addDelLay.addWidget(addInstructButton)
		addDelLay.addWidget(delInstructButton)

		addDelete.setLayout(addDelLay)

		self.keywordLayout.addWidget(addDelete)
		self.keywordsBox.setLayout(self.keywordLayout)

		addInstructButton.clicked.connect(self.addKeyword)
		delInstructButton.clicked.connect(self.delKeyword)


	def createReference(self):
		self.referenceBox = QGroupBox("Reference")
		self.referenceLayout = QVBoxLayout()

		addDelete = QWidget()
		addDelLay = QHBoxLayout()
		addDelLay.setMargin(0)
		addInstructButton = QPushButton("Add Reference")
		delInstructButton = QPushButton("Delete Reference")
		addDelLay.addWidget(addInstructButton)
		addDelLay.addWidget(delInstructButton)

		addDelete.setLayout(addDelLay)

		self.referenceLayout.addWidget(addDelete)
		self.referenceBox.setLayout(self.referenceLayout)

		addInstructButton.clicked.connect(self.addReference)
		delInstructButton.clicked.connect(self.delReference)


	def addIngr(self):
		ingr = Ingredient()
		self.ingrList.append(ingr)
		self.ingrLayout.addWidget(ingr)
		self.ingrBox.setMinimumHeight(self.ingrBox.height() + 35)
		self.ingrBox.setMaximumHeight(self.ingrBox.height() + 35)
		self.innerWidget.setMinimumHeight(self.innerWidget.height() + 35)
		self.innerWidget.setMaximumHeight(self.innerWidget.height() + 35)

	def delIngr(self):
		if len(self.ingrList) > 0:
			button = self.ingrList.pop()
			button.hide()
			self.ingrLayout.removeWidget(button)

			self.ingrBox.setMinimumHeight(self.ingrBox.height() - 35)
			self.ingrBox.setMaximumHeight(self.ingrBox.height() - 35)
			self.innerWidget.setMinimumHeight(self.innerWidget.height() - 35)
			self.innerWidget.setMaximumHeight(self.innerWidget.height() - 35)

	def addInstruct(self):
		instruct = QTextEdit()
		instruct.setMinimumHeight(100)
		instruct.setMaximumHeight(100)

		self.instrList.append(instruct)
		self.instructLayout.addWidget(instruct)
		self.instructBox.setMinimumHeight(self.instructBox.height() + 105)
		self.instructBox.setMaximumHeight(self.instructBox.height() + 105)
		self.innerWidget.setMinimumHeight(self.innerWidget.height() + 105)
		self.innerWidget.setMaximumHeight(self.innerWidget.height() + 105)

	def delInstruct(self):
		if len(self.instrList) > 0:
			button = self.instrList.pop()
			button.hide()
			self.instructLayout.removeWidget(button)

			self.instructBox.setMinimumHeight(self.instructBox.height() - 105)
			self.instructBox.setMaximumHeight(self.instructBox.height() - 105)
			self.innerWidget.setMinimumHeight(self.innerWidget.height() - 105)
			self.innerWidget.setMaximumHeight(self.innerWidget.height() - 105)

	def addComment(self):
		comment = QTextEdit()
		comment.setMinimumHeight(100)
		comment.setMaximumHeight(100)

		self.commList.append(comment)
		self.commentLayout.addWidget(comment)
		self.commentBox.setMinimumHeight(self.commentBox.height() + 105)
		self.commentBox.setMaximumHeight(self.commentBox.height() + 105)
		self.innerWidget.setMinimumHeight(self.innerWidget.height() + 105)
		self.innerWidget.setMaximumHeight(self.innerWidget.height() + 105)

	def delComment(self):
		if len(self.commList) > 0:
			button = self.commList.pop()
			button.hide()
			self.commentLayout.removeWidget(button)

			self.commentBox.setMinimumHeight(self.commentBox.height() - 105)
			self.commentBox.setMaximumHeight(self.commentBox.height() - 105)
			self.innerWidget.setMinimumHeight(self.innerWidget.height() - 105)
			self.innerWidget.setMaximumHeight(self.innerWidget.height() - 105)

	def addKeyword(self):
		keyword = QLineEdit()
		self.keyList.append(keyword)
		self.keywordLayout.addWidget(keyword)
		self.keywordsBox.setMinimumHeight(self.keywordsBox.height() + 26)
		self.keywordsBox.setMaximumHeight(self.keywordsBox.height() + 26)
		self.innerWidget.setMinimumHeight(self.innerWidget.height() + 26)
		self.innerWidget.setMaximumHeight(self.innerWidget.height() + 26)

	def delKeyword(self):
		if len(self.keyList) > 0:
			button = self.keyList.pop()
			button.hide()
			self.keywordLayout.removeWidget(button)

			self.keywordsBox.setMinimumHeight(self.keywordsBox.height() - 26)
			self.keywordsBox.setMaximumHeight(self.keywordsBox.height() - 26)
			self.innerWidget.setMinimumHeight(self.innerWidget.height() - 26)
			self.innerWidget.setMaximumHeight(self.innerWidget.height() - 26)

	def addReference(self):
		reference = QLineEdit()
		self.refList.append(reference)
		self.referenceLayout.addWidget(reference)
		self.referenceBox.setMinimumHeight(self.referenceBox.height() + 26)
		self.referenceBox.setMaximumHeight(self.referenceBox.height() + 26)
		self.innerWidget.setMinimumHeight(self.innerWidget.height() + 26)
		self.innerWidget.setMaximumHeight(self.innerWidget.height() + 26)

	def delReference(self):
		if len(self.refList) > 0:
			button = self.refList.pop()
			button.hide()
			self.referenceLayout.removeWidget(button)

			self.referenceBox.setMinimumHeight(self.referenceBox.height() - 26)
			self.referenceBox.setMaximumHeight(self.referenceBox.height() - 26)
			self.innerWidget.setMinimumHeight(self.innerWidget.height() - 26)
			self.innerWidget.setMaximumHeight(self.innerWidget.height() - 26)

	def resizeEvent(self,e):
		self.innerWidget.setMinimumWidth(self.width()-45)
		self.innerWidget.setMaximumWidth(self.width()-45)