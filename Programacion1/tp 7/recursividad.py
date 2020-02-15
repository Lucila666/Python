#ejercicio 1: Escribir una función que devuelva la
#cantidad de digitos de un numero entero, sin utilizar
#cadenas de caracteres

def digitos(n,cant=1):
    n=n//10
    if n==0:
        return cant
    else:
        return digitos(n,cant+1)
    
n=int(input("Ingrese numero"))
cant_digitos=digitos(n)
print(cant_digitos)   


#ejercicio 2: Desarrollar una función que reciba un
#número binario y lo devuelva convertido a base decimal.

def decimal(binario,e=1,dec=0):
    
    if binario>0:
        residuo=binario%10
        binario=binario//10
        dec=dec+residuo*e
        e=e*2
        return decimal(binario,e,dec)
    else:
        return dec
    
n=int(input("Ingrese numero binario"))
num_binario=decimal(n)
print(num_binario) 


#ejercicio 3: Escribir una función que devuelva la
#suma de los N primeros números naturales.

def suma(n):
    
    if n==1:
        return 1
    else:
        return n+suma(n-1)
    
num=int(input("Ingrese numero"))
sumatoria=suma(num)
print(sumatoria) 

#ejercicio 4: Desarrollar una función que devuelva
#el producto de dos números enteros por sumas sucesivas.
def producto(n1,n2):
    
    if n2==1:
        return n1
    else:
        return n1+producto(n1,n2-1)
    
num1=int(input("Ingrese primer numero"))
num2=int(input("Ingrese numero por el cual multiplicar"))
resultado=producto(num1,num2)
print(resultado)    

#ejercicio 5. Realizar una función que devuelva el resto de dos
#números enteros, utilizando restas sucesivas.
def restar(n1,n2,cont=0):
    if n2==n1:
        return cont
    else:
        cont+=1
        return restar(n1-1,n2,cont)
    
num1=int(input("Ingrese primer numero"))
num2=int(input("Ingrese numero para restar"))
resultado=restar(num1,num2)
print(resultado)

#ejercicio 6. La función de Ackermann A(m,n) se define de la
#siguiente forma:
#n+1 si m = 0
#A(m-1,1) si m>0 y n = 0
#A(m-1,A(m,n-1)) de otro modo
#Imprimir un cuadro con los valores que adopta la función para
#valores de m entre 0 y 3 y de n entre 0 y 7.

def ackermann(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))
    
#Programa Principal
for i in range(4):
    for j in range(4):
        resultado=ackermann(i,j)
        print("%2d" %resultado,end=" ")
    print()
    
#ejercicio 7.Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo
#Común Divisor (también llamado Divisor Común Mayor).Utilizando la función anterior calcular el MCD de todos los elementos de una lista
#de números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
#utilizar iteraciones en ninguna etapa del proceso.

def mcd(n1,n2):
    if n1==n2:
        return n1
    elif n1>n2:
        return mcd(n1-n2,n2)
    else:
        return mcd(n2,n1)

def calcularmcd(lista, pos=0):
    if pos<len(lista)-2:
        return mcd(lista[pos], calcularmcd(lista, pos+1))
    else:
        return mcd(lista[pos], lista[pos+1])
    
#Programa Principal
arreglo=[4,8,16]
    
print(calcularmcd(arreglo))

#ejercicio 8. Realizar la implementación recursiva del método de selección para ordenar una
#lista de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
#posición, y luego ordenar el resto de la lista con una llamada recursiva
import random

def ordenar_burbujeo(lista,pos=0):
    if pos<len(lista)-1:
        actual=lista[pos]
        siguiente=ordenar_lista(lista,pos+1)
        if actual>siguiente:
            aux=lista[pos]
            lista[pos]=lista[pos+1]
            lista[pos+1]=aux
    return lista[pos]

def ordenar_seleccion(lista,pos=0):
    if pos<len(lista):
        minimo=min(lista[pos:])
        posicion=lista[pos:].index(minimo)+pos
        aux=lista[posicion]
        lista[posicion]=lista[pos]
        lista[pos]=aux
        ordenar_seleccion(lista,pos+1)
                          

    
#Programa Principal
arreglo=[random.randint(0,15) for i in range(10)]
print(arreglo)
for i in range(len(arreglo)//2):
    ordenar_burbujeo(arreglo)
print(arreglo)
ordenar_seleccion(arreglo)
print(arreglo)

#ejercicio 9. Realizar una función recursiva para imprimir una matriz de M x N.
# ejercicio 10. Escribir una función que sume todos los elementos de una matriz de M x N
#y devuelva el resultado.
#ejercicio 11.Desarrollar una función que devuelva el elemento de valor mínimo de una matriz de M x N.
import random

def crear_matriz(n,m,matriz,f=0):
    if f<n:
        matriz.append([])
        for i in range(m):
            aleatorio=random.randint(1,10)
            matriz[f].append(aleatorio)
        return crear_matriz(n,m,matriz,f+1)

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()
                          
def suma_elementos(matriz,suma=0,c=0,f=0):
    if c<len(matriz[f]):
        suma=suma+matriz[f][c]
        c=c+1
        return suma_elementos(matriz,suma,c,f)
    else:
        f=f+1
        c=0
        if f<len(matriz):
            suma=suma+matriz[f][c]
            c=c+1
            return suma_elementos(matriz,suma,c,f)
        else:
            return suma
            
def buscar_minimo(matriz,c=0,f=0,minimo=0):
    if c==0 and f==0:
        minimo=matriz[f][c]
        c=c+1
        return buscar_minimo(matriz,c,f,minimo)
    
    elif c>=len(matriz[f]):
        f=f+1
        c=0
        
    if f<len(matriz):
        if minimo>matriz[f][c]:
            minimo=matriz[f][c]
        c=c+1
        return buscar_minimo(matriz,c,f,minimo)
    else:
        return minimo
            
    
    
#Programa Principal
filas=int(input("Ingrese num de filas"))
col=int(input("Ingrese num de columnas"))
mat=[]
crear_matriz(filas,col,mat)
imprimir_matriz(mat)
sumatoria=suma_elementos(mat)
print(sumatoria)
min=buscar_minimo(mat)
print(min)    
