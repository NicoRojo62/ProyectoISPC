# LABORATORIO
# 
# Tiempo Estimado
# 10-15 minutos
# 
# Nivel de Dificultad
# Fácil
# 
# Objectives
# Familiarizar al estudiante con:
# 
# Utilizar la instrucción continue en los bucles.
# Reflejar situaciones de la vida real en código de computadora.
# Escenario
# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.
# 
# Se puede usar tanto con while y for.
# 
# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
# 
# Un bucle for.
# El concepto de ejecución condicional (if-elif-else).
# La sentencia continue.
# Tu programa debe:
# 
# Pedir al usuario que ingrese una palabra.
# Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
# Prueba tu programa con los datos que le proporcionamos.
# 
# 
# Datos de Prueba
# Entrada de muestra: Gregory
# 
# Salida esperada:
# 
# G
# R
# G
# R
# Y
# Entrada de muestra: abstemious
# 
# Salida esperada:
# 
# B
# S
# T
# M
# S
# Entrada de muestra: IOUEA
# 
# Salida esperada:
# 

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = input("Ingrese una palabra: ").upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U" :
        continue
    else:
        print(letter)