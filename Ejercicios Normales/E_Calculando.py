try:

    operacion = input()
    resultado = eval(operacion)
    print(f"{resultado:.2f}")

except ZeroDivisionError:
    print("division entre cero")

