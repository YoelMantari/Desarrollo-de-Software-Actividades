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
    with pytest.raises(ValueError, match="más de 100"):
        b.comer(120)
