import sys

with open(sys.argv[1]) as file:
    texto=file.read()
    #caracteres distintos
    caract_distintos = len(set(texto))
        
    #elimina "," del texto
    texto=texto.replace(","," ")
    #elimina "." del texto
    texto=texto.replace(".","")

    #separando palabras
    #arreglo_texto = list(set(arreglo_texto))
    arreglo_texto=texto.split(" ")
    palabras_distintas=len(set(arreglo_texto))
    
    print(f"El número de caracteres distintos es: {caract_distintos}")
    arreglo_texto = list(set(arreglo_texto))
    print(f"El número de palabras distintas es: {palabras_distintas}")
    
    