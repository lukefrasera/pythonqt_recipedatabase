from PyQt4 import QtGui 

class recipe:
	def __init__(self):
		self.title = ""
		self.review = []
		self.image = QtGui.QPixmap()
		self.prptm = 0
		self.cktm = 0
		self.yld = 0
		self.diff = 0
		self.items = []
		self.intruct = []
		self.comm = []
		self.link = ""
		self.ref = ""

	def setTitle(self,value):
		self.title = "" + value

	def addReview(self,value,s):
		temprev = rating()
		temprev.setRating(value)
		temprev.setReview(s)

		self.review.append(temprev)

	def removeReview(self,position):
		self.review.pop(position)

	def setImage(self,filename):
		self.image = QtGui.QPixmap(filename)

	def setPrepTime(self, value):
		self.prptm = value

	def setCookTime(self,value):
		self.cktm = value

	def setYield(self,value):
		self.yld = value

	def setDifficulty(self,value):
		self.diff = value

	def addIngredients(self,ingredient):
		self.items.append(ingredient)

	def removeIngredient(self,position):
		self.items.pop(position)

	def addInstruction(self,string):
		self.intruct.append(string)

	def removeInstruction(self,position):
		self.intruct.pop(position)

	def addComment(self,string):
		self.comm.append(string)

	def removeComment(seld,position):
		self.comm.pop(position)

	def setLink(self,string):
		self.link = "" + string

	def setReference(self,string):
		self.ref = "" + string

	class rating:
		def __init__(self):
			self.rat = 0
			self.rev = ""

		def setRating(self,value):
			self.rat = value

		def setReview(self,value):
			self.rev = "" + value


	class igrdnt:
		def __init__(self):
			self.amount = quantity()
			self.measure = 0
			self.sMeasure = [' ','tsp', 'Tbsp', 'Cup', 'pt', 'qt', 'gal', 'lb', 'oz', 'fl-oz']
			self.item = ""
			self.keyword = ""

		def setUnit(self,value):
			self.measure = vlaue

		def setKeyword(self,value):
			self.keyword = "" + value

		def setItem(self,value):
			self.item = "" + value

	class quantity:
		def __init__(self):
			self.i = 0
			self.f = 0
			self.fVal = ['1/2','1/3','2/3','1/4','2/4','3/4','1/8','2/8','3/8','4/8','5/8','6/8','7/8']

		def setFractVal(self, value):
			self.f = value

		def setQuantVal(self, value):
			self.i = value