s = input()
q = int(input())
for i in range(q):
    a, l, r = input().split()
    cnt = 0
    for j in range(int(l),int(r)+1):
        if s[j] == a:
            cnt+=1
    print(cnt)

### 부분 정답(50점)

