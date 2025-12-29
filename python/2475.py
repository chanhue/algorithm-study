import sys
ls = list(map(int, sys.stdin.readline().split()))
num = 0
for i in range(5):
    num += ls[i]**2
print(num%10)