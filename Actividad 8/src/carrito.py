class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio})"


class ItemCarrito:
    def __init__(self, producto, cantidad=1):
        self.producto = producto
        self.cantidad = cantidad

    def total(self):
        return self.producto.precio * self.cantidad

    def __repr__(self):
        return f"ItemCarrito({self.producto}, cantidad={self.cantidad})"


class Carrito:
    def __init__(self):
        self.items = []

    # se agrega un producto al carrito y si el producto existe entonces incrementa la cantidad
    def agregar_producto(self, producto, cantidad=1):

        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return
        self.items.append(ItemCarrito(producto, cantidad))

    # se remueve una cantidad del producto del carrito y si la cantidad llega 0
    # se elimina el item
    def remover_producto(self, producto, cantidad=1):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    # se actualiza la cantidad de un producto en el carrito y si esta cantidad llega a 0
    # entonces se elimina el item
    def actualizar_cantidad(self, producto, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    # se calcula el total del carrito sin descuento
    def calcular_total(self):
        return sum(item.total() for item in self.items)

    # se aplica un descuento al total del carrito y retorna el total descontado
    def aplicar_descuento(self, porcentaje):

        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    # se retorna el numero total de items de las cantidad en el carrito
    def contar_items(self):

        return sum(item.cantidad for item in self.items)

    # devolver las listas de items del carrito
    def obtener_items(self):

        return self.items

    #elimina todos los items del carrito
    def vaciar(self):
        self.items = []


    