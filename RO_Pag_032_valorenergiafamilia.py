#RO_Pag032_valorenergiafamilia.py
kwh=float(input("Kw gastats per una família = "))
kwheuros=float(input("Precio por Kw = "))

if kwh>700:
    exces=kwh-700
    tarifa1=700*kwheuros
    tarifaextra=exces*kwheuros*1.05
    
else:
    tarifa1=kwh*kwheuros
    tarifaextra=0
    
pago=tarifa1+tarifaextra

print("Preu a pagar per la família = ",pago,"€")