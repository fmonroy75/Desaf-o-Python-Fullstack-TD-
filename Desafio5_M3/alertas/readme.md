# Actividad 1 - Filtrado relevante
Dada una muestra de los productos que actualmente se encuentran disponibles
en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
siguiente:
<ul><li>
Un diccionario con los productos que cumplen una cierta condición dado un umbral</li>
<li>La función debe permitir mostrar los valores mayor que o menor que un umbral
(siempre estrictos).</li>
<li>Por defecto la función debe siempre mostrar los valores mayor que el umbral a
menos que se indique lo contrario.</li></ul>

Para desarrollar la funcionalidad se le entrega a usted un diccionario de prueba para verificar
sus resultados.
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

Se espera ejecutar el programa de la siguiente manera:
● Si se especifica un argumento, este debe ser el umbral y por defecto debe calcular
los que son estrictamente mayores al umbral.

python filtro.py 30000

Los productos mayores al umbral son: Notebook, Monitor, Escritorio,Tarjeta de Video

● En caso de que se ingresen dos valores, el primero seguirá siendo el umbral,
mientras el segundo podrá tomar los valores mayor o menor. Por ejemplo, el
siguiente código calculará los que son estrictamente menores.

python filtro.py 30000 menor

Los productos menores al umbral son: Teclado, Mouse

En caso que otro elemento se utilice se debe devolver lo siguiente:

python filtro.py 30000 otro

Lo sentimos, no es una operación válida


## Prerrequisitos o Dependencias
Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

Sistema Operativo  Windows 10, linux, Mac
Lenguaje de programación Python 3.12.4

## Instrucciones para Ejecutar el Proyecto
python filtro.py 30000
python filtro.py 30000 menor
python filtro.py 30000 otro

## Autor
Francisco Monroy