import sys

n = int(input())
dic = {}

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x not in dic:
        dic[x] = [y]
    else:
        dic[x].append(y)

for x in sorted(dic.keys()):
    dic[x].sort() 
    for y in dic[x]:
        print(x, y)