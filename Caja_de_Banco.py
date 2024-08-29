# Variables globales
usuarios = []
saldos = []

def mostrar_menu():
    print("\nBienvenido al sistema de caja del banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Consultar saldo")
    print("4. Retiro")
    print("5. Salir")

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado.")
    else:
        usuarios.append(nombre)
        saldos.append(0)
        print(f"Usuario {nombre} registrado con éxito.")
        
def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        monto = float(input("Introduce el monto a depositar: "))
        saldos[indice] += monto
        print(f"Depósito de {monto} realizado con éxito. Nuevo saldo: {saldos[indice]}")
    else:
        print("El usuario no existe.")

def consultar_saldo():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        print(f"El saldo actual de {nombre} es: {saldos[indice]}")
    else:
        print("El usuario no existe.")
        
def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        monto = float(input("Introduce el monto a retirar: "))
        if monto <= saldos[indice]:
            saldos[indice] -= monto
            print(f"Retiro de {monto} realizado con éxito. Nuevo saldo: {saldos[indice]}")
        else:
            print("Fondos insuficientes.")
    else:
        print("El usuario no existe.")
              
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            consultar_saldo()
        elif opcion == "4":
            retirar()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()