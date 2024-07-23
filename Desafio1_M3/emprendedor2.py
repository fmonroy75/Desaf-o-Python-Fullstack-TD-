import math

precioSuscripcion = float(input("“Ingrese el precio por Suscripción: \n"))
numUsuariosN = float(input("“Ingrese el número total de usuarios Normales\n"))
numUsuariosP = float(input("“Ingrese el número total de usuarios Premium\n"))
gastosTotales = float(input("“Ingrese los Gastos Totales \n"))
utilidad= (precioSuscripcion*numUsuariosN-gastosTotales) + (precioSuscripcion*1.5*numUsuariosP-gastosTotales)

print(f"“El valor de utilidad es {round(utilidad,2)} ")