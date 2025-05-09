# tests/test_stock.py

import pytest
from src.carrito import Carrito, Producto

def test_agregar_producto_excede_stock():
    """
    Red: Se espera que al intentar agregar una cantidad mayor a la disponible en stock se lance un ValueError.
    """
    # Arrange
    producto = Producto("ProductoStock", 100.00, stock=5)
    carrito = Carrito()

    # Act & Assert
    with pytest.raises(ValueError, match="Cantidad a agregar excede el stock disponible"):
        carrito.agregar_producto(producto, cantidad=6)
