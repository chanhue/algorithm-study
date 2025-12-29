import sys 
n = int(sys.stdin.readline())
for i in range(n):
    c = sys.stdin.readline()
    s = 0
    num = 0
    for j in range(len(c)):
        if c[j] == 'O':
            num +=1
            s += num
        else:
            num =0
    print(s)