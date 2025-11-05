from funciones_calzados import *
from funciones_clientes import *
from funciones_vendedores import *
from funciones_ventas import *
from consultas_avanzadas import *
from reportes import *

class SistemaVentas:
    def __init__(self):
        pass

    def mostrar_menu_principal(self):
        print("\n=== SISTEMA DE VENTAS DE CALZADOS ===")
        print("1. Gestión de Calzados")
        print("2. Gestión de Clientes")
        print("3. Gestión de Vendedores")
        print("4. Gestión de Ventas")
        print("5. Consultas avanzadas")
        print("6. Reportes y estadísticas")
        print("7. Salir")


    def menu_calzados(self):
        while True:
            print("\n--- MENÚ CALZADOS ---")
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
                print("Opción inválida.")

    def menu_clientes(self):
        while True:
            print("\n--- MENÚ CLIENTES ---")
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
                print("Opción inválida.")

    def menu_vendedores(self):
        while True:
            print("\n--- MENÚ VENDEDORES ---")
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
                print("Opción inválida.")

    def menu_ventas(self):
        while True:
            print("\n--- MENÚ VENTAS ---")
            print("1. Registrar venta")
            print("2. Consultar ventas")
            print("3. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                registrar_venta()
            elif opcion == "2":
                ver_ventas()
            elif opcion == "3":
                break
            else:
                print(" Opción inválida.")

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_calzados()
            elif opcion == "2":
                self.menu_clientes()
            elif opcion == "3":
                self.menu_vendedores()
            elif opcion == "4":
                self.menu_ventas()
            elif opcion == "5":
                self.menu_consultas_avanzadas()  
            elif opcion == "6":
                self.menu_reportes()
            elif opcion == "7":
                print("GRACIAS POR USAR EL SISTEMA.")
                break

    def menu_consultas_avanzadas(self):
        while True:
            print("\n--- MENÚ DE CONSULTAS AVANZADAS ---")
            print("1. Ventas por vendedor (GROUP BY)")
            print("2. Calzados no vendidos (Subconsulta)")
            print("3. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ventas_por_vendedor()
            elif opcion == "2":
                calzados_no_vendidos()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")

    def menu_reportes(self):
        while True:
            print("\n--- MENÚ DE REPORTES ---")
            print("1. Exportar ventas a CSV")
            print("2. Exportar detalle de ventas a TXT")
            print("3. Gráfico de ventas por vendedor")
            print("4. Realizar backup de la base de datos")
            print("5. Restaurar base de datos desde backup")
            print("6. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                exportar_ventas_csv()
            elif opcion == "2":
                exportar_detalle_ventas_txt()
            elif opcion == "3":
                grafico_ventas_por_vendedor()
            elif opcion == "4":
                backup_tablas()
            elif opcion == "5":
                restaurar_tablas()
            elif opcion == "6":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    sistema = SistemaVentas()
    sistema.ejecutar()