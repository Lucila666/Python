#1. Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
#y luego escribir un programa para verificar su comportamiento:
#a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
#b. Sumar N días a una fecha.
#c. Ingresar un horario desde teclado, verificando que sea correcto.
#d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerará que el primero corresponde 
#al día anterior. En ningún caso la diferencia en horas puede superar las 24 horas.


def verificacion_fecha(tupla):
    devolver=False
    if 1<=tupla[1]<=12:
        if tupla[1]==1 or tupla[1]==3 or tupla[1]==5 or tupla[1]==7 or tupla[1]==8 or tupla[1]==10 or tupla[1]==12:
            if 1<=tupla[0]<=31:
                devolver=True
        elif tupla[1]==2:
            if tupla[2]%400==0 or (tupla[2]%4==0 and tupla[2]%100!=0):
                 if 1<=tupla[0]<=29:
                     devolver=True
            else:
                 if 1<=tupla[0]<=28:
                     devolver=True
        else:
            if 1<=tupla[0]<=30:
                devolver=True
    return devolver

def dia_siguiente(tupla):
    tupla1=()
    if 1<=tupla[1]<=12:
        if tupla[1]==1 or tupla[1]==3 or tupla[1]==5 or tupla[1]==7 or tupla[1]==8 or tupla[1]==10 or tupla[1]==12:
            if 1<=tupla[0]<31:
                tupla1=tupla[0]+1,tupla[1],tupla[2]
            else:
                
                if tupla[1]!=12:
                    tupla1=1,tupla[1]+1,tupla[2]
                else:
                    tupla1=1,1,tupla[2]+1
                    
        elif tupla[1]==2:
            if tupla[2]%400==0 or (tupla[2]%4==0 and tupla[2]%100!=0):
                if 1<=tupla[0]<29:
                    tupla1=tupla[0]+1,2,tupla[2]
                elif tupla[0]==29:
                    tupla1=1,3,tupla[2]
            else:
                if 1<=tupla[0]<28:
                    tupla1=tupla[0]+1,2,tupla[2]
                elif tupla[0]==28:
                    tupla1=1,3,tupla[2]
                                         
        else:
            if 1<=tupla[0]<30:
                tupla1=tupla[0]+1,tupla[1],tupla[2]
            elif tupla[0]==30:
                tupla1=1,tupla[1]+1,tupla[2]
                
    return tupla1

def validar_hora(tupla):
    if 0<=tupla[0]<24 and 0<=tupla[1]<60:
        return True
    else:
        return False
def diferencia_horas(tupla):
    if tupla[0]<tupla[2]:
        min=60-tupla[1]+tupla[3]
        hor=(tupla[2]-tupla[0]-1)
    elif tupla[0]>tupla[2]:
        min=60-tupla[1]+tupla[3]
        hor=(24-tupla[0]+tupla[2]-1)
    while min>=60:
        min=min-60
        hor=hor+1
    return (str(hor)+":"+str(min))

#Programa principal

dia=int(input("Ingrese dia"))
mes=int(input("Ingrese mes"))
año=int(input("ingrese año"))
fecha=(dia,mes,año)
validacion=verificacion_fecha(fecha)
print("La fecha ingresada es",validacion)

n=int(input("Ingrese cuantos dias quiere sumarle"))
fechai=()
for i in range (n):
    fechai=dia_siguiente(fecha)
    fecha=fechai
print(fecha)

print("Se utiliza formato 24 horas, es decir entre 00:00 y 23:59 minutos")

hora=()
for i in range (2):
    while True:
        hi=int(input("hora"))
        mi=int(input("Ingrese minutos"))
        horai=(hi,mi)
        if  validar_hora(horai):
            hora=hora+horai
            break
        else:
            print("Hora incorrecta, ingrese una nueva")
            
print("Hay una diferencia de", diferencia_horas(hora))            




#2. Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres
#con la misma fecha expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
#2017". Escribir también un programa para verificar su comportamiento

def verificacion_fecha(tupla):
    devolver=False
    if 1<=tupla[1]<=12:
        if tupla[1]==1 or tupla[1]==3 or tupla[1]==5 or tupla[1]==7 or tupla[1]==8 or tupla[1]==10 or tupla[1]==12:
            if 1<=tupla[0]<=31:
                devolver=True
        elif tupla[1]==2:
            if tupla[2]%400==0 or (tupla[2]%4==0 and tupla[2]%100!=0):
                 if 1<=tupla[0]<=29:
                     devolver=True
            else:
                 if 1<=tupla[0]<=28:
                     devolver=True
        else:
            if 1<=tupla[0]<=30:
                devolver=True
    return devolver

def fecha_extendida(tupla):
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    m=tupla[1]
    m=meses[m-1]
    
    fecha=f"{tupla[0]:02} de {m} de {tupla[2]}"
    return fecha
    
#Programa principal
validacion=False
while validacion==False:
    dia=int(input("Ingrese dia"))
    mes=int(input("Ingrese mes"))
    año=int(input("ingrese año"))
    fecha=(dia,mes,año)
    validacion=verificacion_fecha(fecha)

print(fecha_extendida(fecha))



#3. Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una dirección de 
#correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección. Ejemplo:
#alguien@uade.edu.ar -> (alguien, uade, edu, ar).

#Ejercicio 3
def modificar_correo(cadena):
   cad1,cad2=cadena.split("@")
   cad2,cad3,cad4=cad2.split(".")
   partes_mail=(cad1,cad2,cad3,cad4)
   return (partes_mail)
    
#Programa principal
mail="vercelli@uade.com.ar"
mail_descompuesto=modificar_correo(mail)
print(mail_descompuesto)


#4. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, 
#por ejemplo: (3, 4) y (5, 4). La función devuelve True o False. Escribir también un programa para verificar su comportamiento.

#Ejercicio 4
import random
def jugada_domino(tupla1,tupla2):
    if tupla1[0]==tupla2[0] or \
      tupla1[0]==tupla2[1] or \
      tupla1[1]==tupla2[0] or \
      tupla1[1]==tupla2[1]:
        return True
    else:
        return False
   
    
#Programa principal
ficha_domino1=(random.randint(1,6),random.randint(1,6))
ficha_domino2=(random.randint(1,6),random.randint(1,6))
encastre=jugada_domino(ficha_domino1,ficha_domino2)
print(ficha_domino1,ficha_domino2)
if encastre:
    print("Jugada permitida")
else:
    print("Jugada invalida")
    
#5. Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no. 
#Desarrollar también un programa que permita verificar el comportamiento de la función.
#+ 6. Ídem anterior, pero determinando si los vectores son paralelos

#Ejercicio 5 y 6

def verificar_ortogonalidad(tupla1,tupla2):
    ortg=tupla1[0]*tupla2[0]+tupla1[1]*tupla2[1]
    if ortg==0:
        return True
    else:
        return False
def verificar_paralelos(tupla1,tupla2):
    if tupla1[0]/tupla2[0]==tupla1[1]/tupla2[1]:
        return True
    else:
        return False
    
#Programa principal
vector1=(2,3)
vector2=(-3,2)
ortogonalidad=verificar_ortogonalidad(vector1,vector2)
if ortogonalidad:
    print("Los vectores son ortogonales")
else:
    print("Los vectores no son ortogonales")
    
vector3=(3,-1)
vector4=(-9,3)
paralelismo=verificar_paralelos(vector3,vector4)
if paralelismo:
    print("Los vectores son paralelos")
else:
    print("Los vectores no son paralelos")
