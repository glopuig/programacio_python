pi=3.1415926535897932384626433832795028841971
def prin(A,P):
    print("Àrea = ",A,"\n""Perímetre = ",P)

def quadrat(a):
    A=a**2
    P=4*a
    
    prin(A,P)

def triangle(a,b,c,h):
    A=(a*h)/2
    P=a+b+c
    prin(A,P)

def rectangle(a,b):
    A=b*a
    P=2*(b+a)
    prin(A,P)

def paralelogram(a,b,h):
    A=b*h
    P=2*(b+a)
    prin(A,P)

def rombe(D,d,a):
    A=(D*d)/2
    P=4*a
    prin(A,P)
    
def cometa(D,d,a,b):
    A=(D*d)/2
    P=2*(a+b)
    prin(A,P)
    
def trapeci(B,b,h,a,c):
    A=((B+b)*h)/2
    P=B+b+a+c
    prin(A,P)
    
def cercle(r):
    A=pi*(r**2)
    P=2*pi*r
    prin(A,P)
    
def poligonregular(n,a,b):
    P=n*b
    A=(P*a)/2
    prin(A,P)
    
def coronacircular(R,r):
    A=pi*((R**2)-(r*2))
    P="Not calculated"
    prin(A,P)
    
def sectorcircular(r,n):
    A=(pi*(r**2)*n)/360
    P="Not calculated"
    prin(A,P)

opcio=int(input("\n""1.Quadrat""\n""2.Triangle""\n""3.Rectangle""\n""4.Paralelogram""\n""5.Rombe""\n""6.Cometa""\n""7.Trapeci""\n""8.Cercle""\n""9.Poligon regular""\n""10.Corona circular""\n""11.Sector circular""\n""Quina opció vols? = "))

if opcio==1:
    print("\n""~QUADRAT~""\n")
    costat=float(input("Costat del quadrat ="))
    print("\n")
    quadrat(costat)
    
elif opcio==2:
    print("\n""~TRIANGLE~""\n")
    costat1=float(input("Primer costat (base) del triangle ="))
    costat2=float(input("Segon costat del triangle ="))
    costat3=float(input("Tercer costat del triangle ="))
    altura=float(input("Altura del triangle ="))
    print("\n")
    triangle(costat1,costat2,costat3,altura)
        
elif opcio==3:
    print("\n""~RECTANGLE~""\n")
    base=float(input("Base del rectangle ="))
    altura=float(input("Altura del rectangle ="))
    print("\n")
    rectangle(altura,base)

elif opcio==4:
    print("\n""~PARALELOGRAM~""\n")
    base=float(input("Base del paralelogram ="))
    costat=float(input("Costat inclinat del paralelogram ="))
    altura=float(input("Altura del paralelogram ="))
    print("\n")
    paralelogram(costat,base,altura)
    
elif opcio==5:
    print("\n""~ROMBE~""\n")
    costat=float(input("Mesura dels costats del rombe ="))
    diagonal1=float(input("Digonal llarga del rombe ="))
    diagonal2=float(input("Digonal curta del rombe ="))
    print("\n")
    rombe(diagonal1,diagonal2,costat)
    
elif opcio==6:
    print("\n""~COMETA~""\n")
    costat=float(input("Mesura dels costats curts del cometa ="))
    costat1=float(input("Mesura dels costats llargs del cometa ="))
    diagonal1=float(input("Digonal llarga del cometa ="))
    diagonal2=float(input("Digonal curta del cometa ="))
    print("\n")
    cometa(diagonal1,diagonal2,costat,costat1)

elif opcio==7:
    print("\n""~TRAPECI~""\n")
    baseg=float(input("Base gran del trapeci ="))
    basep=float(input("Base petita del trapeci ="))
    costata=float(input("Costat del trapeci ="))
    costatc=float(input("Costat del trapeci ="))
    altura=float(input("Altura del trapeci ="))
    print("\n")
    trapeci(baseg,basep,altura,costata,costatc)

elif opcio==8:
    print("\n""~CERCLE~""\n")
    radi=float(input("Radi del cercle ="))
    print("\n")
    cercle(radi)

elif opcio==9:
    print("\n""~POLIGON REGULAR~""\n")
    costats=float(input("Nombre de costats del poligon ="))
    altura=float(input("La meitat de l'altura del poligon ="))
    costat=float(input("Quan mesuren els costats del poligon ="))
    poligonregular(costats,altura,costat)

elif opcio==10:
    print("\n""~CORONA CIRCULAR~""\n")
    radig=float(input("Radi interior del cercle ="))
    radip=float(input("Radi exterior del cercle ="))
    coronacircular(radig,radip)

elif opcio==11:
    print("\n""~SECTOR CIRCULAR~""\n")
    radi=float(input("Radi del cercle ="))
    graus=float(input("Graus del sector circular ="))
    sectorcircular(radi,graus)