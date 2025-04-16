N = int(input())
min = 1000000
max = -1000000
ls = map(int, input().split())
for i in ls:
    if i>max:
        max = i
    if i<min:
        min = i
print(min, max)