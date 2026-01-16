import queue
n, k = map(int, input().split())
ls = queue.Queue()
pivot = 0
for i in range(n):
    ls.put(i+1)
print("<",end="")
for i in range(n):
    for j in range(k-1):
        ls.put(ls.get())
    print(ls.get(), end="")
    if i != n-1:
        print(", ",end="")
print(">")