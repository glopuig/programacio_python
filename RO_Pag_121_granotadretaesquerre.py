from random import*
x=10
i=0

while 0<x<20:
    direccio=randint (1,2)
    if direccio==1:
        x=x+1
    elif direccio ==2:
        x=x-1
    i=i+1
    print("Salt",i,"    ""La granota està a la posició -->",x)