def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un entero positivo: "))
print(f"El factorial de {numero} es {factorial(numero)}")

"la función recibe n como parámetro y empieza con resultado = 1. El ciclo multiplica resultado por cada número de 2 hasta n, y al final return devuelve el valor. Toda la lógica está dentro de la función, y fuera solo se pide el dato y se imprime. Con n = 0 o n = 1 el ciclo no se ejecuta y devuelve 1, que es el factorial correcto."