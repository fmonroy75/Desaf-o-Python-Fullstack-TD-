preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál es la capital de Romania?'],
    'alternativas': [['A. Berlín', 0], 
                     ['B. París', 0], 
                     ['C. Bucarest', 1], 
                     ['D. Roma', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es la capital de Canada?'],
    'alternativas': [['A. Montreal', 0], 
                     ['B. Ottawa', 1], 
                     ['C. Quebec', 0], 
                     ['D. Toronto', 0]]},
    
'pregunta_3': {'enunciado':['¿Cuál es la capital de Ucrania?'],
    'alternativas': [['A. Jarkov', 0], 
                     ['B. Kiev', 1], 
                     ['C. Lviv', 0], 
                     ['D. Korostishiv', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Qué gas es necesario para la respiración humana?'],
    'alternativas': [['A. Nitrógeno', 0], 
                     ['B. Oxígeno', 1], 
                     ['C. Dióxido de carbono', 0], 
                     ['D. Hidrógeno', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es el órgano más grande del cuerpo humano?'],
    'alternativas': [
            ['A. Hígado', 0],
            ['B. Pulmones', 0],
            ['C. Piel', 1],
            ['D. Corazón', 0]]},
    
'pregunta_3': {'enunciado':['¿Quien fue el creador de Microsoft?'],
    'alternativas': [['Steve Jobs', 0], 
                     ['Michael Witman', 0], 
                     ['Bill Gates', 1], 
                     ['Joachim Peiper', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuál es la ecuación de la relatividad?'],
    'alternativas': [
            ['A. E=mc^2', 1],
            ['B. F=ma', 0],
            ['C. a^2+b^2=c^2', 0],
            ['D. V=IR', 0]]},
    'pregunta_2': {'enunciado':['¿Quién escribió "La Odisea"?'],
    'alternativas': [ 
	    ['A. Sófocles', 0],
            ['B. Homero', 1],
            ['C. Platón', 0],
            ['D. Aristóteles', 0]]},
    
'pregunta_3': {'enunciado':['¿En qué año llegó el hombre a la luna?'],
    'alternativas': [            
	    ['A. 1965', 0],
            ['B. 1969', 1],
            ['C. 1972', 0],
            ['D. 1980', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}