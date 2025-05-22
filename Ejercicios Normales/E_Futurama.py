def verificar(cadena):

    for i in cadena:
        if i in {'#', '%', '&', '@'}:
            return False

    return True

n, l = map(int, input().split())
cadena = input().split()
tsuma = 0
for palabra in cadena:
    if not (verificar(palabra)):
        tsuma += 1

if tsuma <= l:
    print("Si se estrena")
else:
    print("Adios Futurama")
