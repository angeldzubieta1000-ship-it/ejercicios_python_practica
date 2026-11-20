n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

A = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"A[{i}][{j}]: ")))
    A.append(fila)

transpuesta = []
for j in range(m):
    fila = []
    for i in range(n):
        fila.append(A[i][j])
    transpuesta.append(fila)

print("Matriz original:")
for i in range(n):
    for j in range(m):
        print(f"{A[i][j]:>5}", end="")
    print()

print("Matriz transpuesta:")
for j in range(m):
    for i in range(n):
        print(f"{transpuesta[j][i]:>5}", end="")
    print()

"se lee la matriz de n×m con ciclos anidados. Para la transpuesta, los ciclos van al revés: el de afuera recorre las columnas (j) y el de adentro las filas (i), y cada fila nueva se forma con los elementos de una columna de la original (A[i][j] pasa a la posición [j][i]). Por eso una matriz de n×m queda de m×n, y funciona aunque no sea cuadrada. Para imprimir, :>5 alinea los números en columnas."
