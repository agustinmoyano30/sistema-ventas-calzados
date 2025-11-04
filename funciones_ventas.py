from database import conectar

def menu_ventas():
    while True:
        print("\n=== MENÚ DE VENTAS ===")
        print("1. Registrar una venta")
        print("2. Ver todas las ventas")
        print("3. Ver detalles de una venta")
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

    import datetime
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

    print(f"\n Venta registrada correctamente. Total: ${total_venta:.2f}")
    conexion.close()

def ver_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT v.id_venta, v.fecha, c.nombre || ' ' || c.apellido AS cliente,
               ve.nombre || ' ' || ve.apellido AS vendedor
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
        ORDER BY v.id_venta DESC
    """)
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print("\n=== LISTADO DE VENTAS ===")
        for fila in resultados:
            print(f"ID: {fila[0]} | Fecha: {fila[1]} | Cliente: {fila[2]} | Vendedor: {fila[3]}")
    else:
        print("No hay ventas registradas.")

def ver_detalle_venta():
    id_venta = input("Ingrese el ID de la venta: ")
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT c.codigo, c.marca, c.modelo, d.cantidad, d.precio_unitario, d.subtotal
        FROM detalle_ventas d
        JOIN calzados c ON d.id_calzado = c.id_calzado
        WHERE d.id_venta = ?
    """, (id_venta,))
    resultados = cursor.fetchall()

    if resultados:
        print(f"\n=== Detalle de la venta {id_venta} ===")
        for fila in resultados:
            print(f"Código: {fila[0]} | {fila[1]} {fila[2]} | Cantidad: {fila[3]} | Precio: ${fila[4]} | Subtotal: ${fila[5]}")
    else:
        print("No hay detalle para esa venta.")

    conexion.close()