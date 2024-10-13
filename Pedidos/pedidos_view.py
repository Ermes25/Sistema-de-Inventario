import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QLineEdit, QTextEdit, QDialog)
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor, QBrush
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base de Datos")
        self.setGeometry(100, 100, 1024, 768)  # Tamaño apropiado para laptop

        # Configurar el fondo de la ventana principal con una imagen
        palette = self.palette()
        background_image = QPixmap("imagenes/fondo.jpg")  # Asegúrate de tener esta imagen
        scaled_image = background_image.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_image))
        self.setPalette(palette)

        # Widget central y layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Frame con fondo y borde más visible
        frame = QWidget(self)
        frame.setStyleSheet("""
            background-color: #f69f34; 
            border-radius: 10px;
            border: 3px solid black;
        """)
        frame_layout = QVBoxLayout(frame)

        # Botones CRUD con nuevo estilo
        crud_layout = QHBoxLayout()
        crud_buttons = [
            ("Crear", self.create, "imagenes/Crear.png"),
            ("Leer", self.read, "imagenes/mostrar.png"),
            ("Actualizar", self.update, "imagenes/refrescar.png"),
            ("Eliminar", self.delete, "imagenes/eliminar.png"),
            ("Buscar", self.search, "imagenes/buscar.png"),
        ]

        button_style = """
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """

        for text, slot, icon_path in crud_buttons:
            button = QPushButton(text)
            button.setIcon(QIcon(icon_path))
            button.clicked.connect(slot)
            button.setStyleSheet(button_style)
            crud_layout.addWidget(button)

        frame_layout.addLayout(crud_layout)

        # Botón de menú con el mismo estilo
        menu_button = QPushButton("Menú")
        menu_button.setIcon(QIcon("imagenes/menu.png"))
        menu_button.clicked.connect(self.show_menu)
        menu_button.setStyleSheet(button_style)
        frame_layout.addWidget(menu_button)

        layout.addWidget(frame)

    def create(self):
        dialog = CRUDDialog(self, "Crear")
        dialog.exec()

    def read(self):
        dialog = CRUDDialog(self, "Leer")
        dialog.exec()

    def update(self):
        dialog = CRUDDialog(self, "Actualizar")
        dialog.exec()

    def delete(self):
        dialog = CRUDDialog(self, "Eliminar")
        dialog.exec()

    def search(self):
        dialog = CRUDDialog(self, "Buscar")
        dialog.exec()

    def show_menu(self):
        print("Volviendo al menú principal")

class CRUDDialog(QDialog):
    def __init__(self, parent=None, operation=""):
        super().__init__(parent)
        self.setWindowTitle(f"{operation} Registro")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout(self)

        # Campos de ejemplo (ajusta según tus necesidades)
        self.id_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.description_input = QTextEdit(self)

        layout.addWidget(QLabel("ID:"))
        layout.addWidget(self.id_input)
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Descripción:"))
        layout.addWidget(self.description_input)

        # Botón de acción con el mismo estilo que los botones CRUD
        action_button = QPushButton(operation)
        action_button.clicked.connect(self.perform_action)
        action_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
        layout.addWidget(action_button)

    def perform_action(self):
        # Aquí iría la lógica para interactuar con la base de datos
        print(f"Realizando operación: {self.windowTitle()}")
        print(f"ID: {self.id_input.text()}")
        print(f"Nombre: {self.name_input.text()}")
        print(f"Descripción: {self.description_input.toPlainText()}")
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())