t = int(input())
for i in range(t):
    q, d, n, p = 0, 0, 0, 0
    c = int(input())
    q = c//25
    c = c%25
    d = c//10
    c = c%10
    n = c//5
    c = c%5
    p = c
    print(q, d, n, p)