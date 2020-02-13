#2. Escribir un programa que permita grabar un archivo los datos de lluvia caída durante
#un año. Cada línea del archivo se grabará con el siguiente formato:
#<dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
#Los datos se generarán mediante números al azar, asegurándose que las fechas
#sean válidas. La cantidad de registros también será un número al azar entre 50 y
#200. Por último se solicita leer el archivo generado e imprimir un informe en formato
#matricial donde cada columna represente a un mes y cada fila corresponda a
#los días del mes. Imprimir además el total de lluvia caída en todo el año.

#Ejercicio 2:
import random
def generar_fecha():
    mes0=random.randint(1,12)
    if mes0 in [1,3,5,7,8,10,12]:
        dia0=random.randint(1,31)
    elif mes0 in [4,6,9,11]:
        dia0=random.randint(1,30)
    else:
        dia0=random.randint(1,28)
    return dia0,mes0

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("%3d" %matriz[i][j],end="  ")
        print()
    print()

#Programa Principal

#Creacion del registro
try:
    registro_lluvias=open("lluvias.txt","wt")
    
    numero_registros=random.randint(50,200)
    for i in range (numero_registros):
        dia1,mes1=generar_fecha()
        mm1=random.randint(1,500)
        registro_lluvias.write(str(dia1)+';'+str(mes1)+';'+str(mm1)+'\n')
    

except OSError as mensaje:
    print("Error:", mensaje)
else:
    print("Archivo creado correctamente")
    
finally:
    try:
        registro_lluvias.close()
    except NameError:
        pass
    
#Genero matriz y suma de lluvias
calendario=[[0 for c in range(1,14)]for f in range(1,33)]
calendario[0]=[x for x in range(13)]
for i in range(32):
    calendario[i][0]=i
mm_totales=0

try:
    registro_lluvias=open("lluvias.txt","rt")
    linea=registro_lluvias.readline()
    
    while linea:
        dia2,mes2,mm2=linea.split(';')
        calendario[int(dia2)][int(mes2)]=int(mm2)
        mm_totales=mm_totales+int(mm2)
        linea=registro_lluvias.readline()
    
    
except FileNotFoundError as mensaje:
    print ("No se puede abrir el archivo", mensaje)
except OSError as mensaje:
    print("Error", mensaje)
    
finally:
    try:
        registro_lluvias.close()
    except NameError:
        pass

imprimir_matriz(calendario)
print(f"En total llovieron {mm_totales} de lluvia")
