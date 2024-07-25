#bibliotecas
import random

#lista  de opciones
opc = ["piedra", "papel", "tijeras"]

#resp: variable para preguntar si continua jugando
resp='S'
while (resp=='S'):
    user = input('¿Piedra, Papel o Tijeras?\n')
    user=user.lower()
    
    print(user)
    
    while (user not in opc):
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
        user = input('¿Piedra, Papel o Tijeras o C para cancelar\n')
        if str.upper(user)=="C":
            break
    #azar computador
    compu=random.choice(opc)   
    
    #jugadas
    print(f"Tu jugaste {user.capitalize()}")
    print(f"YO jugué {compu.capitalize()}") 
    
    #caso :Empate
    if (compu==user): 
        print("Empatamos!!")
    #caso: computador juega Papel
    if (compu.capitalize()=='Papel'):
        if (user.capitalize()=='Piedra'):
            print("Yo gané")
        else:
            print("Tú Ganaste")
    #caso: computador juega Piedra        
    if (compu.capitalize()=='Piedra'):
        if (user.capitalize()=='Tijeras'):
            print("Yo gané")
        else:
            print("Tú Ganaste")
    #caso: computador juega Tijeras        
    if (compu.capitalize()=='Tijeras'):
        if (user.capitalize()=='Papel'):
            print("Yo gané")
        else:
            print("Tú Ganaste")
    
    
    resp=str.upper(input("Desea Jugar nuevamente S/N:"))
    
    