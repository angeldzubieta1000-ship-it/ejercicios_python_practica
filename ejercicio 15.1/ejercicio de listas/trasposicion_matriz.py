filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

A = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"A[{i}][{j}]: ")))
    A.append(fila)

transpuesta = []
for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(A[i][j])
    transpuesta.append(fila)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)

"el programa lee la matriz y construye una nueva donde los ciclos van al revés: el de afuera recorre las columnas (j) y el de adentro las filas (i). Así, cada fila de la transpuesta se forma con los elementos de una columna de la original (A[i][j] pasa a la posición [j][i]). Si la matriz original es de 2×3, la transpuesta queda de 3×2."