a = int(input())
numlist = map(int,input().split())
cnt = 0
for i in numlist:
    prime = True
    if i == 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break
    if prime == True:
        cnt += 1
print(cnt)