#RO_Pag030_obrers.py

ht=float(input("hores treballades = "))
tarifa=float(input("tarifa per hora = "))
descomptes=float(input("descomptes = "))

if ht>40:
    exces=ht-40
    tarifa1=40*tarifa
    tarifaextra=exces*tarifa*1.5
    
else:
    tarifa1=ht*tarifa
    tarifaextra=0
    
pago=tarifa1+tarifaextra-descomptes

print("Salari de l'obrer = ",pago,"€")