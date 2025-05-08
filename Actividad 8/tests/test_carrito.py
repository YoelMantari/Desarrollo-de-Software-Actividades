import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory


def test_agregar_producto_nuevo():

    #AAA

    # Arrange: se crea un carrito y se genera un producto
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act: se agrega el producto al carrito
    carrito.agregar_producto(producto)
    
    # Assert: se verifica que el carrito contiene un item con el producto y cantidad 1
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():


    # Arrange: se crea un carrito y se agrega un producto
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act: se agrega el mismo producto nuevamente aumentando la cantidad 
    carrito.agregar_producto(producto, cantidad=2)
    
    # Assert: se verifica que la antidad del producto se incrementa en el item
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():

    # Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    #Act: Se remueve una unidad del producto.
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert: Assert: Se verifica que la cantidad del producto se reduce a 2.
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
 
    # Arrange: Se crea un carrito y se agrega un producto.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act: se remueve la totalidad de la cantidad del producto.
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert: Se verifica que el producto es eliminado del carrito.
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():

    # Arrange: Se crea un carrito y se agrega un producto.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act: Se actualiza la cantidad del producto a 5.
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert: Se verifica que la cantidad se actualiza correctamente.
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():

    #Arrange: Se crea un carrito y se agrega un producto.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    #Act: Se actualiza la cantidad del producto a 0.
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    #Assert: Se verifica que el producto se elimina del carrito.
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():

    # Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act: Se calcula el total del carrito.
    total = carrito.calcular_total()
    
    # Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    assert total == 550.00


def test_aplicar_descuento():

    # Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act: Se aplica un descuento del 10% al total.
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert: Se verifica que el total con descuento sea el correcto.
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites():

    # Arrange: Se crea un carrito y se agrega un producto.
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_vaciar_carrito():

    # Arrange: se crea carrito y se agregan productos
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Teclado", precio=100.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total = 200
    carrito.agregar_producto(producto2, cantidad=1)  # Total = 50
    
    #Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0