n = int(input())
card = map(int, input().split())
m = int(input())
has = map(int, input().split())
dic = dict()
for i in card:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in has:
    if i not in dic:
        print("0", end= "")
    else:
        print(dic[i], end="")
    m -= 1
    if m != 0:
        print(" ", end="")
