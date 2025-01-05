def calcularModulo(a, m):
    residuo = 0
    for digito in a:
        residuo = (residuo * 10 + int(digito))%m
    return residuo

n = int(input())
for i in range(n):
    a, m = input().split()
    print(calcularModulo(a,int(m)))
