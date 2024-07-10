from utilidades import *

# Menú principal
while True:
    print("\nMenú:")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    try:
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_asientos_disponibles()
        elif opcion == "2":
            comprar_asiento()
        elif opcion == "3":
            anular_vuelo()
        elif opcion == "4":
            modificar_datos_pasajero()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    except EOFError:
        print("\n¡Gracias por usar el sistema de Vuelos Duoc! ¡Hasta luego!")
        break
