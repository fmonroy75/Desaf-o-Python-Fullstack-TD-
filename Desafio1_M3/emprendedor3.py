import math

precioSuscripcion = float(input("“Ingrese el precio por Suscripción: \n"))
numUsuarios = float(input("“Ingrese el número total de usuarios Normales \n"))
gastosTotales = float(input("“Ingrese los Gastos Totales \n"))
print("Para poder calcular la razón de utilidad con respecto al año anterior. La utilidad del año anterior debe ser mayor a 0")
utilidadanterior = float(input("“Ingrese la Utilidad del año anterior \n"))

utilidad= precioSuscripcion*numUsuarios-gastosTotales
razon=utilidad/utilidadanterior

print(f"“El valor de utilidad actual es {round(utilidad,2)} ")
print(f"“La razon de utilidad es {round(razon,2)} ")