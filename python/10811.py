n, m = map(int, input().split())
bucket = [i for i in range(1,n+1)]
for i in range(m):
    a, b = map(int, input().split())
    bucket[a-1:b] = bucket[a-1:b][::-1]
for i in range(n):
    print(bucket[i], end=' ')
