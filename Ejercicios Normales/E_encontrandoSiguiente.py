# Ejercicio
nroCasos = int(input())
for i in range(0,nroCasos):
    n = int(input())
    if(n == 1):
        print(n)
    else:
        print(f"{(n-1)**3}+{n**3}")
