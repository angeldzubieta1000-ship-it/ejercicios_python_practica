#es par e impar

def es_par (n):
 if n%2==0:
    return True
 else:
    return False

a=int(input("ingrese un numero: "))
if es_par(a):
    print("El numero ",a, " es par")
else:
    print("El numero ",a, " es impar")

"Antes de escribir una función, di qué entra y qué sale: en es_par entra n y sale True o False.Sangría: lo que va dentro de un def, if o else se mete 4 espacios.Dentro de la función usa el parámetro (n), no variables de afuera.Los return van dentro de la función; los print, afuera.Guarda con Ctrl + S antes de ejecutar."

