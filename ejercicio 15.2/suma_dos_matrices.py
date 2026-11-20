print("Matriz A")
filas_a = int(input("Número de filas: "))
columnas_a = int(input("Número de columnas: "))

print("Matriz B")
filas_b = int(input("Número de filas: "))
columnas_b = int(input("Número de columnas: "))

if filas_a != filas_b or columnas_a != columnas_b:
    print("Error: las matrices deben tener las mismas dimensiones para poder sumarse.")
else:
    filas = filas_a
    columnas = columnas_a

    print("Ingrese los elementos de la matriz A:")
    A = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"A[{i}][{j}]: ")))
        A.append(fila)

    print("Ingrese los elementos de la matriz B:")
    B = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"B[{i}][{j}]: ")))
        B.append(fila)

    suma = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        suma.append(fila)

    print("Matriz resultante:")
    for i in range(filas):
        for j in range(columnas):
            print(f"{suma[i][j]:>5}", end="")
        print()

"El programa pide las filas y columnas de cada matriz por separado y las compara. Si no coinciden, muestra un mensaje de error y termina. Si coinciden, pide los elementos de A y B, crea una matriz nueva donde cada posición (i, j) guarda A[i][j] + B[i][j], y la imprime con :>5 para que las columnas queden alineada"