import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

@pytest.mark.parametrize("precio_unitario, cantidad, descuento, total_esperado",
    [
        (100, 1, 0, 100),
        (100, 2, 10, 180),
        (50, 4, 25, 150),
        (200, 1, 50, 100),
    ]
)
def test_aplicar_descuento_parametrizado(precio_unitario, cantidad, descuento, total_esperado):

    # Arrange, se crea carrito con un producto dado
    carrito = Carrito()
    producto = Producto("Promo", precio_unitario, stock=10)
    carrito.agregar_producto(producto, cantidad)

    # Act, se aplica descuento
    total_con_descuento = carrito.aplicar_descuento(descuento)

    # Assert, se compra con el total esperado
    assert total_con_descuento == total_esperado





def test_agregar_producto_nuevo(carrito,producto_generico):

    # Act: se agrega el producto al carrito
    carrito.agregar_producto(producto_generico)
    
    # Assert: se verifica que el carrito contiene un item con el producto y cantidad 1
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Genérico"
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

@pytest.mark.parametrize(
    "nueva_cantidad, debe_fallar",
    [
        (5, False),
        (0, False),  # Se permite 0 (debería eliminar el producto)
        (-1, True),
        (-10, True),
    ]
)

def test_actualizar_cantidad_parametrizada(nueva_cantidad, debe_fallar):

    # Arrange, se crea carrito y producto.
    carrito = Carrito()
    producto = Producto("Item", 50, stock=10)
    carrito.agregar_producto(producto, cantidad=2)

    # Act y Assert: se erifica comportamiento según cantidad valida o no
    if debe_fallar:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto, nueva_cantidad)
    else:
        carrito.actualizar_cantidad(producto, nueva_cantidad)
        cantidad_resultante = sum(i.cantidad for i in carrito.obtener_items())
        assert cantidad_resultante == nueva_cantidad


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

    # Arrange, se crea un carrito y se agregan varios productos con distintas cantidades.
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act, se calcula el total del carrito.
    total = carrito.calcular_total()
    
    # Assert, se verifica que el total es la suma correcta de cada item (precio * cantidad).
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

# verificar que el descuento se aplique cuando el total del carrito cumple al menos con el minimo
def test_descuento_condicional_aplicado():

    # Arrange, se crea un carrito con un total mayor al minimo
    carrito = Carrito()
    producto = ProductoFactory(nombre="TV", precio=600.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 600

    # Act, se aplica el descuento condicional
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 500)

    # Assert, se crea un carrito con un total mayor al miniomo
    assert total_con_descuento == 510.00 

# verificar que ningun descuento no se aplique cuando el total no cumple al menos con el minimo
def test_descuento_condicional_no_aplicado():

    # Arrange, se crea un carrito con total menor al minimo
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=300.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 300

    # Act, aplica el descuento
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 500)

    # Assert, se crea un carrito con total menos al minimo
    assert total_con_descuento == 300.00

# se puede agregar dentro del limite del stock
def test_agregar_producto_dentro_del_stock():

    # Arrange, se crea un producto con stock y carrito
    producto = Producto("Memoria RAM", 120.0, stock=5)
    carrito = Carrito()

    # Act, se agrega producto dentro del limite permitido
    carrito.agregar_producto(producto, cantidad=3)

    # Assert, se crea un producto con stock y carrito
    assert len(carrito.obtener_items()) == 1
    assert carrito.obtener_items()[0].cantidad == 3

def test_agregar_producto_excede_stock_lanza_excepcion():

    # Arrange, se crea un producto con stock limitado
    producto = Producto("SSD", 200.0, stock=4)
    carrito = Carrito()

    # Act & Assert: se intenta agregar mas de lo que se permite y
    # se captura el error
    with pytest.raises(ValueError, match="Cantidad a agregar excede el stock disponible"):
        carrito.agregar_producto(producto, cantidad=5)

def test_ordenar_items_por_precio():

    # Arrange, se agrega productos con distintos precios
    carrito = Carrito()
    producto1 = Producto("A", 300.0, stock=10)
    producto2 = Producto("B", 100.0, stock=10)
    producto3 = Producto("C", 200.0, stock=10)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)

    # Act: se obtiene los items ordenados por precio
    ordenados = carrito.obtener_items_ordenados("precio")

    # Assert: se verifica que el orden sea ascendente por precio
    precios = [item.producto.precio for item in ordenados]
    assert precios == [100.0, 200.0, 300.0]

def test_ordenar_items_criterio_invalido():

    # Arrange, se agrega un producto al carrito
    carrito = Carrito()
    producto = Producto("X", 100.0, stock=5)
    carrito.agregar_producto(producto)

    # Act y Assert, se verifica que al usar un criterio invalido lanza excepción.
    
    with pytest.raises(ValueError, match="Criterio inválido"):
        carrito.obtener_items_ordenados("peso")

# ordenamiento correcto por precio
def test_ordenar_items_por_precio():

    #Arrange, se agrega productos con distintos precios.
    carrito = Carrito()
    producto1 = Producto("A", 300.0, stock=10)
    producto2 = Producto("B", 100.0, stock=10)
    producto3 = Producto("C", 200.0, stock=10)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)

    #Act, se obtiene items ordenados por precio
    ordenados = carrito.obtener_items_ordenados("precio")

    #Assert, se verifica que el orden sea ascendente por precio
    precios = [item.producto.precio for item in ordenados]
    assert precios == [100.0, 200.0, 300.0]

# ordenamiento correcto por nombre
def test_ordenar_items_por_nombre():

    #Arrange, se agrega productos con distintos nombres
    carrito = Carrito()
    producto1 = Producto("Zanahoria", 10.0, stock=10)
    producto2 = Producto("Banana", 20.0, stock=10)
    producto3 = Producto("Aguacate", 30.0, stock=10)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)

    #Act, se obtiene items ordenados por nombre
    ordenados = carrito.obtener_items_ordenados("nombre")

    #Assert, se verifica que el orden sea alfabético
    nombres = [item.producto.nombre for item in ordenados]
    assert nombres == ["Aguacate", "Banana", "Zanahoria"]

# validacion de criterio invalido
def test_ordenar_items_criterio_invalido():
    #Arrange, se agrega un producto al carrito
    carrito = Carrito()
    producto = Producto("X", 100.0, stock=5)
    carrito.agregar_producto(producto)

    #Act y Assert, se verifica que usar un criterio invalido lanza excepcion
    with pytest.raises(ValueError, match="Criterio inválido"):
        carrito.obtener_items_ordenados("peso")

