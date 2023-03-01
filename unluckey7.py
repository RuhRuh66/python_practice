K = int(input())

A = [0]
s = 7 % K
A.append(s)
i = 2

flag = True

while flag == True:
    s = ((A[i] % K)*10 + 7) % K
    if s == 0:
        print(i)
        exit()
    i += 1
