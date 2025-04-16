n, m = map(int, input().split())
min = n
max = m
if m< n:
    min = m
    max = n
for i in range(min, 0, -1):
    if n%i == 0 and m%i ==0:
        print(i)
        break
mul = 1
while(1):
    if (max * mul) % min == 0:
        print(max * mul)
        break
    mul += 1