#7. Ingresar una frase desde el teclado y eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar 
#las palabras ordenadas según su longitud. La eliminación de las palabras duplicadas debe realizarse a través de un conjunto.

#Ejercicio 7

#Programa Principal

frase=input("Ingrese frase")
frase_lista=frase.split()
frase_conjunto=set(frase_lista)
frase_corta=list(frase_conjunto)
frase_corta.sort(key=lambda x:len(x))
print (frase_corta)


#8. Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el
#método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
#Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.


#Ejercicio 8
#Programa Principal
numeros={0,1,2,3,4,5,6,7,8,9}
n=0
while n!=-1:
    try:
        n=int(input("Ingrese numero a eliminar o -1 para terminar"))
        numeros.remove(n)
        print(numeros)
        
    except KeyError:
        print("Ese numero no se encuentra en el conjunto, ingrese otro o -1 para terminar")
