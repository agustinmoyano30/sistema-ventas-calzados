from database import conectar

# === CONSULTA 1:
def ventas_por_vendedor():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT ve.nombre || ' ' || ve.apellido AS vendedor,
               COUNT(v.id_venta) AS cantidad_ventas,
               SUM(v.total) AS total_recaudado
        FROM ventas v
        JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
        GROUP BY ve.id_vendedor
        ORDER BY total_recaudado DESC;
    """)
    resultados = cursor.fetchall()
    conexion.close()

    print("\n=== Ventas totales por vendedor ===")
    if resultados:
        for fila in resultados:
            print(f"Vendedor: {fila[0]} | Ventas: {fila[1]} | Total vendido: ${fila[2]:.2f}")
    else:
        print("No hay ventas registradas.")


# === CONSULTA 2:
def calzados_no_vendidos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT c.marca, c.modelo, c.talle, c.precio
        FROM calzados c
        WHERE c.id_calzado NOT IN (
            SELECT DISTINCT id_calzado FROM detalle_ventas
        );
    """)
    resultados = cursor.fetchall()
    conexion.close()

    print("\n=== Calzados que nunca fueron vendidos ===")
    if resultados:
        for fila in resultados:
            print(f"{fila[0]} {fila[1]} (Talle {fila[2]}) - ${fila[3]}")
    else:
        print("Todos los calzados tienen al menos una venta.")