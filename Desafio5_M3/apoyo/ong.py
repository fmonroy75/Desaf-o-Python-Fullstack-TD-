#modo de ejecucion por terminal
#python ong.py "fact_1 = 5; prod_1 = [3,6,4,2,8]; fact_2 = 6"


import sys
i=0

#funcion calculo factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#funcion calculo del producto de una lista    
def producto(arr):
    result = 1
    for num in arr:
#        print(num)
        result *= num
    return result    



# Función de control de operaciones
def calcular(**kwargs):
    resultados = {}
    for clave, valor in kwargs.items():
        if clave.startswith('fact_'):
            resultados[clave] = factorial(valor)
            print(f"El factorial de {resultados[clave]} es {factorial(valor)}")
        elif clave.startswith('prod_'):
            resultados[clave] = producto(valor)
            print(f"La productoria de {resultados[clave]} es {producto(valor)}")
        else:
            raise ValueError(f"Operación no reconocida: {clave}")
    return 


if len(sys.argv)>1:
    sys.argv.pop(0)

    print(sys.argv[0])



     # Procesar argumentos manualmente
    argumentos = {}
    arr_aux=sys.argv[0].split(';')
    for arg in arr_aux:
        clave, valor = arg.split('=')
        clave = clave.strip()
        #print(valor)
        # Determinar si el valor es un entero o una lista
        if "[" in valor and "]" in valor:
            valor=eval(valor)
        else:
            valor = int(valor.strip())
        argumentos[clave] = valor
    print("por argumentos")

    #print(sys.argv[0])
    #print(argumentos)
    calcular(**argumentos)
    
else:

    print("ejecucion desde script")
    calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

#for operatorias in sys.argv:
#    if i>0:  
#        if "fact" in operatorias:
#            arr_calculo=operatorias.split("=")
#            print(f"El factorial de {arr_calculo[1]} es {factorial(int(arr_calculo[1]))}")
#        if "prod" in operatorias:
#            arr_calculo=operatorias.split("=")
#            print(f"La productoria de {arr_calculo[1]} es {producto(eval(arr_calculo[1]))}")
#    i=i+1


#calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
#lista_num = [int(num.strip()) for num in lista_str.split(',') if num.strip()]
