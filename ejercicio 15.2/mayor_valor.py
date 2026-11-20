n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

A = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"A[{i}][{j}]: ")))
    A.append(fila)

maximo = A[0][0]
pos_fila = 0
pos_columna = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > maximo:
            maximo = A[i][j]
            pos_fila = i
            pos_columna = j

print("Matriz:")
for i in range(n):
    for j in range(m):
        print(f"{A[i][j]:>5}", end="")
    print()

print("Valor máximo:", maximo)
print(f"Posición: fila {pos_fila}, columna {pos_columna}")

"se lee la matriz y se toma A[0][0] como máximo inicial, con su posición (0, 0). Al recorrer todos los elementos, si uno es mayor que el máximo actual, se actualizan el valor y la posición. Como se usa > y no >=, los repetidos no reemplazan al primero. Al final se imprime la matriz, el máximo y su posición."
