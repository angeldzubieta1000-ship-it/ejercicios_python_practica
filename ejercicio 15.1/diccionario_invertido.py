original = {"a": 1, "b": 2, "c": 3}

invertido = {v: k for k, v in original.items()}

print("Original:", original)
print("Invertido:", invertido)


#"original.items() entrega cada pareja (k, v), y la comprensión construye un diccionario nuevo poniendo el valor v como clave y la clave k como valor. Es decir, cada pareja clave → valor pasa a ser valor → clave.Un detalle importante: los valores originales deben ser únicos y no modificables (como números o textos). Si dos claves tienen el mismo valor, el segundo sobrescribe al primero, porque las claves de un diccionario no se pueden repetir. Por ejemplo, {"a": 1, "b": 1} se invierte a {1: 'b'}.Variables: original, invertido, k y v (o clave y valor)."

#cantidad = int(input("¿Cuántos pares clave-valor? "))

#original = {}
#for i in range(cantidad):
    #clave = input("Clave: ")
    #valor = input("Valor: ")
    #original[clave] = valor

#invertido = {v: k for k, v in original.items()}

#print("Invertido:", invertido)