import pytest
from src.belly import Belly

def test_belly_gruñido_con_segundos():
    b = Belly()
    b.comer(35)
    b.esperar(1 + 30/60 + 45/3600)  # 1h 30m 45s
    assert b.esta_gruñendo()

def test_pepinos_fraccionarios():
    b = Belly()
    b.comer(0.5)
    b.esperar(2)
    assert not b.esta_gruñendo()

def test_pepinos_negativos():
    b = Belly()
    with pytest.raises(ValueError, match="negativa"):
        b.comer(-5)

def test_pepinos_mayor_que_100():
    b = Belly()
    with pytest.raises(ValueError, match="más de 1000"):
        b.comer(1500)

def test_escalabilidad_1000_pepinos():
    b = Belly()
    b.comer(1000)
    b.esperar(10)
    assert b.esta_gruñendo()

def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo()

def test_pepinos_comidos():
    belly = Belly()
    belly.comer(15)
    assert belly.obtener_pepinos_comidos() == 15

def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() is True
