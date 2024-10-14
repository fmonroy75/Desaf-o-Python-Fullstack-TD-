from django.shortcuts import render

# Lista de empleados
empleados = [
    'Santiago Posteguillo',
    'Massimo Manfredi',
    'Michael Witman',
    'Joachim Peiper',
    'Kurt Meyer'
]

def mostrar_lista(request):
    return render(request, "empleados.html", {'empleados':empleados})

# Create your views here.
