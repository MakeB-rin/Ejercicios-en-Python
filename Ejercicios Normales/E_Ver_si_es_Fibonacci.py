import sys
def es_cuadrado_perfecto(numero):
    if numero < 0:
        return False
    raiz = int(numero**0.5)

    return raiz * raiz == numero

def es_fibonacci(n):
    return es_cuadrado_perfecto(5 * n * n + 4) or es_cuadrado_perfecto(5 * n * n - 4)

for casos in sys.stdin:
    numero = int(casos)
    if es_fibonacci(numero):
        print(f"{numero} is a Fibonacci Number")
    else:
        print(f"{numero} is a not Fibonacci Number")
