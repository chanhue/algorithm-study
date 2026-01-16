import sys
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip()
    ls = []
    vps = True
    for j in s:
        if j == "(":
            ls.append("(")
        else:
            if len(ls)==0:
                vps = False
                break
            else:
                ls.pop()
    if len(ls)!= 0:
        vps = False
    if vps:
        print("YES")
    else:
        print("NO")