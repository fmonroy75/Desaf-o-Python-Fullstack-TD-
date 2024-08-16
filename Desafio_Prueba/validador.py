
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    while True:
        es_valida = False
        for opcion in opciones:
            if eleccion == opcion:
                es_valida = True
                break
        
        if es_valida:
            break
        else:
            print(f'---->Opción no válida, ingrese una de las opciones válidas: {opciones}')
            eleccion = input("Ingresa una opción: ")
    
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
