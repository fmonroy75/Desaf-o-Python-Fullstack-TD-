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




for operatorias in sys.argv:
    if i>0:  
        if "fact" in operatorias:
            arr_calculo=operatorias.split("=")
            print(f"El factorial de {arr_calculo[1]} es {factorial(int(arr_calculo[1]))}")
        if "prod" in operatorias:
            arr_calculo=operatorias.split("=")
            print(f"La productoria de {arr_calculo[1]} es {producto(eval(arr_calculo[1]))}")
    i=i+1


#calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
#lista_num = [int(num.strip()) for num in lista_str.split(',') if num.strip()]
