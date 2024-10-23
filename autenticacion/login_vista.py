from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

class LoginForm(QWidget):
    login_signal = pyqtSignal(str, str)  # Señal para enviar usuario y contraseña

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistema de Inventario')
        self.setFixedSize(1366, 768)

        # Establecer imagen de fondo
        background = QLabel(self)
        background.setPixmap(QPixmap("imagenes/background/Background.jpg"))
        background.setScaledContents(True)
        background.setGeometry(0, 0, 1366, 768)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(200, 150, 200, 150)

        frame = QFrame(self)
        frame.setStyleSheet("background-color: rgba(255, 255, 255, 200); border-radius: 10px;")
        frame_layout = QVBoxLayout(frame)

        # Icono del logo
        logo_label = QLabel(frame)
        logo_pixmap = QPixmap("imagenes/logines/Usuario2.png")
        logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame_layout.addWidget(logo_label)

        title_label = QLabel("Iniciar sesión", frame)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Times New Roman", 24, QFont.Weight.Bold))
        frame_layout.addWidget(title_label)

        # Entrada de nombre de usuario
        username_layout = QHBoxLayout()
        username_icon = QLabel()
        username_icon.setPixmap(QPixmap("imagenes/logines/Usuario1.png").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        username_input = QLineEdit()
        username_input.setPlaceholderText("Usuario")
        username_input.setFont(QFont("Times New Roman", 16))
        username_layout.addWidget(username_icon)
        username_layout.addWidget(username_input)
        frame_layout.addLayout(username_layout)

        # Entrada de contraseña
        password_layout = QHBoxLayout()
        password_icon = QLabel()
        password_icon.setPixmap(QPixmap("imagenes/logines/pwd.png").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        password_input = QLineEdit()
        password_input.setPlaceholderText("Contraseña")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setFont(QFont("Times New Roman", 16))
        password_layout.addWidget(password_icon)
        password_layout.addWidget(password_input)
        frame_layout.addLayout(password_layout)

        # Botón de Ingresar
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
        login_button.clicked.connect(self.on_login)
        frame_layout.addWidget(login_button)

        create_account_label = QLabel("<a href='#'>Crear una cuenta</a>")
        create_account_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        create_account_label.setFont(QFont("Times New Roman", 12))
        create_account_label.setOpenExternalLinks(False)
        create_account_label.linkActivated.connect(self.create_account)
        frame_layout.addWidget(create_account_label)

        main_layout.addWidget(frame)
        self.setLayout(main_layout)

        self.username_input = username_input
        self.password_input = password_input

    def on_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.login_signal.emit(username, password)

    def create_account(self):
        print("Crear cuenta clickeado")
