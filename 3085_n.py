# 브루트포스 알고리즘

ls = []
max = 1
n = int(input())
for i in range(n):
    ls.append(input())
for i in range(n):
    for j in range(n):
        print(ls[i][j])