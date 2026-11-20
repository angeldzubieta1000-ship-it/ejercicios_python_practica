frase = input("Ingresa una frase: ")

palabras = frase.lower().split()

frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")

"Explicación resumida: .lower() pasa todo a minúsculas para que “Hola” y “hola” cuenten como la misma palabra, y .split() separa la frase en una lista de palabras. Luego se recorre esa lista: si la palabra ya está en el diccionario, se le suma 1 a su contador; si no está, se agrega con valor 1. Al final se imprime cada palabra con su frecuencia.Versión más corta usando .get():"