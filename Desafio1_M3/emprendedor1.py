import math

precioSuscripcion = float(input("“Ingrese el precio por Suscripción: \n"))
numUsuarios = float(input("“Ingrese el número total de usuarios \n"))
gastosTotales = float(input("“Ingrese los Gastos Totales \n"))
utilidad= precioSuscripcion*numUsuarios-gastosTotales

print(f"“El valor de utilidad es {round(utilidad,2)} ")