
# Actividad 8


#### 1. Creación de la estructura del proyecto

```text
Desarrollo-de-Software-Actividades/
├── src/
│   ├── __init__.py
│   └── carrito.py
├── tests/
│   ├── __init__.py
│   └── test_carrito.py
├── pytest.ini
├── requirements.txt

```
![Descripción](Imagenes/Eje11.png)

#### 2.Se crea un archivo pytest.ini para que `pytest` encuentro los modulos
```text
[pytest]
pythonpath = .
testpaths = tests
```

#### 3. Se agrega las siguientes clases en el archivo `carrito.py`
```text
Producto: representa un producto personal
ItemCarrito : representa una entrada al carrito
Carrito: es el contenedor principal donde se agregan, actualizan y eliminan el producto

```
![Descripción](Imagenes/Eje12.png)

## Ejercicio 1: Método para vaciar el carrito

**Se añade el siguiente método que reemplaza la lista de items or una lista vacia**
```python
def vaciar(self):
	self.items=[]
```

**Se añade una prueba automatizada en test_carrito.py que comprueba si el carro queda vacio
  y al retornar una lista vacia**

```python
def test_vaciar_carrito():

    # Arrange, se crea carrito y se agregan productos
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Teclado", precio=100.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total = 200
    carrito.agregar_producto(producto2, cantidad=1)  # Total = 50
    
    #Act, llama al metodo vaciar
    carrito.vaciar()

    # Assert, verificar que el carro este vacio y su total en 0
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0
```

**Resultados**

- Cuando ejecutamos `pytest --cov=src --cov-report=term-missing` nos entrega como resultado
   las 10 pruebas unitarias pasaron correctamente
- Cuando ejecutamos `pytest --cov=src --cov-report=term-missing`  nos muestra que el 86% es bueno
  , aunque no del todo, ya que hay lineas no cubiertas o evaluadas en el archivo `carrito.py`
	![Descripción](Imagenes/Eje13.png)

## Ejercicio 2: Descuento por compra mínima

**Se implementa el metodo `aplicar_descuento_condicional`, aplica descuento si carrito>= minimo**
```python
    # aplica un descuento si el total del carrito es mayor o igual al minimo
    def aplicar_descuento_condicional(self, porcentaje, minimo):

        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        if minimo < 0:
            raise ValueError("El monto mínimo no puede ser negativo")

        total = self.calcular_total()
        if total >= minimo:
            descuento = total * (porcentaje / 100)
            return total - descuento
        return total
```
**Se implementa prueba unitaria tanto para el descuento condicional como el no condicional**

- Verifica que el descuento se aplique cuando el total del carrito cumple con el minimo
```python
sdef test_descuento_condicional_aplicado():

    # Arrange, se crea un carrito con un total mayor al minimo
    carrito = Carrito()
    producto = ProductoFactory(nombre="TV", precio=600.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 600

    # Act, se aplica el descuento condicional
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 500)

    # Assert, se crea un carrito con un total mayor al miniomo
    assert total_con_descuento == 510.00 

```
- Verifica que no se aplique ningun descuento si el  total es menor al minimo
```python
def test_descuento_condicional_no_aplicado():

    # Arrange, se crea un carrito con total menor al minimo
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=300.00)
    carrito.agregar_producto(producto, cantidad=1)  # Total = 300

    # Act, aplica el descuento
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 500)

    # Assert, se crea un carrito con total menos al minimo
    assert total_con_descuento == 300.00
```
**Resultados**
- Se ejecuta todas las pruebas y las 12 pruebas pasaron correctamente, tambien se ve 2 warning pero eso se debe al error del pytest-cov, y el 86% se debe a que hay linea faltantes que la prueba no esta ejecutanto.
![Descripción](Imagenes/Eje21.png)
