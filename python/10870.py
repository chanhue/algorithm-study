n = int(input())
ls = []
for i in range(n+1):
    if i == 0:
        ls.append(0)
    elif i == 1:
        ls.append(1)
    else:
        ls.append(ls[i-2]+ls[i-1])
print(ls[n])