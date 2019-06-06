#!/usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow

class RegExpTestGui(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.run_button_.clicked.connect(self.loadRegExp)

	def loadRegExp(self):
		self.ui.result_text_browser_.setText("Yeah\nClicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = RegExpTestGui()
	gui.show()
	sys.exit(app.exec_())	
