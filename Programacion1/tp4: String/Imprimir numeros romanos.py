
lista_unidades=['I','II','III','IV','V','VI','VII','VIII','IX']        
lista_decenas=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
lista_centenas=['C','CC','CCC','CD','D','DC','DC','DCC','DCCC','CM']

numero=int(input("Ingrese un numero"))
while (numero<=0 or numero>3999):
    numero=int(input("Ingrese un numero"))

numero=str(numero)
if len(numero)==4:
    m=int(numero[0])
    c=int(numero[1])
    d=int(numero[2])
    u=int(numero[2])
elif len(numero)==3:
    c=int(numero[0])
    d=int(numero[1])
    u=int(numero[2])
    m=0
elif len(numero)==2:
    d=int(numero[0])
    u=int(numero[1])
    m=0
    c=0
else:
    u=int(numero[0])
    m=0
    c=0
    d=0
    
if u!=0:
    uni=lista_unidades[u-1]
else:
    uni=""
if d!=0:
    dec=lista_decenas[d-1]
else:
    dec=""
if c!=0:
    cen=lista_centenas[c-1]
else:
    cen=""
if m!=0:
    mil=m*'M'
else:
    mil=""
numero_romano=mil+cen+dec+uni
print(numero_romano)
