# RO_Pag025_01_diametre_cilindre.py

volum = float(input("volum en litres = "))
altura = float(input("altura en metres = "))

diametre = ((volum/1000 * 4) / (3.1416 * altura))**0.5

print("diametre en m = ", diametre)

volum = float(input("volum en metres = "))
altura = float(input("altura en metres = "))

diametre = ((volum * 4) / (3.1416 * altura))**0.5

print("diametre en m = ", diametre)

