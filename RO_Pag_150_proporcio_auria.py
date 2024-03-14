n=int(input("nombre al qual vols arribar = "))
print("Parelles de numeros (a,b) entre 1 i n")
print("=====================================")
for a in range(1,n+1):
    for b in range(1,n+1):
        print("(",a,",",b,")")
        if  ((a+b)/b)==a/b:
            print("^^^aquesta parella cumpeix la proporció àuria^^^")