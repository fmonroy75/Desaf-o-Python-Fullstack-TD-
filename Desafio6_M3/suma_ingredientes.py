def agregar_ingredientes(ingredientes,lista_ingredientes, eleccion):


    if eleccion>len(lista_ingredientes):
        print('El valor no es válido, intente nuevamente')
    elif lista_ingredientes[eleccion-1] in ingredientes:
        print("El ingrediente ya ha sido ingresado")
    else:
        ingredientes.append(lista_ingredientes[eleccion-1])
        print(f'Se ha agregado {lista_ingredientes[eleccion-1]}')

    return ingredientes