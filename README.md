# Arreglos 
## Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
reales1 = [1, 2, 3, 4, 5] # Lista de Reales
m : int =  0 # Valor para acumular suma de valores
for i in reales1: # se suman todos los valores de la lista
   m += i 
k = m / len(reales1) # la suma de los valores se dividie entre la cantidad de valores de la lista
print(k)
```
## Producto Punto de dos arreglos de reales
```python
l1 = [1,2,2,3,3] # Listas de reales
l2 = [1,7,6,6,6]
m = [] # Lista que acumula valores
for x in range(len(l1)): # se agrega cada producto en su respectiva posición
 m.insert(x,l1[x]*l2[x])
print(m)
```
## Agregar ceros que aparezcan en un arreglo al final de la lista
```python
l1 = [0,0,1,1,2] # Lista de valores
m = l1.count(0) # Contador de Cantidad de ceros
while l1.count(0) > 0: # Remueve todos los ceros
    l1.remove(0)
while m > 0: # ingresa al final de la lista la cantidad de ceros eliminados
    l1.append(0) # se ingresa el cero en la ultima posicion
    m -= 1  # se reduce en 1 la cantidad de ceros a agregar
print(l1)
```
