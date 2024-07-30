#bibliotecas
from string import ascii_lowercase

#variables
password_resuelta=""
alfabeto= ascii_lowercase
print(alfabeto)
resp='S'
while (resp=='S'):
    intentos=0
    password=str.lower(input("Favor ingrese una password de caracteres en minúsculas:"))
    #ciclo lista de la password
    for letras in password:
        #ciclo para recorrer la lista alfabeto
        for letra_compara in alfabeto:
            intentos=intentos+1
            if letras==letra_compara:
                #si encuentra coincidencia sale del ciclo
                password_resuelta=password_resuelta + letra_compara
                break
                #print(letras)
    print(f"Su password es: {password_resuelta}")
    print(f"La contraseña fue forzada en {intentos} intentos")
    resp=str.upper(input("Desea realizar otra busqueda S/N:"))
print("gracias por utilizar nuestros servicios")