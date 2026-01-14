import sys
while True:
    stack = []
    balance = True
    s = sys.stdin.readline()[:-1]
    if s ==".":
        break
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                balance = False
                break
            elif stack[-1] == "[":
                balance = False
                break
            else:
                stack.pop()
        elif i == "]":
            if len(stack) == 0:
                balance = False
                break
            elif stack[-1] == "(":
                balance = False
                break
            else:
                stack.pop()
    if len(stack) != 0:
        balance = False
    if balance == True:
        print('yes')
    else:
        print('no')
