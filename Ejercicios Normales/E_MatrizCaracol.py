def descomponer(n):
    suma = 0
    while(n != 0):
        aux = n%10
        n //= 10
        suma += aux
    return suma
n = int(input())
matriz =[[0]*n for i in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
pos = 0

x, y = 0, 0
valor = 1
for i in range(n*n):
    matriz[x][y] = descomponer(valor)
    valor += 1
    if(x + dx[pos] < 0 or x + dx[pos] >= n or y + dy[pos] < 0 or y + dy[pos] >= n or matriz[x + dx[pos]][y + dy[pos]] != 0):
        pos = (pos + 1)%4
    x += dx[pos]
    y += dy[pos]

for i in range(n):
    for j in range(n):
        if(j == n-1):
            print(matriz[i][j], end="\n")
        else:
            print(matriz[i][j], end=" ")
