import sys
n = int(sys.stdin.readline())
ls = []
cmd = []
for i in range(n):
    tmp = sys.stdin.readline()
    cmd = tmp.split()
    if cmd[0] == 'push':
        ls.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(ls)==0:
            print(-1)
        else:
            print(ls.pop())
    elif cmd[0] == 'size':
        print(len(ls))
    elif cmd[0] == 'empty':
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[-1])