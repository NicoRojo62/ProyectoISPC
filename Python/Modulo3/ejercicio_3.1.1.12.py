# LABORATORIO
# 
# Tiempo Estimado
# 10-15 minutos
# 
# Nivel de Dificultad
# Fácil/Medio
# 
# Objetivos
# Familiarizar al estudiante con:
# 
# Utilizar la sentencia if-elif-else.
# Encontrar la implementación adecuada de las reglas definidas verbalmente.
# Emplear el código de prueba empleando entradas y salidas de muestra.
# Escenario
# Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.
# 
# Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:
# 
# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.
# Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.
# 
# El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.
# 
# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.
# 
# Prueba tu código con los datos que hemos proporcionado.
# 
# Datos de Prueba
# Entrada de muestra: 2000
# Resultado esperado: Año Bisiesto
# Entrada de muestra: 2015
# Resultado esperado: Año Común
# Entrada de muestra: 1999
# Resultado esperado: Año Común
# Entrada de muestra: 1996
# Resultado esperado: Año Bisiesto
# Entrada de muestra: 1580
# Resultado esperado: No esta dentro del período del calendario Gregoriano

year = int(input("Introduce un año:"))

if(year>=1582):
    if(year%4!=0):
        print("Año Comun")
    elif(year%100!=0):
        print("Año Bisiesto")
    elif(year%400!=0):
        print("Año Comun")
    else:
        print("Año Bisiesto")
else:
    print("No esta dentro del periodo del calendario Gregoriano")