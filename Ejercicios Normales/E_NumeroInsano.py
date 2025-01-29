def encontrar_diferente(lista):
    diccionario = {}
    for num in lista:
        diccionario[num] = diccionario.get(num, 0) + 1


    for num, count in diccionario.items():
        if count == 1:
            return num, lista.index(num)


casos = int(input())
for i in range(casos):
    lista = list(input().split())
    resultado, posicion = encontrar_diferente(lista)

    if posicion == 0:
        print("Herland")
    elif posicion == 1:
        print("Sami")
    else:
        print("Luisin")
