from database import conectar

def menu_crud_clientes():
    while True:
        print("\n=== MENÚ CRUD DE CLIENTES ===")
        print("1. Agregar cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Ver todos los clientes")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            ver_clientes()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    cursor.execute("""
        INSERT INTO clientes (nombre, apellido, telefono, email)
        VALUES (?, ?, ?, ?)
    """, (nombre, apellido, telefono, email))

    conexion.commit()
    conexion.close()
    print("Cliente agregado correctamente.")

def ver_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        for fila in resultados:
            print(fila)
    else:
        print("No hay clientes registrados.")

def modificar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    print("¿Qué desea modificar?")
    print("1. Teléfono")
    print("2. Email")
    opcion = input("Opción: ")

    if opcion == "1":
        nuevo_telefono = input("Nuevo teléfono: ")
        cursor.execute("UPDATE clientes SET telefono = ? WHERE id_cliente = ?", (nuevo_telefono, id_cliente))
    elif opcion == "2":
        nuevo_email = input("Nuevo email: ")
        cursor.execute("UPDATE clientes SET email = ? WHERE id_cliente = ?", (nuevo_email, id_cliente))
    else:
        print("Opción inválida.")
        return

    conexion.commit()
    conexion.close()
    print("Cliente modificado correctamente.")

def eliminar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))
    conexion.commit()
    conexion.close()
    print("Cliente eliminado correctamente.")