#Ejercicio 15: Muchas aplicaciones financieras requieren que los números sean expresados también
#en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
#cincuenta y tres". Escribir un programa que utilice una función para convertir un
#número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
#la función si también aceptara números negativos? ¿Y números con decimales?
#def armar_cientos(trio):
    ltrio=list(trio)
    a=int(ltrio[0])
    b=int(ltrio[1])
    c=int(ltrio[2])
    cadenita=""
    lista_unidades=['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']        
    lista_decenas=['diez','veinti','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa']
    lista_centenas=['ciento','doscientos','trescientos','cuatrocientos','quinientos','seisientos','setecientos','ochocientos','novecientos']

    if b!=0 and b!=1 :
        cadenita= lista_decenas[b-1]+ " y "+ lista_unidades[c-1]
    elif b==0 and c!=0:
        cadenita=lista_unidades[c-1]
    elif b==1:
        diez=['diez','once','doce','trece','catorce','quince','dieciseis','diecisiete','dieciocho','diecinueve']
        cadenita=diez[c]
    if a==1 and b==0 and c==0:
        cadenita=cien
    elif a!=0:
        cadenita=lista_centenas[a-1]+" "+cadenita
    return cadenita

#Programa Principal        
billones=["","un billon"]
numero=int(input("Ingrese un numero"))
while (numero<0 or numero>1000000000000):
    numero=int(input("Ingrese un numero"))
    
numero=str(numero).zfill(13)

billon=int(numero[0])
numero_leido=billones[billon]

milmillones="".join(numero[1:4])
if milmillones!="000":
    milmillones=armar_cientos(milmillones)
    numero_leido=numero_leido+milmillones+ " mil "
    
millones=numero[4:7]
if millones!="000":
    millones=armar_cientos(millones)
    numero_leido=numero_leido+millones+ " millones "
    
mil=numero[7:10]
if mil!="000":
    mil=armar_cientos(mil)
    numero_leido=numero_leido+mil+ " mil "
    
cientos=numero[10:13]
if cientos!="000":
    cientos=armar_cientos(cientos)
    numero_leido=numero_leido+cientos
if numero=="0000000000000":
    numero_leido="cero"

print(numero_leido)
