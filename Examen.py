"""
Examen 1 - Python
"""

def ConsultarSaldo(saldo):
    print("Su saldo actual es: $", saldo)

# FUNCION PARA DEPOSITAR DINERO
def Depositar(saldo):
    monto = float(input("Ingrese el monto a depositar: "))
    
    if monto > 0:
        saldo = saldo + monto
        print("Depósito exitoso.")
        print("Su nuevo saldo es: $", saldo)
    else:
        print("Error: el monto a depositar debe ser mayor que cero.")

    return saldo

# FUNCION PARA RETIRAR DINERO
def Retirar(saldo):
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto <= 0:
        print("Error: el monto a retirar debe ser mayor que cero.")
    elif monto > saldo:
        print("Error: saldo insuficiente.")
    else:
        saldo = saldo - monto
        print("Retiro exitoso.")
        print("Su nuevo saldo es: $", saldo)

    return saldo

# Algoritmo Principal
def CajeroAutomatico():

    #Entrada
    saldo = 1000
    opcion = -1

    #Proceso
    while opcion != 0:
        print("\n===== CAJERO AUTOMÁTICO =====")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ConsultarSaldo(saldo)
        elif opcion == 2:
            saldo = Depositar(saldo)
        elif opcion == 3:
            saldo = Retirar(saldo)
        elif opcion == 0:
            print("Gracias por usar el cajero automático.")
        else:
            print("Opción inválida. Seleccione una opción válida.")
    #Salida
    print("Saldo final: $", saldo)

CajeroAutomatico()