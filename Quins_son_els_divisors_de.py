nombre=int(input("Vull trobar tots els divisors de: "))
def conteo(n):
    v=[]
    for i in range (1, n+1):
        if n%i==0:
            v=v+[i]
    return v
print(conteo(nombre))