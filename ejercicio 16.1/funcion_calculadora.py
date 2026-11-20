def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def calculadora():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("Operaciones: 1) Sumar  2) Restar  3) Multiplicar  4) Dividir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        resultado = sumar(a, b)
    elif opcion == 2:
        resultado = restar(a, b)
    elif opcion == 3:
        resultado = multiplicar(a, b)
    elif opcion == 4:
        resultado = dividir(a, b)
    else:
        resultado = "Error: opción no válida"

    print("Resultado:", resultado)

calculadora()

"cada operación vive en su propia función, que recibe a y b y devuelve el resultado con return. dividir revisa primero si b es 0 para evitar el error. calculadora() pide los dos números y la opción, y con if/elif/else llama a la función correspondiente, guarda lo que devuelve en resultado y lo imprime. Al final, calculadora() se llama una vez para que el programa arranque."