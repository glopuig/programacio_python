def conteo(n):
    i=n
    contador=0
    while i > 0:
        if n%i==0:
            contador = contador+1
        i=i-1
    return contador

new = 0
maxim = 0
for n in range(1,101):
    print("El nombre",n,"té",conteo(n),"divisors")
    new=conteo(n)
    if new>maxim:
        maxim = new
        numero = n
    
print("El nombre que més divisors té és el número",numero)