recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

opc=0
while opc!=5:
    print("1.-Agregar a la lista")
    print("2.-Modificar lista")
    print("3.-Eliminar de la lista")
    print("4.-Listar de la lista")
    print("5.-Salir")
    
    opc=int(input("ingrese opcion:"))
    #ingresar nuevo elemento    
    if (opc==1):
        arr_entrada=[]
        print("*****************************************")
        print("Ingreso de datos")
        print("*****************************************")        
        fecha=input("ingrese Fecha (YYYY-MM-DD):")
        arr_entrada.append(fecha)
        hora=input("ingrese Hora (HH:MM):")
        arr_entrada.append(hora)
        motivo=input("ingrese Motivo:")
        arr_entrada.append(motivo)
        recordatorios.append(arr_entrada)

    #eliminar elemento    
    if (opc==2):
        arr_busca=[]
        print("*****************************************")
        print("Modificar elemento de la lista")
        print("*****************************************")        
        indice=int(input("ingrese clave del elemento que desea Modificar:"))
        print(f"Clave : {indice}")
        arr_busca=recordatorios[indice]
        print(f"Fecha : {arr_busca[0]}")
        print(f"Hora : {arr_busca[1]}")
        print(f"Motivo : {arr_busca[2]}")
        seg=input("Esta seguro que desea Modoficar este elemento S/N:")
        if seg.upper()=='S':
            arr_entrada=[]
            fecha=input("ingrese Fecha (YYYY-MM-DD):")
            recordatorios[indice][0]=fecha
            hora=input("ingrese Hora (HH:MM):")
            recordatorios[indice][1]=hora
            motivo=input("ingrese Motivo:")
            recordatorios[indice][2]=fecha


        
    #eliminar elemento    
    if (opc==3):
        arr_busca=[]
        print("*****************************************")
        print("Eliminar elemento de la lista")
        print("*****************************************")        
        indice=int(input("ingrese clave del elemento que desea eliminar:"))
        print(f"Clave : {indice}")
        arr_busca=recordatorios[indice]
        print(f"Fecha : {arr_busca[0]}")
        print(f"Hora : {arr_busca[1]}")
        print(f"Motivo : {arr_busca[2]}")
        seg=input("Esta seguro que desea eliminar este elemento S/N:")
        if seg.upper()=='S':
            recordatorios.pop(indice)
        
        
    
    #Mostrar todos los elementos
    if (opc==4):
        print("*****************************************")
        print("Listado de datos")
        print("*****************************************")    
        for i in range(len(recordatorios)):
            print(f"Clave : {i}")
            print(f"Fecha : {recordatorios[i][0]}")
            print(f"Hora : {recordatorios[i][1]}")
            print(f"Motivo : {recordatorios[i][2]}")
            print("*****************************************")
            carac=input("Presione ENTER tecla para continuar")
            print("*****************************************")
        #for elemento in recordatorios:
        #    print(f"Clave : {recordatorios.index}")
        #    print(f"Fecha : {elemento[0]}")
        #    print(f"Hora : {elemento[1]}")
        #    print(f"Motivo : {elemento[2]}")
        #    print("***************************************")
        #    carac=input("Presione ENTER tecla para continuar")
        #    print("***************************************")
    #salir
    if(opc==5):
        break
            