

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, img

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 832)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 50, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 20, 280, 430))
        self.label.setStyleSheet("background-image: url(:/img/dlyafotoshopa1.jpg);\n"
"border-top-left-radius: 50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 280, 430))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(30, 80, 241, 131))
        self.widget_2.setStyleSheet("background-color: rgb(0,0,0,75);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(250,250,250,210);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 240, 430))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 90, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton, #pushButton_2,#pushButton_3{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.0454545, x2:0.9375, y2:0.813, stop:0 rgba(220, 2, 227, 255), stop:1 rgba(249, 158, 255, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover, #pushButton_2:hover,#pushButton_3:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"}\n"
"QPushButton#pushButton:pressed, #pushButton_2:pressed,#pushButton_3:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(320, 30, 220, 391))
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 95, 85, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(15, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.0454545, x2:0.9375, y2:0.813, stop:0 rgba(220, 2, 227, 255), stop:1 rgba(249, 158, 255, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit.setGeometry(QtCore.QRect(15, 95, 85, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(15, 240, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(15, 195, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(325, 20, 220, 315))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 255, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton, #pushButton_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.0454545, x2:0.9375, y2:0.813, stop:0 rgba(220, 2, 227, 255), stop:1 rgba(249, 158, 255, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover, #pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"}\n"
"QPushButton#pushButton:pressed, #pushButton_2:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.647727, y2:0.415, stop:0 rgba(24, 35, 186, 255), stop:1 rgba(14, 170, 147, 255));\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 175, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgb(46, 82, 101, 200);\n"
"padding-bottom: 7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(55, 40, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0, 200);")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Tim-C0DE"))
        self.pushButton_3.setText(_translate("Form", ">"))
        self.label_4.setText(_translate("Form", "Register"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Last Name"))
        self.pushButton.setText(_translate("Form", "R e g i s t e r"))
        self.lineEdit.setPlaceholderText(_translate("Form", "First Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Email Address"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Confrim Password"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "User Name"))
        self.pushButton_2.setText(_translate("Form", "L o g I n"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Password"))
        self.label_6.setText(_translate("Form", "Log In"))

