arribar=int(input("Fins a quin nombre volem comprobar: "))
def conteo(n):
    s=0
    for i in range (1, n+1):
        if n%i==0:
            s=s+1
    return s
a=1

for n in range (1, arribar):
    if conteo(n)>conteo(a):
        a=n

print(a)