def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor

x = float(input("Primer número: "))
y = float(input("Segundo número: "))
z = float(input("Tercer número: "))
print("El mayor es:", maximo_de_tres(x, y, z))
"e asume que a es el mayor (mayor = a). Luego se compara con b: si b es más grande, pasa a ser el mayor. Después se compara con c de la misma forma. Al final return devuelve el valor que quedó en mayor. No usa listas ni max(), solo condicionales."
