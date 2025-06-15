caracter = input()
# ord convierte a su valor ascii
num_caracter = ord(caracter)

if(num_caracter >= 65 and num_caracter <= 90):
    if(caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U'):
        print("mayuscula")
        print("vocal")
    else:
        print("mayuscula")
        print("consonante")

if(num_caracter >= 97 and num_caracter <= 122):
    if(caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u'):
        print("minuscula")
        print("vocal")
    else:
        print("minuscula")
        print("consonante")
