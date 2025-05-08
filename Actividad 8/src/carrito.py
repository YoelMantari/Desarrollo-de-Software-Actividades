class Producto:
    def __init__(self, nombre, precio, stock = 10):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio},stock ={self.stock})"


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
        total_en_carrito = 0
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                total_en_carrito += item.cantidad
                break

        if total_en_carrito + cantidad > producto.stock:
               raise ValueError("Cantidad a agregar excede el stock disponible")
    
               # si el producto ya esta solo suma
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

    # se elimina todos los items del carrito
    def vaciar(self):
        self.items = []

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

    # se retorna la lista de items ordenados segun precio o nombre
    def obtener_items_ordenados(self, criterio: str):

        if criterio == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        elif criterio == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre.lower())
        else:
            raise ValueError("Criterio inválido. Usa 'precio' o 'nombre'.")



