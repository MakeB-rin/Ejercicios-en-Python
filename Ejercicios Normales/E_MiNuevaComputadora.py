t = int(input())
numeros = [0] * 10
for casos in range(0, t):
    c, n, p = input().split()
    n, p = int(n), int(p)

    if(c == '+'):
        numeros[p] += n
    if(c == '-'):
        numeros[p] -= n
    if(c == '*'):
        numeros[p] *= n
    if(c == '/'):
        numeros[p] = int(numeros[p]//(n))

for i in range(0, 5):
    if i == 4:
        print(numeros[i], end="")
    else:
        print(numeros[i], end=" ")
