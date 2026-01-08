import sys

n = int(sys.stdin.readline())
ls = [0]*10000
for i in range(n):
    tmp = int(sys.stdin.readline())
    ls[tmp-1]+=1
for i in range(len(ls)):
    for j in range(ls[i]):
        print(i+1)

## 이 문제를 단순회 배열에 요소를 넣고 정렬하게 된다면 메모리적인 제한이 발생할 수 있음
## 요소를 출력하는 것이 아니라 값의 범위를 지정하고 해당 범위에서 요소의 개수를 센 후 출력하는 것이 메모리를 아낌