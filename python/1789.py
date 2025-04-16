s = int(input())
n = 0
i = 1
while s>=i:
    s -= i
    i += 1
    n += 1
print(n)