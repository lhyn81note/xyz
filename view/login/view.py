from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PySide6.QtCore import Qt

class LoginWindow(QDialog):
    def __init__(self, TblUser):
        super().__init__()
        self.TblUser = TblUser
        self.setWindowTitle("静载试验台上位机程序")
        self.setFixedSize(400, 300)

        # Central widget and layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Title label
        title = QLabel("用户登陆")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Username field
        self.usernames = QComboBox()
        users_from_db = self.TblUser.Handler.getAll()
        for user in users_from_db:
            self.usernames.addItem(user.UserName)
        layout.addWidget(self.usernames)

        # Password field
        self.password = QLineEdit()
        self.password.setPlaceholderText("密码")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        # Login button
        self.login_button = QPushButton("登陆")
        layout.addWidget(self.login_button)

        # Apply QSS styling
        self.setStyleSheet("""
            QDialog {
                background-color: #2C2F33;
            }
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
                font-family: Arial;
            }
            QComboBox {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: black;
            }            
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: black;
            }
            QLineEdit:focus {
                border: 1px solid #007BFF;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #003d80;
            }
        """)

        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.usernames.currentText()
        password = self.password.text()
        # select user_id from db where username = username:
        # password_from_db = self.TblUser.Handler.getById(1).LoginPassword
        password_from_db = self.TblUser.Handler.getByAny('UserName', username).LoginPassword
        print(password_from_db)

        try:
            if password == password_from_db:
                print("登陆成功")
                self.accept()
            else:
                print("登陆失败")
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.critical(self, "错误", "密码错误，请重试")
        except Exception as e:
            print(e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
