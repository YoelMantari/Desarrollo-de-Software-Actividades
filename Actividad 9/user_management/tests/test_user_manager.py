# tests/test_user_manager.py
import pytest
from user_manager import UserManager, UserNotFoundError,UserAlreadyExistsError
from unittest.mock import MagicMock

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


def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange, se crea un servicio de hashing simulado usando MagicMock
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act, se agrega el usuario
    manager.add_user(username, password)

    # Assert, se verifica que se llamó hash exactamente una vez
    mock_hash_service.hash.assert_called_once_with(password)

def test_no_se_puede_agregar_usuario_existente_stub():
    # Este stub forzará que user_exists devuelva True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)



class InMemoryUserRepository:
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_password):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_password

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    # Arrange, se instancia un repositorio falso
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)
    username = "fakeUser"
    password = "fakePass"

    # Act, se agrega el usuario
    manager.add_user(username, password)

    # Assert, se verifica que el usuario existe en el repo
    assert manager.user_exists(username)

def test_envio_correo_bienvenida_al_agregar_usuario():
    
    #Arrange, se crea un mock de un servicio de email y se inyecta en UserManager

    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act, Se agrega un usuario.
    manager.add_user(username, password)
   
    #Assert, Se verifica que el servicio de email fue llamado correctamente
    mock_email_service.send_welcome_email.assert_called_once_with(username)
