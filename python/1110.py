import sys
n = int(sys.stdin.readline())
num = n
cnt = 0
while True:
    num = (num%10) *10 + (num//10 + num%10)%10
    cnt +=1
    if num == n:
        break
print(cnt)