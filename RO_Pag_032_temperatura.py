#RO_Pag032_temperatura.py

t=float(input("temperatura = "))
p=int(input("p = "))

if p==1:
    c=5/9*(t-32)
    print("temperatura en celcius = ",c)
if p==2:
     f=32+9*t/5
     print("temperatura en farenhait = ",f)

if p>2 or p<1:
    print("p must be 1 or 2")