#resp: variable que acepta la respuesta a ingresar datos nuevamente
#W : corresponde al peso de la persona en Kg.
#H: corresponde a la altura en metros.
#IMC: EL valor del IMC, en [Kg/m2]


resp='S'
while (resp=='S'):
    W=float(input('Ingrese el peso de la persona en Kg:'))
    H=float(input('Ingrese la altura en metros:'))
    
    IMC=(W/(H**2))
    print(F'EL valor del IMC, en [Kg/m2]: {IMC}')
    resp=str.upper(input("Desea ingresar nuevos datos S/N:"))
    