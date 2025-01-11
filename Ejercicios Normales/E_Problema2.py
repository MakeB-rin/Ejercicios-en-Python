numlistaN = int(input())
listaNegra = []
for casos in range(numlistaN):
    n = input()
    listaNegra.append(n)

numlista = int(input())
lista = []
for casos in range(numlista):
    n = input()
    lista.append(n)
 # el if verifica si el nombre se encuentra dentro la lista negra
for nombre in lista:
    if nombre in listaNegra:
        print("SSS")
    else:
        print("-")
