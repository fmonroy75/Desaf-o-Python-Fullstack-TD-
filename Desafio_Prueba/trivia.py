import validador


print("***************************************")
print("¡Bienvenido a la Trivia Interactiva 2P!")
print("***************************************")

n_preguntas_por_nivel = int(validador.validate([ '2', '3','4'], input("¿Cuántas preguntas por nivel deseas (2, 3 o 4)? ")))
    
n_pregunta = 1
total_preguntas = n_preguntas_por_nivel * 3  # 3 niveles
while n_pregunta <= total_preguntas:
    nivel = choose_level(n_pregunta, n_preguntas_por_nivel)
    enunciado, alternativas = choose_q(nivel)
    alternativas_mezcladas = shuffle_alt({'enunciado': enunciado, 'alternativas': alternativas})
       
    print_pregunta(enunciado, alternativas_mezcladas)
        
    eleccion_usuario = validate(['A', 'B', 'C', 'D'], input("Elige una alternativa: "))
    eleccion_idx = ['A', 'B', 'C', 'D'].index(eleccion_usuario)
        
    if verificar(alternativas_mezcladas, eleccion_idx):
        print("¡Respuesta correcta!\n")
    else:
        print("¡Respuesta incorrecta!\n")
        print("Juego terminado. Mejor suerte la próxima vez.")    
        
    n_pregunta = n_pregunta + 1
    
print(" ****** ¡Felicidades! Has respondido todas las preguntas correctamente. ******")