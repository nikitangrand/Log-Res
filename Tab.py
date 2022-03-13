from PyQt5 import QtCore, QtGui, QtWidgets
from Tab_Button import Ui_TTTWidget

class Tab (QtWidgets.QWidget, Ui_TTTWidget):
    clicked = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        super(Tab, self).__init__(parent= parent)
        self.setupUi(self)
    def setActive(self, act):
        if act == 0:    
            self.TTTWidget_2.setStyleSheet("QWidget {\n"
"        background-color:rgba(0, 0, 0, 0);\n"
"        color:rgb(144,144,144);\n"
"        padding:2px;\n"
"}QWidget:hover {\n"
"        background-color:rgb(25, 25, 25);\n"
"        border-top-left-radius:5px;\n"
"        border-top-right-radius:5px;\n"
"}")    
        else: 
             self.TTTWidget_2.setStyleSheet("QWidget {\n"
"        background-color: qlineargradient(spread:pad, x1:0.0397727, y1:0.511, x2:0.705682, y2:0.495, stop:0 rgba(160, 0, 218, 255), stop:1 rgba(57, 188, 255, 255));\n"
"        color:rgb(170,170,170);\n"
"        border-top-left-radius:5px;\n"
"        border-top-right-radius:5px;\n"
"        padding:2px;\n"
"}")
    def setid (self, bId):
        self.TTTPushButton.setObjectName(str(bId))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(int(self.TTTPushButton.objectName()))
        
import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Tab(Form)
Form.show
sys.exit(app.exec_())