def contar_vocales(cad):
    cnt = 0
    for i in range(0, len(cad)):
        if (cad[i]=='a' or cad[i]=='e' or cad[i]=='i' or cad[i]=='o' or cad[i]=='u'):
            cnt += 1

    return cnt

cadena = list(input().split())
for i in range(0, len(cadena)-1):
    for j in range(i + 1, len(cadena)):
        if contar_vocales(cadena[i]) > contar_vocales(cadena[j]):
            aux = cadena[i]
            cadena[i] = cadena[j]
            cadena[j] = aux

for i in range(0, len(cadena)):
    if i == len(cadena)-1:
        print(cadena[i],end="")
    else:
        print(cadena[i],end=" ")
