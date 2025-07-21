from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == '1':
        deq.appendleft(int(c[1]))
    elif c[0] == '2':
        deq.append(int(c[1]))
    elif c[0] == '3':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif c[0] =='4':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif c[0] =='5':
        print(len(deq))
    elif c[0] =='6':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] =='7':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif c[0] =='8':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])