import sys
for multiplesCasos in sys.stdin:
    n = int(multiplesCasos)
    matriz = [[0]*n for i in range(n)]

    #Guardamos en una lista los elementos que nos da la primera fila
    Pfila = list(map(int,input().split()))

    #Guardamos en una lista los elementos que nos da la primera Columna
    Pcolumna = list(map(int,input().split()))

    for i in range(0, n):
        matriz[0][i] = Pfila[i]
        matriz[i][0] = Pcolumna[i]

    for i in range(1, n):
        for j in range(1, n):

            #Sumamos la posicion de arriba, la izquierda y la de arriba a la izquierda
            matriz[i][j] = matriz[i-1][j] + matriz[i][j-1] + matriz[i-1][j-1]

    print(matriz[n-1][n-1])
