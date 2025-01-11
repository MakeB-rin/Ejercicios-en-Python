m, n = map(int, input().split())
dpalabras = {}

for casos in range(m):
    palabra, monto = input().split()
    monto = int(monto)
    dpalabras[palabra] = monto

# cuando leemos con un input una frase solo se lee la primera linea si hay otra linea abajo no la lee
for i in range(n):
    s = 0
    texto = ""
    while True:
        # leemos la frase y eliminamos los espacios
        frase = input().strip()
        # si la frase está vacía, hemos terminado la entrada para esta tarea
        if frase == ".":
            break
        # concatenamos la frase con un espacio al final
        texto += frase + " "

    separar = texto.split()
    for palabra in dpalabras:
        contar = separar.count(palabra)
        if contar > 0:
            s += (dpalabras[palabra]*contar)
    print(s)
