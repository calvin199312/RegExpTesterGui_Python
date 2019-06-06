# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jun  6 07:41:52 2019
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 249)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regex_label_ = QtGui.QLabel(self.centralWidget)
        self.regex_label_.setObjectName("regex_label_")
        self.horizontalLayout.addWidget(self.regex_label_)
        self.regex_line_edit_ = QtGui.QLineEdit(self.centralWidget)
        self.regex_line_edit_.setObjectName("regex_line_edit_")
        self.horizontalLayout.addWidget(self.regex_line_edit_)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_text_label_ = QtGui.QLabel(self.centralWidget)
        self.check_text_label_.setObjectName("check_text_label_")
        self.horizontalLayout_2.addWidget(self.check_text_label_)
        self.check_text_line_edit_ = QtGui.QLineEdit(self.centralWidget)
        self.check_text_line_edit_.setObjectName("check_text_line_edit_")
        self.horizontalLayout_2.addWidget(self.check_text_line_edit_)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_button_ = QtGui.QPushButton(self.centralWidget)
        self.run_button_.setObjectName("run_button_")
        self.horizontalLayout_3.addWidget(self.run_button_)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.result_text_browser_ = QtGui.QTextBrowser(self.centralWidget)
        self.result_text_browser_.setObjectName("result_text_browser_")
        self.verticalLayout.addWidget(self.result_text_browser_)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.regex_label_.setText(QtGui.QApplication.translate("MainWindow", "Enter RegExp :     ", None, QtGui.QApplication.UnicodeUTF8))
        self.regex_line_edit_.setText(QtGui.QApplication.translate("MainWindow", "ipar\\(([^)]+)\\)", None, QtGui.QApplication.UnicodeUTF8))
        self.check_text_label_.setText(QtGui.QApplication.translate("MainWindow", "Enter CheckText :", None, QtGui.QApplication.UnicodeUTF8))
        self.check_text_line_edit_.setText(QtGui.QApplication.translate("MainWindow", "ipar(jacky) ipar(donna) ipar(kelso)", None, QtGui.QApplication.UnicodeUTF8))
        self.run_button_.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))

