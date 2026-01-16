import queue
import sys
q = queue.Queue()
n = int(sys.stdin.readline())
for i in range(n):
    tmp = sys.stdin.readline()
    cmd = tmp.split()
    if cmd[0] == "push":
        q.put(cmd[1])
    elif cmd[0] == "pop":
        if q.qsize()==0:
            print(-1)
        else:
            print(q.get())
    elif cmd[0] == "size":
        print(q.qsize())
    elif cmd[0] == "empty":
        if q.qsize()==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if q.qsize()==0:
            print(-1)
        else:
            print(q.queue[0])
    else:
        if q.qsize()==0:
            print(-1)
        else:
            print(q.queue[-1])