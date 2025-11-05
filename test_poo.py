from modelos import Cliente, Vendedor, Calzado, Venta
import datetime

cliente = Cliente("Sofía", "López", "387458965", "sofia@mail.com")
vendedor = Vendedor("Juan", "Pérez", "387456123", "juan@mail.com", 250000)
calzado1 = Calzado("A123", "Deportivo", "Negro", 42, "Nike", 55000, 10)
calzado2 = Calzado("B234", "Botín", "Marrón", 40, "Topper", 48000, 5)

venta = Venta(1, cliente, vendedor, datetime.date.today())

venta.agregar_detalle(calzado1, 2)
venta.agregar_detalle(calzado2, 1)
venta.mostrar_detalle()