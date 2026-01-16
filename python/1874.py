import sys
stack = []
ans = []
cnt = 1
pos = True
n = int(sys.stdin.readline())
for i in range(n):
    tmp = int(sys.stdin.readline())
    while cnt <= tmp:
        ans.append("+")
        stack.append(cnt)
        cnt +=1

    if stack[-1] == tmp:
        ans.append("-")
        stack.pop()
    else:
        pos = False
        break
            
if pos:
    for i in ans:   
        print(i)
else:
    print("NO")

