import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from autenticacion.login_vista import LoginForm
from conectores.db_conectores import authenticate_user

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_form = LoginForm()
        self.login_form.login_signal.connect(self.authenticate_user)

    def authenticate_user(self, username, password):
        if authenticate_user(username, password):
            QMessageBox.information(self.login_form, "Autenticación Exitosa", "Bienvenido al sistema.")
        else:
            QMessageBox.warning(self.login_form, "Error de Autenticación", "Usuario o contraseña incorrectos.")

    def run(self):
        self.login_form.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = MainApp()
    app.run()
