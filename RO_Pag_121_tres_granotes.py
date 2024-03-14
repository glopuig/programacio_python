from random import*

x=0
y=0
z=0
i=0
a=2
arribada=int(input("A quants metres han d'arribar les granotes = "))
while a==2:
    
    aleatorip=randint(1,4)
    if aleatorip==1:
        x=x
    elif aleatorip==2:
        x=x+0.5
    elif aleatorip==3:
        x=x+1
    elif aleatorip==4:
        x=x-0.5
        
    aleatoris=randint(1,4)
    if aleatoris==1:
        y=y
    elif aleatoris==2:
        y=y+0.5
    elif aleatoris==3:
        y=y+1
    elif aleatoris==4:
        y=y-0.5

    aleatorit=randint(1,4)
    if aleatorit==1:
        z=z
    elif aleatorit==2:
        z=z+0.5
    elif aleatorit==3:
        z=z+1
    elif aleatorit==4:
        z=z-0.5
    i=i+1
    
    print("Salt numero",i,":     ""Posició Granota 1 -->",x,"     ","Posició Granota 2 -->",y,"     ""Posició Granota 3 -->",z,)
    if x>=arribada:
        break
    elif y>=arribada:
        break
    elif z>=arribada:
        break

if x>=arribada:
    print("Ha guanyat la granota 1!")
elif y>=arribada:
    print("Ha guanyat la granota 2!")
elif z>=arribada:
    print("Ha guanyat la granota 3!")