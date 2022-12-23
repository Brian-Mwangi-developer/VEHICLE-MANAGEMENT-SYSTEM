from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit,QApplication
import sys
from DatabaseOperation import DBOperation
from HomeWindow import HomeScreen


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.resize(250, 100)
        layout = QVBoxLayout()

        label_username = QLabel("username : ")
        self.input_username = QLineEdit()
        label_password = QLabel("password: ")
        self.error_msg = QLabel()
        self.error_msg.setStyleSheet("color:red")
        self.input_password = QLineEdit()

        btn_login = QPushButton("Login")
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.clicked.connect(self.showHome)
        self.setLayout(layout)

    def showLoginScreen(self):
        self.show()

    def showHome(self):
        if self.input_username.text()=="":
            self.error_msg.setText("Please Enter Username")
            return
        if self.input_password.text()=="":
            self.error_msg.setText("Please Enter Password")
            return
        dboperation = DBOperation()
        result = dboperation.doAdminLogin(self.input_username.text(), self.input_password.text())
        if result:
            self.error_msg.setText("Login Successful")
            self.close()
            self.home = HomeScreen()
            self.home.show()
        else:
            self.error_msg.setText("Invalid Login Details")


