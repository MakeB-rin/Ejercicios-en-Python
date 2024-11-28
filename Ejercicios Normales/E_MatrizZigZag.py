# Ejercicio
n = int(input())
matriz =[[0]*n for i in range(n)]
dx = [1, -1, 0, 1]
dy = [0, 1, 1, -1]
x, y = 0, 0

valor = 1
pos = 3
for i in range(n*n):
    matriz[x][y] = valor
    valor += 1
    if(pos == 0 or pos == 2):
        pos = (pos + 1)%4
    while(x + dx[pos] < 0 or x + dx[pos] >= n or y + dy[pos] < 0 or y + dy[pos] >= n or matriz[x + dx[pos]][y + dy[pos]] != 0) and i != (n*n) - 1:
        pos = (pos + 1)%4
    x += dx[pos]
    y += dy[pos]

for i in range(n):
    for j in range(n):
        if(j == n-1):
            print(matriz[i][j], end="\n")
        else:
            print(matriz[i][j], end=" ")
