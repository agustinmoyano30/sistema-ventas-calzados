class Persona:
    def __init__(self, nombre, apellido, telefono, email):
        self._nombre = nombre         
        self._apellido = apellido
        self._telefono = telefono
        self._email = email

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_telefono(self):
        return self._telefono

    def get_email(self):
        return self._email
    
    def set_telefono(self, nuevo_telefono):
        if not nuevo_telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")
        self._telefono = nuevo_telefono

    def set_email(self, nuevo_email):
        if "@" not in nuevo_email:
            raise ValueError("El email debe contener '@'.")
        self._email = nuevo_email

class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, email, id_cliente=None):
        super().__init__(nombre, apellido, telefono, email)
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self._nombre} {self._apellido} - Tel: {self._telefono}"

class Vendedor(Persona):
    def __init__(self, nombre, apellido, telefono, email, sueldo, id_vendedor=None):
        super().__init__(nombre, apellido, telefono, email)
        self.sueldo = sueldo
        self.id_vendedor = id_vendedor

    def __str__(self):
        return f"Vendedor: {self._nombre} {self._apellido} - Sueldo: ${self.sueldo}"


class Calzado:
    def __init__(self, codigo, modelo, color, talle, marca, precio, stock, id_calzado=None):
        self.codigo = codigo
        self.modelo = modelo
        self.color = color
        self.talle = talle
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.id_calzado = id_calzado

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            raise ValueError("No hay suficiente stock para realizar esta operación.")
        self.stock += cantidad

    def __str__(self):
        return f"{self.marca} {self.modelo} (Talle {self.talle}) - ${self.precio}"
    
class Venta:
    def __init__(self, id_venta, cliente, vendedor, fecha, total=0):
        self.id_venta = id_venta
        self.cliente = cliente
        self.vendedor = vendedor
        self.fecha = fecha
        self.total = total
        self.detalles = []  
    def agregar_detalle(self, calzado, cantidad):
        try:
            calzado.actualizar_stock(-cantidad)
            subtotal = calzado.precio * cantidad
            self.detalles.append((calzado, cantidad, subtotal))
            self.total += subtotal
        except ValueError as e:
            print(f"Error al agregar producto: {e}")

    def mostrar_detalle(self):
        print(f"\nVenta #{self.id_venta} - {self.fecha}")
        print(f"Cliente: {self.cliente.get_nombre()} {self.cliente.get_apellido()}")
        print(f"Vendedor: {self.vendedor.get_nombre()} {self.vendedor.get_apellido()}")
        print("Productos:")
        for calzado, cantidad, subtotal in self.detalles:
            print(f"  - {calzado.marca} {calzado.modelo} x{cantidad} = ${subtotal}")
        print(f"TOTAL: ${self.total}")

    def __str__(self):
        return f"Venta #{self.id_venta} - Total: ${self.total}"
