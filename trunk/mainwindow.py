#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from mainwindowui import Ui_MainWindow

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main(args):
    app = QtGui.QApplication(args)
    mainWindow = MyWindow()
    mainWindow.show()
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'), app, QtCore.SLOT('quit()'))
    app.exec_()

if __name__ == '__main__':
    main(sys.argv)

