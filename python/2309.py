import sys
ls = []
sum = 0

def find(ls, sum):
    for i in range(9):
        tmp = ls[:]
        tmpsum = sum
        tmpsum -= tmp.pop(i)
        for j in range(8):
            tmp2 = tmp[:]
            tmp2sum = tmpsum
            tmp2sum -= tmp2.pop(j)
            if tmp2sum == 100:
                return tmp2

for i in range(9):
    a = int(sys.stdin.readline())
    ls.append(a)
    sum += a
ls.sort()
ans = find(ls,sum)
for i in range(7):
    print(ans[i])