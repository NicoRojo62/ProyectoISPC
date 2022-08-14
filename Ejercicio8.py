
#8) Crear una tupla en Python con el nombre de “Historial4” la cual contenga los siguientes valores:
# 7510, 7960, 76180, 800, 4100
#Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Olivia”. 
# Cree una función para determinar el valor mínimo de atención gastada en “Olivia”  mostrándolo en pantalla.



Historial4= (7510, 7960, 76180, 800, 4100)

minimo = Historial4[0]

for i in Historial4:
    if i < minimo:
        minimo = i
        
print("El minimo de atenciòn gastada por Olivia es:", minimo)
        
    
        