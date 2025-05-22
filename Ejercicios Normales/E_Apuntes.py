while True:
    try:

        cadena = input().lower()
        palabra = input().lower()

        # remplaza los espacios por nada
        texto = palabra.replace(" ","")

        #busca una subcadena find
        posicion = cadena.find(texto)

        if posicion != -1:
            posicion += 1
            print(posicion)
        else:
            print(-1)
    except EOFError:
        break
        
