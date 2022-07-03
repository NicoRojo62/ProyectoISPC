# LABORATORIO
# 
# Tiempo Estimado
# 5 minutos
# 
# Nivel de Dificultad
# Muy Fácil
# 
# Objetivos
# Familiarizarse con la función input().
# Familiarizarse con los operadores de comparación en Python.
# Escenario
# Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True si n es mayor o igual que 100.
# 
# No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos.
# 
# Datos de Prueba
# 
# Ejemplo de entrada: 55
# Resultado esperado: False 
# Ejemplo de entrada: 99 
# Resultado esperado: False 
# Ejemplo de entrada: 100 
# Resultado esperado: True 
# Ejemplo de entrada: 101 
# Resultado esperado: True 
# Ejemplo de entrada: -5 
# Resultado esperado: False 
# Ejemplo de entrada: +123 
# Resultado esperado: True

num = input()
print(int(num)>=100)