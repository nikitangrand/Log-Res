# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tab_Button.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TTTWidget(object):
    def setupUi(self, TTTWidget):
        TTTWidget.setObjectName("TTTWidget")
        TTTWidget.resize(180, 35)
        TTTWidget.setMinimumSize(QtCore.QSize(40, 35))
        TTTWidget.setMaximumSize(QtCore.QSize(180, 35))
        self.horizontalLayout = QtWidgets.QHBoxLayout(TTTWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TTTWidget_2 = QtWidgets.QWidget(TTTWidget)
        self.TTTWidget_2.setMinimumSize(QtCore.QSize(40, 35))
        self.TTTWidget_2.setMaximumSize(QtCore.QSize(180, 35))
        self.TTTWidget_2.setStyleSheet("QWidget {\n"
"        background-color: qlineargradient(spread:pad, x1:0.0397727, y1:0.511, x2:0.705682, y2:0.495, stop:0 rgba(160, 0, 218, 255), stop:1 rgba(57, 188, 255, 255));\n"
"        color:rgb(170,170,170);\n"
"        border-top-left-radius:5px;\n"
"        border-top-right-radius:5px;\n"
"        padding:2px;\n"
"}")
        self.TTTWidget_2.setObjectName("TTTWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TTTWidget_2)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TTTLabel = QtWidgets.QLabel(self.TTTWidget_2)
        self.TTTLabel.setMinimumSize(QtCore.QSize(10, 25))
        self.TTTLabel.setMaximumSize(QtCore.QSize(150, 25))
        self.TTTLabel.setAutoFillBackground(False)
        self.TTTLabel.setStyleSheet("QLabel {\n"
"\n"
"}\n"
"")
        self.TTTLabel.setObjectName("TTTLabel")
        self.horizontalLayout_2.addWidget(self.TTTLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TTTPushButton = QtWidgets.QPushButton(self.TTTWidget_2)
        self.TTTPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.TTTPushButton.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.TTTPushButton.setFont(font)
        self.TTTPushButton.setStyleSheet("QPushButton {\n"
"        background-color:rgba(0,0,0,0);\n"
"        color:rgb(144,144,144);\n"
"}\n"
"QPushButton:hover {\n"
"        color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"        padding-top:5px;\n"
"        padding-left:5px;\n"
"}")
        self.TTTPushButton.setObjectName("-1")
        self.horizontalLayout_2.addWidget(self.TTTPushButton)
        self.horizontalLayout.addWidget(self.TTTWidget_2)

        self.retranslateUi(TTTWidget)
        QtCore.QMetaObject.connectSlotsByName(TTTWidget)

    def retranslateUi(self, TTTWidget):
        _translate = QtCore.QCoreApplication.translate
        TTTWidget.setWindowTitle(_translate("TTTWidget", "Form"))
        self.TTTLabel.setText(_translate("TTTWidget", "New Tab"))
        self.TTTPushButton.setText(_translate("TTTWidget", "x"))
