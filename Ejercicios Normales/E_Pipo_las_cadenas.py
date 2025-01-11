def operar_cadena(cadena, operaciones):
    palabra = cadena
    for i in operaciones:
        i = int(i)
        sub_cadena = palabra[-i:]
        palabra = sub_cadena + palabra[:-i]
    return palabra

cadena = input()
casos = int(input())
operaciones = []
for i in range(casos):
    valor = int(input())
    operaciones.append(valor)
res = operar_cadena(cadena,operaciones)
print(res)
