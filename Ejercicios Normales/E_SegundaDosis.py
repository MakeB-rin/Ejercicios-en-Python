# Ejercicio
from datetime import datetime
from datetime import timedelta

nroCasos = int(input())
for i in range(0,nroCasos):

    fecha, id = input().split()
    id = int(id)
    a = int(fecha[0:4])
    m = int(fecha[5:7])
    y = int(fecha[8:10])
    fechaactual = datetime(a,m,y)
    if(id == 5):
        print("NO APLICA")
    else:
        F1=F2=fechaactual
        if(id == 1):
            F1 = F1 + timedelta(days=21)
            F2 = F2 + timedelta(days=42)
        elif(id == 2):
            F1 = F1 + timedelta(days=56)
            F2 = F2 + timedelta(days=84)
        elif(id == 3) or (id == 4):
            F1 = F1 + timedelta(days=21)
            F2 = F2 + timedelta(days=28)

        print(f"{F1.year:04}-{F1.month:02}-{F1.day:02} {F2.year:04}-{F2.month:02}-{F2.day:02}")
