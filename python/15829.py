import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
h = 0
r = 31
for i in range(n):
    tmp = ord(s[i])-96
    h += r**i * tmp
h = h%1234567891
print(h)