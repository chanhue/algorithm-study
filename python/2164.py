from collections import deque
n = int(input())

card = deque([i for i in range(1,n+1)])
while (len(card)>1):
    card.popleft()
    card.append(card.popleft()) #deque의 append는 하나의 인자를 받음
print(card[0])