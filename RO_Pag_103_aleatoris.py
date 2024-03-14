
from random import*
x=int(input("El numero que vols que surti = "))
i=x+1
c=0
while i!=x:
    i=randint(1,6)
    c=c+1
print ("El nobre de vegades que s'ha hagut de tirar el dau per a que surtis",x,"han sigut",c,"tirades")