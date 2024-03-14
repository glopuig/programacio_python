#RO_Pag028_vendrellantas.py

n = float(input("Quantitat de llantas = "))
p = float(input("Preu individual de la llanta = "))

if n>4:
    p=p*0.9
else:
    p=p
t=p*n

print("Preu total = ", t, "€")