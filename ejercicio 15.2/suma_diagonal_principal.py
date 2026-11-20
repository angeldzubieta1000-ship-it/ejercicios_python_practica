filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

if filas != columnas:
    print("Error: la matriz debe ser cuadrada (mismo número de filas y columnas).")
else:
    A = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"A[{i}][{j}]: ")))
        A.append(fila)

    suma_diagonal = 0
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                suma_diagonal += A[i][j]

    print("Matriz completa:")
    for i in range(filas):
        for j in range(columnas):
            print(f"{A[i][j]:>5}", end="")
        print()

    print("Suma de la diagonal principal:", suma_diagonal)

"el if compara filas y columnas; si son distintas, muestra el error y termina. Si son iguales, se lee la matriz con ciclos anidados y, en otro par de ciclos, se suma A[i][j] solo cuando i == j, que son los elementos de la diagonal principal. Al final se imprime la matriz alineada con :>5 y el valor de la suma"
