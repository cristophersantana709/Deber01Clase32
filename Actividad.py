# Variables globales
usuarios = {}

def mostrar_menu():
    print("\nBienvenido al sistema de caja del banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Salir")
    
def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado.")
    else:
        usuarios[nombre] = 0
        print(f"Usuario {nombre} registrado con éxito.")
        
def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
        print(f"Depósito de {monto} realizado con éxito. Nuevo saldo: {usuarios[nombre]}")
    else:
        print("El usuario no existe.")
        
def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:      
        monto = float(input("Introduce el monto a retirar: "))
        if monto <= usuarios[nombre]:
            usuarios[nombre] -= monto
            print(f"Retiro de {monto} realizado con éxito. Nuevo saldo: {usuarios[nombre]}")
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
            retirar()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
    