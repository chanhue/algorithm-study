cnt_p = []
m, p = map(int, input().split())
cnt_p.append(p)
for i in range(1,10):
    m, p = map(int, input().split())
    cnt_p.append(cnt_p[i-1] - m + p)
max = 0
for i in range(10):
    if cnt_p[i] > max:
        max = cnt_p[i]
print(max)