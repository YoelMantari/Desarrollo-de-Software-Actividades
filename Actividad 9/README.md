# Actividad 8


#### 1. Creación de la estructura del proyecto

```text
user_management/
├── user_manager.py
└── tests/
    └── test_user_manager.py
```
![Descripción](Imagenes/Eje.png)

## Iteración 1: Agregar usuario (Básico)

**Se escribe una prueba automatizada para verificar que un usuario pueda ser agregado correctamente**

```python
def test_agregar_usuario_exitoso():
    # Arrange: se crea una instancia de UserManager y se define sus datos
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act: agregamos usuario
    manager.add_user(username, password)

    # Assert: verificamos que el usuario fue registrado
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
```
**Si se ejecuta `pytest` la prueba fallara debido a que aun no se ha h implementado la clase `UserManager`**
`
![Descripción](Imagenes/Eje11.png)


**Se implemento la clase `UserManager` y el método `add_user()` para que la prueba pase correctamente**

```python
class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users
```

**Ahora con la implementacion de la clase `UserManager` se ejecuta correctamente**

![Descripción](Imagenes/Eje12.png)


## Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)

**(RED)Se implementa una prueba unitaria para verificar que se puede autenticar  correctamente a un usuario usando hasshing** 
```python
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
```
**Cuando se ejecute la prueba fallara ya que no se implemento `authenticate_user`**
![Descripción](Imagenes/Eje21.png)

**(Green)e implementa el metodo `authenticate_user` y se permite la inyeccion del servicio hashing**

```python
class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None):
        self.users = {}
        self.hash_service = hash_service

        if not self.hash_service:
            class DefaultHashService:
                def hash(self, plain_text: str) -> str:
                    return plain_text

                def verify(self, plain_text: str, hashed_text: str) -> bool:
                    return plain_text == hashed_text
            self.hash_service = DefaultHashService()

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self, username):
        return username in self.users

    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        stored_hash = self.users[username]
        return self.hash_service.verify(password, stored_hash)
```

**Resultado:**

- Esto confirma que la autenticación con un servicio de hashing inyectado mediante dependencias funciona como se espera usando un `FakeHashService`

![Descripción](Imagenes/Eje22.png)