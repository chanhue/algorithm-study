import sys

n = int(sys.stdin.readline())
ans = list(sys.stdin.readline())
for i in range(n-1):
    input = sys.stdin.readline()
    for i in range(len(input)):
        if ans[i] != input[i]:
            ans[i] = '?'
print(''.join(ans))

#https://www.acmicpc.net/board/view/91661