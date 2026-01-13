import sys
n = int(sys.stdin.readline())
ls = [0]*2000001
for i in range(n):
    num = int(sys.stdin.readline())
    ls[num + 1000000] += 1
for i in range(len(ls)):
    if ls[i]==1:
        print(i-1000000)