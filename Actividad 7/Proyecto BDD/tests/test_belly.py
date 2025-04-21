import pytest
from src.belly import Belly

def test_belly_gruñido_con_segundos():
    b = Belly()
    b.comer(35)
    b.esperar(1 + 30/60 + 45/3600)  # 1h 30m 45s
    assert b.esta_gruñendo()