from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Ingredient(QWidget):
	def __init__(self):
		super(Ingredient,self).__init__()

		ingrLabel = QLabel("Item:")
		self.ingr = QLineEdit()

		keywordLabel = QLabel("Keyword")
		self.keyword = QLineEdit()

		intQauntLabel = QLabel("Amount: ")
		self.intQuant = QSpinBox()
		self.intQuant.setRange(0,100)

		numeratorLabel = QLabel("Numerator")
		self.fractQuantNum = QSpinBox()
		self.fractQuantNum.setRange(0,8)

		denomenator = QLabel("Denomenator")
		self.fractQuantDen = QSpinBox()
		self.fractQuantDen.setRange(0,8)

		unitsLabel = QLabel("Units:")
		self.unit = QComboBox()
		self.unit.addItem("tsp")
		self.unit.addItem("Tbsp")
		self.unit.addItem("oz")
		self.unit.addItem("cup")
		self.unit.addItem("pt")
		self.unit.addItem("qt")
		self.unit.addItem("gal")
		self.unit.addItem("lb")
		self.unit.addItem("Dash")
		self.unit.addItem("Pinch")

		layout = QHBoxLayout()

		layout.addWidget(ingrLabel)
		layout.addWidget(self.ingr)
		layout.addWidget(intQauntLabel)
		layout.addWidget(self.intQuant)
		layout.addWidget(numeratorLabel)
		layout.addWidget(self.fractQuantNum)
		layout.addWidget(denomenator)
		layout.addWidget(self.fractQuantDen)
		layout.addWidget(unitsLabel)
		layout.addWidget(self.unit)
		layout.addWidget(keywordLabel)
		layout.addWidget(self.keyword)

		self.setLayout(layout)