from random import*
i=0
x=0
y=0
while not (abs(x)==4 and abs(y)==4):
    d=randint(1,4)
    if d==1:
        x=x+1
    elif d==2:
        x=x-1
    elif d==3:
        y=y+1
    elif d==4:
        y=y-1
    
    if x==5:
        x=4
    elif x==-5:
        x=-4
    elif y==5:
        y=4
    elif y==-5:
        y=-4
    i=i+1
    print("(",x,",",y,") amb :",i,"Intents")