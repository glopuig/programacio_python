
def primer(n):
    contador=0
    for i in range(1,n+1):
        if n%i==0:
            contador=contador+1
    if contador>2:
        return "no és 1primer"
    else:
        return "és primer"
        

nombre=int(input("n = "))
print ("El nombre",nombre,primer(nombre))        