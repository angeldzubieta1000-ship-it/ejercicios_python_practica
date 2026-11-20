agenda = {}

while True:
    nombre = input("Nombre (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print("Agenda telefónica:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

"se crea un diccionario vacío y un ciclo infinito (while True) que pide el nombre. Si el usuario escribe “fin”, el break sale del ciclo. Si no, pide el teléfono y lo guarda con agenda[nombre] = telefono, donde el nombre es la clave y el teléfono el valor. Al final, .items() permite recorrer e imprimir cada pareja clave-valor. Si dos personas tienen el mismo nombre, la segunda sobrescribe a la primera, porque las claves de un diccionario no se repiten."