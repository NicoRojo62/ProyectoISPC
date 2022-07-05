# LABORATORIO
# 
# Tiempo Estimado
# 15-20 minutos
# 
# Nivel de Dificultad
# Medio
# 
# Requisitos Previos
# LABORATORIO 4.1.3.6
# 
# Objetivos
# Familiarizar al estudiante con:
# 
# Proyectar y escribir funciones parametrizadas.
# Utilizar la instrucción return.
# Utilizar las funciones propias del estudiante.
# Escenario
# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).
# 
# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
# 
# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco acortará significativamente el código.
# 
# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else :
        return True

def days_in_month(year, month):
    leap = is_year_leap(year)
    if leap == True:
        m = [["JA",31],["FE",29],["MC",31],["AP",30],["MY",31],["JN",30],["JY",31],["AU",31],["SE",30],["OC",31],["NO",30],["DE",31]]
        return m[month-1][1]    
    else:
        m = [["JA",31],["FE",28],["MC",31],["AP",30],["MY",31],["JN",30],["JY",31],["AU",31],["SE",30],["OC",31],["NO",30],["DE",31]]
        return m[month-1][1]
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")




# Codigo mas sencillo

# def is_year_leap(year):
# 	if year % 4 != 0:
# 		return False
# 	elif year % 100 != 0:
# 		return True
# 	elif year % 400 != 0:
# 		return False
# 	else:
# 		return True
# 
# def days_in_month(year, month):
# 	# if statement
# 		# ...
# 	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	res  = days[month - 1]
# 	if month == 2 and is_year_leap(year):
# 		res = 29
# 	return res
# 
# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr,mo,"-> ",end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Fallido")
# 