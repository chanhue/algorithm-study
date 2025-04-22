n, b = input().split()
b = int(b)
result = 0

for i in range(len(n)):
    if ord(n[len(n) - 1 - i])<65:
        result += int(n[len(n) - 1 - i]) * b**i
    else:
        result += (ord(n[len(n) - 1 - i])-55) * b**i
print(result)

# 파이썬에선 int 내장함수로 바로 진법변환 가능
# n, b = input().split()
# print(int(n, int(b)))