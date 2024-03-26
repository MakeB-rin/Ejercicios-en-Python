n = int(input())

a = -1
b = 1
c = 0

for i in range(0,n):
    c = a + b
    if(i == n-1):
        print(c, end = "")
    else:
        print(c, end = " ")
    a = b
    b = c
