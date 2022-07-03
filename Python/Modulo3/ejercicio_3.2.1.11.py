# LABORATORIO
# 
# Tiempo Estimado
# 5-10 minutos
# 
# Nivel de Dificultad
# Fácil
# 
# Objetivos
# Familiarizar al estudiante con:
# 
# Utilizar la instrucción continue en los bucles.
# Modificar y actualizar el código existente.
# Reflejar situaciones de la vida real en código de computadora.
# Escenario
# Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior (3.1.2.10) y crear un mejor devorador de vocales (bonito) mejorado! Escribe un programa que use:
# 
# Un bucle for.
# El concepto de ejecución condicional (if-elif-else).
# La instrucción continue.
# Tu programa debe:
# 
# Pedir al usuario que ingrese una palabra.
# Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
# Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.
# 
# Prueba tu programa con los datos que le proporcionamos.
# 
# 
# Datos de Prueba
# Entrada de muestra: Gregory
# 
# Salida esperada:
# 
# GRGRY
# Entrada de muestra: abstemious
# 
# Salida esperada:
# 
# BSTMS
# Entrada de muestra: IOUEA
# 
# Salida esperada:

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingrese una palabra: ").upper()

for letter in user_word:
   # Completa el cuerpo del bucle.
   if letter == "A":
       continue
   elif letter == "E":
       continue
   elif letter == "I":
       continue
   elif letter == "O":
       continue
   elif letter == "U":
       continue
   else:
       word_without_vowels += letter
print(word_without_vowels)