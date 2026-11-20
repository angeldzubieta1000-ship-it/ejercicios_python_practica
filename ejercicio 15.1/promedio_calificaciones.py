cantidad = int(input("¿Cuántos estudiantes vas a ingresar? "))

notas = {}
for i in range(cantidad):
    nombre = input("Nombre del estudiante: ")
    nota = float(input(f"Nota de {nombre}: "))
    notas[nombre] = nota

promedio = sum(notas.values()) / len(notas)

print("Notas registradas:")
for nombre, nota in notas.items():
    print(f"{nombre}: {nota}")

print(f"Promedio general: {promedio:.2f}")

"se pide cuántos estudiantes habrá y, con un ciclo for, se guarda cada nombre como clave y su nota como valor (con float para aceptar decimales). Luego notas.values() da solo las notas, sum() las suma y len(notas) cuenta cuántos estudiantes hay, así que sum() / len() es el promedio. El :.2f muestra el resultado con 2 decimales. Variables: cantidad, notas (diccionario), nombre, nota y promedio."

#TIP Si prefieres terminar con “fin” como en el ejercicio de la agenda, puedes cambiar el for por un while True que pare cuando el nombre sea “fin”.