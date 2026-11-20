n = int(input("Ingresa el tamaño n de la matriz: "))

identidad = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    identidad.append(fila)

for fila in identidad:
    print(fila)

"Una matriz identidad es una matriz cuadrada con 1 en la diagonal principal y 0 en el resto. El programa pide un número n y, con dos ciclos anidados (uno para filas y otro para columnas), agrega un 1 cuando la fila es igual a la columna y un 0 en los demás casos. Al final imprime la matriz una fila por línea."
