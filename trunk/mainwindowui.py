# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowui.ui'
#
# Created: Sun Aug 24 22:01:20 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,825,628).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.filterWidget = QtGui.QWidget(self.centralwidget)
        self.filterWidget.setMinimumSize(QtCore.QSize(0,24))
        self.filterWidget.setObjectName("filterWidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.filterWidget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.modalNameComboBox = QtGui.QComboBox(self.filterWidget)
        self.modalNameComboBox.setMaximumSize(QtCore.QSize(100,16777215))
        self.modalNameComboBox.setEditable(True)
        self.modalNameComboBox.setFrame(True)
        self.modalNameComboBox.setObjectName("modalNameComboBox")
        self.hboxlayout.addWidget(self.modalNameComboBox)

        self.timeComboBox = QtGui.QComboBox(self.filterWidget)
        self.timeComboBox.setMaximumSize(QtCore.QSize(100,16777215))
        self.timeComboBox.setEditable(True)
        self.timeComboBox.setFrame(True)
        self.timeComboBox.setObjectName("timeComboBox")
        self.hboxlayout.addWidget(self.timeComboBox)

        self.levelComboBox = QtGui.QComboBox(self.filterWidget)
        self.levelComboBox.setMaximumSize(QtCore.QSize(100,16777215))
        self.levelComboBox.setEditable(True)
        self.levelComboBox.setFrame(True)
        self.levelComboBox.setObjectName("levelComboBox")
        self.hboxlayout.addWidget(self.levelComboBox)

        self.contentComboBox = QtGui.QComboBox(self.filterWidget)
        self.contentComboBox.setEditable(True)
        self.contentComboBox.setFrame(True)
        self.contentComboBox.setObjectName("contentComboBox")
        self.hboxlayout.addWidget(self.contentComboBox)
        self.vboxlayout.addWidget(self.filterWidget)

        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.vboxlayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0,0,825,30))
        self.menuBar.setObjectName("menuBar")

        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)

        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "打开", None, QtGui.QApplication.UnicodeUTF8))

