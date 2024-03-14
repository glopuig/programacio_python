#RO_Pg_25_areaivolumdunquadrat.py
altura = float(input("altura = "))
profunditat = float(input("profunditat = "))
amplada = float(input("amplada = "))

area = (altura*profunditat)*2+(profunditat*amplada)*2+(amplada*altura)*2

volum=altura*profunditat*amplada

print("Area = ", area)
print("Volum = ", volum)