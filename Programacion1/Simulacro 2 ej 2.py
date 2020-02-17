#2. Desarrollar un programa que permita ingresar una palabra a traves del teclado y la busque en un archivo de texto,
#reemplazando todas sus apariciones por otra palabra ingresada por el usuario. Deben evitarse los falsos positivos.
#Programa Principal
buscar=input("Que palabra desea buscar?")
reemplazo=input("Con que palabra desa reemplazarla?")

try:
    entrada=open("segundoparcial.txt","rt")
    salida=open("modificado.txt","wt")
    
    for linea in entrada:
        while buscar in linea:
            inicio=linea.find(buscar)
            final=inicio+len(buscar)
            linea=linea[0:inicio]+reemplazo+linea[final:]
            
        salida.write(linea+"\n")
                    
    
except FileNotFoundError as mensaje:
    print("Error:", mensaje)
except OSError as mensaje:
    print("Error:", mensaje)
    
else:
    print("Se modifico el archivo correctamente")
    
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass