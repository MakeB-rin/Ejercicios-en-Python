def encontrar_numero(n, k):
    # calcula los primeros n numeros impares
    mitad = (n + 1) // 2

    # k = que es la posicion es menor a los primeros numeros impares (eso quiere decir que esta en ese rango)
    if k <= mitad:
        # formula para calcular el impar en esa posicion
        return 2 * k - 1
    else:
        # formula para calcular el par en esa posicion
        return 2 * (k - mitad)


casos = int(input())

for casos in range(0, casos):
    n, k = map(int, input().split())
    print(encontrar_numero(n, k))

