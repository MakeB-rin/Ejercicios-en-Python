import math
def esCuadradoPerfecto(numero):
    if numero < 0:
        return False
    raiz = int(math.isqrt(numero))
    return  raiz * raiz == numero


def subsecuencia_no_cuadrado(lista_numeros):
    for x in lista_numeros:
        if not esCuadradoPerfecto(x):
            return True
    return False

casos = int(input())
for _ in range(casos):
    numero = int(input())
    lista_numeros = list(map(int, input().split()))
    if(subsecuencia_no_cuadrado(lista_numeros)):
        print("YES")
    else:
        print("NO")

#Vector perfectamente imperfecto
