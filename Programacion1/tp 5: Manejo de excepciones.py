#1. Desarrollar una función para ingresar a través del teclado un número natural. La
#función rechazará cualquier ingreso inválido de datos utilizando excepciones y
#mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
#número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
#éste sea correcto. Escribir también un programa que permita probar el correcto
#funcionamiento de la misma.

#Ejercicio 1
def validar_numero():
    while True:
        numero=input("Ingrese un numero natural")
        try:
            numero=float(numero)
    
            assert numero==int(numero), "El numero debe ser entero"
            assert numero>=0, "El numero debe ser mayor a cero"
            break
        except ValueError:
            print("Se deben ingresar numeros enteros")
        except AssertionError as mensaje:
            print(mensaje)
            print("Intente nuevamente")
    return int(numero)
    
#Programa Principal

n=validar_numero()
print(n)

#2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
#números reales, sume ambos valores y devuelva el resultado como un
#número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
#utilizando manejo de excepciones para detectar el error.

#Ejercicio 2
def sumar_cadenas(lista1,lista2):
    largo=len(lista1)
    try:
        lista3=[lista1[i]+lista2[i] for i in range(largo)]
    except TypeError:
        print("Caracteres incorrectos")
        lista3=[-1]
    except IndexError:
        print("Cadenas de diferente largo")
        lista3=[-1]
    return lista3
    
#Programa Principal
cad1=[3,4,5,6]
cad2=[3,4,5,"x"]
suma=sumar_cadenas(cad1,cad2)
print(suma)


#3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del
#mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
#obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
#Devolver una cadena vacía si el número de mes es inválido. La detección de meses
#inválidos deberá realizarse a través de excepciones.


#Ejercicio 3
def buscar_mes(n):
    meses=["Enero","Febrero","Marzo","Abril","Mayo",\
           "Junio","Julio","Agosto","Septiembre",\
           "Octubre","Noviembre","Diciembre"]
    try:
        mes=meses[n-1]
        
    except IndexError:
        mes=""
    return mes
    
#Programa Principal
num=int(input("Ingrese numero de mes"))
nombre_mes=buscar_mes(num)
print(nombre_mes)

#4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
#las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
#un programa para imprimir los números enteros entre 1 y 100000, y que solicite
#confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

#Ejercicio 4
i=1
bandera=True
while (bandera==True) and (i<100000):
    try:
        print(i)
        i+=1
    except KeyboardInterrupt:
        confirmacion=input("Ud. esta seguro de \
detener el programa? (S/N)")
        if confirmacion.upper()=="S":
            bandera=False
            
#5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
#módulo math. Escribir un programa que utilice esta función para calcular la raíz
#cuadrada de un número cualquiera ingresado a través del teclado. El programa
#debe utilizar manejo de excepciones para evitar errores si se ingresa un número
#negativo.

#Ejercicio 5
import math
numero=int(input("Ingrese numero"))
try:
    raiz=math.sqrt(numero)
    print(f"La raiz cuadrada es: {raiz}")   
except ValueError:
    print("El numero debe ser mayor a cero")
    
#6. El método index permite buscar un elemento dentro de una lista, devolviendo la
#posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
#produce una excepción de tipo ValueError. Desarrollar un programa que cargue
#una lista con números enteros ingresados a través del teclado (terminando con -1)
#y permita que el usuario ingrese el valor de algunos elementos para visualizar la
#posición que ocupan, utilizando el método index. Si el número no pertenece a la
#lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
#proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

#Ejercicio 6
import random
lista=[random.randint(0,100) for i in range(10)]
print(lista)
bandera=True
cont=0
while cont<3 and bandera==True:
    buscar=int(input("Ingrese el valor a buscar"))
    try:
        posicion=lista.index(buscar)
        print(f"El elemento se encuentra en la posicion {posicion}")
        bandera=False
    except ValueError:
        print("Numero no encontrado, ingrese otro")
        cont+=1
#7.Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar 
#entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje indicando
# si el número que tiene  que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe imprimir en 
#pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número se
# mostrará un mensaje en pantalla y se lo contará como un intento más.

#Ejercicio 7
import random
adivinar=random.randint(1,500)
arriesgar=0
bandera=True
cont=0
while adivinar!=arriesgar:
    try:
        arriesgar=int(input("Que numero crees que es?"))
        if arriesgar<adivinar:
            print(f"El numero es mayor a {arriesgar}")
        elif arriesgar>adivinar:
            print(f"El numero es menor a {arriesgar}")
        else:
            print(f"FELICITACIONES! Efectivamente el numero era {arriesgar} y te tomó {cont} intento descubrirlo!")
    except ValueError:
        print("Caracter invalido, intente nuevamente")
    
    finally:
        cont+=1
