n = int(input("Cops q vols posar nombres a la llista : "))
v=[]

for i in range (1,n+1):
    seguent=int(input("Següent nombre de la llista : "))
    v=v+[seguent]

s=0
for t in v:
    if t%2==0:
        s=s+t
        
print(s)
    