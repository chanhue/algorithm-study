n = int(input())
size = list(map(int,input().split()))
t, p = map(int, input().split())
shirt = 0
for i in range(6):
    shirt += size[i]//t
    if size[i]%t != 0:
        shirt += 1
print(shirt)
print(n//p, n%p)