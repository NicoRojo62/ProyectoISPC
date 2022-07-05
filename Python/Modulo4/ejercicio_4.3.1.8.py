# Tiempo Estimado
# 20-30 minutos
# 
# Nivel de Dificultad
# Medio
# 
# Requisitos Previos
# LABORATORIO 4.1.3.6
# LABORATORIO 4.1.3.7
# 
# Objetivos
# Familiarizar al estudiante con:
# 
# Proyectar y escribir funciones con parámetros.
# Utilizar la sentencia return.
# Construir un conjunto de funciones de utilidad.
# Utilizar las funciones propias del estudiante.
# Escenario
# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
# 
# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.

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

def day_of_year(year, month, day):
    total_days = day
    month = month - 1
    while month > 0:
        total_days += days_in_month(year,month)
        month -= 1
    return total_days

print(day_of_year(2000, 12, 31))