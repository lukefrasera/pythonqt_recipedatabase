from PyQt4.QtGui import *
from PyQt4.QtCore import *
from dListClass import DList
import MySQLdb as mdb
import sys

class addWidget(QWidget):
	def __init__(self):
		super(addWidget,self).__init__()

		self.createTopLeftCorner()
		self.createTopRightCorner()
		# self.createBottomLeftCorner()
		self.createBottonRightCorner()


		mainlayout = QGridLayout()
		mainlayout.addWidget(self.TopLeft,0,0)
		mainlayout.addWidget(self.TopRight,0,1)
		# mainlayout.addWidget(self.BottomLeft)
		mainlayout.addWidget(self.BottomRight,1,1)

		mainlayout.setColumnStretch(0,15)
		mainlayout.setColumnStretch(1,40)
		mainlayout.setRowStretch(0,15)
		mainlayout.setRowStretch(1,70)

		self.setLayout(mainlayout)

		self.BottomRight.commitButton.clicked.connect(self.saveCommit)

	def createTopLeftCorner(self):
		self.TopLeft = QGroupBox("Image")
		layout = QVBoxLayout()
		self.filebutton = QPushButton("Choose File")
		self.scene = QGraphicsScene()
		self.view = QGraphicsView(self.scene)

		layout.addWidget(self.view)
		layout.addWidget(self.filebutton)
		self.TopLeft.setLayout(layout)

		self.filebutton.clicked.connect(self.openFile)

	def openFile(self):
		self.filename = QFileDialog.getOpenFileName(self, 'Open file', 'c:/')

		self.image = QPixmap(self.filename)
		self.item = QGraphicsPixmapItem(self.image.scaledToHeight(150))
		self.scene.addItem(self.item)
		self.view.show()

	def setPass(self, username, password):
		self.username = username
		self.password = password

	def saveCommit(self):
		# create connection
			con = mdb.connect(host = '127.0.0.1',
				user = self.username,
				passwd = self.password,
				db = 'myrecipes')

			with con:

			# insert Recipe

				# insert Title

				cur = con.cursor()
				# insert Image

				f = open(self.filename, 'rb')
				img = f.read()


				cur.execute("INSERT INTO Recipes(title, image, preptime, cooktime, serving, difficulty, description, rating)\
								VALUES('{title}', '{image}', '{preptime}', '{cooktime}', '{serving}', '{difficulty}', '{description}', '{rating}')".format(
							title = self.title.text(),
							image = mdb.escape_string(img),
							preptime = (self.prepTimeHour.value()*60 + self.prepTimeMin.value()),
							cooktime = (self.cookTimeHour.value()*60 + self.cookTimeMin.value()),
							serving = self.servingSize.value(),
							difficulty = self.dRating.value(),
							description = mdb.escape_string(str(self.description.toPlainText().toAscii())),
							rating = self.oRating.value()))
				recipeId = con.insert_id()

			# insert Ingredients
				for ingr in self.BottomRight.ingrList:

					cur.execute("INSERT INTO ingredients(recipe_id, wholeNum, fractNumNum, fractNumDen, unit, item, keyword)\
						VALUES('{recipe_ida}', '{wholeNum}', '{fractNumNum}', '{fractNumDen}', '{unit}', '{item}', '{keyword}')".format(
							recipe_ida = recipeId,
							wholeNum = ingr.intQuant.value(),
							fractNumNum = ingr.fractQuantNum.value(),
							fractNumDen = ingr.fractQuantDen.value(),
							unit = str(ingr.unit.currentText().toAscii()),
							item = str(ingr.ingr.text()),
							keyword = ingr.keyword.text()))

			# insert Instruction
				for instr in self.BottomRight.instrList:
					cur.execute("INSERT INTO instructions(recipe_id, order, instruct)\
						VALUES('{recipe_ida}','{order}', '{instruct}')".format(
							recipe_ida = recipeId,
							order = 1,
							instruct = mdb.escape_string(str(instr.toPlainText().toAscii()))))

				# insert Instruction number

			# insert comments
				for com in self.BottomRight.commList:
					cur.execute("INSERT INTO comments(recipe_id, comment)\
						VALUES('{recipe_ida}', '{comment}')".format(
							recipe_ida = recipeId,
							comment = mdb.escape_string(str(com.toPlainText().toAscii()))))
				# insert comment

			# insert recipe keyword
				for key in self.BottomRight.keyList:
					cur.execute("INSERT INTO keywordRecipe(recipe_id, keyword)\
						VALUES('{recipe_id}', '{keyword}')".format(
							recipe_id = recipeId,
							keyword = str(key.text())))

				# insert keyword

				con.commit()
				cur.close()

			self.emit(SIGNAL("addComplete()"))

	def createTopRightCorner(self):
		self.TopRight = QGroupBox("Description")
		layout = QGridLayout()
		layout2 = QHBoxLayout()
		TitleBar = QWidget()

		self.title = QLineEdit("Title")
		self.titleLabel = QLabel("Title")
		self.createBasicDescription()

		layout2.addWidget(self.titleLabel)
		layout2.addWidget(self.title)
		TitleBar.setLayout(layout2)

		layout.addWidget(TitleBar,0,0)
		layout.addWidget(self.basicDescript,1,0)

		layout.setRowStretch(0,5)
		layout.setRowStretch(1,30)

		self.TopRight.setLayout(layout)

	def createBasicDescription(self):
		self.basicDescript = QWidget()
		layout = QHBoxLayout()

		self.description = QTextEdit("Description")
		self.createSummaryBox()

		layout.addWidget(self.description)
		layout.addWidget(self.summary)
		
		self.basicDescript.setLayout(layout)

	def createSummaryBox(self):
		self.summary = QWidget()
		layout = QGridLayout()

		#  Create Rating Box
		oRatingBox = QWidget()
		oRatingBoxLayout = QGridLayout()

		oRatingLabel = QLabel("Overall Rating: ")
		self.oRating = QSpinBox()
		self.oRating.setRange(0,5)

		dRatingLabel = QLabel("Difficulty Rating: ")
		self.dRating = QSpinBox()
		self.dRating.setRange(0,5)

		oRatingBoxLayout.addWidget(oRatingLabel,0,0)
		oRatingBoxLayout.addWidget(self.oRating,0,1)
		oRatingBoxLayout.addWidget(dRatingLabel,1,0)
		oRatingBoxLayout.addWidget(self.dRating,1,1)

		oRatingBox.setLayout(oRatingBoxLayout)

		#  create Prep Time and Cook Time SpinBoxs
		timeBox = QWidget()
		timeBoxLayout = QHBoxLayout()

		self.prepTimeHour = QSpinBox()
		self.prepTimeMin  = QSpinBox()
		prepTimeLabel = QLabel("Prep Time: ")
		self.cookTimeHour = QSpinBox()
		self.cookTimeMin  = QSpinBox()
		cookTimeLabel = QLabel("Cook Time: ")

		self.prepTimeHour.setRange(0,100)
		self.prepTimeMin.setRange(0,59)
		self.cookTimeHour.setRange(0,100)
		self.cookTimeMin.setRange(0,59)

		timeBoxLayout.addWidget(prepTimeLabel)
		timeBoxLayout.addWidget(self.prepTimeHour)
		timeBoxLayout.addWidget(self.prepTimeMin)
		timeBoxLayout.addWidget(cookTimeLabel)
		timeBoxLayout.addWidget(self.cookTimeHour)
		timeBoxLayout.addWidget(self.cookTimeMin)

		timeBox.setLayout(timeBoxLayout)

		#create Serving Size and Total Time
		totalTimeLabel = QLabel("Total Time: ")
		servingSizeLabel = QLabel("ServingSize: ")
		self.totalTime = QLabel("1234")
		self.servingSize = QSpinBox()
		self.servingSize.setRange(1,30)

		#  add Total Layout

		layout.addWidget(oRatingBox,0,0)
		layout.addWidget(timeBox,1,0)
		layout.addWidget(servingSizeLabel,0,1)
		layout.addWidget(self.servingSize,0,2)
		layout.addWidget(totalTimeLabel,1,1)
		layout.addWidget(self.totalTime,1,2)
		self.summary.setLayout(layout)

	# def createBottomLeftCorner(self):

	def createBottonRightCorner(self):

		self.BottomRight = DList()