
from ingredientes import vegetales_posibles, proteicos_posibles, masas_posibles

def __init__(self):
    self.ingrediente_proteico = None
    self.ingrediente_vegetal_1 = None
    self.ingrediente_vegetal_2 = None
    self.masa = None
    self.es_valida = False

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "Familiar"
    
    @staticmethod
    def validar_ingrediente(ingrediente, opciones):
        return ingrediente in opciones
    
    def realizar_pedido(self):
        self.ingr_prot = input("Ingrese el ingrediente proteico: ")
        self.ingr_veg1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingr_veg2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.masa = input("Ingrese el tipo de masa: ")
        
        if self.validar_ingrediente(self.ingr_prot, proteicos_posibles) and self.validar_ingrediente(self.ingr_veg1, vegetales_posibles) and self.validar_ingrediente(self.ingr_veg2, vegetales_posibles) and  self.validar_ingrediente(self.masa, masas_posibles):
            self.es_valida = True
        else:
            self.es_valida = False
        
        