import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from database import conectar


def exportar_ventas_csv():
    conexion = conectar()
    query = """
    SELECT v.id_venta, v.fecha, c.nombre || ' ' || c.apellido AS cliente,
           ve.nombre || ' ' || ve.apellido AS vendedor, v.total
    FROM ventas v
    JOIN clientes c ON v.id_cliente = c.id_cliente
    JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
    ORDER BY v.id_venta;
    """
    df = pd.read_sql_query(query, conexion)
    conexion.close()

    df.to_csv("reporte_ventas.csv", index=False, encoding="utf-8-sig")
    print("Archivo 'reporte_ventas.csv' generado correctamente.")


def exportar_detalle_ventas_txt():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT v.id_venta, v.fecha, 
               c.nombre || ' ' || c.apellido AS cliente,
               cal.marca, cal.modelo, cal.talle,
               dv.cantidad, dv.precio_unitario, dv.subtotal
        FROM detalle_ventas dv
        JOIN ventas v ON dv.id_venta = v.id_venta
        JOIN calzados cal ON dv.id_calzado = cal.id_calzado
        JOIN clientes c ON v.id_cliente = c.id_cliente
        ORDER BY v.id_venta;
    """)
    registros = cursor.fetchall()
    conexion.close()

    with open("detalle_ventas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("=== DETALLE DE VENTAS ===\n\n")
        for fila in registros:
            archivo.write(f"Venta {fila[0]} | Fecha: {fila[1]} | Cliente: {fila[2]}\n")
            archivo.write(f"{fila[3]} {fila[4]} (Talle {fila[5]}) x{fila[6]} "
                          f"- ${fila[7]} c/u = ${fila[8]}\n")
            archivo.write("-" * 70 + "\n")

    print("Archivo 'detalle_ventas.txt' generado correctamente.")


def grafico_ventas_por_vendedor():
    conexion = conectar()
    query = """
    SELECT ve.nombre || ' ' || ve.apellido AS vendedor,
           SUM(v.total) AS total_recaudado
    FROM ventas v
    JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
    GROUP BY ve.id_vendedor
    ORDER BY total_recaudado DESC;
    """
    df = pd.read_sql_query(query, conexion)
    conexion.close()

    if df.empty:
        print("No hay ventas registradas.")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(df["vendedor"], df["total_recaudado"])
    plt.title("Total vendido por Vendedor")
    plt.xlabel("Vendedor")
    plt.ylabel("Monto Total ($)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def backup_tablas():
    conexion = conectar()
    tablas = ["clientes", "vendedores", "calzados", "ventas", "detalle_ventas"]

    for tabla in tablas:
        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conexion)
        df.to_csv(f"backup_{tabla}.csv", index=False, encoding="utf-8-sig")
    conexion.close()
    print("Backups generados correctamente en archivos CSV.")


def restaurar_tablas():
    conexion = conectar()
    tablas = ["clientes", "vendedores", "calzados", "ventas", "detalle_ventas"]

    for tabla in tablas:
        try:
            df = pd.read_csv(f"backup_{tabla}.csv")
            df.to_sql(tabla, conexion, if_exists="replace", index=False)
            print(f"Tabla '{tabla}' restaurada correctamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo backup_{tabla}.csv, se omitió.")
    conexion.close()