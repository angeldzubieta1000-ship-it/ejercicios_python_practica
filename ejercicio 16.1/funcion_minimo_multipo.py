def mcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)

x = int(input("Primer número: "))
y = int(input("Segundo número: "))
print(f"MCD({x}, {y}) = {mcd(x, y)}")
print(f"MCM({x}, {y}) = {mcm(x, y)}")

#mcd: el algoritmo de Euclides repite a, b = b, a % b hasta que b sea 0. Con 12 y 18: (12, 18) → (18, 12) → (12, 6) → (6, 0). Cuando b llega a 0, a es el MCD, en este caso 6. Se usa abs para que funcione con negativos.
#mcm: aplica la fórmula |a * b| / mcd(a, b). Con 12 y 18: |12 * 18| / 6 = 216 / 6 = 36. Se usa // para que el resultado sea entero, y si alguno de los números es 0 devuelve 0 para evitar dividir entre cero.