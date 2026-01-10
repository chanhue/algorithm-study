n = int(input())
ls = {}
for i in range(n):
    tmp = input()
    ls[tmp] = len(tmp)
    
for i in range(50):
    tmpls = list()
    for j in ls:
        if ls[j]==i+1:
            tmpls.append(j)
    tmpls.sort()
    for k in tmpls:
        print(k)