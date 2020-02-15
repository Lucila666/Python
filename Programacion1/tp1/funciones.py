#1.Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres,
# sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. 
#No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar 
#los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste 
#no existe.

#Ejercicio 1
def encontrar_mayor(n1,n2,n3):
    devolver=-1
    if n1>n2:
        if n1>n3:
            devolver=n1
        elif n3>n1:
            devolver=n3
    elif n2>n1:
        if n2>n3:
           devolver=n2
        elif n3>n2:
            devolver=n3
    return devolver

#Programa principal
a=int(input("Ingrese numero 1"))
b=int(input("Ingrese numero 2"))
c=int(input("ingrese numero 2"))    
resultado=encontrar_mayor(a,b,c)

if resultado==-1:
    print("Ningun numero es estrictamente mayor")
else:
    print("El mayor es:",resultado)

#2.Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha 
#gregoriana válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. 
#Realizar también un programa para verificar el comportamiento de la función.

#Ejercicio 2
def verificacion_fecha(d,m,a):
    devolver=False
    if 1<=m<=12:
        if if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if 1<=d<=31:
                devolver=True
        elif m==2:
            if a%400==0 or (a%4==0 and a%100!=0):
                 if 1<=d<=29:
                     devolver=True
            else:
                 if 1<=d<=28:
                     devolver=True
        else:
            if 1<=d<=30:
                devolver=True
    return devolver

#Programa principal
dia=int(input("Ingrese dia"))
mes=int(input("Ingrese mes"))
año=int(input("ingrese año"))    
resultado=verificacion_fecha(dia,mes,año)
print("La fecha ingresada es",resultado)


#3.Para un número entero N menor de 100 recibido como parámetro, 
#escribir un programa que utilice una función para devolver la suma de los cuadrados 
#de aquellos números entre 1 y N que están separados entre si por cuatro unidades. (12 + 52 + 92 + 132 + …)

#Ejercicio 3
def ecuacion(n):
    devolver=0
    for i in range(1,n+1,4):
        devolver=devolver+i**2
        
    return devolver

#Programa principal
a=int(input("Ingrese numero"))
resultado=ecuacion(a)

print("El resultado es",resultado)

#4.Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
 #Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes
 #(detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la 
#cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también
 #un programa para verificar el comportamiento de la función.

#Cantidad de viajes Valor del pasaje 1 a 20 Averiguar valor actualizado 
#21 a 30 20% de descuento sobre tarifa máxima 
#31 a 40 30% de descuento sobre tarifa máxima 
#Más de 40 40% de descuento sobre tarifa máxima

#Ejercicio 4
def costo_viajes(nviajes):
    gasto=0.00
    if 0<nviajes<21:
        gasto=nviajes*19
    elif 20<nviajes<31:
        gasto=20*19+(nviajes-20)*0.8*19
    elif 30<nviajes<41:
        gasto=20*19+10*0.8*19+(nviajes-30)*0.7*19
    elif 40<nviajes:
        gasto=20*19+10*0.8*19+10*0.7*19+(nviajes-40)*0.6*19
        
    return gasto

#Programa principal
a=int(input("Ingrese numero de viajes realizados"))
resultado=float(costo_viajes(a))

print("El gasto fue de",resultado)

#Solucion propuesta por el profe: considera el valor del pasaje una variable!!!
# Práctica 1, Ejercicio 4

def calculargasto(viajes, tarifa):
    """ Devuelve el importe a pagar segun la cantidad de viajes realizados,
        considerando el esquema de tarifas decrecientes vigente """
    tarifa1 = tarifa*0.80  # tarifa con el 20% de descuento
    tarifa2 = tarifa*0.70  # tarifa con el 30% de descuento
    tarifa3 = tarifa*0.60  # tarifa con el 40% de descuento
    if viajes<=0:
        total=0
    elif viajes<=20:
        total = viajes*tarifa
    elif viajes<=30:
        total = 20*tarifa+(viajes-20)*tarifa1
    elif viajes<=40:
        total = 20*tarifa+10*tarifa1+(viajes-30)*tarifa2
    else:
        total = 20*tarifa+10*tarifa1+10*tarifa2+(viajes-40)*tarifa3
    return total

# Programa principal
n = int(input("Cantidad de viajes? "))
p = float(input("Precio del pasaje? "))
importe = calculargasto(n, p)
print()
print("Por", n, "viajes se gastaron $", importe)
print()


#5. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
#le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
#dos números enteros, correspondientes al total de la compra y al dinero recibido.
#Informar cuántos billetes de cada denominación deben ser entregados al cliente
#como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
#existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
#si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona
#con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
#de $20, 1 billete de $10 y 3 billetes de $1.

#Ejercicio 5
def darVuelto(recibo, precio):
    b500 = 0
    b100 = 0
    b50 = 0
    b20 = 0
    b10 = 0
    b5 = 0
    b1 = 0
    vuelto = recibo - precio
    while vuelto >= 500:
        b500 += 1
        vuelto -= 500
    while vuelto >= 100:
        b100 += 1
        vuelto -= 100
    while vuelto >= 50:
        b50 += 1
        vuelto -= 50
    while vuelto >= 20:
        b20 += 1
        vuelto -= 20
    while vuelto >= 10:
        b10 += 1
        vuelto -= 10
    while vuelto >= 5:
        b5 += 1
        vuelto -= 5
    while vuelto >= 1:
        b1 += 1
        vuelto -= 1            
    return (b500, b100, b50, b20, b10, b5, b1)

recibo=int(input("Ingrese el monto recibido: "))
precio=int(input("Ingrese el precio del producto: "))
if recibo>=precio:
    b500, b100, b50, b20, b10, b5, b1 = darVuelto(recibo,precio)
    print ("Vuelto:\n")
    print ("%d billetes de $500\n%d billetes de $100\n%d billetes de $50\n%d billetes de $20\n%d billetes de $10\n%d billetes de $5\n%d billetes de $1" %(b500, b100, b50,
                                                                                                                                                         b20, b10, b5, b1))
else:
    print ("El dinero recibido es insuficiente para realizar esta compra")

#6. Escribir dos funciones para imprimir por pantalla cada uno de los siguientes
#patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
#**********   **
#**********   ****
#**********   ******
#**********   ********
#**********   **********

#Ejercicio 6
def patron1(filas):
   for i in range (1,filas+1):
       for j in range(10):
           print("*",end="")
       print()
   
def patron2(filas):
     for i in range (1,filas+1):
       for j in range(2*i):
           print("*",end="")
       print()
    

#Programa principal
a=int(input("numero de filas"))
patron1(a)
print()
patron2(a)

#7. Desarrollar una función que reciba como parámetros dos números enteros y devuelva
#el número que resulte de concatenar ambos valores. Por ejemplo, si recibe
#1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no
#vistas en clase.

#Ejercicio 7
def concatenacion(n1,n2):
   concatenar=int(n1+n2)
   return concatenar
   
 

#Programa principal
a=input("primer numero")
b=input("segundo numero")
resultado=concatenacion(a,b)
print(resultado)

#8. Escribir una función que reciba como parámetro número del 1 al 9 y devuelva el
#resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido.
#Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333). Escribir
#también un programa para verificar el comportamiento de la función. No se
#permite utilizar facilidades de Python no vistas en clase.

#Ejercicio 8
def ecuacion(n):
    """La ecuacion a realizar es n+nn+nnn+nnnn"""
    sumando1=n
    sumando2=n+n
    sumando3=n+n+n
    sumando4=n+n+n+n
    suma=int(sumando1)+int(sumando2)+int(sumando3)+int(sumando4)
    return suma
   
 

#Programa principal

numero=input("ingrese numero")
resultado=ecuacion(numero)
print(resultado)

#9. Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
#expresada por tres enteros (correspondientes al día, mes y año) y calcule y
#devuelva tres enteros correspondientes el día siguiente al dado.

#Ejercicio 9
def dia_siguiente(d,m,a):
    if 1<=m<=12:
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if 1<=d<31:
                d=d+1
            else:
                d=1
                if m!=12:
                    m=m+1
                else:
                    m=1
                    a=a+1
        elif m==2:
            if a%400==0 or (a%4==0 and a%100!=0):
                if 1<=d<29:
                    d=d+1
                elif d==29:
                    d=1
                    if m!=12:
                        m=m+1
                    else:
                        m=1
                        a=a+1
                     
            else:
                if 1<=d<28:
                    d=d+1
                elif d==28:
                    d=1
                    if m!=12:
                        m=m+1
                    else:
                        m=1
                        a=a+1
                     
        else:
            if 1<=d<30:
                d=d+1
            elif d==30:
                d=1
                if m!=12:
                    m=m+1
                else:
                    m=1
                    a=a+1
                
    return d,m,a
   
 #Utilizando esta función, desarrollar programas que permitan:
#a. Sumar N días a una fecha.

#Programa principal A

dia=int(input("Ingrese el dia"))
mes=int(input("Ingrese el mes"))
año=int(input("Ingrese el año"))
n=int(input("Ingrese cuantos dias quiere sumarle"))
for i in range (n):
    diai,mesi,añoi=dia_siguiente(dia,mes,año)
    dia,mes,año=diai,mesi,añoi
print(dia,mes,año)

#b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

#Programa principal B. Nota la primer fecha debe ser anterior a la segunda

dia1=int(input("Ingrese el dia"))
mes1=int(input("Ingrese el mes"))
año1=int(input("Ingrese el año"))

dia2=int(input("Ingrese el dia"))
mes2=int(input("Ingrese el mes"))
año2=int(input("Ingrese el año"))

n=0
while dia2!=dia1 or mes2!=mes1 or año2!=año1:
    dia1,mes1,año1=dia_siguiente(dia1,mes1,año1)
    n=n+1
print(n)
