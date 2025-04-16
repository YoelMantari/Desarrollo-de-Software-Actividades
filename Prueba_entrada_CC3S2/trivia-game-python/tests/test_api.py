from fastapi.testclient import TestClient
from app.main import app

# crear instancia del testClient
client = TestClient(app)

def test_root_endpoint():
    # llamada del endpoint raíz
    response = client.get("/")
    
    # verificar que el status code sea 200
    assert response.status_code == 200

    # verifica que el mensaje sea el esperado
    data = response.json()
    assert "mensaje" in data and data["mensaje"] == "Bienvenido al juego de trivia"
