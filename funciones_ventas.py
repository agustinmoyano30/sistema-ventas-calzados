from database import conectar
import datetime

def menu_ventas():
    while True:
        print("\n=== MENÚ DE VENTAS ===")
        print("1. Registrar una venta")
        print("2. Ver todas las ventas (con detalle)")
        print("3. Ver detalle de una venta específica")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            ver_ventas()
        elif opcion == "3":
            ver_detalle_venta()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def registrar_venta():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== Registrar nueva venta ===")
    id_cliente = input("Ingrese el ID del cliente: ")
    id_vendedor = input("Ingrese el ID del vendedor: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO ventas (fecha, id_cliente, id_vendedor)
        VALUES (?, ?, ?)
    """, (fecha, id_cliente, id_vendedor))
    conexion.commit()

    id_venta = cursor.lastrowid
    total_venta = 0

    while True:
        id_calzado = input("\nIngrese el ID del calzado (o 0 para finalizar): ")
        if id_calzado == "0":
            break

        cantidad = int(input("Cantidad: "))

        cursor.execute("SELECT precio, stock FROM calzados WHERE id_calzado = ?", (id_calzado,))
        calzado = cursor.fetchone()

        if not calzado:
            print("Calzado no encontrado.")
            continue

        precio_unitario, stock_actual = calzado

        if cantidad > stock_actual:
            print("Stock insuficiente.")
            continue

        subtotal = precio_unitario * cantidad
        total_venta += subtotal

        cursor.execute("""
            INSERT INTO detalle_ventas (id_venta, id_calzado, cantidad, precio_unitario, subtotal)
            VALUES (?, ?, ?, ?, ?)
        """, (id_venta, id_calzado, cantidad, precio_unitario, subtotal))

        nuevo_stock = stock_actual - cantidad
        cursor.execute("UPDATE calzados SET stock = ? WHERE id_calzado = ?", (nuevo_stock, id_calzado))

        conexion.commit()
        print(f"Producto agregado. Subtotal: ${subtotal:.2f}")

    cursor.execute("UPDATE ventas SET total = ? WHERE id_venta = ?", (total_venta, id_venta))
    conexion.commit()

    print(f"\nVenta registrada correctamente. Total: ${total_venta:.2f}")
    conexion.close()


def ver_ventas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT v.id_venta, v.fecha, 
               c.nombre || ' ' || c.apellido AS cliente,
               ve.nombre || ' ' || ve.apellido AS vendedor,
               v.total
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
        ORDER BY v.id_venta;
    """)
    ventas = cursor.fetchall()

    if not ventas:
        print("\nNo hay ventas registradas.")
        conexion.close()
        return

    print("\n=== LISTADO DE VENTAS (DETALLADO) ===")

    for venta in ventas:
        id_venta = venta[0]
        print(f"\nVenta N°{id_venta} | Fecha: {venta[1]}")
        print(f"Cliente: {venta[2]} | Vendedor: {venta[3]}")
        print("-" * 70)

        cursor.execute("""
            SELECT c.codigo, c.marca, c.modelo, d.cantidad, d.precio_unitario, d.subtotal
            FROM detalle_ventas d
            JOIN calzados c ON d.id_calzado = c.id_calzado
            WHERE d.id_venta = ?;
        """, (id_venta,))
        detalles = cursor.fetchall()

        for fila in detalles:
            print(f"Código: {fila[0]} | {fila[1]} {fila[2]} | "
                  f"Cantidad: {fila[3]} | Precio: ${fila[4]} | Subtotal: ${fila[5]}")

        print(f"Total de la venta: ${venta[4]:.2f}")
        print("=" * 70)

    conexion.close()


def ver_detalle_venta():
    id_venta = input("Ingrese el ID de la venta: ")
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT v.fecha, c.nombre || ' ' || c.apellido AS cliente,
               ve.nombre || ' ' || ve.apellido AS vendedor, v.total
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
        WHERE v.id_venta = ?;
    """, (id_venta,))
    cabecera = cursor.fetchone()

    if not cabecera:
        print("No existe una venta con ese ID.")
        conexion.close()
        return

    print(f"\n=== Detalle de la venta N°{id_venta} ===")
    print(f"Fecha: {cabecera[0]} | Cliente: {cabecera[1]} | Vendedor: {cabecera[2]}")
    print("-" * 70)

    cursor.execute("""
        SELECT c.codigo, c.marca, c.modelo, d.cantidad, d.precio_unitario, d.subtotal
        FROM detalle_ventas d
        JOIN calzados c ON d.id_calzado = c.id_calzado
        WHERE d.id_venta = ?;
    """, (id_venta,))
    detalles = cursor.fetchall()

    for fila in detalles:
        print(f"Código: {fila[0]} | {fila[1]} {fila[2]} | "
              f"Cantidad: {fila[3]} | Precio: ${fila[4]} | Subtotal: ${fila[5]}")

    print(f"Total de la venta: ${cabecera[3]:.2f}")
    print("=" * 70)
    conexion.close()