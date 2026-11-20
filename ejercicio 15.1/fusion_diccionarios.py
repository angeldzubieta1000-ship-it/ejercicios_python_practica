def pedir_diccionario(nombre):
    cantidad = int(input(f"¿Cuántos pares tendrá {nombre}? "))
    dic = {}
    for i in range(cantidad):
        clave = input("Clave: ")
        valor = input("Valor: ")
        dic[clave] = valor
    return dic

dic1 = pedir_diccionario("el diccionario 1")
dic2 = pedir_diccionario("el diccionario 2")

combinado = dic1.copy()
combinado.update(dic2)

print("Dic1:", dic1)
print("Dic2:", dic2)
print("Combinado:", combinado)

"la función pedir_diccionario se escribe una sola vez y sirve para armar cualquiera de los dos diccionarios, así no repites el mismo ciclo dos veces. Recibe un texto (nombre) solo para mostrar a cuál diccionario se le están pidiendo los datos, crea un diccionario vacío, lo llena con los pares que ingresa el usuario y lo devuelve con return. Luego se llama dos veces y se combinan con update().Si tu profesor pide el operador |, cambia las dos líneas de combinado por:"