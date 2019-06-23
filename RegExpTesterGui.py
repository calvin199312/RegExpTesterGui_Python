#!/usr/bin/python

import sys
import re
from PyQt4.QtGui import *
from PyQt4 import QtCore as qt_core
from PyQt4 import QtGui 
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
			message_list = qt_core.QStringList()
			message_list << "<font color=\"red\">Failed</font>"
			message_list << "RegExp field is empty."
			message_list << "Nothing to do."
			self.ui.result_text_browser_.setHtml(message_list.join("<br>"))
		elif check_text.isEmpty() :
			message_list = qt_core.QStringList()
			message_list << "<font color=\"red\">Failed</font>"
			message_list << "CheckText field is empty."
			message_list << "Nothing to do."
			self.ui.result_text_browser_.setHtml(message_list.join("<br>"))
		else :
			self.ui.result_text_browser_.setText("Ready to go")
			regexp = re.compile(str(regexp_pattern))
			full_matches = qt_core.QStringList()
			captures = qt_core.QStringList()
			pos = 0
			while True :
				match = regexp.match(check_text, pos)
				if match is None :
					break
				pos = match.end(0) + 1
				full_matches << match.group(0)
				for capture in match.groups(0) :
					captures << capture

			if full_matches.count() == 0 :
				message_list = qt_core.QStringList()
				message_list << "<font color=\"red\">Failed</font>"
				message_list << "RegExp does not match CheckText"
				self.ui.result_text_browser_.setHtml(message_list.join("<br>"))
			else :
				message_list = qt_core.QStringList()
				message_list << "<font color=\"green\">Success</font>"
				message_list << "RegExp matches CheckText"

				if full_matches.count() is 1 :
					message_list << qt_core.QString("There is 1 full text match")
				else :
					message_list << qt_core.QString("There are %1 full text matches").arg(full_matches.count())
				
				message_list << "\"" + full_matches.join("\"<br>\"") + "\"<br>"
				

				if full_matches.count() is 0 :
					message_list << qt_core.QString("There are no captures")
				elif full_matches.count() is 1 :
					message_list << qt_core.QString("There is 1 capture")
				else :
					message_list << qt_core.QString("There are %1 captures").arg(captures.count())
				
				message_list << "\"" + captures.join("\"<br>\"") + "\"<br>"

				self.ui.result_text_browser_.setHtml(message_list.join("<br>"))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = RegExpTestGui()
	gui.show()
	sys.exit(app.exec_())	
