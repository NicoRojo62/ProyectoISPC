historial5 = (8520, 9510, 7530, 3570, 1590) #se declara la tupla
montomax = historial5[0] #igualo variable montomax a tupla posición 0
for var in historial5[1:]: #bucle para revisar la tupla desde posición 1 al final
    if var > montomax:
        montomax = var
        
print("el monto máximo gastado en Toto es:", montomax, "pesos")