from database import conectar

def buscar_por_marca():
    marca = input("Ingrese la marca: ")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM calzados WHERE marca LIKE ?", ('%' + marca + '%',))
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        for calzado in resultados:
            print(calzado)
    else:
        print("No se encontraron calzados de esa marca.")

def buscar_por_talle():
    talle = input("Ingrese el talle: ")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM calzados WHERE talle = ?", (talle,))
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        for calzado in resultados:
            print(calzado)
    else:
        print("No se encontraron calzados de ese talle.")

def ver_todos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM calzados")
    resultados = cursor.fetchall()
    conexion.close()

    for calzado in resultados:
        print(calzado)

def menu_crud_calzados():
    while True:
        print("\n=== MENÚ CRUD DE CALZADOS ===")
        print("1. Agregar calzado")
        print("2. Modificar calzado")
        print("3. Eliminar calzado")
        print("4. Ver todos los calzados")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_calzado()
        elif opcion == "2":
            modificar_calzado()
        elif opcion == "3":
            eliminar_calzado()
        elif opcion == "4":
            ver_todos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")


def agregar_calzado():
    conexion = conectar()
    cursor = conexion.cursor()

    codigo = input("Código: ")
    modelo = input("Modelo: ")
    color = input("Color: ")
    talle = int(input("Talle: "))
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    cursor.execute("""
        INSERT INTO calzados (codigo, modelo, color, talle, marca, precio, stock)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (codigo, modelo, color, talle, marca, precio, stock))

    conexion.commit()
    conexion.close()
    print("Calzado agregado exitosamente.")

def modificar_calzado():
    conexion = conectar()
    cursor = conexion.cursor()

    id_calzado = input("Ingrese el ID del calzado a modificar: ")

    print("¿Qué desea modificar?")
    print("1. Precio")
    print("2. Stock")
    print("3. Marca")
    opcion = input("Opción: ")

    if opcion == "1":
        nuevo_precio = float(input("Nuevo precio: "))
        cursor.execute("UPDATE calzados SET precio = ? WHERE id_calzado = ?", (nuevo_precio, id_calzado))
    elif opcion == "2":
        nuevo_stock = int(input("Nuevo stock: "))
        cursor.execute("UPDATE calzados SET stock = ? WHERE id_calzado = ?", (nuevo_stock, id_calzado))
    elif opcion == "3":
        nueva_marca = input("Nueva marca: ")
        cursor.execute("UPDATE calzados SET marca = ? WHERE id_calzado = ?", (nueva_marca, id_calzado))
    else:
        print("Opción inválida.")
        return

    conexion.commit()
    conexion.close()
    print("Calzado modificado exitosamente.") 

def eliminar_calzado():
    conexion = conectar()
    cursor = conexion.cursor()

    id_calzado = input("Ingrese el ID del calzado a eliminar: ")
    cursor.execute("DELETE FROM calzados WHERE id_calzado = ?", (id_calzado,))
    conexion.commit()
    conexion.close()
    print("Calzado eliminado exitosamente.") 