movimientos = []

def guardar_movimientos():
    with open("finanzas.txt", "w") as archivo:
        for desc, tipo, monto in movimientos:
            archivo.write(f"{desc} | {tipo} | {monto}\n")


try:
    with open("finanzas.txt", "r") as archivo:
        movimientos = []
        for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 3:
                desc, tipo, monto = partes
                movimientos.append([desc, tipo, float(monto)])
except FileNotFoundError:
    pass

while True:
    print("\n--- REGISTRO DE FINANZAS ---")
    print("1 - Agregar ingreso")
    print("2 - Agregar gasto")
    print("3 - Ver historial")
    print("4 - Ver balance")
    print("5 - Salir")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        desc = input("Descripcion del ingreso: ")
        try:
            monto = float(input("Monto: "))
            movimientos.append([desc, "ingreso", monto])
            guardar_movimientos()
            print("Ingreso agregado.")
        except ValueError:
            print("Monto invalido.")

    elif opcion == "2":
        desc = input("Descripcion del gasto: ")
        try:
            monto = float(input("Monto: "))
            movimientos.append([desc, "Gasto", monto])
            guardar_movimientos()
            print("Gasto agregado.")
        except ValueError:
            print("Monto invalido.")

    elif opcion == "3":
        print("\n--- HISTORIAL ---")
        for i, (desc, tipo, monto) in enumerate(movimientos, 1):
            print(f"{i}. {tipo}: {desc} - ${monto}")

    elif opcion == "4":
        balance = 0
        for _, tipo, monto in movimientos:
            if tipo == "Ingreso":
                balance += monto
            else:
                balance -= monto
        print(F"\nBalance actual: $ {balance}")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opcion invalida. intente nuevamente")
