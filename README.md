# Arreglos 
## Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
reales1 = [1, 2, 3, 4, 5]
m : int =  0
for i in reales1:
   m += i
print(m / len(reales1))
```
## Producto Punto de dos arreglos de reales
```python
l1 = [1,2,2,3,3]
l2 = [1,7,6,6,6]
m : int = 0
for x in range(0,len(l1)):
 m += l1[x]*l2[x]
 x += 1
print(m)
```
## Ceros que aparezcan en un arreglo.
```python
l1 = [0,0,1,1,2,0]
m = l1.count(0)
while l1.count(0) > 0:
    l1.remove(0)
while m > 0:
    l1.insert(len(l1), 0)
    m -= 1      
print(l1)
```
