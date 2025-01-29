import sys
def numeros_con_dos_bits_en_uno(n):
    resultado = []

    for i in range(32):
        for j in range(i + 1, 32):
            num = (1 << i) + (1 << j)
            resultado.append(num)

    resultado.sort()
    return resultado[:n]

for caso in sys.stdin:
    n = int(caso)
    print(" ".join(map(str, numeros_con_dos_bits_en_uno(n))))
