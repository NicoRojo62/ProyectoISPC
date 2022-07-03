# LABORATORIO
# 
# Tiempo Estimado
# 5-10 minutos
# 
# Nivel de Dificultad
# Fácil
# 
# Objetivos
# Familiarizarse con la función input().
# Familiarizarse con los operadores de comparación en Python.
# Familiarizarse con el concepto de ejecución condicional.
# Escenario
# Espatifilo, más comúnmente conocida como la planta de cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.
# 
# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grita involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"
# 
# 
# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
# 
# Imprima el enunciado "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO".
# Imprima "No, ¡quiero un gran ESPATIFILIO!" si la cadena ingresada es "espatifilo".
# Imprima "¡ESPATIFILIO!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
# 
# Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un ESPATIFILIO también!
# 
# 
# Datos de Prueba
# Entrada de muestra: espatifilo
# Resultado esperado: No, ¡quiero un gran ESPATIFILIO!
# Entrada de ejemplo: pelargonio
# Resultado esperado: !ESPATIFILIO!, ¡No pelargonio!
# Entrada de muestra: ESPATIFILIO
# Resultado esperado: Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!

plant = input()
if(plant == "ESPATIFILIO"):
    print("Si, ¡EL ESPATIFILIO! es la mejor planta")
elif(plant == "espatifilio"):
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO! , ¡No ",plant,"!")