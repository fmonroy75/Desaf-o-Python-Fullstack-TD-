import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    if dificultad == 'basicas':
        preguntas = p.preguntas_basicas
    elif dificultad == 'intermedias':
        preguntas = p.preguntas_intermedias
    elif dificultad == 'avanzadas':
        preguntas = p.preguntas_avanzadas
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    random.shuffle(opciones[dificultad])
    # n_elegido = recoge la primera opcion ya randonmizada
    # siempre existira un número en el indice 0
    n_elegido = opciones[dificultad][0]
    
    # eliminarla del ambiente global para no escogerla de nuevo
    # opciones['basicas'].remove(2) EJEMPLO
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    # 'pregunta_' + '2' -> 'pregunta_2'
    pregunta = preguntas['pregunta_'+ str(n_elegido)]
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')