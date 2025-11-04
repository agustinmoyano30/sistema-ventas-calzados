from database import conectar

def menu_crud_vendedores():
    while True:
        print("\n=== MENÚ CRUD DE VENDEDORES ===")
        print("1. Agregar vendedor")
        print("2. Modificar vendedor")
        print("3. Eliminar vendedor")
        print("4. Ver todos los vendedores")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_vendedor()
        elif opcion == "2":
            modificar_vendedor()
        elif opcion == "3":
            eliminar_vendedor()
        elif opcion == "4":
            ver_vendedores()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_vendedor():
    conexion = conectar()
    cursor = conexion.cursor()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    sueldo = float(input("Sueldo: "))

    cursor.execute("""
        INSERT INTO vendedores (nombre, apellido, telefono, email, sueldo)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellido, telefono, email, sueldo))

    conexion.commit()
    conexion.close()
    print("Vendedor agregado correctamente.")

def ver_vendedores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM vendedores")
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        for fila in resultados:
            print(fila)
    else:
        print("No hay vendedores registrados.")

def modificar_vendedor():
    conexion = conectar()
    cursor = conexion.cursor()

    id_vendedor = input("Ingrese el ID del vendedor a modificar: ")
    print("¿Qué desea modificar?")
    print("1. Teléfono")
    print("2. Email")
    print("3. Sueldo")
    opcion = input("Opción: ")

    if opcion == "1":
        nuevo_tel = input("Nuevo teléfono: ")
        cursor.execute("UPDATE vendedores SET telefono = ? WHERE id_vendedor = ?", (nuevo_tel, id_vendedor))
    elif opcion == "2":
        nuevo_email = input("Nuevo email: ")
        cursor.execute("UPDATE vendedores SET email = ? WHERE id_vendedor = ?", (nuevo_email, id_vendedor))
    elif opcion == "3":
        nuevo_sueldo = float(input("Nuevo sueldo: "))
        cursor.execute("UPDATE vendedores SET sueldo = ? WHERE id_vendedor = ?", (nuevo_sueldo, id_vendedor))
    else:
        print("Opción inválida.")
        return

    conexion.commit()
    conexion.close()
    print("Vendedor modificado correctamente.")

def eliminar_vendedor():
    conexion = conectar()
    cursor = conexion.cursor()
    id_vendedor = input("Ingrese el ID del vendedor a eliminar: ")
    cursor.execute("DELETE FROM vendedores WHERE id_vendedor = ?", (id_vendedor,))
    conexion.commit()
    conexion.close()
    print("Vendedor eliminado correctamente.")