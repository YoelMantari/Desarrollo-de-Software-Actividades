# tests/test_user_manager.py
import pytest
from user_manager import UserManager, UserNotFoundError,UserAlreadyExistsError


class FakeHashService:
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"


def test_autenticar_usuario_exitoso_con_hash():
    # Arrange, inyectamos el servicio de hashing falso
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)

    # Act, autenticamos al usuario
    autenticado = manager.authenticate_user(username, password)

    # Assert, debe autenticarse correctamente
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."




