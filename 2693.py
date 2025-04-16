T = int(input())
for i in range(T):
    ls = list(map(int, input().split()))
    ls.sort()
    print(ls[7])
