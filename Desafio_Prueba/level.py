def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if p_level == 2:
        if n_pregunta in [1, 2]:
            return 'básica'
        elif n_pregunta in [3, 4]:
            return 'intermedia'
        else:
            return 'avanzada'
    elif p_level == 3:
        if n_pregunta in [1, 2, 3]:
            return 'básica'
        elif n_pregunta in [4, 5, 6]:
            return 'intermedia'
        else:
            return 'avanzada'
    
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias