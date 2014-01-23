from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import MySQLdb as mdb



try:
	con = mdb.connect(host='127.0.0.1', user='admin', passwd='123adrian', db='myrecipes')

	cursor = con.cursor()

	cursor.execute("SELECT image FROM Recipes LIMIT 1")

	fout = open('testimage.jpg', 'wb')
	fout.write(cursor.fetchone()[0])
	fout.close()

	cursor.close()
	con.close()
except IOError, e:

	print "ERROR"
	sys.exit(1)