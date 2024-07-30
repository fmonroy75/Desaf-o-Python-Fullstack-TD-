 
            
# Inicialización de variables
respira = ""
Llego_ambulancia = "N"

# Solicitud de entrada del usuario para verificar si responde a estímulos
responde_estimulos = input("Responde a Estimulos S/N: ")

# Verificar la respuesta del usuario
if responde_estimulos.upper() == "S":
    print("Valorar necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir vía aérea")
    
    # Solicitud de entrada del usuario para verificar si respira
    respira = input("Respira S/N? ")

    if respira.upper() == "S":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        
        # Bucle para esperar la llegada de la ambulancia
        while Llego_ambulancia.upper() == "N":
            signos_de_vida = input("Tiene signos vitales S/N? ")

            if signos_de_vida.upper() == "S":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            
            # Actualizar el estado de la llegada de la ambulancia
            Llego_ambulancia = input("Llegó ambulancia S/N? ")