# encoding: UTF-8
# Autor: Silvia Ferman
# Programa que tiene dos funciones, Una que divide y otra que encuentra el numero mas grande dentro de un conjunto


# Funcion que muestra el MENU con las diferentes opciones que muestra cada ejercicio
def leerMenu():
    print("Misión 07. Ciclos while")
    print("Autor: Silvia Ferman")
    print("Matricula: A01376718")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opcion: "))
    return opcion


# Función que divide dos valores e imprime su cociente y residuo
def dividir(dividendo, divisor):
    cociente = 0
    residuo = dividendo

    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1

    print("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, residuo))


# Funcion que encuentra el numero MAYOR de un conjunto de valores.
def encontrarMayor():
    numeroMayor = 0
    print("Teclea una serie de números para encontrar el mayor")
    valor = 0

    while valor != -1:
        valor = int(input("Teclea un número [-1 para salir]: "))
        if valor > numeroMayor:
            numeroMayor = valor

    if numeroMayor == 0:
        print("NO hay un valor mayor")
    else:
        print("El mayor es: ", numeroMayor)


# Función principal
def main():
    opcion = leerMenu()

    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)

        elif opcion == 2:
            encontrarMayor()


# LLama a la función principal
main()