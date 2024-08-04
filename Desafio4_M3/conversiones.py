import sys

monedas = {
"Sol peruano:": 0,
"Peso Argentino:": 0,
"Dólar Americano:": 0
}
try:
    i=1
    for clave, valor in monedas.items():
        monedas[clave]=float(sys.argv[4])*float(sys.argv[i])
        i=i+1
    print(f"Los {int(sys.argv[4])} pesos equivalen a:")    
    for clave, valor in monedas.items():
        print(f'{valor}: {clave}')
except:
    print("Favor ingrese valores numéricos válidos.")
