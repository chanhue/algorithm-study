import sys
n = int(sys.stdin.readline().strip())
stack = []
for i in range(n):
    m = sys.stdin.readline().strip()
    if m[0] == '1':
        t,n = map(int, m.split())
        stack.append(n)
    elif m == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop()
    elif m == '3':
        print(len(stack))
    elif m == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])