l1 = [0,0,1,1,2] # Lista de valores
m = l1.count(0) # Contador de Cantidad de ceros
while l1.count(0) > 0: # Remueve todos los ceros
    l1.remove(0)
while m > 0: # ingresa al final de la lista la cantidad de ceros eliminados
    l1.append(0) # se ingresa el cero en la ultima posicion
    m -= 1  # se reduce en 1 la cantidad de ceros a agregar
print(l1)