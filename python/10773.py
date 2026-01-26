import sys
k = int(sys.stdin.readline())
ls = {}
tmp = []
sum = 0
for i in range(k):        
    num = int(sys.stdin.readline())
    if num == 0:
        ls[tmp[-1]] -= 1
        tmp.pop()
        continue
    if num in ls:
        ls[num] += 1
    else:
        ls[num] = 1
    tmp.append(num)
for i in ls:
    sum += i*ls[i]
print(sum)
    
