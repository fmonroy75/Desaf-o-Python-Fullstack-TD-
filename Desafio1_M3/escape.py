import math

radio = float(input("“Ingrese el radio en Kilómetros: \n"))
constante = float(input("“Ingrese la constante g \n"))
escape= math.sqrt(2*radio*constante)

print(f"“La velocidad de Escape es {round(escape,2)} [m/s]")