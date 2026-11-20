def invertir(cadena, i=None):
    if i is None:
        i = len(cadena) - 1
    if i < 0:
        return ""
    return cadena[i] + invertir(cadena, i - 1)

texto = input("Ingrese una cadena: ")
print("Invertida:", invertir(texto))

#"la función empieza por la última posición (i = len(cadena) - 1) y va hacia atrás. Si i < 0, ya recorrió toda la cadena y devuelve "" (caso base). Si no, toma el carácter cadena[i] y le suma el resultado de llamarse con i - 1. Con “hola” sería "a" + "l" + "o" + "h" + "", que da "aloh". No usa slicing, solo índices simples."