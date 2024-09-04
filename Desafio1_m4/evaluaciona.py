from pizza import Pizza
from ingredientes import salsas_posibles
#a
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamaño)
#b
print("¿Está 'salsa de tomate' en la lista? :", Pizza.validar_ingrediente("salsa de tomate",salsas_posibles))
#c
mi_pizza = Pizza()
mi_pizza.realizar_pedido()
#d
print("Ingrediente proteico:", mi_pizza.ingr_prot)
print("Primer ingrediente vegetal:", mi_pizza.ingr_veg1)
print("Segundo ingrediente vegetal:", mi_pizza.ingr_veg2)
print("Tipo de masa:", mi_pizza.masa)
print("¿Es una pizza válida?:", mi_pizza.es_valida)
#e
print(Pizza.es_valida)