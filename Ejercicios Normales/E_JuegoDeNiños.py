# Ejercicios
n = int(input())
while (n != 0):
    v = list(map(str, input().split()))
    v.sort()
    v.reverse()

    cad = ""
    for i in range(0, n):
        cad = cad + v[i]
    print(cad)
    n = int(input())
