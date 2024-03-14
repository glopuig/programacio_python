def nombre_triangular(n):
    x=0
    for i in range (1,n+1):
        
        x=x+i
        print(i,"-->",x)

nombre=int(input("~FET AMB FOR~""\n""Nombre al qual vols arribar = "))
print("\n")

nombre_triangular(nombre)


def nombre_triangularr(nn):
    xx=0
    ii=1
    while ii<=nn:
        
        xx=xx+ii
        
        print(ii,"-->",xx)
        
        ii+=1
        
print("\n""~FET AMB WHILE~""\n")
print("\n")

nombre_triangularr(nombre)