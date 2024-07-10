asientos = list(range(1, 43))
pasajeros = {}

# Función para mostrar los asientos disponibles
def mostrar_asientos_disponibles():
    print("Asientos disponibles:")
    for i, asiento in enumerate(asientos):
        if i % 6 == 0:
            print() # Salto de línea cada 6 asientos
        if asiento == "X":
            print("| X ", end="")
        else:
            print(f"| {asiento:2} ", end="")  # Formateo para alinear los números
    print("\n")

# Función para comprar un asiento
def comprar_asiento():
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")
    telefono = input("Ingrese su teléfono: ")
    banco = input("Ingrese su banco: ")

    mostrar_asientos_disponibles()

    while True:
        try:
            num_asiento = int(input("Seleccione un asiento disponible: "))
            if num_asiento in asientos:
                break
            else:
                print("Asiento no disponible o inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    if num_asiento >= 31:
        precio = 250000
    else:
        precio = 80200

    if banco.lower() == "Banco Duoc":
        precio *= 0.85

    print(f"El precio del pasaje es ${precio:.2f}")
    confirmar = input("¿Desea confirmar la compra? (Sí/No): ")
    if confirmar.lower() == "Sí" or "si" or "sí":
        pasajeros[num_asiento] = {"nombre": nombre, "rut": rut, "telefono": telefono, "banco": banco}
        asientos[num_asiento - 1] = "X"
        print("Compra realizada con éxito.")
    else:
        print("Compra cancelada.")

# Función para anular un vuelo
def anular_vuelo():
    while True:
        try:
            num_asiento = int(input("Ingrese el número de asiento a anular: "))
            if num_asiento in pasajeros:
                break
            else:
                print("Asiento no ocupado o inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    del pasajeros[num_asiento]
    asientos[num_asiento - 1] = num_asiento
    print("Vuelo anulado con éxito.")

# Función para modificar los datos de un pasajero
def modificar_datos_pasajero():
    while True:
        num_asiento = int(input("Ingrese el número de asiento: "))
        rut = input("Ingrese su RUT: ")
        if num_asiento in pasajeros and pasajeros[num_asiento]["rut"] == rut:
            break
        else:
            print("Datos incorrectos. Intente nuevamente.")

    while True:
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Teléfono")
        opcion = input("Ingrese una opción: ")
        if opcion in ["1", "2"]:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    if opcion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        pasajeros[num_asiento]["nombre"] = nuevo_nombre
    else:
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
        pasajeros[num_asiento]["telefono"] = nuevo_telefono

    print("Datos modificados con éxito.")