import sys
monto_buscado = int(sys.argv[1])
if len(sys.argv)== 3 and str.lower(sys.argv[2])=="menor":
    condicion = "menores o igual"
    flag_condicion=1
elif len(sys.argv)== 2 :
    condicion="mayores"
    flag_condicion=0
else:
    print("Lo sentimos, no es una operación válida")
    exit()
    
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}
filtrado=[]

    #ciclo para recorrer la lista  
for clave,valor in precios.items():
    if valor>monto_buscado and flag_condicion==0:
        filtrado.append(clave)
    elif valor<=monto_buscado and flag_condicion==1:
        filtrado.append(clave)



print(f"Los productos {condicion} al umbral son: {', '.join(filtrado)} ")
print("gracias por utilizar nuestros servicios")