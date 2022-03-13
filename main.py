from PyQt5 import QtWidgets, QtCore, QtSql
from App import Ui_Form
import sys, sqlite3, webbrowser

class LoginApp(QtWidgets.QWidget, Ui_Form):
    def changeform(self):
        if self.pushButton_3.isChecked():
            self.widget_3.hide()
            self.widget_4.show()
            self.pushButton_3.setText("<")
            self.label_7.hide()
            self.label_8.show()
        else:
            self.widget_3.show()
            self.widget_4.hide()
            self.pushButton_3.setText(">")
            self.label_7.show()
            self.label_8.hide()
            self.label_9.hide()
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #self.widget_3.show()
        self.widget_4.hide()
        #self.label_7.hide()
        #self.label_8.hide()
        self.label_9.hide()
        self.pushButton_3.clicked.connect(self.changeform)
        self.pushButton_2.clicked.connect(self.loginfunction)
        self.pushButton.clicked.connect(self.signupfunction)

    def loginfunction(self):
        user = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        if len(user)==0 or len(password)==0:
            self.label_7.setText("Please input all fields.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\'' + user + "\'"
            cur.execute(query)
            record = cur.fetchone()
            if record and record[0] == password:
                print("Successfully logged in.")
                self.label_7.setText("")
                webbrowser.open_new('https://vk.com/nikitaytobuer')

            else:
                self.label_7.setText("Invalid username or password")

    def signupfunction(self):
        userr = self.lineEdit.text()
        passwordd = self.lineEdit_6.text()
        confirmpasswordd = self.lineEdit_7.text()

        if len(userr) == 0 or len(passwordd) == 0 or len(confirmpasswordd) == 0:
            self.label_8.setText("Please fill in all inputs.")

        elif passwordd != confirmpasswordd:
            self.label_8.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()

            user_info = [userr, passwordd]
            cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)
            conn.commit()
            conn.close()
            self.label_9.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec())

