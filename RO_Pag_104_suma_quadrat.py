n=int(input("El nombre al que vols arribar = "))
s=0
i=1

while i<=n:
    c=i**2
    s=s+c
    i=i+1
    
print ("Tots els quadrats fins el nombre",n,"sumen",s)