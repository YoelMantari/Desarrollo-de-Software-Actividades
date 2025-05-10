# tests/test_user_manager.py
import pytest
from user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():
    # Arrange: Se crea una instancia de UserManager y se define sus datos
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act: Agregamos usuario
    manager.add_user(username, password)

    # Assert: Verificamos que el usuario fue registrado
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
