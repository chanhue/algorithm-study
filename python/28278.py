# 기존 코드
# import sys
# n = int(sys.stdin.readline().strip())
# stack = []
# for i in range(n):
#     m = sys.stdin.readline().strip()
#     if m[0] == '1':
#         t,n = map(int, m.split())
#         stack.append(n)
#     elif m == '2':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[len(stack)-1])
#             stack.pop()
#     elif m == '3':
#         print(len(stack))
#     elif m == '4':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[len(stack)-1])

# 파이썬 시간초과를 해결하기 위해서는 (특히 반복된 입력 받을 때) import sys / sys.stdin.readline()을 사용하자
# 추가적으로 strip을 하지 않으면 개행문자가 포함된다