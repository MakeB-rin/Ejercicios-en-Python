import re

def contrasenia_segura(palabra):
    #verifica la longitud minima de 10 caracteres
    if len(palabra) < 10:
        return False

    #Verifica al menos 4 numeros
    #re.findall Busca
    if len(re.findall(r'\d', palabra)) < 4:
        return False

    #Verifica al menos 2 letras mayusculas
    if len(re.findall(r'[A-Z]', palabra)) < 2:
        return False

    #Verifica al menos 2 letras mayusculas
    if len(re.findall(r'[a-z]', palabra)) < 2:
        return False

    #Verifica al menos 1 caracter especial
    #si existe al menos una coincidencia re.search return false, true
    if not re.search(r'[*!#<>]', palabra):
        return False
    return True

n = int(input())
for i in range(n):
    palabra = input()
    if contrasenia_segura(palabra):
        print("Segura")
    else:
        print("Debil")
