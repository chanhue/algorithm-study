import sys
n = int(sys.stdin.readline())
ls = [0]*8001
mean = 0.0
median = 0
mode = []
numrange = 0
maxnum = -4001
minnum = 4001
for i in range(n):
    tmp = int(sys.stdin.readline())
    mean += tmp
    ls[tmp+4000] +=1
mean /= n
for i in  range(len(ls)):
    median += ls[i]
    if median >= n/2:
        median = i-4000
        break
for i in range(len(ls)):
    if ls [i] == max(ls):
        mode.append(i-4000)
    if ls[i] >= 1:
        if minnum> i-4000:
            minnum = i-4000
        if maxnum < i - 4000:
            maxnum = i - 4000
range = maxnum-minnum
mode.sort()
print(round(mean))
print(median)
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])
print(range)
