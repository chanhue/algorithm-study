from collections import deque
import sys
deque = deque()
n = int(sys.stdin.readline().strip())
for i in range(n):
    c = sys.stdin.readline().strip().split()
    if c[0] == 'push':
        deque.append(c[1])
    elif c[0] == 'pop':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft()) 
    elif c[0] == 'size':
        print(len(deque))
    elif c[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif c[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])