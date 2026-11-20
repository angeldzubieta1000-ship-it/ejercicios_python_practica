def contar_digitos(n):
    if n < 0:
        n = -n
    if n == 0:
        return 1
    cantidad = 0
    while n > 0:
        n = n // 10
        cantidad += 1
    return cantidad

numero = int(input("Ingrese un número entero: "))
print(f"{numero} tiene {contar_digitos(numero)} dígitos")

"si el número es negativo, se vuelve positivo para no contar el signo. Si es 0, devuelve 1, porque el 0 tiene un dígito. Luego, en el ciclo, cada n // 10 le quita el último dígito y cantidad suma 1, hasta que n llega a 0. Al final devuelve cantidad. No usa listas ni convierte el número a texto."