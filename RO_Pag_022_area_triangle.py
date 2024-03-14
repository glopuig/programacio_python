# RO_P022_area_triangle.py
from math import* 

a = float(input("a = ")) # entrada de dades reals
b = float(input("b = "))
c = float(input("c = "))
    
t = (a+b+c)/2 # variables
s = math.sqrt(t*(t-a)*(t-b)*(t-c)) # càlculs
print("t =", t)
print("s =", s)  # sortida de dades
