n=int(input("nombre de llençaments = "))
i=1
money=0
d=0
from random import*

while i<=n:
    d=randint(1,6)
    if d==1:
        money=money+1
    elif d==6:
        money=money+5
    elif d==2 or d==3 or d==4 or d==5:
        money=money-2
    print ("Tirada",i,"-->",d)
    i=i+1
    
if money<0:
    print("Li deus al banc un total de",abs(money),"€")

elif money>0:
    print("Has guanyat un total de",money, "€")
    
else:
    print("No has guanyat ni perdut diners")