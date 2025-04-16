ls = []
sum = 0
for i in range(9):
    a = int(input())
    ls.append(a)
    sum += a
ls.sort()
remain = sum - 100
correct = ls[:]

for i in range(9):
    correct.remove(ls[i])
    for j in range(8):
        correct
        