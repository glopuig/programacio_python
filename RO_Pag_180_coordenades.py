from math import*

x=float(input("x = "))
y=float(input("y = "))

r=sqrt((x**2)+(y**2))
fi_rad=atan2(y,x)
fi_grau=fi_rad*(180/pi)

print("La r val -->",r,"          /          L'angle és de -->",fi_grau,"º          /          L'angle és de",fi_rad,"rad.")