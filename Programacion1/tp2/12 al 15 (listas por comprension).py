#Ejercicio 12: Utilizar la técnica de listas por comprensión para construir una lista con todos los
#números impares comprendidos entre 100 y 200.

lista=[i for i in range(100,200) if i%2!=0]
print(lista)

#13. Escribir un programa para generar una lista con los múltiplos
#de 7 que no sean múltiplos de 5, entre 2000 y 3500.
#Imprimir la lista obtenida.

lista=[]
for i in range(2000,3500):
    if i%7==0 and i%5!=0:
        lista.append(i)
print(lista)

#14.Repetir el ejercicio anterior,
#pero utilizando la técnica de listas por comprensión.

lista=[i for i in range(2000,3500) if i%7==0 and i%5!=0]
print(lista)


#15.Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
#los elementos de la primera que sean impares. El proceso deberá realizarse utilizando
#listas por comprensión. Imprimir las dos listas por pantalla.


#Ejercicio 15
import random

n=random.randint(0,15)
lista=[]
for i in range(n):
    lista.append(random.randint(0,100))
    
lista2=[ i for i in lista if i%2!=0]

print(lista)
print(lista2)
