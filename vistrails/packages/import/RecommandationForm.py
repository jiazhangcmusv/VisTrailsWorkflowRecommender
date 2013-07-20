'''
Created on Dec 5, 2012

@author: xiaoxiao
'''
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTextEdit


class ComponentSearchForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
#        self.createEventMap()
        self.setWindowTitle('API Recommendation')

        self.lableTitle = QtGui.QLabel('', self)
        self.lableTitle.setFixedWidth(500)
        self.lableTitle.move(20, 20)
        self.lableTitle.setText("People used this API also used:")

        self.apiLabel1 = QtGui.QLabel('', self)
        self.apiLabel1.setFixedWidth(200)
        self.apiLabel1.move(20, 70)
        self.apiLabel1.setText("google-base")

        self.apiLabel2 = QtGui.QLabel('', self)
        self.apiLabel2.setFixedWidth(200)
        self.apiLabel2.move(20, 120)
        self.apiLabel2.setText("google-chart")


        self.btn1 = QtGui.QPushButton("Import this", self)
        self.btn1.move(100, 70)
        
        self.btn2 = QtGui.QPushButton("Import this", self)
        self.btn2.move(100, 120)
        
