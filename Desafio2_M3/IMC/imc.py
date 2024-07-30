#resp: variable que acepta la respuesta a ingresar datos nuevamente
#W : corresponde al peso de la persona en Kg.
#H: corresponde a la altura en metros.
#IMC: EL valor del IMC, en [Kg/m2]

#tupla con los rangos de valores
#valor minimo se asumió como 0 y el maximo como indeterminado
rangos_imc = [
    (None, 18.5, "Bajo Peso"),        # Para valores menores a 18.5
    (18.5, 25, "Adecuado"),           # Para el rango [18.5, 25)
    (25, 30, "Sobrepeso"),            # Para el rango [25, 30)
    (30, 35, "Obesidad Grado I"),     # Para el rango [30, 35)
    (35, 40, "Obesidad Grado II"),    # Para el rango [35, 40)
    (40, None, "Obesidad Grado III")  # Para valores mayores a 40
]

resp='S'
while (resp=='S'):
    W=float(input('Ingrese el peso de la persona en Kg:'))
    H=float(input('Ingrese la altura en metros:'))
    #se asume como peso maximo 300kg y altura maxima 2.5 mt
    if (W>0 and W<300) or(H>0 and H<2.5) :
        IMC=(W/(H**2))
        print(F'EL valor del IMC, en [Kg/m2]: {round(IMC,2)}')
        #rutna para recuperar la descripcion del IMC calculado
        for rango in rangos_imc:
            min_val, max_val, descripcion = rango
            #print(IMC)
            # Comparar valores
            #ultimo valor de la tupla
            if min_val is None and IMC < max_val:
                print(f"IMC corresponde a {descripcion}")
                break
            if max_val is None and IMC > min_val:
                print(f"IMC corresponde a {descripcion}")
                break
            if min_val != None and max_val != None:
                if min_val < IMC <= max_val:
                    print(f"IMC corresponde a {descripcion}")
                    break
    else:
        print("los valores ingresados se encuentran fuera de los intervalos permitodos")
    resp=str.upper(input("Desea ingresar nuevos datos S/N:"))
    
    
    