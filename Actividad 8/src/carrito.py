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


    def calcular_impuestos(self, porcentaje):
        """
        Calcula el valor de los impuestos basados en el porcentaje indicado.

        Args:
            porcentaje (float): Porcentaje de impuesto a aplicar (entre 0 y 100).

        Returns:
            float: Monto del impuesto.

        Raises:
            ValueError: Si el porcentaje no está entre 0 y 100.
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (porcentaje / 100)

    def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
        """
        Aplica un cupón de descuento al total del carrito, asegurando que el descuento no exceda el máximo permitido.
        
        Args:
            descuento_porcentaje (float): Porcentaje de descuento a aplicar.
            descuento_maximo (float): Valor máximo de descuento permitido.
        
        Returns:
            float: Total del carrito después de aplicar el cupón.
        
        Raises:
            ValueError: Si alguno de los valores es negativo.
        """
        if descuento_porcentaje < 0 or descuento_maximo < 0:
            raise ValueError("Los valores de descuento deben ser positivos")
        
        total = self.calcular_total()
        descuento_calculado = total * (descuento_porcentaje / 100)
        descuento_final = min(descuento_calculado, descuento_maximo)
        return total - descuento_final

    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito verificando que la cantidad no exceda el stock disponible.
        
        Args:
            producto (Producto): Producto a agregar.
            cantidad (int): Cantidad a agregar.
        
        Raises:
            ValueError: Si la cantidad total excede el stock del producto.
        """
        item = self._buscar_item(producto)
        cantidad_actual = item.cantidad if item else 0

        if cantidad_actual + cantidad > producto.stock:
            raise ValueError("Cantidad a agregar excede el stock disponible")
        
        if item:
            item.cantidad += cantidad
        else:
            self.items.append(ItemCarrito(producto, cantidad))


    # devuelve el item del carrito q contiene el producto
    def _buscar_item(self, producto):

        for item in self.items:
            if item.producto.nombre == producto.nombre:
                return item
        return None
