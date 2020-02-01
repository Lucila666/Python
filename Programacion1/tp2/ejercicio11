#Ejercicio 11: Intercalar los elementos de una lista entre los elementos de otra. La intercalación
#deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
#una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
#y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

#Solo sirve si lista1 y 2 tienen la misma cantidad de elementos
import random
def crearlista():
    n=6
    lista=[]
    for i in range(n):
        lista.append(random.randint(0,100))
    return lista

lista1=crearlista()
print(lista1)
lista2=crearlista()
print(lista2)
j=0

for i in range(0,len(lista1)+len(lista2),2):
            lista1[i+1:i+1]=[lista2[j]]
            j=j+1
print(lista1)
