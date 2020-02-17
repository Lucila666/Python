#2. Una oficina cuenta con dos cajas fuertes cuyas claves son
#numeros de 4 cifras. Para evitar extraviarlos
#se los combino formando un solo numero de 8 digitos, donde las
#posiciones pares corresponden a una de las cajas y las impares a
#la otra. Desarrollas un programa para ingresar la clave combinada
#y separar en dos variables las claves de cada caja fuert.
#Mostrar ambos codigos por pantalla.
#Por ej si se ingresa 19283746 debe mostrarse 1234 y 9876.
#rechazar el numero si no contiene 8 digitos.

clave1=[]
clave2=[]
for i in range(8):
    num=int(input("Ingrese digito de la clave"))
    if i%2==0:
        clave1.append(num)
    else:
        clave2.append(num)
        
print(clave1)
print(clave2)