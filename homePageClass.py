from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HomeWidget(QWidget):
    def __init__(self):
        super(HomeWidget,self).__init__()

        self.createHorizontalGroupBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.horizonatalGroupBox)
        self.setLayout(mainLayout)

        self.addRecipeButton.clicked.connect(self.emitaddPage)

    def createHorizontalGroupBox(self):
        self.horizonatalGroupBox = QGroupBox("Two Buttons")
        layout = QHBoxLayout()

        self.searchButton = QPushButton("Search")
        self.searchButton.setMinimumWidth(150)
        self.searchButton.setMaximumWidth(150)
        self.searchButton.setMinimumHeight(150)

        spacerMid = QSpacerItem(100,500)
        spacerLeft = QSpacerItem(100,10)
        spacerRight = QSpacerItem(100,10)

        self.addRecipeButton = QPushButton("Add")
        self.addRecipeButton.setMinimumWidth(150)
        self.addRecipeButton.setMaximumWidth(150)
        self.addRecipeButton.setMinimumHeight(150)

        layout.addSpacerItem(spacerLeft)
        layout.addWidget(self.searchButton)
        layout.addSpacerItem(spacerMid)
        layout.addWidget(self.addRecipeButton)
        layout.addSpacerItem(spacerRight)
        self.horizonatalGroupBox.setLayout(layout)

    def emitaddPage(self):
        self.emit(SIGNAL("addSignal()"))