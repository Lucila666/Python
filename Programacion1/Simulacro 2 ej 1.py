#1. Desarrollar una funcion recursiva para determinar si un numero entero es primo o no. la funcion recibe el numero
#como parametro y vevuelve True o False

def primo(num, div=2):
    if div<num:
        division=num%div
        if division==0:
            bandera=False
            return bandera
        else:
            return primo(num, div+1)
    elif div==num or num==1:
        bandera=True
        return bandera
    
    
#Programa principal
n=int(input("Ingrese un numero"))
resultado=primo(n)
if resultado:
    print(f"El numero {n} es un numero primo")
else:
    print(f"El numero {n} no es un numero primo")