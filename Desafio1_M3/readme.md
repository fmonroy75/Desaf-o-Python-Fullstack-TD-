#Ejercicio 1 Modulo3

Desarrolla las actividades 1 y 2, según los requerimientos solicitados a continuación:

## Actividad 1 - Velocidad de escape
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉𝑒 = sqr(2𝑔𝑟)

Ve : corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s2].
r: Corresponde al radio del planeta en [m].


## Actividad 2 - Rentabilidad
Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
del proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
Para ello, se te pide desarrollar este cálculo en tres versiones.

### Requerimientos
#### Actividad 1 - Velocidad de escape
1. Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().

2. El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.

Ejemplo:
“Ingrese el radio en Kilómetros:”,
“Ingrese la constante g: ”
La respuesta del programa también debe mostrarse con un texto apropiado:
Ejemplo:
“La velocidad de Escape es 11174.6 [m/s]”

<ul><li>
 Para verificar el correcto funcionamiento del programa, se puede verificar con
los siguientes datos:
○ g = 9.8 [m/s2]
○ r = 6371 [Km]
</li><li>

 Se obtiene como resultado:
○ Velocidad de Escape = 11174.6 [m/s]
</li></ul>

#### Actividad 2 - Rentabilidad
1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.

2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.

3. Considera ahora una tercera versión llamada emprendedor3.py. Necesitarás la
fórmula original de utilidades
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Ahora, debes crear una nueva función en la que se pida (por medio de input()) los
siguientes datos:
● precio de suscripción P
● número de usuarios normales U
● gastos GT
● utilidades del año anterior Uanterior
El programa debe calcular las utilidades actuales Uactuales y mostrar la razón entre las
utilidades actuales y las del año anterior
𝑅𝑎𝑧ó𝑛 =𝑈𝑎𝑐𝑡𝑢𝑎𝑙𝑒𝑠/𝑈𝑎𝑛𝑡𝑒𝑟𝑖𝑜𝑟
El resultado debe estar redondeado a dos decimales.