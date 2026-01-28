n,m = map(int, input().split())
board = ['' for i in range(n)]
minnum = 64
for i in range(n):
    board[i] = list(input())

def findboard(ls):
    num = 0
    color = ls[0][0]
    for i in range(8):
        for j in range(8):
            if i%2 ==0 and j%2 == 0:
                if ls[i][j]!= color:
                    num += 1
            elif i%2 ==1 and j%2 == 0:
                if ls[i][j]== color:
                    num += 1
            elif i%2 ==1 and j%2 == 1:
                if ls[i][j]!= color:
                    num += 1
            else:
                if ls[i][j]== color:
                    num += 1
    if num > 32:
        num = 64-num
    return num

for i in range(n-7):
    for j in range(m-7):
        tmp = findboard([row[j:j+8] for row in board[i:i+8]])
        if tmp < minnum:
            minnum = tmp
print(minnum)