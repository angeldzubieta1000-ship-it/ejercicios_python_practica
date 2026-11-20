n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

A = []
for i in range(n):
    fila = []
    for j in range(m):
        valido = False
        while not valido:
            texto = input(f"A[{i}][{j}]: ").strip()
            prueba = texto
            if prueba.startswith("-"):
                prueba = prueba[1:]
            if prueba.replace(".", "", 1).isdecimal():
                valido = True
            else:
                print("Error: ingrese un valor numérico.")
        fila.append(float(texto) + 0.0)
    A.append(fila)

valido = False
while not valido:
    texto = input("Escalar: ").strip()
    prueba = texto
    if prueba.startswith("-"):
        prueba = prueba[1:]
    if prueba.replace(".", "", 1).isdecimal():
        valido = True
    else:
        print("Error: ingrese un valor numérico.")
escalar = float(texto)

resultado = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(A[i][j] * escalar + 0.0)
    resultado.append(fila)

print("Matriz original:")
for i in range(n):
    for j in range(m):
        print(f"{A[i][j]:>8.2f}", end="")
    print()

print(f"Matriz multiplicada por {escalar}:")
for i in range(n):
    for j in range(m):
        print(f"{resultado[i][j]:>8.2f}", end="")
    print()

"Se leen n y m y se llena la matriz con dos ciclos anidados, validando cada dato como número (si no lo es, muestra error y lo vuelve a pedir). El escalar se pide y valida igual. Luego se crea una matriz nueva donde cada posición guarda A[i][j] * escalar, y se imprimen la original y la resultante con las columnas alineadas."