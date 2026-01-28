import sys
n = int(sys.stdin.readline())

for i in range(n):
    dn, point = map(int, sys.stdin.readline().split())
    ls = list(sys.stdin.readline().split())

    cnt = 1
    while ls:
        if ls[0] < max(ls):
            ls.append(ls.pop(0))
        else:
            if point == 0:
                break
            else:
                ls.pop(0)
                cnt += 1
        if point > 0:
            point = point - 1
        else:
            point = len(ls) - 1

    print(cnt)