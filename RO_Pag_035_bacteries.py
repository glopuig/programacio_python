#RO_Pag035_bacteries.py

x=int(input("Quantitat inicial de bacteries = "))
m=int(input("Quantitat màxima de bacteries = "))
d=0

while x<=m:
    x=2*x
    d=d+1
print ("dies = ",d)