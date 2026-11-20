def invertir(cadena, i=None):
    if i is None:
        i = len(cadena) - 1
    if i < 0:
        return ""
    return cadena[i] + invertir(cadena, i - 1)

def es_palindromo(cadena):
    cadena = cadena.lower()
    inversa = invertir(cadena)
    for i in range(len(cadena)):
        if cadena[i] != inversa[i]:
            return False
    return True

texto = input("Ingrese una cadena: ")
if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")

"es_palindromo pasa la cadena a minúsculas y obtiene su inversa con invertir. Luego compara carácter por carácter: si en alguna posición cadena[i] es distinto de inversa[i], devuelve False de inmediato. Si recorre todo sin diferencias, devuelve True."