num = int(input())
q = [[0]*2 for i in range(num)]
for i in range(num):
    k = int(input())
    n = int(input())
    q[i][0] = k
    q[i][1] = n
kmax = max(q)[0]
apt = [[0]*14 for i in range(kmax+1)]
for i in range(len(apt[0])):
    apt[0][i]=i+1
for i in range(1,kmax+1):
    for j in range(14):
        tmp = 0
        for k in range(j+1):
            tmp += apt[i-1][k]
        apt[i][j] += tmp
for i in range(num):
    print(apt[q[i][0]][q[i][1]-1])