from funciones_calzados import *
from funciones_clientes import *
from funciones_vendedores import *
from funciones_ventas import *
from database import crear_tablas

def mostrar_menu():
    print("=== MENÚ PRINCIPAL DEL SISTEMA DE CALZADOS ===")
    print("1. Gestión de Calzados")
    print("2. Gestión de Clientes")
    print("3. Gestión de Vendedores")
    print("4. Gestión de Ventas")
    print("5. Salir")

def ejecutar_menu():
    crear_tablas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_crud_calzados()
        elif opcion == "2":
            menu_crud_clientes()
        elif opcion == "3":
            menu_crud_vendedores()
        elif opcion == "4":
            menu_ventas()
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()