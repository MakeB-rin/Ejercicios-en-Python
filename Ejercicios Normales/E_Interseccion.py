a, b = map(int, input().split())

lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

lista1 = set(lista1)
lista2 = set(lista2)
interseccion = lista1 & lista2

print(len(interseccion))
#intersección
