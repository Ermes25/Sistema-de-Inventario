import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QFrame)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistema de Inventario')
        self.setFixedSize(1366, 768)

        # Establecer imagen de fondo
        background = QLabel(self)
        background.setPixmap(QPixmap("C:/Users/ermes/OneDrive/Documentos/programacion/Inventario_sistema/imagenes/Background.jpg"))
        background.setScaledContents(True)
        background.setGeometry(0, 0, 1366, 768)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(200, 150, 200, 150)

        frame = QFrame(self)
        frame.setStyleSheet("background-color: rgba(255, 255, 255, 200); border-radius: 10px;")
        frame_layout = QVBoxLayout(frame)

        # Icono encima de los campos de ingreso
        logo_label = QLabel(frame)
        logo_pixmap = QPixmap("C:/Users/ermes/OneDrive/Documentos/programacion/Inventario_sistema/imagenes/Usuario2.png")
        logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame_layout.addWidget(logo_label)

        title_label = QLabel("Iniciar sesión", frame)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Times New Roman", 24, QFont.Weight.Bold))
        frame_layout.addWidget(title_label)
        title_label.setStyleSheet("color: black;")
        # Entrada de nombre de usuario con icono
        username_layout = QHBoxLayout()
        username_icon = QLabel()
        username_icon.setPixmap(QPixmap("imagenes/Usuario1.png").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        username_input = QLineEdit()
        username_input.setPlaceholderText("Usuario")
        username_input.setFont(QFont("Times New Roman", 16))
        username_input.setStyleSheet("color: black; background-color: rgba(255, 255, 255, 150); border: 1px solid gray; border-radius: 5px; padding: 5px;")
        username_layout.addWidget(username_icon)
        username_layout.addWidget(username_input)
        frame_layout.addLayout(username_layout)

        # Entrada de contraseña con icono
        password_layout = QHBoxLayout()
        password_icon = QLabel()
        password_icon.setPixmap(QPixmap("imagenes/pwd.png").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        password_input = QLineEdit()
        password_input.setPlaceholderText("Contraseña")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setFont(QFont("Times New Roman", 16))
        password_input.setStyleSheet("color: black; background-color: rgba(255, 255, 255, 150); border: 1px solid gray; border-radius: 5px; padding: 5px;")
        password_layout.addWidget(password_icon)
        password_layout.addWidget(password_input)
        frame_layout.addLayout(password_layout)

        login_button = QPushButton("Ingresar")
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #fb7d51;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Times New Roman';
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #FFC700;
            }
        """)
        frame_layout.addWidget(login_button)

        create_account_label = QLabel("<a href='#'>Crear una cuenta</a>")
        create_account_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        create_account_label.setFont(QFont("Times New Roman", 12))
        create_account_label.setOpenExternalLinks(False)
        create_account_label.linkActivated.connect(self.create_account)
        frame_layout.addWidget(create_account_label)

        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def create_account(self):
        print("Create account link clicked")

def Component():
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())

Component()