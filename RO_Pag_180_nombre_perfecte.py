def perfecte(n):
    suma_dels_divisors=0
    for i in range(1, n):
        if n % i == 0:
            suma_dels_divisors=suma_dels_divisors+i
    if suma_dels_divisors==n:
        print("El nombre",n,"és perfecte")

for n in range (1,1001):
    perfecte(n)