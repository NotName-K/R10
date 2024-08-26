l1 = [1,2,2,3,3] # Listas de reales
l2 = [1,7,6,6,6]
m = [] # Lista que acumula valores
for x in range(len(l1)): # se agrega cada producto en su respectiva posición
 m.insert(x,l1[x]*l2[x])
print(m)