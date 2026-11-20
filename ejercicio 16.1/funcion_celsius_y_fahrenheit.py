def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32

celsius = float(input("Temperatura en °C: "))
print(f"{celsius} °C equivalen a {celsius_fahrenheit(celsius)} °F")

"la función recibe c, aplica la fórmula F = (C × 9/5) + 32 y devuelve el resultado con return. Fuera de la función solo se pide el dato y se imprime. Se usa float para aceptar decimales, como 36.5 °C."
