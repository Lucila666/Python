#1. Desarrollar un programa para eliminar todos los comentarios de un programa escrito
#en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
#signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
#y que también se considera comentario a las cadenas de documentación
#(docstrings).

#Ejercicio 1:
try:
    entrada=open("guia 1.txt","rt")
    salida=open("guia modificada.txt","wt")
    
    for linea in entrada:
        if linea[0]!="#":
            if linea.find("\"\"\"")!=-1:
                if linea.rfind("\"\"\"")==-1:
                    bandera=True
                    while bandera==True:
                        entrada.readline()
                        if linea.find("\"\"\""):
                            bandera=False
            else:    
                salida.write(linea)
        
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:",mensaje)
except OSError as mensaje:
    print("Error:", mensaje)
else:
    print("Copia finalizada")
    
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass
