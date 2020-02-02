#Ejercicio 2: Verificado para matrices cuadradas.
import random
def crear_matriz(n):
    matriz=[[0]*n for i in range(n)]
    return matriz

def imprimir_matriz(matriz):
    for i in range(n):
        for j in range(n):
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
                   
def diagonal_principal(matriz,n):
    impar=1
    for i in range(n):
        for j in range(n):
            if i==j:
                matriz[i][j]=impar
                impar=impar+2
                
def diagonal_secundaria(matriz,n):
    filas=n-1
    columna=0
    while columna<n:
        multiplos=3**(columna)
        matriz[filas][columna]=multiplos
        filas=filas-1
        columna=columna+1
        
def diagonal_inferior(matriz,n):
    num=n
    for i in range(n):
        for j in range(n):
            while j<=i:
                matriz[i][j]=num
                break
        num=num-1

def multiplos_dos(matriz,n):
    num=1
    for i in range(n-1,-1,-1):
        matriz[i]=list([num]*n)
        num=num*2
def iterativo(matriz,n):
    count=0
    num=1
    for i in range(n):
        for j in range(n):
            if count%2!=0:
                matriz[i][j]=num
                num=num+1
            count=count+1
        count=count+1

def inferior_derecha(matriz,n):
    num=1
    for i in range(n):
        for j in range(n-1,n-2-i,-1):
            matriz[i][j]=num
            num=num+1
def espiral(matriz,n):
    contador = 1
    for cuadro in range(n//2+1):
    # Fila superior del recuadro
        for c in range(cuadro,n-cuadro):
            matriz[cuadro][c] = contador
            contador = contador + 1
    # Columna derecha del recuadro
        for f in range(cuadro+1,n-cuadro):
            matriz[f][n-1-cuadro] = contador
            contador = contador + 1
    # Fila inferior del recuadro
        for c in range(n-2-cuadro,cuadro-1,-1):
            matriz[n-1-cuadro][c] = contador
            contador = contador + 1
    # Columna izquierda del recuadro
        for f in range(n-2-cuadro,cuadro,-1):
            matriz[f][cuadro] = contador
            contador = contador + 1
def diagonales(matriz,n):
    num=1
    for vuelta in range(n):
        x=0
        for j in range(vuelta,-1,-1):
            matriz[x][j]=num
            num=num+1
            x=x+1

    for vuelta2 in range(n):
        for i in range(0+1,n):
            x=i
            for j in range(n-1,i-1,-1):
                matriz[x][j]=num
                num=num+1
                x=x+1
        break
        
                
#Programa Principal
n=int(input("Dimension de la matriz cuadrada"))            
matriza=crear_matriz(n)
diagonal_principal(matriza,n)
imprimir_matriz(matriza)

matrizb=crear_matriz(n)
diagonal_secundaria(matrizb,n)
imprimir_matriz(matrizb)

matrizc=crear_matriz(n)
diagonal_inferior(matrizc,n)
imprimir_matriz(matrizc)

matrizd=crear_matriz(n)
multiplos_dos(matrizd,n)
imprimir_matriz(matrizd)

matrize=crear_matriz(n)
iterativo(matrize,n)
imprimir_matriz(matrize)

matrizf=crear_matriz(n)
inferior_derecha(matrizf,n)
imprimir_matriz(matrizf)

matrizg=crear_matriz(n)
espiral(matrizg,n)
imprimir_matriz(matrizg)

matrizh=crear_matriz(n)
diagonales(matrizh,n)
imprimir_matriz(matrizh)
