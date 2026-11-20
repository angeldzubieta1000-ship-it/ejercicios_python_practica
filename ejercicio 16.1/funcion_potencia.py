def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

b = float(input("Base: "))
e = int(input("Exponente (entero positivo o 0): "))
print(f"{b} elevado a {e} = {potencia(b, e)}")

# resultado empieza en 1 y el ciclo lo multiplica por base tantas veces como indique exponente. Con 2 y 5 sería 1 × 2 × 2 × 2 × 2 × 2 = 32. Si el exponente es 0, el ciclo no se ejecuta y devuelve 1, que es correcto (cualquier número elevado a 0 es 1).