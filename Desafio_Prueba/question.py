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
    #escoger preguntas por dificultad
    preguntas = list(p.pool_preguntas[dificultad].keys())
    
    # usar opciones desde ambiente global
    #global ----------------------------------->>>> no se entiende 
    # escoger una pregunta
    n_elegido = random.choice(preguntas)
    # eliminarla del ambiente global para no escogerla de nuevo
    pregunta = p.pool_preguntas[dificultad].pop(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = pregunta['enunciado']
    alternativas = pregunta['alternativas']
    
    
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