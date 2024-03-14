#RO_020_areatriangle.py
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

t = (a+b+c)/2
s = math.sqrt(t*(t-a)*(t-b)*(t-c))
print("t =", t)
print("s =", s)