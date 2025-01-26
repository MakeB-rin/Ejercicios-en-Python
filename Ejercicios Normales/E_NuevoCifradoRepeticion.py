def descifrar_cadena(n, t):

    s = []
    i = 0  # Índice para recorrer la cadena cifrada


    #ooopppssss
    while i < n: # 0 + 1 = 1, 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10
        repeticiones = len(s) + 1  # El número de repeticiones esperadas
        s.append(t[i])  # Agregamos el carácter correspondiente a la cadena original
        i += repeticiones  # Saltamos a la siguiente posición considerando las repeticiones

    return "".join(s)


# Entrada
n = int(input())  # Longitud de la cadena cifrada
t = input().strip()  # Cadena cifrada

# Procesamos y mostramos la salida
resultado = descifrar_cadena(n, t)
print(resultado)
