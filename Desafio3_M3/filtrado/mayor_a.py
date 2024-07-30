ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}


resp='S'
while (resp=='S'):
    #lista de filtrado
    filtrado={}

    monto_buscado=int(input("Favor ingrese el monto minimo a buscar:"))

    #ciclo para recorrer la lista
    for pos_lista in ventas:
        if ventas[pos_lista]>monto_buscado:
            filtrado[pos_lista]=ventas[pos_lista]

    print(f"Los datos mayores a {monto_buscado} son los siguientes")
    print(filtrado) # mostramos el resultado
    resp=str.upper(input("Desea realizar otra busqueda S/N:"))
print("gracias por utilizar nuestros servicios")