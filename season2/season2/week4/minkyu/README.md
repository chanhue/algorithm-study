# 투 포인터
 - 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘    
 

1차원 배열이 있을 때 그 배열에서 각자의 원소(같은 원소 또는 다른 원소)를 가리키고 있는 2개의 포인터를 조작.    
완전 탐색으로 풀 때 O(n^2)의 시간복잡도를 가지는 반면에 투 포인터 알고리즘은 O(n)으로 시간을 굉장히 줄일 수 있어 유용하다.

## 백준 2470번
이번 문제를 풀 때는 정렬된 리스트에서 투 포인터 알고리즘을 사용했어야하는데, 정렬되지 않은 리스트에서도 사용 가능한 경우가 있다.    
ex) [정렬 되지 않은 리스트](https://www.youtube.com/watch?v=ttLRltNDiCo&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=40)

ex) 입력 : [-2, 4, -99, -1, 98]    
&nbsp;정렬 후 : [-99, -2, -1, 4, 98]

left 포인터에 젤 작은 숫자가 저장되어 있는 인덱스 0, right 포인터에 젤 큰 숫자가 저장되어 있는 인덱스 4를 저장한다.    
만약 포인터가 가리키고 있는 숫자들의 합인 num 이 0보다 크다면 작아져야 하고 0보다 작으면 커져야 한다.    
따라서 num 이 0보다 작을 땐 왼쪽 포인터를 오른쪽으로 한 칸, 0보다 클 땐 오른쪽 포인터를 왼쪽으로 한 칸 옮긴다.    
|left|right|num|result|
|:--:|:---:|:-:|:----:|
|-99|98|-1|1|
|-2|98|96|1|
|-2|4|2|1|
|-1|-1|---|---|