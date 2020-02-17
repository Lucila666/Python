#1. Escribir una funcion para rellenar una matriz de enteros de
#N*N con los numeros del 1 al 4, respetando el patrón por cuadrantes
#detallado. La funcion debe servir para cualquier valor par de N,
#el que se ingresa por teclado. Escribir, también, el programa que invoque
#funcion y muestre la matriz generada. Ej. N=8
#1 1 1 1 2 2 2 2
#1 1 1 1 2 2 2 2
#1 1 1 1 2 2 2 2
#1 1 1 1 2 2 2 2
#3 3 3 3 4 4 4 4
#3 3 3 3 4 4 4 4
#3 3 3 3 4 4 4 4
#3 3 3 3 4 4 4 4

n=int(input("Ingrese dimension de la matriz cuadrada"))
while n%2!=0:
    n=int(input("Ingrese dimension de la matriz cuadrada"))
matriz=[[0]*n for i in range(n)]
f=0
c=len(matriz)-1
for i in range(n):
    for j in range(n):
        if i!=j:
            if (i==f and j==c):
                f=f+1
                c=c-1
            else:
                if i<n/2 and j<n/2:
                    matriz[i][j]=1
                elif i>=n/2 and j<n/2:
                    matriz[i][j]=3
                elif i<n/2 and j>=n/2:
                    matriz[i][j]=2
                else:
                    matriz[i][j]=4

for f in range(n):
    for c in range(n):
        print(matriz[f][c],end=" ")
    print()