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
		#self.ui.result_text_browser_.setText("Yeah\nClicked")
		regexp_pattern = self.ui.regex_line_edit_.text()
		check_text = self.ui.check_text_line_edit_.text()
		if regexp_pattern.isEmpty() :
			self.ui.result_text_browser_.setText("RegExp empty")
		elif check_text.isEmpty() :
			self.ui.result_text_browser_.setText("Check text empty")
		else :
			self.ui.result_text_browser_.setText("Ready to go")
			

if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = RegExpTestGui()
	gui.show()
	sys.exit(app.exec_())	
