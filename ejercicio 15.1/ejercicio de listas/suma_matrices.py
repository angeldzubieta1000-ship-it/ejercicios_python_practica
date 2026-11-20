filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

print("Matriz A:")
A = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"A[{i}][{j}]: ")))
    A.append(fila)

print("Matriz B:")
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

print("Suma:")
for fila in suma:
    print(fila)

"Para sumar dos matrices del mismo tamaño, el programa pide el número de filas y columnas, y luego lee los valores de la matriz A y de la matriz B con dos ciclos anidados (uno para filas y otro para columnas). Después crea una matriz nueva, suma, y en cada posición (i, j) guarda A[i][j] + B[i][j]. Al final imprime el resultado una fila por línea. Por ejemplo, la posición (0, 0) de la suma es 1 + 5 = 6, la (0, 1) es 2 + 6 = 8, y así con todas."