preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál es la capital de Romania?'],
    'alternativas': [['Bucarest', 1],
                     ['Berlín', 0], 
                     ['París', 0], 
                     ['Roma', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es la capital de Canada?'],
    'alternativas': [['Montreal', 0], 
                     ['Quebec', 0], 
                     ['Ottawa', 1],
                     ['Toronto', 0]]},
    
'pregunta_3': {'enunciado':['¿Cuál es la capital de Ucrania?'],
    'alternativas': [['Jarkov', 0], 
                     ['Kiev', 1], 
                     ['Lviv', 0], 
                     ['Korostishiv', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Qué gas es necesario para la respiración humana?'],
    'alternativas': [['Nitrógeno', 0], 
                     ['Oxígeno', 1], 
                     ['Dióxido de carbono', 0], 
                     ['Hidrógeno', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es el órgano más grande del cuerpo humano?'],
    'alternativas': [
            ['Hígado', 0],
            ['Pulmones', 0],
            ['Piel', 1],
            ['Corazón', 0]]},
    
'pregunta_3': {'enunciado':['¿Quien fue el creador de Microsoft?'],
    'alternativas': [['Steve Jobs', 0], 
                     ['Michael Witman', 0], 
                     ['Joachim Peiper', 0],
                     ['Bill Gates', 1]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuál es la ecuación de la relatividad?'],
    'alternativas': [
            ['E=mc^2', 1],
            ['F=ma', 0],
            ['a^2+b^2=c^2', 0],
            ['V=IR', 0]]},
    'pregunta_2': {'enunciado':['¿Quién escribió "La Odisea"?'],
    'alternativas': [ 
	    ['Sófocles', 0],
            ['Homero', 1],
            ['Platón', 0],
            ['Aristóteles', 0]]},
    
'pregunta_3': {'enunciado':['¿En qué año llegó el hombre a la luna?'],
    'alternativas': [            
	    ['1965', 0],
            ['1969', 1],
            ['1972', 0],
            ['1980', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}