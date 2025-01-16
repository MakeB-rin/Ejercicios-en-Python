import sys
def es_panagram(cadena):
    #caracter.isalpha() devuelve true si es letra (minuscula o mayuscula)
    # y False si es otro simbolo o numero
    cadena = ''.join([caracter.lower() for caracter in cadena if caracter.isalpha()])

    nueva_cadena = set(cadena)
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")

    # Verifica si nueva_cadena contiene al menos todas las letras del alfabeto
    # return true o false(no importa el orden)
    return nueva_cadena >= alfabeto

for casos in sys.stdin:
    #cuando son multiples casos solo se pone casos
    cadena = casos
    if casos == "*":
        break

    resultado = es_panagram(cadena)
    if resultado:
        print("Y")
    else:
        print("N")

#Ejemplos como usar
'''palabra = "Hola mundo123"
palabra = ''.join([caracter.lower() for caracter in palabra if caracter.isalpha()])

print(palabra)'''
