def f(x):
    y=2*x**2+1
    return y
def g(x):
    y=3*x**3+5
    return y
for i in range(0,11):
    j=f(i)
    t=g(i)
    print("Quan la x és",i,"--> f(x)=",j,"i g(x)=",t,"\n")