#1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
#verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
#a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
#b. Ordenar en forma ascendente cada una de las filas de la matriz.
#c. Intercambiar dos filas, cuyos números se reciben como parámetro.
#d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
#e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
#f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
#g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
#h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
#i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
#j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
#k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.

#Ejercicio 1: Verificado para matrices cuadradas.
import random
def crear_matriz(n,m):
    matriz=[[0]*m for i in range(n)]
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("%02d" %matriz[i][j],end="  ")
        print()
    print()
        
def carga_estatica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=int(input("Ingrese valor"))
            
def carga_dinamica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=random.randint(0,99)
                   
            
def ordenar_matriz(matriz):
    for i in range(len(matriz)):
        matriz[i].sort()
def cambiar_filas(matriz,f1,f2):
    aux=list(matriz[f1])
    matriz[f1]=matriz[f2].copy()
    matriz[f2]=aux.copy()
    
def cambiar_columnas(matriz,c1,c2):
    for i in range(len(matriz)):
        aux=matriz[i][c1]
        matriz[i][c1]=matriz[i][c2]
        matriz[i][c2]=aux
        
def fila_columna(matriz,f,c):
    lista=[]
    aux=matriz[f].copy()
    for i in range(len(matriz)):
        lista.append(matriz[i][c])
        matriz[i][c]=aux[i]
    matriz[f]=lista.copy()
            
def transponer(matriz):
    ft=len(matriz)
    ct=len(matriz[0])
    matrizT=crear_matriz(ct,ft)
    for i in range(len(matrizT)):
        for j in range(len(matrizT[i])):
            matrizT[i][j]=matriz[j][i]
    return matrizT

def promedio_fila(matriz,f):
    promedio=sum(matriz[f])/len(matriz[f])
    return promedio

def impares_columna(matriz,c):
    count=0
    for i in range(len(matriz)):
        if matriz[i][c]%2!=0:
            count=count+1
    porcentaje=count/len(matriz)
    return porcentaje

def matriz_simetrica(matriza,matrizb):
    bandera=True
    for i in range(len(matriza)):
        for j in range(len(matriza[i])):
            if matriza[i][j]!=matrizb[i][j]:
                bandera=False
    return bandera

def columnas_capicua(matriz):
    for i in range(len(matriz[0])):
        indice=len(matriz)-1
        cont=0
        dev=True
        lista=[]
        for x in range(0,len(matriz)//2):
            lista.append(matriz[x][i])
            if matriz[x][i]!=matriz[indice][i]:
                dev=False
                indice=indice-1
        if dev==True:
            print("La columna",i,"Es capicua")
            print(lista)
        else:
            print("La columna",i,"No es capicua")
    return 
                
#Programa principal
f=int(input("Ingrese numero de filas"))
c=int(input("ingrese numero de columnas"))
matriz=crear_matriz(f,c)
imprimir_matriz(matriz)
carga_dinamica(matriz)
imprimir_matriz(matriz)
ordenar_matriz(matriz)
imprimir_matriz(matriz)
fila1=int(input("Ingrese primer fila a intercambiar"))
fila2=int(input("Ingrese segunda fila a intercambiar"))
cambiar_filas(matriz,fila1,fila2)
imprimir_matriz(matriz)
columna1=int(input("Ingrese primer columna a intercambiar"))
columna2=int(input("Ingrese segunda columna a intercambiar"))
cambiar_columnas(matriz,columna1,columna2)
imprimir_matriz(matriz)
fila=int(input("Ingrese fila a intercambiar"))
columna=int(input("Ingrese columna a intercambiar"))
fila_columna(matriz,fila,columna)
imprimir_matriz(matriz)
transpuesta=transponer(matriz)
print("Matriz transpuesta: ")
imprimir_matriz(transpuesta)
n=int(input("Ingrese fila a promediar"))
prom=promedio_fila(matriz,n)
print("El promedio de la fila",n,"es : ",prom)
m=int(input("Ingrese columna a sacar porcentaje de imapres"))
porcentaje=impares_columna(matriz,m)
print("El porcentaje de numeros impares en la columna",m,"es :",porcentaje)
simetria=matriz_simetrica(matriz,transpuesta)
if simetria==True:
    print("Matriz simetrica")
else:
    print("Matriz no simetrica")
columnas_capicua(matriz)
