def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

"n es menor que 2 devuelve False. Luego prueba divisores desde 2 mientras i * i <= n (equivale a llegar hasta la raíz cuadrada); si alguno divide a n, devuelve False. Si no encuentra ninguno, devuelve True."
