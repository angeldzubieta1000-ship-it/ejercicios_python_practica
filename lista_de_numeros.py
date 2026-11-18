numeros = [1,8,4,5,12,16,20,24]

suma = 90
cantidad = 8

promedio = suma / cantidad

mayores = []

for numero in numeros:
 if numero > promedio:
    mayores.append(numero)
    

print("El promedio es:", promedio)
print("Mayores que el promedio:", mayores)


# Esto es para encontrar un par a un promedio
# if numero % 2 == 0:
#    print(numero)


# Contar cuantos son mayores que el promedio
# contador = 0

# for numero in numeros:
 #   if numero > promedio:
  #      contador += 1