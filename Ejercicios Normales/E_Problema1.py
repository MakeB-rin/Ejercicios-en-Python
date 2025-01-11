import sys
"""Calcula el MCD de dos números usando el Algoritmo de Euclides."""
def maximo_comun_divisor(a, b):
    while b != 0:

        a, b = b, a % b
    return a

for multiplescasos in sys.stdin:
    a, b = map(int, multiplescasos.split())
    mcd = maximo_comun_divisor(a, b)
    if mcd == 1:
        print("PRIMOS AMIGOS")
    else:
        print("PRIMOS ENEMIGOS")
