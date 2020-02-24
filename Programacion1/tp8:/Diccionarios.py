#9. Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

#Ejercicio 9
#Programa Principal

dic={x:x**2 for x in range (1,21)}
print (dic)

#10. Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12.
#Escribir también un programa para probar la función.

#Ejercicio 10

def multiplos(n):
    tabla={x:x*n for x in range(1,13)}
    return tabla
#Programa Principal

num=int(input("Ingrese numero para generar tabla"))
print(multiplos(num))

#11.Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar
#del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad
q#ue indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

#Ejercicio 11

def eliminar_claves(dic,claves):
    try:
        for clave in claves:
            del dic[clave]
    except KeyError:
        print(f"No se encontro {clave}")
    else:
        print("Proceso excitoso")
    return dic
#Programa Principal
capitales={
    "Buenos Aires":"La Plata",
    "Catamarca":"San Fernando del Valle de Catamarca",
    "Chaco":"Resistencia",
    "Chubut":"Rawson",
    "Córdoba":"Córdoba",
    "Corrientes":"Corrientes",
    "Entre Ríos":"Paraná",
    "Formosa":"Formosa",
    "Jujuy":"San Salvador de Jujuy",
    "La Pampa":"Santa Rosa",
    "La Rioja":"La Rioja",
    "Mendoza":"Mendoza",
    "Misiones":"Posadas",
    "Neuquén":"Neuquén",
    "Río Negro":"Viedma",
    "Salta":"Salta",
    "San Juan":"San Juan",
    "San Luis":"San Luis",
    "Santa Cruz":"Río Gallegos",
    "Santa Fe":"Santa Fe de la Vera Cruz",
    "Santiago del Estero":"Santiago del Estero",
    "Tierra del Fuego":"Ushuaia",
    "Tucumán":"San Miguel del Tucumán",
    }
norte=["Jujuy","Salta","Catamarca","Tucumán","La Rioja","Santiago del Estero"]
print(eliminar_claves(capitales,norte))

#12.Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i", etc. 
#Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a la función por cada
#palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales hallada.


#Ejercicio 12

def contar_vocales(cadena):
    vocales={'a':0,
             'e':0,
             'i':0,
             'o':0,
             'u':0}
    for letra in cadena:
        if letra in vocales:
            vocales[letra]=vocales[letra]+1
    return vocales
#Programa Principal

frase="La unica forma de vencer la tentacion, es ceder ante ella"
frase_lista=frase.split()    
for palabra in frase_lista:
    print(palabra, contar_vocales(palabra))
    
    
#13. Una librería almacena su lista de precios en un diccionario. Diseñar un programa para crearlo, incrementar los precios de los 
#cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
#costoso que venden en el comercio.


#Ejercicio 13

def crear_lista():
    lista={}
    n=input("quiere ingresar un producto nuevo o 'no' para terminar")
    while n!='no':
        p=n
        c=float(input("Ingrese precio"))
        lista[p]=c
        n=input("quiere ingresar un producto nuevo o 'no' para terminar")
    return lista
def aumentar_precios(dic):
    for item in dic:
        dic[item]=dic[item]*1.15
        
#Programa Principal

lista_productos=crear_lista()
print(lista_productos)
aumentar_precios(lista_productos)
print(lista_productos)

producto=list(lista_productos.keys())
precio=list(lista_productos.values())
precio_mayor=max(precio)
pos=str(precio_mayor).find(str(precio))
print(f"El producto mas caro es {producto[pos]}, que vale {precio_mayor} pesos")

#14. Escribir una función buscarclave() que reciba como parámetros un diccionario y un valor, y devuelva una lista de claves que apunten
#("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado.

#Ejercicio 14

def buscar_clave(dic,valor):
    claves=list(dic.keys())
    valores=list(dic.values())
    claves_seleccionadas=[]
    for i in range (len(claves)):
        if valores[i]==valor:
            claves_seleccionadas.append(claves[i])
    return claves_seleccionadas
        
#Programa Principal

personas={
    "Mauro":28,
    "Marcela":15,
    "Juana":20,
    "Pedro":15,
    "Luciana":25,
    "Roberto":15,
    "Juancito":21,
    }

quinceañeros=buscar_clave(personas,15)
print("Del grupo tienen 15 las siguientes personas",quinceañeros)
