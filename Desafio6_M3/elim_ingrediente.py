def elim_ingredientes(ingredientes,lista_ingredientes, eleccion):
    
      
    if len(ingredientes) == 0:
        print('No hay ningun ingrediente que quitar')
    elif eleccion>len(lista_ingredientes):
        print('El valor no es válido, intente nuevamente')
    elif lista_ingredientes[eleccion-1] not in ingredientes:
         print('Ingrediente no se encuentra en la lista')
    elif lista_ingredientes[eleccion-1] in ingredientes:
        ingredientes.remove(lista_ingredientes[eleccion-1])
        print(f'Se ha quitado {lista_ingredientes[eleccion-1]}')
    
    
    return ingredientes