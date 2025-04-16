T = int(input())
ls = []
for i in range(T):
    n = int(input())
    while n>=1:
        # print(n%2)
        ls.append(n%2)
        n = n//2
    for j in range(0, len(ls)):
        if ls[j] == 1:
            print(j, end=' ')
    ls = []
    print()