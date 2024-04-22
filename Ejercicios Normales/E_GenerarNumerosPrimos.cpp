N = int(input())
pr = 2
j = 1
while j <= N:
    i = 2
    flag = True
    while i*i <= pr:
        if pr%i == 0:
            flag = False
            break
        i = i + 1

    if flag == True:
        print(pr, end = " ")
        j = j + 1
    pr = pr + 1
