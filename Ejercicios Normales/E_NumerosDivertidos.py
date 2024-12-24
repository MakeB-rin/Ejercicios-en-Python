def sumaTriangulares(n):
    # Generar números triangulares y almacenarlos en un conjunto
    # crea un conjunto vacío. Un conjunto es una colección de elementos no ordenados y no repetidos

    t = set()
    k = 1
    # := Sin este operador, normalmente tendrías que hacer la asignación
    # en una línea separada y luego evaluar la variable en una expresión posterior
    while (i := k * (k + 1) // 2) <= n:
        t.add(i)
        k += 1
    # Verificar si existe un número triangular T_i tal que n - T_i también sea triangular

    for j in t:
        if (n - j) in t:
            return "SI"
    return "NO"

entradas = int(input())

for entrada in range(entradas):
    n = int(input())
    print(sumaTriangulares(n))
