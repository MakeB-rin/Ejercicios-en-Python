import sys
def convertirNumero(cadena):
    ceros_contados = 0
    encontrado_uno = False

    for char in cadena:
        if char == '1' and not encontrado_uno:
            encontrado_uno = True
        elif encontrado_uno and char == '0':
            ceros_contados += 1
        if ceros_contados >= 3:
            return "SI"

    return "NO"

for casos in sys.stdin:
    entradas = casos.strip()
    resultados = convertirNumero(entradas)
    print(resultados)
