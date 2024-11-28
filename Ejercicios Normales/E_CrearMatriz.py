#Ejercicio
#Cantidad Filas, Columnas
n, m = map(int, input().split())
#Leer una matriz de n filas y m columnas
matriz = []
# Llenar un matriz con datos por teclado

for i in range(0, n):
    v = list(map(int,input().split()))
    matriz.append(v)

for i in range(0 ,n):
    for j in range(0, m):
        print(matriz[i][j], end=" ")
    print()
