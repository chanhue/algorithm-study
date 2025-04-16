m = int(input())
n = int(input())
min = 0
cnt = 0
sum = 0

for i in range(m,n+1):
    if i < 2:
        continue
    prime = True
    for ii in range(2, i):
        if i%ii == 0:
            prime = False
    if prime == True:
        if cnt == 0:
            min = i
        sum += i
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(sum)
    print(min)

#1은 소수 아니다 찬희야