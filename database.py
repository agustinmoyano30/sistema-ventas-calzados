import sqlite3

def conectar():
    conexion = sqlite3.connect("calzados.db")
    return conexion

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        telefono TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendedores (
        id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        telefono TEXT,
        email TEXT,
        sueldo REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calzados (
        id_calzado INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT,
        modelo TEXT,
        color TEXT,
        talle INTEGER,
        marca TEXT,
        precio REAL,
        stock INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        id_cliente INTEGER,
        id_vendedor INTEGER,
        FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY(id_vendedor) REFERENCES vendedores(id_vendedor)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_ventas (
        id_venta INTEGER,
        id_calzado INTEGER,
        cantidad INTEGER,
        precio_unitario REAL,
        subtotal REAL,
        FOREIGN KEY(id_venta) REFERENCES ventas(id_venta),
        FOREIGN KEY(id_calzado) REFERENCES calzados(id_calzado)
    )
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()